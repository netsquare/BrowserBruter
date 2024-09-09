##################################################################
"""
Name  : filter_data.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.show_data.display_data import display_data
from modules.report_explorer.global_variables.global_variables import re_global_variable

##################################################################
"""
Name          -> filter_data
Functionality -> Filters report's HTTP request/response by looking the string into HTTP request/response
Algorithm     ->
    1. Check the filter_text
    2. Get the columns which contains data to match against filter string
    3. create new dataframe to hold filtered results
    4. for every column
        a. filter the data
    5. remove any duplicates
    6. display the filtered data
Parameters    -> filter_text, pd, tree
Return        -> 
"""
##################################################################

# Function to filter for text in specific columns and display the results
def filter_data(filter_text, pd, tree):
    if not filter_text:
        # If filter text is empty, display all data
        display_data(re_global_variable.df, tree)
        return

    # Define columns to filter for text
    filter_columns = ['URL','Web Page Before', 'Web Page After', 'Request Body', 'Request Headers', 'Response Headers', 'Response Body']
    # Create a new DataFrame to store the filtered results
    filtered_df = pd.DataFrame(columns=re_global_variable.df.columns)

    # Iterate over filter columns and filter the DataFrame
    for col in filter_columns:
        condition = re_global_variable.df[col].str.contains(filter_text, case=False, na=False)
        filtered_df = pd.concat([filtered_df, re_global_variable.df[condition]])

    # Remove duplicate rows from the filtered DataFrame
    filtered_df = filtered_df.drop_duplicates()
    # Display the filtered data in the Treeview
    display_data(filtered_df, tree)
