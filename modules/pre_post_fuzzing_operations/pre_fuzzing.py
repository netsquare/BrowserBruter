##################################################################
"""
Name  : pre_fuzzing.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.run_browser.add_cookies import add_cookies
from modules.element_interaction.wait_and_handle_popup import wait_and_handle_popup
from modules.element_interaction.press_button import press_button
from modules.element_interaction.get_element import get_element
from modules.input_validation.auto_remove import remove_javascript_validation
from modules.input_validation.disable_js_events import disable_js_events
from modules.pse1.pse1 import python_scripting_engine
from modules.error_handling.error_handling import handle_unknown_exception
from modules.misc_functions.sleep_while_pause import sleep_while_pause
from modules.automatic_navigation_handler.load_navigation import load_navigation

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # Used to pause the script
from sys import exit # used to close the script

##################################################################
# Importing Exception
##################################################################
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import JavascriptException


##################################################################
"""
Name          -> initial_operations_before_filling_the_form
Functionality -> Function to perform generic initial operations before filling the form
Algorithm ->
    1. Set the cookies again if --force-cookie flag is set
    2. Call wait_and_handle_popup(driver)
    3. Clear the previous requests
    4. Check if --interactive is set, because if it set then, the browser has already navigated to target URL, else if it is not then navigate to target url.
    5. if --reload-page is set then reload the page
    6. if there is python code to execute then execute the python code
    7. if there is javascript code to execute then execute the javascript code
    8. if there is --no-css code, then remove inline css
    9. delay the execution of script incase of --delay-before option is supplied
    10. if there are any buttons to press before fuzzing the form, press those buttons
    11. if --auto-remove-javascript-validation then call remove_javascript_validation function 
    12. if --disable-events then call disable_js_events to disable js events
    13. If there is any pop up, then handle it.
Parameters    -> driver(webdriver.Chrome)
Return        -> 
"""
################################################################## 

def initial_operations_before_filling_the_form(driver):
    # Algorithm step: 1 If --force-cookie is set then set the initial cookies
    if global_variable.args.force_cookie:
        add_cookies(driver)
    # Algorithm step: 2 Wait for body to be loaded in case of slow response
    wait_and_handle_popup(driver)
    # Algorithm step: 3 Clear previous requests
    del driver.requests
    # if user has supplied the --no-reload-page switch then reload one time and set global flag to prevent further reload
    if global_variable.args.no_reload_page and global_variable.no_reload:
        driver.get(global_variable.args.target)
        global_variable.no_reload = False
    # Algorithm step: 4 Go to the target website
    if not (global_variable.args.interactive and global_variable.args.no_reload_page): # Check if --interactive is set, because if it set then, the browser has already navigated to target URL, else if it is not then navigate to target url.
        try:
           # if not driver.get(global_variable.args.no_reload_page): # Check if user specified not to visit the target URL
            driver.get(global_variable.args.target) # navigate to url
        except TimeoutException as e: # if there is a timeout in navigating to url
            print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
            global_variable.global_variable.pause_event.set()
            sleep_while_pause()
    # Algorithm step: 5 if global_variable.args.reload_page then reload the current page
    if global_variable.args.reload_page:
        # Force reload the page using javascript 'location.reload(true);'
        driver.execute_script("location.reload(true);")
        wait_and_handle_popup(driver) # handle any popup as well as wait for page to fully load
        sleep(0.5)
    # Do the automatic navigation
    if global_variable.args.load_navigation_before:
        load_navigation(driver, global_variable.args.load_navigation_before)
    # Algorithm step: 6 Execute python code 
    if not global_variable.python_to_execute == '\0': # if python code to execute is not null then do following
        sleep(0.2) # wait for some time
        try:
            python_scripting_engine(driver,global_variable.python_to_execute) # call the python_scripting_engine()
        except Exception as e: # in case of error do following
            if global_variable.first_payload: # if this is first round of fuzzing then raise exception and close the fuzzing
                handle_unknown_exception(e)
                driver.quit()
                exit(0)
            sleep(3) # else retry two more times
            try:
                python_scripting_engine(driver,global_variable.python_to_execute)
            except:
                sleep(7)
                python_scripting_engine(driver,global_variable.python_to_execute)
    # Algorithm step: 7 Execute custom javascript code
    if not global_variable.javascript_to_execute == '\0': # if javascript code to execute is not null then do following
        sleep(0.3) # wait for some time
        try:
            driver.execute_script(global_variable.javascript_to_execute) # execute the javascript using driver object
        except JavascriptException as e: # if there is an error then do following
            if global_variable.first_payload: # if this is the first round of the fuzzing then raise exception and close the script
                handle_unknown_exception(e)
                driver.quit()
                exit(0)
            sleep(3) # else wait for sometime and retry two more times
            try:
                driver.execute_script(global_variable.javascript_to_execute)
            except JavascriptException:
                sleep(7)
                driver.execute_script(global_variable.javascript_to_execute)
    # Algorithm step: 8 if global_variable.args.no_css then remove css
    if global_variable.args.no_css:
        # Execute JavaScript to remove CSS
        driver.execute_script("""
            var styleElement = document.querySelector('style');
            if (styleElement) {
                styleElement.parentNode.removeChild(styleElement);
            }
        """)
    # Algorithm step: 9 delay the execution of script incase of --delay-before option is supplied
    if global_variable.args.delay_before:
        sleep(global_variable.args.delay_before)
    # Algorithm step: 10 if there are any buttons to press before fuzzing the form, press those buttons doing following
    if global_variable.args.buttons_to_press_before_fuzz:
        for button_to_press in global_variable.buttons_to_press_before_fuzz: # get single button which is to press
            press_button(driver,get_element(driver,button_to_press,True),True) # press that button
            sleep(0.3)
    # Algorithm step: 11 Remove common javascript validation
    if global_variable.args.auto_remove_javascript_validation:
        remove_javascript_validation(driver) # call the remove_javascript_validation() 
    # Algorithm step: 12 Remove javascript events if there are any to be removed
    if global_variable.args.disable_events:
        disable_js_events(driver)
    # Algorithm step: 13 Handle alert if it is present
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException: # if there is not alert then move on
        pass