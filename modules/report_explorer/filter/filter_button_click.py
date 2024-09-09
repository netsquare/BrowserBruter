##################################################################
"""
Name  : filter_button_click.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
from tkinter.simpledialog import askstring

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable
from modules.report_explorer.filter.filter_data import filter_data

##################################################################
"""
Name          -> filter_button_click
Functionality -> Get's the filter string from user
Algorithm     ->
    1. Show the popup to get string form user
    2. call filter_data() method and pass the filter string
Parameters    -> pd, tree
Return        -> 
"""
##################################################################

# Function to handle the click event of the filter button
def filter_button_click(pd, tree):
    # Prompt the user to enter filter text
    filter_text = askstring("filter", "Enter filter text:")
    if filter_text is not None:
        # Perform the filter and display the results
        filter_data(filter_text, pd, tree)
