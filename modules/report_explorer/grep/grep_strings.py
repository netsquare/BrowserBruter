##################################################################
"""
Name  : grep_strings.py 
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
Name          -> grep_strings
Functionality -> Shows new columns for grep strings, find the strings in HTTP request/response, web page source code
Algorithm     ->
    1. Check greppables
    2. get the filter_columns
    3. for each greppables string, create a new column
    4. for greppable,
        a. count the appearance of string in every row
        b. add this count in that row of greppable column
    5. display data
Parameters    -> greppable, tree
Return        -> 
"""
##################################################################

# If user has entered the greppable values, count the occurences of those strings in data and display the occurrence coun
def grep_strings(greppables, tree):

    if not greppables:
        return

    # Define columns to filter for text
    filter_columns = ['Web Page Before', 'Web Page After', 'Response Headers', 'Response Body', 'URL']

    # Add greppable columns at the last position in the DataFrame and UI
    for greppable in greppables:
        re_global_variable.df = re_global_variable.df.assign(col_name=greppable)
        re_global_variable.df[greppable] = 0

    # Iterate over each greppable string
    for greppable in greppables:
        greppable_lower = greppable.lower()  # Convert greppable string to lowercase
        # Iterate over each row
        for index, row in re_global_variable.df.iterrows():
            # Convert content to lowercase before counting
            count = sum([str(row[col]).lower().count(greppable_lower) for col in filter_columns])
            # Update the value in the greppable column for the current row
            re_global_variable.df.at[index, greppable] = count

    # Update the display after processing all greppable strings
    display_data(re_global_variable.df, tree)
