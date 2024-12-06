##################################################################
"""
Name  : pause_menu.py 
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
from modules.pause_and_stop.signal_handler import signal_handler

##################################################################
# Importing Python Libraries
##################################################################
from traceback import format_exc # used for getting the proper exceptions
from pytimedinput import timedKey # used for pausing and resuming the browser bruter tool
import signal # used for handling CTRL+C key
from sys import exit # used to close the script

##################################################################
"""
Name          -> pause_resume
Functionality -> Function to run in a separate thread to pause and resume the browserbruter if user presses enter key
Algorithm     ->
    1. while the global_variable.terminate flag is not set, do following
        a. Get the key pressed by user
        b. set the pause event
        c. Print the pause menu and wait for input from user
        d. store the user input into variable called 'k'
        e. if k is y or Y then enter into interactive mode
            if k is v or V enable or disable the verbosity
        f. else get out of the interactive mode
        g. clear the global_variable.pause_event
    3. if there is any error then handle it
Parameters    -> 
Return        -> 
"""
##################################################################

def pause_resume():
    try:
        while not global_variable.terminate: # Algorithm step: 2. while the global_variable.terminate flag is not set, do following
            userText, timeout = timedKey(prompt="", timeout=-1, resetOnInput=True) # Constantly look for user input
            if not (timeout):
                global_variable.pause_event.set()  # Algorithm step: 2.b Set the pause event
                # Algorithm step: 2.c print the pause menu
                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nWARNING: {global_variable.RESET}BROWSERBRUTER IS PAUSED\npress ENTER to resume\nPress y to Enter Interactive Mode\nPress n to Exit Interactive Mode\nPress v to enable verbosity\nPress V to decrease the verbosity\nPress CTRL+C to exit\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                k = input() # Algorithm step: 2.d store the user input in k
                if k == 'Y' or k == 'y': # Algorithm step: 2.e check if user has entered y
                    global_variable.args.interactive = True # Enable interactive mode
                elif k == 'N' or k == 'n': # Algorithm step: 2.f 
                    global_variable.args.interactive = False # Algorithm step: 2.f get out of the interactive mode
                elif k == 'v': # if k is V then enable the verbosity
                    global_variable.args.verbose = True # enable the verbosity
                elif k == 'V': # if k is v then disable the verbosity
                    global_variable.args.verbose = False # disable the verbosity
                global_variable.pause_event.clear()  # Algorithm step: 2.g Clear the pause event 
                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nWARNING: {global_variable.RESET}Resuming BROWSERBRUTER\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    except KeyboardInterrupt as e: # Algorithm step: 3 handle the exception this exception occurs when user keeps pressing CTRL+C CTRL+C multiple times
        signal_handler(signal.SIGINT, None) # handle the keyboard interrupt
        log_error(format_exc()) # log the error
        exit(0) # exit the script
