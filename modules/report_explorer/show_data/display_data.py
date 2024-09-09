##################################################################
"""
Name  : display_data.py 
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
Name          -> display_data
Functionality -> Shows data in Treeview widget
Algorithm     ->
    1. Check if 'Index' column is present in the DataFrame
    2. If 'Index' column is missing, reset the index
    3. Clear existing data in the Treeview
    4. Get the sorted index of the DataFrame
    5. Insert data from the DataFrame into the Treeview using the sorted index
Parameters    -> dataframe, tree
Return        -> 
"""
##################################################################

# Function to display data in the Treeview widget
def display_data(dataframe, tree):
    # Check if 'Index' column is present in the DataFrame
    if 'Index' not in dataframe.columns:
        # If 'Index' column is missing, reset the index
        dataframe.reset_index(drop=False, inplace=True)
    # Clear existing data in the Treeview
    tree.delete(*tree.get_children())
    # Get the sorted index of the DataFrame
    sorted_index = dataframe.index.tolist()
    # Insert data from the DataFrame into the Treeview using the sorted index
    for index in sorted_index:
        item_id = str(index)
        values = [dataframe.at[index, col] for col in re_global_variable.columns]
        tree.insert("", "end", iid=item_id, values=values)
