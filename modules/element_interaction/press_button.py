##################################################################
"""
Name  : press_button.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # Used to pause the script
from sys import exit # used to close the script
from traceback import format_exc, print_exc # used for getting the proper exceptions
from selenium.common.exceptions import ElementClickInterceptedException

##################################################################
# Importing Custom Modules
##################################################################
from modules.error_handling.error_handling import log_error
from modules.global_config_arguments.global_variables import global_variable

##################################################################
"""
Name          -> press_button
Functionality -> Function to press the button
Algorithm     -> 
    1. if --press-enter-no-click is set and this method is not called from buttons_to_press() method then send '\n' keystroke to press the enter
    2. else click on the button 
    3. if there is an error then retry three more times
    4. if there is error again the close the script 
Parameters    -> driver(webdriver.Chrome), button(element), from_buttons_to_press(boolean)
Return        -> 
"""
################################################################## 

def press_button(driver,button,from_buttons_to_press):
    try:
        # Algorithm step:1. if --press-enter-no-click is set and this method is not called from buttons_to_press() method then send '\n' keystroke to press the enter
        if global_variable.args.press_enter_no_click and not from_buttons_to_press:
            button.send_keys("\n") # send ENTER or in other words '\n' new line keystroke
        else: # Algorithm step: 2 click on the button
            button.click() # clicking the button
    except ElementClickInterceptedException as e: # Algorithm step: 3 if there is an error then do following
        sleep(3) # wait for some time
        try: # retry one more time
            if global_variable.args.press_enter_no_click and not from_buttons_to_press:
                button.send_keys("\n")
            else:
                button.click()
        except ElementClickInterceptedException as e: # retry third time
            sleep(6)
            try:
                if global_variable.args.press_enter_no_click and not from_buttons_to_press:
                    button.send_keys("\n")
                else:
                    button.click()
            except ElementClickInterceptedException as e: # Algorithm step: 4 if error again then do following 
                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}The button -> {button} is not clickable or click has been intercepted by some other element, there might be some javascript being executed on web page which is preventing the click. Please remove the code intercepting the click.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                if global_variable.args.debug: # if --debug is set then print the exception on console
                    print_exc()
                    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Refer Above Stack Trace\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                log_error(format_exc()) # log the error
                driver.quit() # close the browser
                exit(0) # exit the script

