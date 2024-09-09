
##################################################################
"""
Name  : pse1.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from selenium.webdriver.common.by import By # used to found elements by various methods
import re # used to extract import statements from the user supplied code

##################################################################
"""
Name          -> python_scripting_engine
Functionality -> Function to execute python code
Algorithm     ->
    1. create dictionary to hold driver object
    2. execute python code using exec() method and pass the driver object to it
[NOTE: User has to import any libraries by themselves in custom code]
Parameters    -> driver(webdriver.Chrome), python_code(string)
Return        -> 
"""
##################################################################

def python_scripting_engine(driver, python_code):
    # Algorithm step:1 create dictionary to hold driver object
    pass_driver_object = {
        'driver': driver
    }
    # Extract and execute import statements
    import_statements = re.findall(r'^\s*import .+$|^\s*from .+ import .+$', python_code, re.MULTILINE)
       # Execute import statements in the global scope
    for statement in import_statements:
        exec(statement, globals())

    # Remove import statements from the original python_code
    code_without_imports = re.sub(r'^\s*import .+$|^\s*from .+ import .+$', '', python_code, flags=re.MULTILINE)

    # Algorithm step: 2 execute the remaining python code using exec() method and pass the driver object to it
    exec(code_without_imports, globals(), pass_driver_object)