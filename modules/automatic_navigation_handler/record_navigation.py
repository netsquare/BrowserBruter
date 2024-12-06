##################################################################
"""
Name  : record_navigation.py 
Date  : 04/08/2024
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.run_browser.add_cookies import add_cookies
from modules.run_browser.get_and_initialize_driver import get_and_initialize_chrome_driver

##################################################################
# Importing Python Libraries
##################################################################
import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

##################################################################
"""
Name          -> record_navigation
Functionality -> Load navigation recorder extension, wait for the extension to record the navigation, save the navigation
Algorithm     ->
    1. TO DO
Parameters    -> 
Return        -> 
"""
##################################################################


#def wait_for_page_load(driver):
#    WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.TAG_NAME, 'body'))
#    )

def record_navigation():
    try:
        driver = get_and_initialize_chrome_driver()
        driver.get(global_variable.args.target)
        if global_variable.args.cookie:
            add_cookies(driver)
            driver.get(global_variable.args.target)
        #inject_tracking_script(driver)

        while True:
            #input(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Press Enter to re-inject the JavaScript code if web page is reloaded \n{global_variable.YELLOW}INFO: {global_variable.RESET}Press Enter when tracking is stopped to save the navigation and exit\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
            # Re-inject the tracking script
            #inject_tracking_script(driver)
            # Wait for the page to be ready after re-injection
            #wait_for_page_load(driver)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            
            # Check for navigation details
            try:
                navigation_details_element = driver.find_element(By.ID, 'navigationDetails')
                navigation_data = json.loads(navigation_details_element.get_attribute('value'))

                criteria = {
                    "type": "click",
                    "id": "BrowserBruterStartTrackingButton",
                    "name": "",
                    "className": "",
                    "xPath": "/html/body/browserbruternavigation/button"
                }  

                criteria2 = {                                                                                                                                                                                                                                                                                                                                                                         
        "type": "click",                                                                                                                                                                    
        "id": "BrowserBruterNavigationHeader",                                                                                                                                              
        "className": "",                                                                                                                                                                    
        "xPath": "/html/body/browserbruternavigation"                                                                                                                                                                                                                                                                           
                } 

                criteria3 = {                                                                                                                                                                                                                                                                                                                                                                      
        "type": "click",                                                                                                                                                                    
        "id": "start_notification",                                                                                                                                                         
        "className": "",                                                                                                                                                                    
        "xPath": "/html/body/browserbruternavigation/p"                                                                                                                                                                                                                                                                
                } 

                criteria4 = {                                                                                                                                                                                       
        "type": "click",                                                                                                                                                                    
        "id": "latest_event",                                                                                                                                                               
        "className": "",                                                                                                                                                                    
        "xPath": "/html/body/browserbruternavigation/p[2]"                                                                                                                                      
                } 

                criteria5 = {                                                                                                                                                                                                                                                                                                                                                                     
        "type": "click",                                                                                                                                                                    
        "id": "",                                                                                                                                                                           
        "className": "",                                                                                                                                                                    
        "xPath": "/html/body/browserbruternavigation/span"                                                                                                                                                                                                                                                    
                } 


                # remove the start and stop button if present in data
                for i,navigation in enumerate(navigation_data):
                    if navigation == criteria or navigation == criteria2 or navigation == criteria3 or navigation == criteria4 or navigation == criteria5:
                        navigation_data.pop(i)

                ### Bad Code to be remove ###
                for i,navigation in enumerate(navigation_data):
                    if navigation == criteria3:
                        navigation_data.pop(i)
                for i,navigation in enumerate(navigation_data):
                    if navigation == criteria4:
                        navigation_data.pop(i)
                # Remove the first entry
                navigation_data.pop(0)
                

                # Check if the first entry matches the criteria
              #  if navigation_data and navigation_data[0] == criteria:
                # convert back to string type JSON
                #navigation_data = json.dumps(navigation_data, indent=2) 
                os.makedirs(f"BrowserBruter_Reports/navigations/{global_variable.hostname}",exist_ok=True) # create BrowserBruter_Reports directory
                with open(f"BrowserBruter_Reports/navigations/{global_variable.hostname}/{global_variable.start_time}_navigation.json", 'w') as f:
                    json.dump(navigation_data, f, indent=4)
                driver.quit()
                formatted_navigation_data = json.dumps(navigation_data, indent=4)
                print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Recorded Following Events:\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\n{global_variable.GREEN}{formatted_navigation_data}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Saved the navigation events in-> {global_variable.BLUE}BrowserBruter_Reports/navigations/{global_variable.hostname}/{global_variable.start_time}_navigation.json{global_variable.RESET}\nRename the File as per requirements.\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                break
            except:
                pass
    except KeyboardInterrupt as e:
        pass
    #except Exception as e:
    #    handle_unknown_exception(e)
    finally:
        driver.quit()
