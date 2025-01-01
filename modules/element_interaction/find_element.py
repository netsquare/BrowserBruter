##################################################################
"""
Name  : find_element.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.common.by import By # used to found elements by various methods

##################################################################
"""
Name          -> single_find_element_try
Functionality -> This function is created two call this two times in case of slow loading of web page
Algorithm     ->
    1. try to find the element using various techniques
    2. return False if element is not found and return element(string)
    3. return True and the element is it is found
Parameters    -> selector(string), element(string)
Return        -> (boolean), element(element)
"""
################################################################## 

def single_find_element_try(selector,element):
    try: # Algorithm step: 1
        # user has provided custom attribute using '++' then find it using that particular attribute
        if "++" in element:
            element_to_found, attribute = element.split('++')
            #print("1")
            #print(element_to_found)
            #print(attribute)
            xpath = f'//*[@{attribute}="{element_to_found}"]' # Construct the XPath
            #print("2")
            element_to_found = selector.find_element(By.XPATH, xpath) # find the element using custom attribute
            #print("3")
            element = element_to_found
            #print("found it")
        else:
            element = selector.find_element(By.ID, element) # by id
    except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException): # if element is not found in previous search move on to the next method to find the element
        try:
            element = selector.find_element(By.NAME, element) # by name
        except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):
            try:
                element = selector.find_element(By.CLASS_NAME, element) # by class
            except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):
                try: 
                    element = selector.find_element(By.CSS_SELECTOR,element) # by css selector
                except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):
                    try:
                        element = selector.find_element(By.XPATH,f"//input[@value='{element}']") # by input
                    except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):
                        try:
                            element = selector.find_element(By.XPATH,f"//input[@Type='{element}']") # by input type
                        except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):
                            try:
                                element = selector.find_element(By.XPATH,f"//textarea[@value='{element}']") # by text area value
                            except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):    
                                try:
                                    element = selector.find_element(By.XPATH,f"//button[@value='{element}']") # by button value
                                except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):
                                    try:
                                        element = selector.find_element(By.XPATH,f"//button[@Type='{element}']") # by button type
                                    except (InvalidSelectorException, NoSuchElementException, StaleElementReferenceException):
                                        return False, element # Algorithm step 2 element is not found, return the element(string) and False
    return True, element # Algorithm step 3 element is found, return the element and True
