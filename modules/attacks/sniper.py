##################################################################
"""
Name  : sniper.py 
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
Name          -> sniper_loop
Functionality -> Function will perform sniper attack by calling sniper_loop
Algorithm     ->
    1. Define and initialize the progress bar.
    2. for each integer starting form 0 to total payloads, call it 'i' and do following
        a. for each element, call it 'j' and do following
            1. Check the termination flag
            2. if --interactive is set then handle it
            3. attempt_sniper_fuzz(elements[j],payloads[i], driver, this_threads_files[0])
            4. if --new-instance is set then handle it
            5. update progress bar
            6. Move on to next element
        b. add processed payload into processed payloads file
        c. Increase i by 1
    3. Close the progress bar
Parameters    -> payloads(list of string), elements(list of string), instance_number(int),
 this_threads_files(list of files), driver(webdriver.Chrome)
Return        -> 
"""
################################################################## 

def sniper_loop(payloads,elements,instance_number,this_threads_files,driver):
    # Algorithm step: 1
    progress_bar = tqdm(total=len(payloads) * len(elements), desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration",dynamic_ncols=True,colour='blue') # Initialize the progress bar, total is the length of the progress bar which the number of times the browser will attempt to fuzz the target
    # Start the Fuzzing process
    for i in range(len(payloads)): # Algorithm step: 2 For each payload 
        for j in range(len(elements)): # Algorithm step: 2.a For each element for each payload
            # Fuzz until global_variable.terminate flag is not set, if it set then exit and close browser
            if not global_variable.terminate: # Algorithm step: 2.a.1 Again check the global_variable.terminate flag before any fuzzing attempt
                if global_variable.args.interactive: # Algorithm step: 2.a.2 if interactive option is set stop and wait for user to continue
                    driver.get(global_variable.args.target) # First browser to the target web site, and then pause the script, so user can interact with the target
                    global_variable.pause_event.set() # Set the pause event
                sleep_while_pause() # if pause event is set then pause the fuzzing process
                try: # Algorithm step: 2.a.3
                    attempt_sniper_fuzz(elements[j],payloads[i], driver, this_threads_files[0]) # Take one payload, one element, and try to fuzz them, also supplying threads report file name so the result is logged
                except StaleElementReferenceException: # If there StaleElementReferenceException error then retry one more time
                    sleep(4) # Wait for 4 seconds before retrying
                    attempt_sniper_fuzz(elements[j],payloads[i], driver, this_threads_files[0]) # Retry the fuzz attempt
                if global_variable.args.new_instance: # Algorithm step: 2.a.4 --new-instance switch is set then we have to close this browser and start the new browser, with payload tracking, so call the handle_new_instance method
                    driver = handle_new_instance(driver)
            if not global_variable.terminate:
                progress_bar.update(1) # Algorithm step: 2.a.5 Update the progress bar
            j += 1 # Algorithm step: 2.a.6 Move on to fuzzing next element with same payload until all elements has been fuzzed with this payload
        with open(this_threads_files[1],'a',newline='') as processed_payload_file: # Algorithm step: 2.b Add the processed payload into the file to keep track of processed payloads by this thread
            processed_payload_file.write(payloads[i]+'\n')
        i+=i # Algorithm step: 2.c Move on to the next payload
    progress_bar.close() # Algorithm step: 3 After fuzzing is completed close the progress bar

##################################################################
"""
Name          -> attempt_sniper_fuzz
Functionality -> Function to attempt a single request-response cycle with payload,
                 Below operations are performed in every single fuzz attempt of all attack types
Algorithm     ->
                1. Call initial_operations_before_filling_the_form(driver),
                2. Store the webpage source code before fuzzing the web application
                3. if --fill then call fill_the_form to fill the form
                4. Store the element to fuzz in element_being_fuzzed variable by calling get_element() method
                5. if element is flagged to remove its class then remove its class attribute
                6. call the fill_payload_in_element() method and fill the payload in element to fuzz
                7. Get and store the button element which will submit the form in button_to_press variable by calling get_element() method
                8. if button element is also flagged to remove the class, then remove the class of button
                9. Press the button by calling press_button() method
                10. call the operations_after_pressing_the_button() method.
Parameters    -> element(element), payload(string), driver(webdriver.Chrome), this_threads_file(string)
Return        -> 
"""
################################################################## 

def attempt_sniper_fuzz(element, payload, driver, this_threads_file):
    # Algorithm step: 1 Call the initial_operations_before_filling_the_form
    try:
        initial_operations_before_filling_the_form(driver)
    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
        sleep(3)
        initial_operations_before_filling_the_form(driver)
    # Algorithm step: 2 Get web page content before making request
    webpage_before = driver.page_source
    # Algorithm step: 3 Automatically handle and fill the form
    if global_variable.args.fill:
        try:
            fill_the_form(driver)
        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
            driver.get(global_variable.args.target)
            wait_and_handle_popup(driver) # As we are calling driver.get() check if there is any popup, if there is any popup then handle it
            sleep(3) # wait before retrying
            try: # retry
                fill_the_form(driver)
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                driver.get(global_variable.args.target)
                wait_and_handle_popup(driver)
                sleep(3)
                fill_the_form(driver)
    # Algorithm step: 4
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    element_being_fuzzed = get_element(driver,element,False) 
    if element in global_variable.remove_class_elements: # Algorithm step: 5
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed) # remove the class attribute using javascript
    # Algorithm step: 6 Fill the payload in element
    try:
        fill_payload_in_element(driver,element_being_fuzzed,payload,element) 
    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
        sleep(6) # wait for sometime before retrying
        try: # retry
            fill_payload_in_element(driver,element_being_fuzzed,payload,element)
        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
            sleep(6)
            try:
                fill_payload_in_element(driver,element_being_fuzzed,payload,element)
            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                sleep(10)
                try:
                    fill_payload_in_element(driver,element_being_fuzzed,payload,element)
                except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                    sleep(20)
                    fill_payload_in_element(driver,element_being_fuzzed,payload,element)
    button_to_press = get_element(driver,global_variable.args.button,False) # Algorithm step: 7 Get the button element
    if global_variable.args.button in global_variable.remove_class_elements: # Algorithm step: 8 remove class if required
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press) # remove the class attribute using javascript
    press_button(driver,button_to_press,False) # Algorithm step: 9 press the button
    operations_after_pressing_the_button(element,driver,webpage_before,this_threads_file,payload) # Algorithm step: 10 perform post fuzz operations