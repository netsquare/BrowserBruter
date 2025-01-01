##################################################################
"""
Name  : battering_ram.py 
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
Name          -> battering_ram_loop
Functionality -> This function will perform battering ram attack by calling attempt_battering_ram_fuzz
Algorithm     ->
    1. Define and initialize the progress bar.
    2. for each integer starting form 0 to total payloads, call it 'i' and do following
        a. Check the termination flag
        b. if --interactive is set then handle it
        c. call attempt_battering_ram_fuzz(elements,payloads[i], driver, this_threads_files[0])
        d. if --new-instance is set then handle it
        e. update progress bar
        f. add processed payload into processed payloads file
        g. Increase i by 1
    3. Close the progress bar
Parameters    -> payloads(list of string), elements(list of strings), instance_number(int), 
this_threads_files(list of string)
Return        -> 
"""
################################################################## 

def battering_ram_loop(payloads,elements,instance_number,this_threads_files,driver):
    # Algorithm step: 1 Progress bar
    progress_bar = tqdm(total=len(payloads), desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration",dynamic_ncols=True,colour='blue')
    # Start the Fuzzing process
    for i in range(len(payloads)): # Algorithm step: 2
        # Algorithm step: 2.a Fuzz until global_variable.terminate flag is not set, if it set then exit and close browser
        if not global_variable.terminate:
        # Algorithm step: 2.b if interactive option is set stop and wait for user to continue
            if global_variable.args.interactive:
                driver.get(global_variable.args.target) # Navigate to target url
                global_variable.pause_event.set() # set pause event
            sleep_while_pause() # call the sleep_while_pause() method to stop the script while global_variable.pause_event is set
            try: # Algorithm step: 2.c call the attack logic
                attempt_battering_ram_fuzz(elements,payloads[i], driver, this_threads_files[0])
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                sleep(4)
                attempt_battering_ram_fuzz(elements,payloads[i], driver, this_threads_files[0])
            if global_variable.args.new_instance: # Algorithm step: 2.d handle --new-instance flag
                handle_new_instance(driver)
            if not global_variable.terminate:
                # Algorithm step: 2.e Update the progress bar
                progress_bar.update(1)
        # Algorithm step: 2.f Add the processed payload into the file to keep track of processed payloads by this thread
        with open(this_threads_files[1],'a',newline='') as processed_payload_file:
            processed_payload_file.write(payloads[i]+'\n')
        i+=i # Algorithm step: 2.g Next payload
    progress_bar.close() # Algorithm step: 3 close the progress bar

##################################################################
"""
Name          -> attempt_battering_ram_fuzz
Functionality -> This function will perform battering ram attack
Algorithm     ->
                1. Call initial_operations_before_filling_the_form(driver)
                2. Store the webpage source code before fuzzing the web application
                3. if --fill then call fill_the_form to fill the form
                4. for each element to fuzz present in elements list, 
                    a. Store the the element in element_being_fuzzed using get_element method
                    b. if element is flagged to remove its class then remove its class attribute
                    c. call the fill_payload_in_element() method and fill the payload in element to fuzz
                5. Get and store the button element which will submit the form in button_to_press variable by calling get_element() method
                6. if button element is also flagged to remove the class, then remove the class of button
                7. Press the button by calling press_button() method
                8. call the operations_after_pressing_the_button() method.
Parameters    -> elements(list of strings), payload(string), driver(webdriver.Chrome),
this_threads_file(string)
Return        -> 
"""
################################################################## 
	
# Function to attempt to fuzz battering ram
def attempt_battering_ram_fuzz(elements, payload, driver, this_threads_file):
    # Algorithm step: 1 Call the initial_operations_before_filling_the_form
    try:
        initial_operations_before_filling_the_form(driver)
    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
        sleep(5)
        initial_operations_before_filling_the_form(driver)
    # Algorithm step: 2 Get web page content before making request
    webpage_before = driver.page_source
    # Algorithm step: 3 Automatically handle and fill the form
    if global_variable.args.fill:
        try:
            fill_the_form(driver)
        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
            driver.get(global_variable.args.target) # navigate to target url
            wait_and_handle_popup(driver) # handle any popup
            sleep(10) # wait for some time
            try: # retry
                fill_the_form(driver)
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                driver.get(global_variable.args.target)
                wait_and_handle_popup(driver)
                sleep(10)
                fill_the_form(driver)
    # Algorithm step: 4
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    for element in elements:
        element_being_fuzzed = get_element(driver,element,False) # Algorithm step: 4.a get the element
        if element in global_variable.remove_class_elements: # Algorithm step: 4.b remove the class attribute if required
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed) # remove the class attribute using javascript
        # Algorithm step: 4.c Fill the payload in element
        try:
            fill_payload_in_element(driver,element_being_fuzzed,payload,element)
        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
            sleep(6)
            try:
                fill_payload_in_element(driver,element_being_fuzzed,payload,element)
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                sleep(6) # wait for sometime before retrying
                try: # retry
                    fill_payload_in_element(driver,element_being_fuzzed,payload,element)
                except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                    sleep(10)
                    try:
                        fill_payload_in_element(driver,element_being_fuzzed,payload,element)
                    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                        sleep(20)
                        fill_payload_in_element(driver,element_being_fuzzed,payload,element)
    button_to_press = get_element(driver,global_variable.args.button,False) # Algorithm step: 5 get the button element
    if global_variable.args.button in global_variable.remove_class_elements: # Algorithm step: 6 remove class attribute if required
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press) # remove the class attribute using javascript
    press_button(driver,button_to_press,False) # Algorithm step: 7 press the button
    operations_after_pressing_the_button(elements,driver,webpage_before,this_threads_file,payload) # Algorithm step: 8 perform post fuzz operations
