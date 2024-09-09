##################################################################
"""
Name  : global_variables.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.arguments_parser import get_args

##################################################################
# Importing Python Libraries
##################################################################
import pandas as pd

##################################################################
"""
Name          -> Global_Variable_Class
Functionality -> Creates a object which contains global variables
"""
##################################################################

class Global_Variable_Class:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Global_Variable_Class, cls).__new__(cls)

            cls._instance.args = get_args()
            cls._instance.greppables = []
            if cls._instance.args.grep:
                # Get Greppable values from user
                cls._instance.greppables = cls._instance.args.grep.split(',')

            # Create a Pandas DataFrame to store the data
            cls._instance.df = pd.DataFrame()

            # Define dictionaries and lists for sorting and managing data
            cls._instance.sort_order = {}
            cls._instance.columns = ['Index', 'Request Time', 'Fuzzing', 'Payload', 'Method', 'URL',
                        'Response Time', 'Cycle Time MilliSeconds',
                       'Response Status Code', 'Response Length']

            # Append greppable columns
            for greppable in cls._instance.greppables:
                cls._instance.columns.append(greppable)

        return cls._instance

re_global_variable = Global_Variable_Class()
