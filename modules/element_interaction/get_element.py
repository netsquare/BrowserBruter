##################################################################
"""
Name  : get_element.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.element_interaction.get_form import get_form
from modules.element_interaction.find_element import single_find_element_try
from modules.error_handling.error_handling import log_error
from modules.global_config_arguments.global_variables import global_variable
from modules.input_validation.remove_attributes import remove_attributes_and_get_focus

##################################################################
# Importing Python Libraries
##################################################################
from traceback import format_exc, print_exc # used for getting the proper exceptions
from time import sleep # Used to pause the script
import sys

##################################################################
"""
Name          -> get_element
Functionality -> Function to get element to be fuzzed
Algorithm     ->
    1. Check if the --form option is supplied and request is not coming from initial_operation method(), if yes then call the get_form() method to specify the selector variable
    2. else initialize the selector variable as driver.
    3. Create a found flag and initially set it as False
    4. for 30 times do following ( here 30 is retry count)
        a. call the single_find_element_try() to try to found the element
        b. if element is found then break out of the loop and move one
        c. if element is not found then wait for 5 seconds and retry
            1. if this is first round of fuzzing then do not wait just retry
    5. if element is not found then print generic message and quit
    6. if element is found then call remove_attributes_and_get_focus() method to remove attributes which can interrupt the fuzzing process from the element and put element on focus
    7. return the element
Parameters    -> driver(webdriver.Chrome), element(string), coming_from_initial_operations_method(boolean)
Return        -> element(element)
"""
################################################################## 

def get_element(driver,element,coming_from_initial_operations_method):
    # Algorithm step 1: 
    if global_variable.args.form and not coming_from_initial_operations_method:
        selector = get_form(driver,global_variable.args.form)
    else:  # Algorithm step: 2 set selector as driver
        selector = driver
    # Algorithm step: 3 set the found flag as False
    found = False
    #retry = True
    #while retry:
    # Algorithm step: 4
    for i in range(30): # retry 30 times
        # Algorithm step: 4.a Try to find the element by calling single_find_element_try()
        found, element = single_find_element_try(selector,element)
        if found: # Algorithm step: 4.b if element is found then break out of the loop
            break
        else: # Algorithm step: 4.c if element is not found then
            if global_variable.first_payload: # Algorithm step: 4.c.1 if this is first round of the fuzzing then do wait for 0.5 sec just retry
                found = False
                sleep(0.5)
            else: # else wait for some time and continue
                sleep(5)
    if not found: # Algorithm step: 5 if element is not found then do below
        global_variable.pause_event.clear()
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Specified element {element} is not found. Please verify the id, name, xpath or class of the element. For more information, check Error.txt or use --debug flag.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        k = input(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Do you want to retry one more time? - Y/N\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        global_variable.pause_event.clear()
        if k in ('Y', 'y'):
            global_variable.pause_event.clear()
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Trying to find element -> {element}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
            # Algorithm step: 4
            for i in range(30): # retry 30 times
                # Algorithm step: 4.a Try to find the element by calling single_find_element_try()
                found, element = single_find_element_try(selector,element)
                if found: # Algorithm step: 4.b if element is found then break out of the loop
                    break
                else: # Algorithm step: 4.c if element is not found then
                    found = False
                    sleep(1.5)
            if not found:
                if global_variable.args.debug: # if --debug flag is set then print the error on console
                    print_exc()
                    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Refer Above Stack Trace\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                driver.quit() # close the browser
                log_error(format_exc()) # log the error in log file
                sys.exit(0) # Exit from the script
        else:
            global_variable.pause_event.clear()
            print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Specified element {element} is not found. Please verify the id, name, xpath or class of the element. For more information, check Error.txt or use --debug flag.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
            if global_variable.args.debug: # if --debug flag is set then print the error on console
                print_exc()
                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Refer Above Stack Trace\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
            driver.quit() # close the browser
            log_error(format_exc()) # log the error in log file
            sys.exit(0) # Exit from the script
        
        #    retry = False
        #if found:
          #  break
        
    remove_attributes_and_get_focus(driver, element) # Algorithm step: 6 remove the input validation related attributes from the element and make it in focus
    return element # Algorithm step: 7 return the element
