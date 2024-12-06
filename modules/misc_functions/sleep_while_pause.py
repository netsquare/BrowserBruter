##################################################################
"""
Name  : sleep_while_pause.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # Used to pause the script

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable

##################################################################
"""
Name          -> sleep_while_pause
Functionality -> Function to sleep while pause
Algorithm     ->
    1. if pause event is set then 
        a. while pause event is set then
            1. pause the script for 1 second
Parameters    -> 
Return        -> 
"""
##################################################################  

def sleep_while_pause():
    if global_variable.pause_event.is_set(): # Algorithm step:1. if pause event is set then 
        while global_variable.pause_event.is_set(): # Algorithm step: 1.a. while pause event is set then
            sleep(1) # Algorithm step: 1.a.1 pause the script for 1 second