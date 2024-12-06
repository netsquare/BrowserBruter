##################################################################
"""
Name  : wait_and_handle_popup.py 
Date  : 13/03/2023
Author: Jafar Pathan 
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
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC # used to wait for all elements of web page are loaded
from selenium.webdriver.support.ui import WebDriverWait # used to wait for web page to fully load

##################################################################
"""
Name          -> wait_and_handle_popup
Functionality -> This function will handle the alert popup  
Algorithm     ->
    1. Create a instance of WebDriverWait() with 500 seconds timeout
    2. Puase the script and wait until all the elements has been fully loaded
    3. If there is any alert then handle it
Parameters    -> driver(webdriver.Chrome)
Return        -> 
"""
##################################################################

def wait_and_handle_popup(driver):
    wait = WebDriverWait(driver, 500) # Algorithm step: 1 wait is an instance of WebDriverWait with a timeout of 500 seconds
    try:
        wait.until(EC.presence_of_all_elements_located(("xpath", '//body'))) # Algorithm step: 2 Wait until all elements located by the XPath '//body' are present in the DOM
    except UnexpectedAlertPresentException: # Algorithm step: 3 If a popup appears before this condition is met, it will raise UnexpectedAlertPresentException
        if global_variable.args.pause_on_popup:
            global_variable.pause_event.set()
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} A POPUP is found, since you are using --pause-on-popup option, Browser Bruter is paused, kindly interact with popup and then press to ENTER to resume the Browser Bruter.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        else:
            try:
                alert = driver.switch_to.alert # Switch focus to the alert box
                alert.accept() # Accept the alert (click OK)
            except NoAlertPresentException: # Handle the case where no alert is present
                pass 
