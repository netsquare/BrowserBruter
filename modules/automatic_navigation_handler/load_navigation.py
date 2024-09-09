##################################################################
"""
Name  : record_navigation.py 
Date  : 04/08/2024
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

from modules.global_config_arguments.global_variables import global_variable

##################################################################
# Importing Python Libraries
##################################################################
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

##################################################################
"""
Name          -> load_navigation
Functionality -> Load navigation and replay it
Algorithm     ->
    1. TO DO
Parameters    -> 
Return        -> 
"""
##################################################################


# Define a mapping of key names to Keys enum
KEY_MAPPING = {
    "Enter": Keys.ENTER,
    "Tab": Keys.TAB,
    "Shift": Keys.SHIFT,
    "Control": Keys.CONTROL,
    "Alt": Keys.ALT,
    "Backspace": Keys.BACKSPACE,
    "Delete": Keys.DELETE,
    "End": Keys.END,
    "Home": Keys.HOME,
    "ArrowUp": Keys.ARROW_UP,
    "ArrowDown": Keys.ARROW_DOWN,
    "ArrowLeft": Keys.ARROW_LEFT,
    "ArrowRight": Keys.ARROW_RIGHT,
    "PageUp": Keys.PAGE_UP,
    "PageDown": Keys.PAGE_DOWN,
    "Insert": Keys.INSERT,
    "Escape": Keys.ESCAPE,
    " ": Keys.SPACE,
}

def load_navigation(driver, file_path):
    try:
        # Load the recorded actions
        with open(file_path, 'r') as file:
            events = json.load(file)
        
        # Perform actions based on the events
        for event in events:
            #print(event)
            try:
                element = None

                try: 
                    element = driver.find_element(By.ID, event.get('id'))
                except:
                    try:
                        element = driver.find_element(By.NAME, event.get('name'))
                    except:
                        try:
                            element = driver.find_element(By.CLASS_NAME, event.get('className'))
                        except:
                            try:
                                element = driver.find_element(By.XPATH, event.get('xPath')) 
                            except:
                                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Element for Automatic Navigation is not found: \n\n{e}\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                                ##print(f"Element is not found: {e}")

                if element:
                    # Focus the element
                    driver.execute_script("arguments[0].focus();", element)
                    #print("Element is focused")

                    if event['type'] == 'key':
                        key = event.get('key')
                        if key in KEY_MAPPING:
                            key = KEY_MAPPING[key]  # Use the mapped Keys value
                        else:
                            key = key  # If key is a string directly, use it
                        #print(f"Sending key: {key}")
                        element.send_keys(key)

                    elif event['type'] == 'click':
                        #print("Attempting to click")
                        # Scroll the element into view
                        driver.execute_script("arguments[0].scrollIntoView(true);", element)
                        
                        # Ensure the element is clickable
                        driver.execute_script("arguments[0].click();", element)
                     
                    # Add a small delay between actions to mimic real user interactions
                    time.sleep(0.1)
                    # remove focus from the element
                    driver.execute_script("document.activeElement.blur();")
                
            except Exception as e:
                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Error processing event -> \n{event}: \n\n{e}\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                #print(f"Error processing event {event}: {e}")

    except Exception as e:
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}An error occurred while loading the navigation: \n\n{e}\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        #print(f"An error occurred while loading the navigation: {e}")

