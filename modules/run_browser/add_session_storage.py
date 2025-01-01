##################################################################
"""
Name  : add_local_storage.py 
Date  : 18/12/2024
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import handle_unknown_exception # to handle and log the error

##################################################################
# Importing Python Libraries
##################################################################

##################################################################
# Importing Exception
##################################################################



##################################################################
"""
Name          -> add_local_storage
Functionality -> Function to add local storage in browser
Algorithm     ->
Parameters    -> driver(webdriver.Chrome)
Return        -> 
"""
##################################################################

def add_session_storage(driver):
    try:
        storage_list = global_variable.args.add_session_storage.split('++')
        for key_value_pair in storage_list: # Algorithm step: 3 for all key:value do below 
            # Algorithm step: 3.a Get the key:value data
            key, value = key_value_pair.split(":",1)
            driver.execute_script(f"window.sessionStorage.setItem('{key}', '{value}');")
            # DEBUG purpose
            #stored_value = driver.execute_script(f"return window.localStorage.getItem('{key}');")
            #print(f"stored value:{stored_value}")
            # Algorithm step: 3.c add key:value into browser
            #driver.add_key:value(key:value_dict)  
    except Exception as e:
        print(e)
        handle_unknown_exception(e)
        
    #except InvalidArgumentException as e: # Algorithm step: 4 handle InvalidArgumentException
            # Algorithm step: 4.a remove domain if error is due to invalid 'domain'
            #if "invalid argument: invalid 'domain'" in str(e):
             #   key:value_dict = {
             #       "name": name,
             #       "value": value
             #   }
                # Add the key:value without domain to current page
             #   driver.add_key:value(key:value_dict)
            #else: # Algorithm step: 4.b throw error 
            #    handle_unknown_exception(e)
            ##    driver.quit()
            #    exit(0)
    #except Invalidkey:valueDomainException as e: # Algorithm step: 5 remove 'domain' from key:value and add it to current page
    #    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} key:value Domain is invalid -> {key:value_dict} -> Skipping adding domain\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    #    key:value_dict = {
    #                "name": name,
    #                "value": value
    #            }
    #    try:
    #        driver.add_key:value(key:value_dict) # add key:value
    #    except Invalidkey:valueDomainException:
    #        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} key:value Domain is invalid -> {key:value_dict} -> Kindly check the domain of the key:value, the BrowserBruter tried to skip it but server returned some unknown error. Kindly recheck the domain name.[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    #    log_error(format_exc())                
    ##except ValueError as e: # Algorithm step: 6 handle ValueError
     #   print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} You have entered arguments in invalid format -> {global_variable.args.key:value} please read help message for valid format of passing key:values. Closing the Fuzzing process\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
     #   driver.quit()
     #   log_error(format_exc())
     #   exit(0)