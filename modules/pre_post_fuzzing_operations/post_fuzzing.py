##################################################################
"""
Name  : post_fuzzing.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.misc_functions.sleep_while_pause import sleep_while_pause
from modules.element_interaction.wait_and_handle_popup import wait_and_handle_popup
from modules.pse1.pse1 import python_scripting_engine
from modules.reporting.write_single_fuzz_traffic import write_http_request_response
from modules.automatic_navigation_handler.load_navigation import load_navigation

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # Used to pause the script
from selenium.common.exceptions import JavascriptException

##################################################################
"""
Name          -> operations_after_pressing_the_button
Functionality -> Function to perform common operations after pressing the button
Algorithm     ->
    1. get the reference of global first_payload variable to know if there is an error in user supplied python or js code, if there is an error then we will close the script
    2. handle --pause-after-submit
    3. handle --delay-after
    4. Wait for all requests to be completed
    5. If there is javascript to execute, then execute it, if there is any error and this is first round of fuzzing then close the script
    6. Execute python if any if there is any error check the first_payload flag, if this is first round of fuzzing close the script
    7. Get the web page content after fuzzing is completed
    8. call the write_http_request_response method to write this round of fuzzing in report file
    9. mark the global first_payload (first round) flag as completed
    10. handle --remove-session
Parameters    -> element(element), driver(webdriver.Chrome), webpage_before(string),
 this_threads_file(string), payload(string)
Return        -> 
"""
################################################################## 

def operations_after_pressing_the_button(element,driver,webpage_before,this_threads_file,payload):
    # Algorithm step: 1 get the reference of first_payload variable
    # If there was an exception in python code which manipulates traffic on first payload close the browser bruter
    # Reference global first_payload variable so we can make it False
    global_variable.first_payload
    # Algorithm step: 2 if pause after submit is present then pause the fuzzing process
    if global_variable.args.pause_after_submit:
        global_variable.pause_event.set()
        sleep_while_pause()
    # Algorithm step: 3 delay before making new request
    if global_variable.args.delay_after:
        sleep(global_variable.args.delay_after)
    # Algorithm step: 4 Wait for all requests to be completed
    wait_and_handle_popup(driver)
    # Do the automatic navigation
    if global_variable.args.load_navigation_after:
        load_navigation(driver, global_variable.args.load_navigation_after)
    # Algorithm step: 5 Execute javascript
    if global_variable.args.javascript_after: # check if there is any javascript code to execute 
        sleep(0.2)
        try:
            driver.execute_script(global_variable.args.javascript_after) # Execute the javascript using driver object
        except JavascriptException as e: # if there is any error then do following
            if first_payload: # if this is the first round of fuzzing then close the script
                raise e # raise the exception
            else:
                sleep(3) # else wait for sometime and retry two more times
                try:
                    driver.execute_script(global_variable.args.javascript_after)
                except JavascriptException:
                    sleep(7)
                    driver.execute_script(global_variable.args.javascript_after)
    # Algorithm step: 7 Execute python by calling python_scripting_engine
    if global_variable.args.python_after: # check the if there is any python code to execute
        sleep(0.2)
        try:
            python_scripting_engine(driver,global_variable.args.python_after) # Execute python code by calling python_scripting_engine()
        except Exception as e: # if there is an error do following
            if first_payload: # if this is first round of fuzzing then close the script by raising the exception
                raise e
            else:
                sleep(3) # else wait for time and retry two more times
                try:
                    python_scripting_engine(driver,global_variable.args.python_after)
                except:
                    sleep(7)
                    python_scripting_engine(driver,global_variable.args.python_after)
    # Algorithm step: 7 Get web page content after making the response
    webpage_after = driver.page_source
    # Algorithm step: 8 write the http request response in report file
    write_http_request_response(element,this_threads_file,driver,payload,webpage_before,webpage_after)
    # Algorithm step: 9 Remove first payload
    first_payload = False
    # Algorithm step: 10 Clear the cookies and other data
    if global_variable.args.remove_session:
        driver.delete_all_cookies()
