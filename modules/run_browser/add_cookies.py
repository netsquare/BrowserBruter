##################################################################
"""
Name  : add_cookies.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import handle_unknown_exception, log_error # to handle and log the error

##################################################################
# Importing Python Libraries
##################################################################
from traceback import format_exc # used to format the exception
from sys import exit # used to close the script

##################################################################
# Importing Exception
##################################################################
from selenium.common.exceptions import InvalidCookieDomainException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import InvalidCookieDomainException
from selenium.common.exceptions import InvalidArgumentException


##################################################################
"""
Name          -> add_cookies
Functionality -> Function to add cookies into selenium session
Algorithm     ->
    1. First delete all present cookies if any
    2. Get the cookies from --cookie options and store them in cookie list
    3. for all cookies present in cookies list do following
        a. split them into name:value pair
        b. create a dictionary to hold the cookie
        c. add this dictionary as cookie into browser
    4. If there is InvalidArgumentException then do following 
        a. if this error is due to domain, then create cookie without domain name, it will be set to default value which is current web page
        b. else handle the unknown exception
    5. If there InvalidCookieDomainException then do step4.a
    6. If there is ValueError then handle it
Parameters    -> driver(webdriver.Chrome)
Return        -> 
"""
##################################################################

def add_cookies(driver):
    try:
        # Algorithm step: 1 Delete any existing cookies and assign initial cookies
        driver.delete_all_cookies()
        cookies_list = global_variable.args.cookie.split(',') # Algorithm step: 2 get the cookies from --cookie
        for cookie_arg in cookies_list: # Algorithm step: 3 for all cookies do below 
            # Algorithm step: 3.a Get the cookie data
            name, value = cookie_arg.split(":")
            # Algorithm step: 3.b Create cookie dictionary as selenium requires them in dictionary format
            cookie_dict = {
                "name": name,
                "value": value,
                "domain": global_variable.hostname
            }
            # Algorithm step: 3.c add cookie into browser
            driver.add_cookie(cookie_dict)  
    except InvalidArgumentException as e: # Algorithm step: 4 handle InvalidArgumentException
            # Algorithm step: 4.a remove domain if error is due to invalid 'domain'
            if "invalid argument: invalid 'domain'" in str(e):
                cookie_dict = {
                    "name": name,
                    "value": value
                }
                # Add the cookie without domain to current page
                driver.add_cookie(cookie_dict)
            else: # Algorithm step: 4.b throw error 
                handle_unknown_exception(e)
                driver.quit()
                exit(0)
    except InvalidCookieDomainException as e: # Algorithm step: 5 remove 'domain' from cookie and add it to current page
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Cookie Domain is invalid -> {cookie_dict} -> Skipping adding domain\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        cookie_dict = {
                    "name": name,
                    "value": value
                }
        try:
            driver.add_cookie(cookie_dict) # add cookie
        except InvalidCookieDomainException:
            print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Cookie Domain is invalid -> {cookie_dict} -> Kindly check the domain of the cookie, the BrowserBruter tried to skip it but server returned some unknown error. Kindly recheck the domain name.[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        log_error(format_exc())                
    except ValueError as e: # Algorithm step: 6 handle ValueError
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} You have entered arguments in invalid format -> {global_variable.args.cookie} please read help message for valid format of passing cookies. Closing the Fuzzing process\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        driver.quit()
        log_error(format_exc())
        exit(0)