##################################################################
"""
Name  : split_report.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
"""
The block of code for --split-here start from here
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable

##################################################################
# Importing Python Libraries
##################################################################
import pandas as pd
from sys import exit

##################################################################
"""
Name          -> split_report
Functionality -> Function to split the report
Algorithm     ->
    1. if --split-report argument is passed then
        a. take the name of report to be split and store it in final_report and take number of rows in which report will be equally split, store that number into row_limit variable
        b. Converting the row_limit from string to integer
        c. Read the CSV file into a pandas DataFrame
        d. Split the DataFrame into chunks
        e. Write each chunk to a new CSV file
        f. Exit the script after splitting the report
Parameters    -> args
Return        -> 
"""
##################################################################

# Splitting the report
def split_report(args): # if --split-report argument is passed then
    final_report, row_limit = args.split_report.split(',') # take the name of report to be split and store it in final_report and take number of rows in which report will be equally split, store that number into row_limit variable
    row_limit = int(row_limit) # Converting the row_limit from string to integer
    df = pd.read_csv(final_report) # Read the CSV file into a pandas DataFrame
    chunks = [df[i:i+row_limit] for i in range(0, len(df), row_limit)] # Split the DataFrame into chunks
    # Write each chunk to a new CSV file
    for i, chunk in enumerate(chunks):
        output_file = f"{final_report}_{i}.csv" # Append index i to each newly created file
        chunk.to_csv(output_file, index=False) # Writing the chunk of final_report to a newly created small file
    exit(0) # Exit the script after splitting the report

##################################################################
"""
The block of code for --split-report ends here,
"""
##################################################################
