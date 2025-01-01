##################################################################
"""
Name  : remove_attributes.py 
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
from time import sleep # Used to pause the script
from selenium.common.exceptions import StaleElementReferenceException

##################################################################
"""
Name          -> remove_attributes_and_get_focus
Functionality -> Function to Remove attributes this is created to reduce code in attempt function
Algorithm     ->
    1. Remove various attributes which are related to input validation
    2. in case of error retry one more time
    3. else move on if error is occured again
Parameters    -> driver(webdriver.Chrome), element(HTML Element)
Return        -> 
"""
##################################################################     

def remove_attributes_and_get_focus(driver, element):
    # Algorithm step: 1 remove the attributes which can cause the interruption in fuzzing as they are related to input validation
    try:
        driver.execute_script("arguments[0].removeAttribute('pattern');",element) # remove pattern
        driver.execute_script("arguments[0].removeAttribute('min');",element) # remove min
        driver.execute_script("arguments[0].removeAttribute('max');",element) # remove max
        driver.execute_script("arguments[0].removeAttribute('maxlength');",element) # remove maxlength
        driver.execute_script("arguments[0].removeAttribute('minlength');",element) # remove minlength
        driver.execute_script("arguments[0].removeAttribute('readonly');",element) # remove readonly
        driver.execute_script("arguments[0].removeAttribute('autocomplete');",element) # remove autocomplete
        driver.execute_script("arguments[0].removeAttribute('disabled');",element) # remove disabled
        driver.execute_script("arguments[0].removeAttribute('hidden');",element) # remove hidden
        driver.execute_script("arguments[0].scrollIntoView(true);", element) # remove true
        driver.execute_script("arguments[0].setAttribute('willValidate', false);", element) # set willValidate to false
        driver.execute_script("arguments[0].focus();", element) # focus on the element
    except StaleElementReferenceException: # Algorithm step: 2 if there is a StaleElementReferenceException then retry
        sleep(2)
        try:
            driver.execute_script("arguments[0].removeAttribute('pattern');",element)
            driver.execute_script("arguments[0].removeAttribute('min');",element)
            driver.execute_script("arguments[0].removeAttribute('max');",element)
            driver.execute_script("arguments[0].removeAttribute('maxlength');",element)
            driver.execute_script("arguments[0].removeAttribute('minlength');",element)
            driver.execute_script("arguments[0].removeAttribute('readonly');",element)
            driver.execute_script("arguments[0].removeAttribute('autocomplete');",element)
            driver.execute_script("arguments[0].removeAttribute('disabled');",element)
            driver.execute_script("arguments[0].removeAttribute('hidden');",element)
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            driver.execute_script("arguments[0].setAttribute('willValidate', false);", element) # set willValidate to false
            driver.execute_script("arguments[0].focus();", element)
        except StaleElementReferenceException: # Algorithm step: 3 move on if error keeps occurring
            pass