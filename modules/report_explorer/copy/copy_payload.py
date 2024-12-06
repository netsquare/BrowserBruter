##################################################################
"""
Name  : copy_payload.py 
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
Name          -> copy_payload
Functionality -> Copies payload from selected row to clipboard
Algorithm     ->
    1. get the selected row
    2. get payload field's value from that row
    3. copy that to clipboard
Parameters    -> tree, root
Return        -> 
"""
##################################################################

# Function to copy payload from selected row
def copy_payload(tree, root):
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)
        payload = re_global_variable.df.at[index, 'Payload']
        root.clipboard_clear()
        root.clipboard_append(payload)
