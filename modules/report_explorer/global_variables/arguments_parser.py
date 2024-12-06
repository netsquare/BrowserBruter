##################################################################
"""
Name  : arguments_parser.py 
Date  : 21/06/2023
Author: Jafar Pathan 
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
import argparse

##################################################################
"""
The block of code for processing arguments starts from here
"""
##################################################################
def get_args():
    # Getting argument parser to parse and process arguments
    argParser = argparse.ArgumentParser(description="The Report Explorer, BrowserBruter's report exploring utility.",formatter_class=argparse.RawTextHelpFormatter)

    args_report = argParser.add_argument_group("Options") # Arranging the arguments in options group

    args_report.add_argument("--report",help="Path of final report to explore",metavar="BrowserBruter_Reports/localhost/2024-03-09_13-48-24/localhost-2024-03-09_13-48-24.csv") # Adding --report argument
    args_report.add_argument("--grep",help="Comma separated list of words or strings to be grepped and display from the HTTP traffic and web page source code.",metavar="error,exception,success,admin") # Adding --grep argument
    args_report.add_argument("--split-report",help="Split the large final report into smaller reports by specifying the maximum limit of rows in single file.",metavar="/path/to/file.csv,200") # Adding --split-report argument

    # Getting the arguments in args variable
    args = argParser.parse_args()

    return args

##################################################################
"""
The block of code for processing arguments ends here
"""
##################################################################