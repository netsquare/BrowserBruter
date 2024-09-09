##################################################################
"""
Name  : signal_handler.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
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
from time import sleep # used for pausing the script


##################################################################
"""
Name          -> signal_handler
Functionality -> Function to Handle CTRL+C
Algorithm     ->
    1. wait for some time
    2. print the generic message
    3. get the reference of the global terminate flag
    4. set the global terminate flag as True
Parameters    -> signal(signal), frame
Return        -> 
"""
##################################################################
def signal_handler(signal, frame):
    sleep(3) # Algorithm step: 1 wait for 3 seconds
    # Algorithm step: 2 print the generic message
    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}CTRL+C pressed. Waiting for remaining request/response to stop. Exiting...\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    # Algorithm step: 3 get the reference of the global terminate flag
    global_variable.terminate = True # Algorithm step: 4. set the global terminate flag as True, Set the global termination flag to True so all threads can stop gracefully
