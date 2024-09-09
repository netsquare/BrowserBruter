##################################################################
"""
Name  : show_context_menu_notebook.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.context_menu.create_context_menu import create_context_menu

##################################################################
"""
Name          -> show_context_menu_notebook
Functionality -> Shows context menu for notebook to copy selected text
Algorithm     ->
    1. Create and initialize context_menu 
    2. call post method on context_menu
Parameters    -> event, text_widget, root, tk
Return        -> 
"""
##################################################################

# show context menu for notebook to copy selected text
def show_context_menu_notebook(event, text_widget, root, tk):
    context_menu = create_context_menu(text_widget, root, tk)
    context_menu.post(event.x_root, event.y_root)
