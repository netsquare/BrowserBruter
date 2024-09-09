##################################################################
"""
Name  : load_csv.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable
from modules.report_explorer.grep.grep_strings import grep_strings
from modules.report_explorer.show_data.display_data import display_data

##################################################################
# Importing Python Libraries
##################################################################
from tkinter import filedialog
from tkinter import messagebox

##################################################################
"""
Name          -> load_csv
Functionality -> Function to load a CSV file and display its data
Algorithm     ->
    1. Open a file dialog to select a CSV file
    2. If a file is selected, read it into a Pandas DataFrame
    3. Set the 'Index' column as the DataFrame index
    4. Fill 'Index' column with sequential numbers starting from 0
    5. Replace incorrect or null values with 0
    6. If there are strings to grep, then call grep_strings
    7. else Display the data in the Treeview widget
    8. Handle any exceptions
Parameters    -> pd, tree
Return        -> 
"""
##################################################################


# Function to load a CSV file and display its data
def load_csv(pd, tree):
    # Open a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    try:
        # If a file is selected, read it into a Pandas DataFrame
        if file_path:
            re_global_variable.df = pd.read_csv(file_path)
            # Set the 'Index' column as the DataFrame index
            re_global_variable.df.set_index('Index', inplace=True)

            # Check if 'Index' column is empty
            if re_global_variable.df.index.isnull().all():
                # Fill 'Index' column with sequential numbers starting from 0
                re_global_variable.df['Index'] = range(len(re_global_variable.df))

            # Replace incorrect or null values with 0
            re_global_variable.df.fillna(0, inplace=True)

            re_global_variable.sort_order = {}
            if re_global_variable.greppables:
                grep_strings(re_global_variable.greppables, tree)
            else:
                # Display the data in the Treeview widget
                display_data(re_global_variable.df, tree)

    except pd.errors.EmptyDataError:
        # Handle empty file error
        messagebox.showerror("Error", "The selected file is empty.")
    except pd.errors.ParserError:
        # Handle parsing error
        messagebox.showerror("Error", "Error parsing the CSV file.")
