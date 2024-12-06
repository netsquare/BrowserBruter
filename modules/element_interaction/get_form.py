##################################################################
"""
Name  : get_form.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import log_error

##################################################################
# Importing Python Libraries
##################################################################
from selenium.webdriver.common.by import By # used to found elements by various methods
from selenium.common.exceptions import NoSuchElementException
from traceback import format_exc, print_exc # used for getting the proper exceptions
from time import sleep
import sys

##################################################################
"""
Name          -> get_form
Functionality -> Function to get the form
Algorithm     ->
    1. Try to find the form using various techniques
    2. if form is not found then print the generic message and close the script
Parameters    -> driver(webdriver.Chrome), form(string)
Return        -> form(element)
"""
################################################################## 

def get_form(driver,form):
    try: # Algorithm step: 1 finding the form element
        return driver.find_element(By.ID, form) # by id
    except NoSuchElementException: # if not found by id then move on to the next methods 
        try:
            return driver.find_element(By.NAME, form) # by name
        except NoSuchElementException:
            try:
                return driver.find_element(By.CLASS_NAME, form) # by class
            except NoSuchElementException:
                try:
                    return driver.find_element(By.XPATH, form) # by xpath
                except NoSuchElementException:
                    try:
                        return driver.find_element(By.CSS_SELECTOR, form) # by css selector
                    except NoSuchElementException as e: # Algorithm step 2: if not found then do as per below
                        #if not found: # Algorithm step: 5 if element is not found then do below
                        global_variable.pause_event.clear()
                        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Specified form {form} is not found. Please verify the id, name, xpath or class of the form. For more information, check Error.txt or use --debug flag.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                        k = input(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Do you want to retry one more time? - Y/N\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                        global_variable.pause_event.clear()
                        if not (k in ('Y','y')):
                            global_variable.pause_event.clear()
                            if global_variable.args.debug: # if --debug flag is set then print the error on console
                                print_exc()
                            print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Refer Above Stack Trace\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                            driver.quit() # close the browser
                            log_error(format_exc()) # log the error in log file
                            sys.exit(0) # Exit from the script
                        else:
                            global_variable.pause_event.clear()
                            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Trying to find form -> {form}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                            sleep(10)
                            try: # Algorithm step: 1 finding the form element
                                return driver.find_element(By.ID, form) # by id
                            except NoSuchElementException: # if not found by id then move on to the next methods 
                                try:
                                    return driver.find_element(By.NAME, form) # by name
                                except NoSuchElementException:
                                    try:
                                        return driver.find_element(By.CLASS_NAME, form) # by class
                                    except NoSuchElementException:
                                        try:
                                            return driver.find_element(By.CSS_SELECTOR, form) # by css selector
                                        except NoSuchElementException as e:
                                            if global_variable.args.debug: # if --debug flag is set then print the error on console
                                                print_exc(e)
                                                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Refer Above Stack Trace\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                                            driver.quit() # close the browser
                                            log_error(format_exc()) # log the error in log file
                                            print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Specified element {form} is not found. Please verify the id, name, xpath or class of the form. For more information, check Error.txt or use --debug flag.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                                            sys.exit(0) # Exit from the script
                    #if found:
                        #break
                    #print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Specified element {global_variable.element} is not found. Please verify the name of the element. For more information, check Error.txt or use --debug flag.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                    #if global_variable.args.debug: # If --debug flag is set then print the exception
                        #print_exc()
                        #print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Refer Above Stack Trace\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                    #driver.quit() # Close the script
                    #log_error(format_exc())
                    #sys.exit(0)
