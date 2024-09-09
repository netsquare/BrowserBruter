##################################################################
"""
Name  : get_and_initialize_driver.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import log_error
from modules.pse_interceptor.request_interceptor import intercept_request
from modules.pse_interceptor.response_interceptor import intercept_response
from modules.run_browser.get_browser_options import get_browser_options

##################################################################
# Importing Python Libraries
##################################################################
from seleniumwire.undetected_chromedriver.v2 import Chrome # undetected chrome driver, used to evade anti bot defences
from seleniumwire import webdriver # normal chrome driver, used to control the browser
from selenium.webdriver.chrome.service import Service # used to hold the executable chrome 
from time import sleep # Used to pause the script
from traceback import format_exc # used for getting the proper exceptions
from sys import exit # used to close the script

##################################################################
"""
Name          -> get_and_initialize_chrome_driver
Functionality -> Function to get and initialize the driver
Algorithm     ->
    1. Acquire a driver_lock so the script does not break due to race condition deadlock
    2. Create and initialize options object to hold browser options by calling get_browser_options() method
    3. if --no-anti-bot switch is set then, start normal chrome browser with normal options, else start chrome browser with anti-bot evasions, call this webdriver.Chrome object as driver
    4. Retry step 3 and 4 three times in case of exception
    5. Set the request interceptor if --remove-images or --python-request or --python-request-file is present.
    6. set the response interceptor if --replace-code or --replace-files --python-response or --python-response-file is persent
    7. Increase the page load timeout to 10 minutes so the browser does not throw timeout in case of delay from server
    8. if --headers option is there then add custom headers
    9. return the webdriver.Chrome object called driver 
Parameters    -> 
Return        -> driver(webdriver.Chrome)
"""
##################################################################

def get_and_initialize_chrome_driver():
    with global_variable.driver_lock: # Algorithm step: 1 acquire driver lock to avoid race conditions and dead lock
        options = get_browser_options() # Algorithm step: 2 get the browser options
        # Algorithm step: 3 getting the webdriver.Chrome object. try to get chrome driver and retry this three times, in case of exceptions, increases the stability in case of multiples threads
        try: 
            if global_variable.args.no_anti_bot: # Checking the --no-anti-bot switch
                service = Service(executable_path="res/chrome/chromedriver") # if --no-anti-bot is set then use normal chrome driver with normal options
                driver = webdriver.Chrome(service=service, options=options, retries=global_variable.max_retry, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {}) # here webdriver.Chrome refers to driver object present in selenium, see imports
            else: # else use undetected_chrome driver to avoid bot detection with max capabilities
                driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, retries=global_variable.max_retry, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {}) # here Chrome refers to driver object present in undetected_chrome driver, see imports
        except: # # Algorithm step: 4 retrying
            sleep(10) # in case of error in above, wait for 10 seconds
            options = get_browser_options() # retry the step 3
            try:
                if global_variable.args.no_anti_bot:
                    service = Service(executable_path="res/chrome/chromedriver")
                    driver = webdriver.Chrome(service=service, options=options, retries=global_variable.max_retry, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {})
                else:
                    driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, retries=global_variable.max_retry, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {})
            except: # retry the step 3 third time in case of error
                sleep(10)
                options = get_browser_options()
                try:
                    if global_variable.args.no_anti_bot:
                        service = Service(executable_path="res/chrome/chromedriver")
                        driver = webdriver.Chrome(service=service, options=options, retries=global_variable.max_retry, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {})
                    else:
                        driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, retries=global_variable.max_retry, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {})
                except: # again retry step 3
                    sleep(10)
                    options = get_browser_options()
                    if global_variable.args.no_anti_bot:
                        service = Service(executable_path="res/chrome/chromedriver")
                        driver = webdriver.Chrome(service=service, options=options, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {})
                    else:
                        driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, seleniumwire_options={'proxy': {'http': global_variable.args.proxy, 'https': global_variable.args.proxy}} if global_variable.args.proxy else {})
        # Algorithm step: 5 Set request interceptor
        if global_variable.args.remove_images or global_variable.args.python_request or global_variable.args.python_request_file:
            driver.request_interceptor = intercept_request
        # Algorithm step: 6 set the response interceptor
        if global_variable.args.replace_code or global_variable.args.replace_files or global_variable.args.python_response or global_variable.args.python_response_file:
        # Intercept HTTP responses to modify the http response body if required
            driver.response_interceptor = intercept_response
        # Algorithm step: 7 Set the timeout limit to 10 minutes
        driver.set_page_load_timeout(600)
        # Algorithm step: 8 Set custom headers
        if global_variable.args.headers:
            custom_headers = {} # Create empty dictionary which will hold headers as key:value pairs
            try:
            # Split the raw string into headers and set each one
                for header in global_variable.args.headers.split(','):
                    key, value = map(str.strip, header.split(':')) # Split them into key and value two different entities
                    custom_headers[key] = value # add them into dictionary
                    # Update header_overrides with all custom headers
                    driver.header_overrides = custom_headers
            except ValueError: # in case of error, handle it properly
                print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR:{global_variable.RESET} Error setting headers. Please provide headers in valid format.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                driver.quit()
                log_error(format_exc())
                exit(0)
        return driver # # Algorithm step: 9
