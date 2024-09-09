##################################################################
"""
Name  : auto_remove.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # Used to pause the script

##################################################################
"""
Name          -> remove_javascript_validation
Functionality -> Function to remove javascript input validation by overriding common methods
Algorithm     ->
    1. wait for some time
    2. Using javascript override various javascript in-built methods which are commonly used for input validation 
Parameters    -> driver(webdriver.Chrome)
Return        -> 
"""
################################################################## 

def remove_javascript_validation(driver):
    # Algorithm step 1 wait for sometime
    sleep(0.3)
    # Algorithm step:2. Using javascript override various javascript in-built methods which are commonly used for input validation 
    driver.execute_script("""
        String.prototype.match = function() {
            return ["123"];
        };
        String.prototype.replace = function() {
            return true;
        };
        String.prototype.replace = function(String,String) {
            return true;
        };
        String.prototype.replace = function(RegExp,String) {
            return true;
        };
        String.prototype.replace = function(RegExp,RegExp) {
            return true;                
        };
        RegExp.prototype.test = function() {
            return true;    
        };
        Number.isInteger = function(value) {
            return true;
        };
        Number.isNaN = function(value) {
            return false;
        };
""")