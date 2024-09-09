##################################################################
"""
Name  : clear_filter.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable
from modules.report_explorer.show_data.display_data import display_data

##################################################################
"""
Name          -> clear_filter
Functionality -> Reloads the report withouth any filters
Algorithm     ->
    1. call display_data method
Parameters    -> tree
Return        -> 
"""
##################################################################

# Function to clear the filter results and display all data
def clear_filter(tree):
    display_data(re_global_variable.df, tree)
