##################################################################
"""
Name  : ignore_keyboard.py 
Date  : 21/06/2023
Author: Jafar Pathan 
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.copy.copy_text import copy_text

##################################################################
"""
Name          -> ignore_keyboard
Functionality -> Ignore keyboard so the HTTP request/response and web page source is not editable
Algorithm     ->
    1. if CTRL+C is pressed then copy the text
    2. if CTRL+A is the select all
    3. ignore all other keys
Parameters    -> event, text_widget, root, tk
Return        -> 
"""
##################################################################

# Function to ignore keyboard events (used for copying text)
def ignore_keyboard(event, text_widget, root, tk):
    if (event.state & 4) != 0:  # Check if the Ctrl key is pressed
        if event.keysym == 'c':
            copy_text(None, text_widget, root, tk)
            return 'break'
        elif event.keysym == 'a':
            text_widget.tag_add(tk.SEL, '1.0', tk.END)
            text_widget.mark_set(tk.INSERT, '1.0')
            text_widget.see(tk.INSERT)
            return 'break'
    return