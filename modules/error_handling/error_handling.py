##################################################################
"""
Name  : error_handling.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable

##################################################################
# Importing Python Libraries
##################################################################
import datetime
from traceback import format_exc, print_exc # used for getting the proper exceptions

##################################################################
"""
Name          -> handle_unknown_exception
Functionality -> Handle Unknown Exception  
Algorithm     ->
    1. Check --debug flag
        a. if this flag is set then print the exception by calling print_exc() method
        b. Print the generic console message
    2. Else just print the generic console message
    3. log the exception if Error.txt file by calling log_error() method
Parameters    -> exception(Exception)
Return        -> 
"""
##################################################################

def handle_unknown_exception(exception):
    if global_variable.args.debug: # Algorithm step: 1 Check --debug flag
        print_exc() # Print the exception
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}An unknown error has been occured, Please open issue request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    else: # Algorithm step: 2 print generic error message
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}An unknown error has been occured, Please refer logs/Error.txt or use --debug flag.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    log_error(format_exc()) # Algorithm step: 3 Log the exception

##################################################################
"""
Name          -> log_error
Functionality -> Function to log errors 
Algorithm     ->
    1. open the Error.txt file in append mode name it as error_log_file
    2. Get the current time
    3. log the error with various details
    4. Print generic message if file is not found
Parameters    -> error(string)
Return        -> 
"""
##################################################################  

def log_error(error):
    try:
        with open("logs/Error.txt","a") as error_log_file: # Algorithm step: 1 Open the log/Error.txt file
            error_time = datetime.datetime.now() # Algorithm step: Get the current time
            error_time = error_time.strftime("%Y-%m-%d_%H-%M-%S") # Convert the raw time in proper format
            # Algorithm step: 3 log the error with various details
            error_log_file.write(f"\n[+]--------------------------------------------------------------------------------------------------------------------------[+]\n")
            error_log_file.write(f"Error Time - {error_time}") # Print the Error time
            error_log_file.write("\n[+]--------------------------------------------------------------------------------------------------------------------------[+]\n")
            error_log_file.write(error) # Print the error message
    except FileNotFoundError as e: # Algorithm step: 4 For any reason if file is not found then throw the generic message
        print("Error: Logging file not found.")
