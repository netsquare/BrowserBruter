##################################################################
"""
Name  : get_browser_options.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import log_error

##################################################################
# Importing Python Libraries
##################################################################
from lib.seleniumwire.undetected_chromedriver.v2 import ChromeOptions # undetected chrome driver, used to evade anti bot defences
from traceback import format_exc

##################################################################
"""
Name          -> get_browser_options
Functionality -> Function to get BrowserOptions
Algorithm     ->
    1. Define the ChromeOptions object called options
    2. Set binary_location to res/chrome/chrome which is chrome browser executable
    3. if this file is not found then this means that script is directly clones from github repo, so throw the error message to download the browser bruter from github releases
    4. if user has supplied --chrome-options then add these user supplied options to options object
    5. if user has supplied --anti-bot feature, then return the options object which will be initialized by undetected chrome driver
    6. add usefull options 
    7. if --headless is present then add that option as well
    8. return the options object
Parameters    -> 
Return        -> options(ChromeOptions)
"""
##################################################################

def get_browser_options():
    options = ChromeOptions() # Algorithm step: 1 create options object
    try:
        # NOTE for contributors, the chrome executable is not present at github repo for the sake of repo size limit, it is included in releases, with each new release, the appropriate chrome will be shipped along with the tool
        if global_variable.args.chrome_binary:
            options.binary_location = global_variable.args.chrome_binary
        else:
            options.binary_location = "res/chrome/chrome" # Algorithm step: 2 set the chrome executable location
    except Exception as e: # Algorithm step: 3
        log_error(format_exc())
        # if chrome driver is still not found, throw proper message to user
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR:{global_variable.RESET} The Chrome binary is not Found\n\n\n\n If you have cloned the code from github repository, kindly download it from releases instead of cloning it. https://github.com/netsquare/BrowserBruter/releases/latest . \n\n\n If you want to provide your own chrome driver and chrome binary, kindly do so using --chrome-binary and --chrome-driver option.\n\n\n Also if you have downloaded the file from the releases and still facing the issue then check the permission, to solve the permission related issue run following command -> 'sudo chmod 777 -R res/chrome' \n\n\n If the permissions are also correct then kindly check the path from where you are executing the Browser Bruter script, you should run the Browser Bruter from Browser Bruter base directory.{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        exit(0)
    if global_variable.args.chrome_options: # Algorithm step: 4 handle --chrome-options
        list_of_options = global_variable.args.chrome_options.split(',') # get the options present in --chrome-options into a list of options
        for option in list_of_options: # iterate over the options
            options.add_argument(f"--{option}") # add user supplied options in to options object
    elif global_variable.args.anti_bot: # Algorithm step: 5 handle --anti-bot
        return options # return the options object so the rest of the option will be set by undetected chrome driver
    else: # Algorithm step: 6 add options to options object
        options.add_argument("--disable-ipc-flooding-protection") # Disables IPC flooding protection, potentially improving inter-process communication performance during tests
        options.add_argument("--disable-xss-auditor")
        options.add_argument("--autoplay-policy=user-gesture-required") # Adjusts the autoplay policy, requiring user gestures to start media playback, potentially reducing unwanted interactions during testing.
        options.add_argument("--allow-running-insecure-content") # Disables the warning message when loading insecure content on a secure page, which can save time during testing.
        options.add_argument("--disable-bundled-ppapi-flash")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-prerender-local-predictor")
        options.add_argument("--disable-sync")
        options.add_argument("--disable-breakpad")	
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disk-cache-size=0")
        options.add_argument("--disable-settings-window")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-speech-api")
        options.add_argument("--disable-file-system")
        options.add_argument("--disable-presentation-api")
        options.add_argument("--disable-permissions-api")
        options.add_argument("--disable-new-zip-unpacker")
        options.add_argument("--disable-media-session-api")
        options.add_argument("--no-experiments")
        options.add_argument("--no-events")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-pings")
        options.add_argument("--no-service-autorun")
        options.add_argument("--media-cache-size=0")
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--dbus-stub")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-features=ChromeWhatsNewUI,HttpsUpgrades")
        options.add_argument("--proxy-bypass-list=0.0.0.0")
        options.add_argument("--ignore-certificate-errors")
        # add below option to prevent use of shared memory
        options.add_argument('--disable-dev-shm-usage')
        # adding below to hide that browser is automatically controlled which can be detected by some websites
        options.add_argument('--disable-blink-features=AutomationControlled')
    if global_variable.args.record_navigation:
        options.add_argument('--load-extension=./res/Automatic_navigation_handler')
    #if global_variable.args.debug:
        #options.add_argument('--load-extension=./res/debug_listener')
    if global_variable.args.headless: # Algorithm step: 7 check --headless option
        options.add_argument('--headless') # add --headless option to run the chrome without any GUI
    if global_variable.args.debug:
        options.add_argument("--remote-allow-origins=*")
        options.debugger_address = f"127.0.0.1:{global_variable.available_debug_ports[0]}"
        options.port = global_variable.available_debug_ports[0]
        global_variable.available_debug_ports.pop(0)
    #options.add_argument("--remote-debugging-port=9222")
    
    #options.debugger_address = "127.0.0.1:9222" 
    #options.add_experimental_option('debuggerAddress', 'localhost:9922')
    return options # Algorithm step: 8 return options object
