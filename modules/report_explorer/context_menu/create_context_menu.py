##################################################################
"""
Name  : create_context_menu.py 
Date  : 21/06/2023
Author: Jafar Pathan 
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable
from modules.report_explorer.copy.copy_text import copy_text

##################################################################
"""
Name          -> create_context_menu
Functionality -> Create Context Menu and return it
Algorithm     ->
    1. Create and initialize context_menu 
    2. add command in context_menu and add copy_text() method
    3. return context_menu
Parameters    -> text_widget, root, tk
Return        -> context_menu
"""
##################################################################

# Same function required to copy text form notebook
def create_context_menu(text_widget, root, tk):
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Copy", command=lambda: copy_text(None, text_widget, root, tk))
    return context_menu