##################################################################
"""
Name  : cluster_bomb.py 
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
from modules.error_handling.error_handling import log_error
from modules.pause_and_stop.signal_handler import signal_handler

##################################################################
# Importing Python Libraries
##################################################################
from traceback import format_exc
import signal # used for handling CTRL+C key
from time import sleep # Used to pause the script
from sys import exit # used to close the script
from tqdm import tqdm # used for progress bar
from selenium.common.exceptions import StaleElementReferenceException

##################################################################
"""
Name          -> attempt_clusterbomb_fuzz
Functionality -> This function will perform clusterbomb attack
Algorithm     -> 
                # The clusterbomb fuzz attempt contains both clusterbomb loop logic as well fuzzing logic
                1. Define and initialize progress_bar
                2. for each payloads list present in payloads_combination
                    a. Check the global_variable.terminate flag
                    b. if --interactive is set then, navigate to the url and pause the script
                    c. Call initial_operations_before_filling_the_form(driver)
                    d. Store the webpage source code before fuzzing the web application
                    e. if --fill then call fill_the_form to fill the form
                    f. for element->payload combination present in elements_payloads->payloads
                        1. Store the the element in element_being_fuzzed using get_element method
                        2. if element is flagged to remove its class then remove its class attribute
                        3. call the fill_payload_in_element() method and fill the payload in element to fuzz
                    g. Get and store the button element which will submit the form in button_to_press variable by calling get_element() method
                    h. if button element is also flagged to remove the class, then remove the class of button
                    i. Press the button by calling press_button() method
                    j. Update progress bar
                    k. call the operations_after_pressing_the_button() method.
                    l. Add the processed payload into the processed payloads file
                    m. If the --new-instance switch is set then handle_new_instance()
                3. Close the progress bar
                4. Handle keyboard interrupt exception
Parameters    -> payloads_combination(list of dictionaries), driver(webdriver.Chrome),
 this_threads_files(list of strings), instance_number(int)
Return        -> 
"""
################################################################## 

def attempt_clusterbomb_fuzz(payloads_combinations, driver, this_threads_files, instance_number):
    try:
        # Algorithm step:1 Create a list to store all combinations of payloads
        progress_bar = tqdm(total=len(payloads_combinations), desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration",dynamic_ncols=True,colour='blue')
        # Algorithm step:2 Iterate through each combination
        for payloads in payloads_combinations:
            if not global_variable.terminate: # Algorithm step:2.a Checking the termination flag
                if global_variable.args.interactive: # Algorithm step:2.b if interactive option is set stop and wait for user to continue
                    driver.get(global_variable.args.target) # Navigate to target url
                    global_variable.pause_event.set() # set the pause flag
                sleep_while_pause() # If the pause event is set, then pause the fuzzing process
                # Call the initial_operations_before_filling_the_form
                try: # Algorithm step:2.c
                    initial_operations_before_filling_the_form(driver)
                except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                    sleep(5)
                    initial_operations_before_filling_the_form(driver)
                # Algorithm step:2.d Get web page content before making request
                webpage_before = driver.page_source
                if global_variable.terminate:
                    break
                # Algorithm step:2.e Automatically handle and fill the form
                if global_variable.args.fill:
                    try:
                        fill_the_form(driver) # Call fill_the_form() to fill the form
                    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                        driver.get(global_variable.args.target) # navigate to url
                        wait_and_handle_popup(driver) # handle if there is any popup and handle the wait logic
                        sleep(5) # wait for some time before next try
                        try:
                            fill_the_form(driver)
                        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                            driver.get(global_variable.args.target)
                            wait_and_handle_popup(driver)
                            sleep(5)
                            fill_the_form(driver)
                if global_variable.terminate:
                    break
                # Algorithm step:2.f Iterate through each element and set its value
                for element, payload in zip(global_variable.elements_payloads.keys(), payloads):
                    if global_variable.terminate:
                        break
                    # Algorithm step:2.f.1 Find the element to be fuzzed
                    element_being_fuzzed = get_element(driver,element,False)
                    # Algorithm step:2.f.2 if element if flagged to remove the class then remove it's class attribute
                    if element in global_variable.remove_class_elements:
                        driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed) # remove the class attribute using javascript
                    # Algorithm step:2.f.3 Fill the payload in element
                    try:
                        fill_payload_in_element(driver,element_being_fuzzed,payload)
                    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                        sleep(4) # wait for sometime before retry
                        try: # retry
                            fill_payload_in_element(driver,element_being_fuzzed,payload)
                        except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                            sleep(10)
                            try:    
                                fill_payload_in_element(driver,element_being_fuzzed,payload,element)
                            except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                                sleep(20)
                                fill_payload_in_element(driver,element_being_fuzzed,payload,element)
                # Algorithm step:2.g Press the button
                if not global_variable.terminate:
                    button_to_press = get_element(driver,global_variable.args.button,False)
                    try:
                        # Algorithm step:2.h if the button element is flagged to remove class, then remove it's class attribute
                        if global_variable.args.button in global_variable.remove_class_elements:
                            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press) # remove the class attribute using javascript
                        press_button(driver,button_to_press,False) # Algorithm step:2.i press the button
                    except StaleElementReferenceException: # if there is a StaleElementReferenceException then retry
                        sleep(4) # wait for some time
                        if global_variable.args.button in global_variable.remove_class_elements:
                            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press) # remove the class attribute using javascript
                        press_button(driver,button_to_press,False)
                else:
                    break
                if not global_variable.terminate:
                    # Algorithm step:2.j update progress bar
                    progress_bar.update(1)
                operations_after_pressing_the_button(list(global_variable.elements_payloads.keys()),driver,webpage_before,this_threads_files[0],payloads) # Algorithm step:2.k call the operation after fuzzing
                # Algorithm step:2.l Add the processed payload into the file to keep track of processed payloads by this thread
                with open(this_threads_files[1], 'w', newline='') as processed_payload_file: # Open this threads file payload file
                    processed_payload_file.write(str(payloads) + '\n') # write payload to this thread's processed payload file
                if global_variable.args.new_instance: # Algorithm step:2.m handle --new-instance switch
                    driver = handle_new_instance(driver) # call the handle_new_instance method()
        # Algorithm step:3 Close the progress bar
        progress_bar.close()
    except KeyboardInterrupt: # Algorithm step:4 handle keyboard interrupt
        signal_handler(signal.SIGINT, None)
        log_error(format_exc())
        exit(0)
