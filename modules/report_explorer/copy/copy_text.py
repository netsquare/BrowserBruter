##################################################################
"""
Name  : copy_text.py 
Date  : 21/06/2023
Author: Jafar Pathan 
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable

##################################################################
"""
Name          -> copy_text
Functionality -> Copies selected text from HTTP request/response and web page before/after
Algorithm     ->
    1. Get the selected_text
    2. Copy the selected_text to clipboard
Parameters    -> event, text_widget, root, tk
Return        -> 
"""
##################################################################

# Copy text from notebook
def copy_text(event, text_widget, root, tk):
    selected_text = text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
    if selected_text:
        root.clipboard_clear()
        root.clipboard_append(selected_text)