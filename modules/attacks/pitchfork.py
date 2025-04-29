##################################################################
"""
Name  : pitchfork.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.misc_functions.sleep_while_pause import sleep_while_pause
from modules.run_browser.handle_new_instance import handle_new_instance
from modules.pre_post_fuzzing_operations.pre_fuzzing import initial_operations_before_filling_the_form
from modules.pre_post_fuzzing_operations.post_fuzzing import operations_after_pressing_the_button
from modules.element_interaction.fill_form import fill_the_form
from modules.element_interaction.fill_payload_in_element import fill_payload_in_element
from modules.element_interaction.get_element import get_element
from modules.element_interaction.wait_and_handle_popup import wait_and_handle_popup
from modules.element_interaction.press_button import press_button
from modules.misc_functions.sleep_while_pause import sleep_while_pause

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # Used to pause the script
from tqdm import tqdm # used for progress bar
from selenium.common.exceptions import StaleElementReferenceException

##################################################################
"""
Name          -> pitchfork_loop
Functionality -> This function will perform pitchfork attack by calling attempt_pitchfork_fuzz
Algorithm     ->
    1. Get the number of iterations by first finding which payload list has most payloads. Then counting the total payloads in that largest list.
    2. Define and initialize the progress bar
    3. Create a empty list to hold processed payloads
    4. for each integer starting from 0 to num_iterations, call it 'i' and do following
        a. Check the global_variable.terminate flag
        b. if --interactive mode is set then enable the interaction
        c. call the  attempt_pitchfork_fuzz(elements_payloads, i, driver, this_threads_files[0])
        d. if --new-instance flag is set then handle it
        e. add processed payload in processed payloads list
        f. update the progress bar
        g. Add all payloads present in processed_payloads into processed payloads file
    5. Close the progress bar
Parameters    -> elements_payloads(list of strings), instance_number(int), this_threads_file(string), 
driver(webdriver.Chrome)
Return        -> 
"""
################################################################## 

def pitchfork_loop(elements_payloads,instance_number,this_threads_files,driver):
    # Algorithm step: 1 Determine the number of iterations based on the maximum length of test data files
    num_iterations = max(len(payload_list) for payload_list in elements_payloads.values())
    # Algorithm step: 2 progress bar
    progress_bar = tqdm(total=num_iterations, desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration", dynamic_ncols=True, colour='blue')
    processed_payloads = [] # Algorithm step: 3 empty list to hold processed payloads
    # Algorithm step: 4 fuzzing loop
    for i in range(num_iterations): 
        # Algorithm step: 4.a Fuzz until global_variable.terminate flag is not set, if it is set then exit and close the browser
        if not global_variable.terminate:
            # Algorithm step: 4.b if interactive option is set stop and wait for user to continue
            if global_variable.args.interactive:
                driver.get(global_variable.args.target) # Navigate to target url
                global_variable.pause_event.set() # set the global_variable.pause_event
            # If the pause event is set, then pause the fuzzing process
            sleep_while_pause()
            try: # Algorithm step: 4.c call the fuzzing logic
                attempt_pitchfork_fuzz(elements_payloads, i, driver, this_threads_files[0])
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                sleep(4)
                attempt_pitchfork_fuzz(elements_payloads, i, driver, this_threads_files[0])
            if global_variable.args.new_instance: # Algorithm step: 4.d handle --new-instance
                handle_new_instance(driver)
            for element, payload_list in elements_payloads.items(): # Algorithm step: 4.e track processed payloads
                processed_payloads.append(payload_list[i])
            if not global_variable.terminate:
                # Algorithm step: 4.f Update the progress bar
                progress_bar.update(1)
        # Algorithm step: 4.g Add the processed payload into the file to keep track of processed payloads by this thread
        with open(this_threads_files[1], 'w', newline='') as processed_payload_file:
            processed_payload_file.write(str(processed_payloads) + '\n') # write the processed payload
    # Algorithm step: 5 Close the progress bar
    progress_bar.close()

##################################################################
"""
Name          -> attempt_pitchfork_fuzz
Functionality -> This function will perform pitchfork attack
Algorithm     ->
                1. Create a empty list called payloads
                2. for each element->payload_list combination in elements_payloads
                    a. Append this payload_list in payloads list
                3. Call initial_operations_before_filling_the_form(driver)
                4. Store the webpage source code before fuzzing the web application
                5. if --fill then call fill_the_form to fill the form
                6. for each element to fuzz and their respective payload_list present in elements_payloads
                    a. Store the the element in element_being_fuzzed using get_element method
                    b. if element is flagged to remove its class then remove its class attribute
                    c. call the fill_payload_in_element() method and fill the payload in element to fuzz
                7. Get and store the button element which will submit the form in button_to_press variable by calling get_element() method
                8. if button element is also flagged to remove the class, then remove the class of button
                9. Press the button by calling press_button() method
                10. call the operations_after_pressing_the_button() method.
Parameters    -> elements_payloads(list of strings), index(int), driver(webdriver.Chrome), 
this_threads_file(string)
Return        -> 
"""
################################################################## 
	
def attempt_pitchfork_fuzz(elements_payloads,index,driver,this_threads_file):
    payloads = [] # Algorithm step: 1 this variable will store payloads lists
    for element, payload_list in elements_payloads.items(): # Algorithm step: 2
        payloads.append(payload_list[index]) # Algorithm step: 2.a append this payload_list in payloads[] list
    # Algorithm step: 3 Call the initial_operations_before_filling_the_form
    try:
        initial_operations_before_filling_the_form(driver)
    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
        sleep(5) # Wait for some time before re-try
        initial_operations_before_filling_the_form(driver)
    # Algorithm step: 4 Get web page content before making request
    webpage_before = driver.page_source
    # Algorithm step: 5 Automatically handle and fill the form
    if global_variable.args.fill: # if --fill flag is present
        try:
            fill_the_form(driver) # call fill_the_form() method to fill the form
        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
            driver.get(global_variable.args.target) # Navigate to target url
            wait_and_handle_popup(driver) # handle any wait and popup
            sleep(5) # wait for some time before retry
            try: # retry
                fill_the_form(driver)
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                driver.get(global_variable.args.target)
                wait_and_handle_popup(driver)
                sleep(5)
                fill_the_form(driver)
    # Algorithm step: 6
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    for element, payload_list in elements_payloads.items(): # Main loop for iterating over element and its associated payloads
        element_being_fuzzed = get_element(driver,element,False) # Algorithm step: 6.a get the element to fuzz
        if element in global_variable.remove_class_elements: # Algorithm step: 6.b
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed) # remove the class attribute using javascript
        # Algorithm step: 6.c Fill the payload in element
        try:
            fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry 
            sleep(6) # wait for some time before retrying
            try:
                fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                sleep(6)
                try:
                    fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
                except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                    sleep(10)
                    try:
                        fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
                    except StaleElementReferenceException:# if there is a StaleElementReferenceException then retry
                        sleep(20)
                        fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
    # Algorithm step: 7 Press the button
    button_to_press = get_element(driver,global_variable.args.button,False)
    if global_variable.args.button in global_variable.remove_class_elements: # Algorithm step: 8
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press) # remove the class attribute using javascript
    # Algorithm step: 9
    press_button(driver,button_to_press,False)
    # Algorithm step: 10
    operations_after_pressing_the_button(list(elements_payloads.keys()),driver,webpage_before,this_threads_file,payloads)
