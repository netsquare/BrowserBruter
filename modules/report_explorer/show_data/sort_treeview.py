##################################################################
"""
Name  : sort_treeview.py 
Date  : 21/06/2023
Author: Jafar Pathan 
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
Name          -> sort_treeview
Functionality -> Function to sort the Treeview based on the selected column
Algorithm     ->
    1. Determine the sorting order for the column
    2. Sort the DataFrame based on the selected column and order
    3. Display the sorted data in the Treeview
    4. Handle KeyError
Parameters    -> column, tree
Return        -> 
"""
##################################################################

# Function to sort the Treeview based on the selected column
def sort_treeview(column, tree):
    try: 

        # Determine the sorting order for the column
        if column not in re_global_variable.sort_order:
            re_global_variable.sort_order[column] = 'asc'
        elif re_global_variable.sort_order[column] == 'asc':
            re_global_variable.sort_order[column] = 'desc'
        else:
            re_global_variable.sort_order.pop(column)

        # Sort the DataFrame based on the selected column and order
        re_global_variable.df = re_global_variable.df.sort_values(by=column, ascending=(re_global_variable.sort_order[column] == 'asc')).reset_index(drop=True)
        # Display the sorted data in the Treeview
        display_data(re_global_variable.df, tree)
    except KeyError:
        pass
