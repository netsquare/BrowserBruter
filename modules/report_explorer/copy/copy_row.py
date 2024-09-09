##################################################################
"""
Name  : copy_row.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable

##################################################################
"""
Name          -> copy_row
Functionality -> Copies whole row's data to clipboard
Algorithm     ->
    1. get the selected row
    2. copy the row data one by one on clipboard
Parameters    -> tree, root
Return        -> 
"""
##################################################################

# Function to copy whole selected row
def copy_row(tree,root):
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)
        # Exclude 'Index' column when copying the row
        row_data = [f"\n\n[+]-------------------------------------------[+]\n{col}\n[+]-------------------------------------------[+]\n\n{re_global_variable.df.at[index, col]}" for col in re_global_variable.columns[1:]]
        row_string = "\n".join(row_data)
        root.clipboard_clear()
        root.clipboard_append(row_string)