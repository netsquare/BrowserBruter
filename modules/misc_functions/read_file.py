##################################################################
"""
Name  : read_file.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
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
from traceback import format_exc # used for getting the proper exceptions
from sys import exit # used to close the script

##################################################################
"""
Name          -> read_file
Functionality -> Simple read file function, this function is only for generating dictionary based payloads  
Algorithm     ->
    1. try to open the file as read mode
    2. read the files and return lines individually as list
    3. if file not found then handle it
Parameters    -> file_path(string)
Return        -> 
"""
##################################################################

def read_file(file_path):
    try: # Algorithm step: 1. try to open the file as read mode
        with open(file_path,'r') as file: # Algorithm step 2: read the files and return lines individually as list
              return file.read().splitlines()
    except FileNotFoundError as e: # Algorithm step: 3 if file not found then handle it
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}The specified payloads file '{file_path}' does not exist.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        log_error(format_exc()) # log the error
        exit(0) # exit the script