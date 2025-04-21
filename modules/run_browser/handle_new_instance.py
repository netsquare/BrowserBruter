##################################################################
"""
Name  : handle_new_instance.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.run_browser.get_and_initialize_driver import get_and_initialize_chrome_driver

##################################################################
# Importing Python Libraries
##################################################################
from lib.seleniumwire.undetected_chromedriver.v2 import ChromeOptions # undetected chrome driver, used to evade anti bot defences

##################################################################
"""
Name          -> handle_new_instance
Functionality -> Function to handle --new-instance option
Algorithm     ->
    1. first close the current browser
    2. Start new browser and initialize the driver object again with this new browser
    3. Navigate to url
    4. return the newly initialized driver object associated with newly started browser
Parameters    -> driver(webdriver.Chrome)
Return        -> driver(webdriver.Chrome)
"""
################################################################## 

def handle_new_instance(driver):
    driver.quit() # Algorithm step: 1 first close the current browser
    driver = get_and_initialize_chrome_driver() # Algorithm step: 2 initialize new driver object by launching new browser
    # Following lines solves the bug in which the --new-instance was not working
    driver.get(global_variable.args.target) # Algorithm step: 3 navigate to target url
    return driver # Algorithm step: 4 return the driver object