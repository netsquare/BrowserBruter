##################################################################
"""
Name  : disable_js_events.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import handle_unknown_exception

##################################################################
# Importing Python Libraries
##################################################################
from selenium.common.exceptions import JavascriptException
from time import sleep # Used to pause the script
from sys import exit # used to close the script

##################################################################
"""
Name          -> disable_js_events
Functionality -> Function to disable any js events specified by user
Algorithm     ->
    1. for each event to be disabled do as per below 
        a. inject javascript which will disable that event
        b. if there is exception then retry this one more time
        c. if there is still exception then throw the unknown_exception
Parameters    -> driver(webdriver.Chrome)
Return        -> 
"""
################################################################## 
def disable_js_events(driver):
    for event_name in global_variable.disable_events: # Algorithm step: 1 for each event to disable do as per below 
        try:
            # Algorithm step: 1.a Inject JavaScript to disable the event
            disable_event_script = f"""
                document.addEventListener("{event_name}", function(event) {{
                event.stopImmediatePropagation();
                event.preventDefault();
            }}, true);
            """
            driver.execute_script(disable_event_script) # execute the javascript using driver to disable the javascript event
        except JavascriptException as e: # Algorithm step: 1.b if there is an error then do following
            sleep(3) # wait for some time
            try:
                # Inject JavaScript to disable the event
                disable_event_script = f"""
                    document.addEventListener("{event_name}", function(event) {{
                    event.stopImmediatePropagation();
                    event.preventDefault();
                }}, true);
                """
                driver.execute_script(disable_event_script) # execute javascript to disable the event
            except Exception as e: # Algorithm step: 1.c if there is again error then 
                handle_unknown_exception(e) # call handle_unknown_exception()
                driver.quit() # close the browser
                exit(0) # close the script

