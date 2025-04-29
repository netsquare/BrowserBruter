##################################################################
"""
Name  : global_variables.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.usage_manual.usage_manual import print_manual # modules.usage_manual.usage_manual file contains code which prints the usage manual of browser bruter
from modules.cli_arguments.arguments import get_arguments # modules.cli_arguments.arguments file contains code which gets the command line arguments
from modules.gui.initialize_gui_args import initialize_gui_args # initialize arguments using gui

##################################################################
# Importing Python Libraries
##################################################################
#from colorama import Fore # used to color code the console output
from urllib.parse import urlparse # used to parse the url
from urllib3.util import Retry # used to set retry count of urllib
from traceback import print_exc # used for getting the proper exceptions
from threading import Lock # used to acquire lock on browser resources to avoid deadlock and race condition
import datetime # used for getting current time and working with time
import json # used for working with json data, the data to fill in form is in json format
import sys # used for multiple purpose related to system like console output and exiting the script
import threading # used for threads and running multiple browser at same time

##################################################################
"""
The block of code for defining and assigning global variables
starts here

Apart from global variables, below code also assigns appropriate
values to these global variables

Below block of code also performs some miscellaneous tasks such as
    1. Creating BrowserBruter report directories and log files 
    2. Suppresses the Encoding and Decoding related warnings
"""
##################################################################


class Global_Variable_Class:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Global_Variable_Class, cls).__new__(cls)

            # All of this color constants are global variables and used throughout the script
            cls._instance.GREEN = '\033[92m' # Using Fore library, defining and assigning cls._instance.GREEN variable
            cls._instance.YELLOW = '\033[93m' # cls._instance.YELLOW color
            cls._instance.RED = '\033[91m' # cls._instance.RED color
            cls._instance.RESET = '\033[0m' # cls._instance.RESET color, go back to default color
            cls._instance.BLUE = '\033[94m' # cls._instance.BLUE color 

            cls._instance.args = get_arguments()

            # Check if none of the argument is given and check if --gui is given
            #if len(vars(cls._instance.args)) == 1:  # Only '--gui' is set
                #initialize_gui_args(cls#cls._instance.args.gui = True
            # Gui
            if cls._instance.args.gui:
                initialize_gui_args(cls._instance.args)

            # If user has enter --manual then print the manual and exit
            if cls._instance.args.help_manual:
                print_manual() # call the print_manual() method to print the help usage manual
                sys.exit(0) # exit the script

            # Check if all required arguments are given and threads are not more than 5
            if cls._instance.args.record_navigation or cls._instance.args.mcp:
                # When --record-navigation or --mcp is present, only --target is compulsory
                if cls._instance.args.target is None:
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}Please Enter --target option.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                # Set the urllib max retry count to 30 to make this script stable as f
                cls._instance.max_retry = Retry(total=30, backoff_factor=1)
                # Creating chrome driver synchronization lock for multithreading
                cls._instance.driver_lock = Lock()
                cls._instance.target_url = urlparse(cls._instance.args.target)
                cls._instance.hostname = cls._instance.target_url.hostname
                cls._instance.start_time_int = datetime.datetime.now() # The start_time_int which is hold time when script is started in raw integer
                cls._instance.start_time = cls._instance.start_time_int.strftime("%Y-%m-%d_%H-%M-%S") # start_time global variable holding time when script is started in proper format
                return cls._instance
            else:
                if ((cls._instance.args.payloads is None or cls._instance.args.elements is None) and (cls._instance.args.elements_payloads is None)) or cls._instance.args.target is None or cls._instance.args.button is None or cls._instance.args.attack is None: # checking that all required arguments are present
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}Please Enter all required arguments --attack, --target, --button, --payloads, --elements or --elements-payloads or --help for help.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                elif cls._instance.args.threads > 20 or cls._instance.args.threads < 0: # if threads are more than 20 and less than 1 then exit the script
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}Value of threads must less than 8 and more than 0\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                elif (cls._instance.args.elements and cls._instance.args.elements_payloads) or (cls._instance.args.payloads and cls._instance.args.elements_payloads): # if --elements and --elements-payloads is given together then throw error
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}--elements and --elements--payloads or --payloads and --elements-payloads can't be used together\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                elif cls._instance.args.attack in (4,3) and (cls._instance.args.payloads or cls._instance.args.elements): # if --elements and --elements-payloads is given together then throw error
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}--elements or --payloads can't be used with attack mode 3. PITCHFORK, 4. CLUSTERBOMB, for these attack modes kindly use --elements-payloads option.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                elif cls._instance.args.attack in (1,2) and cls._instance.args.elements_payloads: # if --elements and --elements-payloads is given together then throw error
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}--elements-payloads can't be used with attack mode 1. SNIPER, 2. BATTERING RAM, for these attack modes kindly use --elements and --payloads option.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                # if force-cookie argument is present withouth --cookie option then throw error 
                elif cls._instance.args.force_cookie:
                    if cls._instance.args.cookie is None: # if --cookie is not given when --force-cookie is present then throw error
                        print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}You can not use --force-cookie without --cookie option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        sys.exit(0)
                # if force-session-storage or force-storage argument is present without respective option then throw error 
                elif cls._instance.args.force_session_storage:
                    if cls._instance.args.add_session_storage is None: 
                        print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}You can not use --force-session-storage without --add-session-storage option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        sys.exit(0)

                elif cls._instance.args.force_storage:
                    if cls._instance.args.add_storage is None: 
                        print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}You can not use --force-storage without --add-storage option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        sys.exit(0)

            # First Payload this global variable is used to stop the script immediately if any error is encountecls._instance.RED of first payload
            cls._instance.first_payload = True
            # Getting hostname from target for filtering the output this will work as one kind scope for filtering output to be stocls._instance.RED in report
            cls._instance.target_url = urlparse(cls._instance.args.target)

            # debug module's related variables
            if cls._instance.args.debug:
                if not cls._instance.args.debug_code:
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}--debug option requires --debug-code option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                cls._instance.available_debug_ports = [9222, 9223, 9224, 9225, 9226, 9227, 9228, 9229, 9230, 9231, 9232, 9234, 9235, 9236, 9237, 9238, 9239, 9240, 9241]
                try:
                    with open(cls._instance.args.debug_code, 'rb') as file: # open the file containing python code in binary read mode
                            print(f"\n\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {cls._instance.RESET}Trying to read the Python file.\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                            cls._instance.args.debug_code = file.read() # read the contents of python file
                            cls._instance.args.debug_code = cls._instance.args.debug_code.decode('utf-8') # encode the code in 'utf-8' format
                except FileNotFoundError: # if file is not found then throw error and exit the script
                        pass
                    #print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified file '{cls._instance.args.python_file}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    #sys.exit(0)
            # Following global variable holds current payload for the iteration, used in --debug switch
            cls._instance.current_payload = ""
            cls._instance.current_element = ""
            cls._instance.hostname = cls._instance.target_url.hostname
            # Get the scope hostnames from the command-line arguments
            cls._instance.scope_hostnames = cls._instance.args.scope.split(',') if cls._instance.args.scope else []
            # Get the urls to be excluded from final report
            cls._instance.list_of_urls_to_be_excluded_from_final_report = []
            if cls._instance.args.outofscope_urls: # if --outofscope-urls then 
                try:
                    with open(cls._instance.args.outofscope_urls,"r") as urls_excluded_file: # open the file containing urls to exclude
                            for line in urls_excluded_file: # for each url present in file to exclude do following
                                line = line.strip() # strip whitespaces at start and end of url
                                cls._instance.list_of_urls_to_be_excluded_from_final_report.append(line) # add this url into global variable holding urls to be excluded from the report
                except FileNotFoundError: # if file is not found then it means user has provided urls in comma separated manner, read the urls given in comma separated list
                   cls._instance.list_of_urls_to_be_excluded_from_final_report = cls._instance.args.outofscope_urls.split(',')
                except Exception as e: # if there is any error then handle it
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}There is a problem with -> {cls._instance.args.outofscope_urls}\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    if cls._instance.args.print_error:
                        print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}{print_exc()}\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
            # Get the urls in scope
            cls._instance.list_of_urls_to_be_included_in_final_report = [] # this global variable holds list of urls to be included in final report
            if cls._instance.args.inscope_urls: # if --inscope-urls is present then 
                try:
                    with open(cls._instance.args.inscope_urls,"r") as urls_included_file: # open the file containing list of urls
                            for line in urls_included_file: # for each url present in list of urls in file
                                line = line.strip() # strip the whitespaces at starting and ending of the URL present in urls list file
                                cls._instance.list_of_urls_to_be_included_in_final_report.append(line) # add this url into global variable holding in scope urls
                except FileNotFoundError: # if file is not found then it means user has provided urls in comma separated manner, read the urls given in comma separated list
                    cls._instance.list_of_urls_to_be_included_in_final_report = cls._instance.args.inscope_urls.split(',')
                except Exception as e: # if there is any error then handle it
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}There is a problem with -> {cls._instance.args.outofscope_urls}\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    if cls._instance.args.print_error:
                        print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}{print_exc()}\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
            # Set the urllib max retry count to 30 to make this script stable as f
            cls._instance.max_retry = Retry(total=30, backoff_factor=1)
            # Creating chrome driver synchronization lock for multithreading
            cls._instance.driver_lock = Lock()
            # Getting time when script started to name the final report
            cls._instance.start_time_int = datetime.datetime.now() # The start_time_int which is hold time when script is started in raw integer
            cls._instance.start_time = cls._instance.start_time_int.strftime("%Y-%m-%d_%H-%M-%S") # start_time global variable holding time when script is started in proper format
            # Get the python code to be executed
            cls._instance.python_to_execute = '\0' # this python_to_execute global variable holds python code to execute on browser
            if cls._instance.args.python: # if --python is present then
                cls._instance.python_to_execute = cls._instance.args.python # store the python code in python_to_execute
            elif cls._instance.args.python_file: # if --python-file is given then 
                if cls._instance.args.python:	# if --python-file is given along with --python then throw error and exit
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The --python-file option can not be used with --python option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                try:
                    with open(cls._instance.args.python_file, 'rb') as file: # open the file containing python code in binary read mode
                        print(f"\n\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {cls._instance.RESET}Trying to read the Python file.\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        cls._instance.python_to_execute = file.read() # read the contents of python file
                        cls._instance.python_to_execute = cls._instance.python_to_execute.decode('utf-8') # encode the code in 'utf-8' format
                except FileNotFoundError: # if file is not found then throw error and exit the script
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified file '{cls._instance.args.python_file}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
            # Get the python code to manipulate HTTP request
            cls._instance.python_http_request = '\0' # this python_http_response global variable holds python code to execute on HTTP request
            if cls._instance.args.python_request: # if --python-request is present then
                cls._instance.python_http_request = cls._instance.args.python_request # store the python code in python_http_request
            elif cls._instance.args.python_request_file:  # if --python-request-file is given then 
                if cls._instance.args.python_request: # if --python-request-file is given along with --python-request then throw error and exit
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The --python-request-file option can not be used with --python-request option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                try:
                    with open(cls._instance.args.python_request_file, 'rb') as file: # open the file containing python code in binary read mode
                        print(f"\n\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {cls._instance.RESET}Trying to read the Python file.\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        cls._instance.python_http_request = file.read() # read the contents of python file
                        cls._instance.python_http_request = cls._instance.python_http_request.decode('utf-8') # encode the code in 'utf-8' format
                except FileNotFoundError: # if file is not found then throw error and exit the script
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified file '{cls._instance.args.python_request_file}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
            # Get the python code to manipulate HTTP response 
            cls._instance.python_http_response = '\0' # this python_http_response global variable holds python code to execute on HTTP response
            if cls._instance.args.python_response: # if --python-response is present then
                cls._instance.python_http_response = cls._instance.args.python_response # store the python code in python_http_response
            elif cls._instance.args.python_response_file: # if --python-response-file is given then 
                if cls._instance.args.python_response: # if --python-response-file is given along with --python-response then throw error and exit
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The --python-response-file option can not be used with --python-response option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                try:
                    with open(cls._instance.args.python_response_file, 'rb') as file: # open the file containing python code in binary read mode
                        print(f"\n\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {cls._instance.RESET}Trying to read the Python file.\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        cls._instance.python_http_response = file.read() # read the contents of python file
                        cls._instance.python_http_response = cls._instance.python_http_response.decode('utf-8') # encode the code in 'utf-8' format
                except FileNotFoundError: # if file is not found then throw error and exit the script
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified file '{cls._instance.args.python_response_file}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)    

            # Get the javascript code to be executed, javascript_to_execute is global variable to hold javascript code to execute
            cls._instance.javascript_to_execute = '\0'
            if cls._instance.args.javascript: # check if --javascript option is present
                cls._instance.javascript_to_execute = cls._instance.args.javascript # store the javascript to execute in javascript_to_execute variable
            elif cls._instance.args.javascript_file: # if --javascript-file is provided then
                if cls._instance.args.javascript:	# if --javascript-file is present along with --javascript option then throw error then exit
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The --javascript-file option can not be used with --javascript option\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                try:
                    with open(cls._instance.args.javascript_file, 'rb') as file: # Open the javascript file as read binary mode
                        print(f"\n\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {cls._instance.RESET}Trying to read the Javascript file\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        cls._instance.javascript_to_execute = file.read() # store the content of the javascript file in javascript_to_execute
                        cls._instance.javascript_to_execute = cls._instance.javascript_to_execute.decode('utf-8') # Convert the code from binary to 'utf-8' encoding
                except FileNotFoundError: # if javascript is not file not found the throw error and exit
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified file '{cls._instance.args.javascript_file}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
            # Setting flag which indicates threads to run or stop, This global terminate flag works as cls._instance.RED flag for the script, this flag is checked at many places in the script
            cls._instance.terminate = False
            # Setting a flag which indicates thread to temporary pause the keyboard thread in case when some user input is required
            cls._instance.pause_keyboard_thread = False
            # Setting flag for --no-reload-page switch
            cls._instance.no_reload = True
            # This global variable Pause event will be used to pause the threads when user presses the ENTER KEY
            cls._instance.pause_event = threading.Event()
            # if there is code to replace, get the code
            if cls._instance.args.replace_code:
                # Split the replace_code argument into individual strings
                cls._instance.replace_codes = cls._instance.args.replace_code.split('+++')
                # Create pairs of replacement codes
                cls._instance.replacement_pairs = []
                #i = 0 # set index
                #while i < len(cls._instance.replace_codes): # get the replacement codes one by one
                #    if i + 1 < len(cls._instance.replace_codes):
                #        to_be_replaced = cls._instance.replace_codes[i] # get the code to replace 
                #        to_be_replaced_with = cls._instance.replace_codes[i + 1] # get the replacement code which will be after code to replace in replace_codes list
                #        cls._instance.replacement_pairs.append((to_be_replaced, to_be_replaced_with)) # Create pairs for replacement and code to replace 
                #    i += 2
                # V2024.10.12 changing replace_code logic
                for find_replace_pair in cls._instance.replace_codes:
                    try:
                        to_be_replaced, to_be_replaced_with = find_replace_pair.split('::')
                        cls._instance.replacement_pairs.append((to_be_replaced, to_be_replaced_with))
                    except ValueError:
                        print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The --replace-code option required data in following format -> --replace-code to_be_replaced::to_be_repalced_with\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                        sys.exit(0)
            # Abort request with following extensions, this global forbidden_extensions holds the extension which will be aborted by request interceptor
            cls._instance.forbidden_extensions = ['.ico', '.png', '.img', '.jpg', '.svg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.gif', '.apng', '.avif', '.webp', '.bmp', '.cur', '.tif', '.tiff', '.mp3', '.mp4', '.avi', '.mkv', '.webm', 'ogv']
            if cls._instance.args.no_css: # if --no-css flag is set the remove .css extension into forbidden_extensions as well
                cls._instance.forbidden_extensions.append('.css')

            # A global variable to store key:value pair of <ng-select> elements and their respective properties
            #cls._instance.elements_properties = {}

            # Get the payloads
            cls._instance.payloads = [] # this global variable holds the payloads for battering ram and sniper attack
            cls._instance.elements_payloads = {} # This global dictionary holds elements and their payloads for clusterbomb and pitchfork attack
            if cls._instance.args.attack in (1, 2): # If attack mode is sniper or battering ram then 
                # Get the elements to be fuzzed
                cls._instance.elements = cls._instance.args.elements.split(',')
                # Get Payloads from file and store them in a list
                try:
                    with open(cls._instance.args.payloads, "r") as payload_file: # open the payload file in read mode
                        for line in payload_file: # for each payload
                            line = line.strip() # strip the whitespaces from beginning and ending of the payload
                            cls._instance.payloads.append(line) # add payload in global payloads list
                except FileNotFoundError: # if file is not found then exit the script
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified payloads file '{cls._instance.args.payloads}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
                            # Process the elements list
                #for i, item in enumerate(cls._instance.elements):
                    #if "::" in item:
                        #elementname, property = item.split("::")  # Split into name and property
                        #cls._instance.elements[i] = elementname  # Update the list with only the element name
                    #if "++" in elementname:
                        #elementname, identifier = elementname.split("++")
                    #cls._instance.elements_properties[elementname] = property  # Add to dictionary

            elif cls._instance.args.attack in (3, 4): # Attack is clusterbomb or pitchfork then 
                try:
                    for i, element_payload in enumerate(cls._instance.args.elements_payloads.split(',')): # for each element_payload pair given by user
                        element, payload_file_path = element_payload.split(':') # divide the element and payload file from element:payload pair
                        # Initialize the list if it doesn't exist
                        cls._instance.elements_payloads.setdefault(element, []) # this holds the element and that element's payloads
                        with open(payload_file_path, 'r') as payload_file: # open the payloads file
                            for line in payload_file: # for each payload
                                line = line.strip() # strip whitespaces from beginning and ending of the payload
                                cls._instance.elements_payloads[element].append(line) # add payloads to the elements_payloads list which hold the element and their payloads
                        if "::" in element:
                            elementname, property = item.split("::")  # Split into name and property
                            element = elementname  # Update the list with only the element name
                            if "++" in elementname:
                                elementname, identifier = elementname.split("++")
                            cls._instance.elements_properties[elementname] = property  # Add to dictionary

                    if cls._instance.args.attack == 3: # if attack mode is pitchfork
                        # Check if all lists have the same length
                        if len(set(len(payloads) for payloads in cls._instance.elements_payloads.values())) > 1:
                            # Find the maximum length of lists in the dictionary
                            max_length = max(len(payloads) for payloads in cls._instance.elements_payloads.values())
                            # Loop through each element in the dictionary and extend the lists to match the maximum length
                            for element in cls._instance.elements_payloads:
                                current_length = len(cls._instance.elements_payloads[element])
                                if current_length < max_length:
                                    # Calculate how many elements are needed to reach the maximum length
                                    needed_elements = max_length - current_length
                                    # Duplicate the list and append elements from the original list until the desicls._instance.RED length is reached
                                    extended_list = cls._instance.elements_payloads[element].copy()
                                    while len(extended_list) < max_length:
                                        extended_list += cls._instance.elements_payloads[element]
                                    # Trim the list to the maximum length
                                    extended_list = extended_list[:max_length]
                                    # Update the dictionary with the extended list
                                    cls._instance.elements_payloads[element] = extended_list
                except FileNotFoundError: # if file is not found then exit the script
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified payloads file does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)
            else: # if attack mode is not in pre-defined value then exit
                print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}Please enter values either 1, 2, 3 or 4 in --attack\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                sys.exit(0)

            # Get the content, Replace the response body with the content of the file provided by the user
            cls._instance.file_contents = {} # this global dictionary will contain list of files which will replace the target files along with their contents.
            if cls._instance.args.replace_files: # if --replace-files is give then 
                try:
                    cls._instance.replace_files = cls._instance.args.replace_files.split(',') # split files given by user into list
                    for replace_file in cls._instance.replace_files: # for every file to replace do following
                        file_name, file_url = replace_file.split('++') # get the file_name and file_url from files list
                        with open(file_name, 'r') as file: # open that file into read mode
                            print(f"\n\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {cls._instance.RESET}Trying to read the replacement file. -> {file_name}\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                            cls._instance.file_contents[file_name] = file.read() # Store the file content into file_contents Dictionary
                except FileNotFoundError: # if file is not found the print generic message and close
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified replacement file '{file_name}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0)

            # Non targeted input field value, will update this to allow user specify them, please contribute to add more types and let us know https://github.com/netsquare/BrowserBruter/issues
            # The global attribute_values holds the default values to enter in the fields of html form while --fill option is given
            cls._instance.attribute_values = { 
	            # This allows BrowserBruter to put default valid values into field which are not being fuzzed
	            # For example BrowserBruter will send 0123456789 in fields which has type tel and which are not being fuzzed
	            "text":"text",
	            "number":"1234567890",
	            "password":"P2$$@@wrd0!@#JJJ",
	            "email":"email@email.com",
	            "url":"http://localhost.xyz/",
	            "file":"name.txt",
	            "tel":"9123456780",
	            "date":"2023-06-17",
	            "datetime":"2023-07-17T10:30",
	            "time":"10:30",
	            "month":"2023-07",
	            "week":"2023-W25",
	            "color":"#ff0000",
	            "range":"50",
                "textarea":"AtextForTextArea"
            }

            # Create list of events to be disabled
            cls._instance.disable_events = []
            if cls._instance.args.disable_events:
                cls._instance.disable_events = cls._instance.args.disable_events.split(',')

            # Create list of elements whose class attribute needs to be removed
            cls._instance.remove_class_elements = []
            if cls._instance.args.remove_class:
                cls._instance.remove_class_elements = cls._instance.args.remove_class.split(',')

            # If user has provided list of buttons to press, get those buttons.
            if cls._instance.args.buttons_to_press_before_fuzz:
               cls._instance.buttons_to_press_before_fuzz = cls._instance.args.buttons_to_press_before_fuzz.split(',')

            # If user has provided values for above, then override them with user's values
            if cls._instance.args.fill_values:
                try:
                    with open(cls._instance.args.fill_values, 'r') as values_file: # open the file provided user in read mode
                        cls._instance.attribute_values = json.load(values_file) # override the values with values given by user
                except FileNotFoundError: # if file not found then print generic message
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}The specified values file '{cls._instance.args.values}' does not exist.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0) # exit the script
                except json.JSONDecodeError: # handle if there is any JSON syntax error in user provided file
                    print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}Invalid JSON format in the specified values file '{cls._instance.args.values}'.\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    if cls._instance.args.print_error: # If --print-error flag is set then print the exception
                        print_exc() # print the exception
                        print(f"\n\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {cls._instance.RESET}Refer Above Stack Trace\n{cls._instance.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")
                    sys.exit(0) # Exit the script

        # Print the legal disclaimer about the use of javascript and python code options
        if any([
            cls._instance.args.javascript,
            cls._instance.args.javascript_after,
            cls._instance.args.javascript_file,
            cls._instance.args.python,
            cls._instance.args.python_file,
            cls._instance.args.python_after,
            cls._instance.args.python_request,
            cls._instance.args.python_request_file,
            cls._instance.args.python_response,
            cls._instance.args.python_response_file,
        ]):
            print(f"\n\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nWarning: {cls._instance.RESET}Use of external javascript or python code is detected, You are solely responsible for ensuring the safety and trustworthiness of the code being executed.\nAny consequences resulting from the use of these features are entirely at your own risk.\nThe developers have no control over the content or behavior of the code you choose to execute.\nAlways review and verify any code before execution to minimize risks. If you do not agree with these terms, refrain from using the Python and JavaScript execution options.\n{cls._instance.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{cls._instance.RESET}")

        return cls._instance

global_variable = Global_Variable_Class()
