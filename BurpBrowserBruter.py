### VARIOUS IMPORTS STARTS ###

import argparse
import datetime
import signal 
import sys
import threading
import os
import json
import platform
from pytimedinput import timedKey
from traceback import format_exc, print_exc
from res.tee import Tee
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException
from http.client import RemoteDisconnected
from urllib3.exceptions import ProtocolError
from urllib3.exceptions import MaxRetryError  
from urllib.parse import urlparse
from colorama import Fore

### VARIOUS IMPORTS ENDS ###

# Defining color contants #
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET

### PRINTING BANNER ###
print(f"""{GREEN}
##################################################################################################################################################################################
##################################################################################################################################################################################
##                                                                                                                                                                             ###
## {YELLOW}██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░                                                       
{GREEN}## {YELLOW}██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗⠀⠀⠀⠀{RED}⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣶⣶⣶⣶⣶⣾⣷⣾⣷⣶⠀{YELLOW}. . . . . . . . . . . . . . . 
{GREEN}## {YELLOW}██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝⠀{RED}⣶⣶⣶⣶⣶⣶⣶⡆⢸⣿⣿⣿⣿⣿⣿⡇⠸⠿⠿⠿⠿⠿⠿⢿⡿⢿⡿⠿⠀{YELLOW}. . . . .  . . . . . . . . . . 
{GREEN}## {YELLOW}██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗⠀{RED}⣿⣿⣿⣿⣿⣿⣿⡇⠘⠛⢻⠟⠛⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠁⠀⠀                  
{GREEN}## {YELLOW}██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║⠀{RED}⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⣸⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  
{GREEN}## {YELLOW}╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝⠀⠀⠀{RED}⣆⠀⢶⡆⠀⠀⠀⢀⡟⠀⣼⡇                                 
{GREEN}##                                                                                                                       ⠀⠀⠀{RED}⢹⣄⠘⣷⡀⠀⢀⡼⠁⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  
{GREEN}##                                                                                                                       ⠀⠀⠀⠀{RED}⠙⠦⡈⠻⢶⣿⣥⡾⠋ {YELLOW}by Jafar Pathan & NetSquare Team v1.0 
{GREEN}##                                                                                                                           {YELLOW}An Advance Browser Automated Web Form Fuzzing Tool{GREEN}### 
{GREEN}##################################################################################################################################################################################
{GREEN}##################################################################################################################################################################################{RESET}""")


### DEFINING AND PARSING COMMAND LINE ARGUMENTS START ###
# Getting argument parser to parse and process arguments
argParser = argparse.ArgumentParser(description="BrowserBruter is a python3 script, utilizing power of selenium and selenium-wire to automate fuzzing of various input fields of webpages to test their security against malicious inputs. For contact and more information about project please visit https://github.com/netsquare/BrowserBruter",formatter_class=argparse.RawTextHelpFormatter)
# Defining the epilog message which will be displayed whith help message
argParser.epilog = f'''
Usage Examples:
	1. Fuzz on login page
	   {YELLOW}python3 BurpBrowserBruter.py -e username,password -p sqli.txt -t http://owasp.com/login -b loginButton{RESET}
	
	2. Fuzz on login page with csrf enabled
	   {YELLOW}python3 BurpBrowserBruter.py -e username,password -p sqli.txt -t http://owasp.com/login -b loginButton --csrf csrfToken{RESET}
	
	3. Fuzz on registration page with csrf enabled no output printed on console
	   {YELLOW}python3 BurpBrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --csrf _token --silent{RESET}
	
	4. Fuzz on 3rd form of registration page with csrf enabled no output printed on console
	   {YELLOW}python3 BurpBrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --csrf _token --silent --form 3{RESET}
	
	5. Fuzz on registration page with csrf and two cookies 1)'difficulty' and 2)'hint'
	   {YELLOW}python3 BurpBrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token{RESET}
	
	6. Fuzz on registration page with csrf and two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request becuase the initiali cookies might be overridden by new cookies values
	   {YELLOW}python3 BurpBrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --forceCookie{RESET}
	
	7. Fuzz on 3rd form of registration page with csrf and two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle [this is useful against Authentication pages when you don't want redirection in case of successful login]
	   {YELLOW}python3 BurpBrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie --removeSession{RESET}
	
	8. Fuzz on 3rd form of registration page with csrf and two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode
	   {YELLOW}python3 BurpBrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie --removeSession --headless{RESET}
	
	9. Fuzz on 3rd form of registration page with csrf and two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode and run 5 instances of browser parallely
	   {YELLOW}python3 BurpBrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie --removeSession --headless --threads 5{RESET}
   
       10. Fuzz CheckBox for example '<input type="checkbox" name="hobbies" value="reading" /> <input type="checkbox" name="hobbies" value="writing" />'
	   {YELLOW}python3 BurpBrowserBruter.py -e hobbies -p paylods.txt -t http://dvwa.com/register -b register{RESET}
   
       11. Fuzz Radio Button for example '<input type="radio" name="yesno" id="yes" value="yes" required/> <input type="radio" name="yesno" id="no" value="no" required/>'
	   {YELLOW}python3 BurpBrowserBruter.py -e yesno -p payloads.txt -t http://dvwa.com/register -b register {RESET}
	 OR
	   {YELLOW}python3 BurpBrowserBruter.py -e no -p payloads.txt -t http://dvwa.com/register -b register{RESET}
   
       12. Fuzz CSRF token + don't overwrite it while fuzzing other fields
           {YELLOW}python3 BurpBrowserBruter.py -e csrfToken,username,password -p payloads.txt -t http://dvwa.com/login -b login --csrf csrfToken{RESET}
   
       13. Fuzz <select> element - for example <select name="selectElement" required> <option value="">Select an option</option> <option value="option1">Option 1</option> </select>
           {YELLOW}python3 BurpBrowserBruter.py -e selectElement -p payloads.txt -t http://dvwa.com/selection -b submit{RESET}
   
       14. Fuzz <textarea> element - for example <textarea name="textareaElement" placeholder="Enter text" required></textarea>
           {YELLOW}python3 BurpBrowserBruter.py -e textareaElement -p payloads.txt -t http://dvwa.com/registration -b submit{RESET}
   
       15. Fuzz colorpicker, datepicker, timepicker - for example <input type="color" name="colorElement" required/> <input type="date" name="dateElement" required/> <input type="time" name="timeElement" required/>
           {YELLOW}python3 BurpBrowserBruter.py -e colorElement,dateElement,timeElement -p payloads.txt -t http://localhost/ -b submit{RESET}

       16. Provide custom values for each form field types, content of the file should be in JSON format and it should contain all of the field types, see example values.json for better understandin.
           {YELLOW}python3 BurpBrowserBruter.py -e username,password -b button -t http://net-square.com/login -p payloads.txt --values fields.json" {RESET}
	 
       17. Provide various fields (elements) to avoid being fuzzed or overwritten by BrowserBruter, set two cookies, force reuse of these cookies, reset session data each time. 
           {YELLOW}python3 BurpBrowserBruter.py -e ip -b Submit -p payloads.txt -t http://example.com/vulnerabilities/exec/ --cookie PHPSESSID:jtq7r9fbgf90h2qm9915qk6551:example.com security:low:example.com  --forceCookie --removeSession --avoid help_button,source_button,user_token {RESET}
      
       18. Pause BrowserBruter on startup to manually login and manually set cookies, press ENTER two times to continue.
           {YELLOW}python3 BurpBrowserBruter.py -e ip -b Submit -p payloads.txt -t http://example.com/vulnerabilities/exec/ --avoid help_button,source_button,user_token --pause
		
       19. Pause the BrowserBruter on each iteration of fuzzing, so user can manually perform any task, complete captcha before BrowserBruter fuzzes the form, this will happen for each attempt to fuzz, so it will take a lot of time and user has to press ENTER two times to continue.
           {YELLOW}python3 BurpBrowserBruter.py -e textarea,select,yesno,hobbies,phone,data,time,calendar,color --avoid _csrf -b submit -p payloads.txt -t http://localhost:3000/ --threads 5 --values values.json --iterative{RESET}

 
 '''
# Adding various command line arguments
argsRequired = argParser.add_argument_group("required")
argsRequired.add_argument("-t","--target",help="Target's url: http://www.net-square.com/index.php")
argsRequired.add_argument("-e","--elements", help="Enter input fields in comma separated values.")
argsRequired.add_argument("-p","--payloads",help="/path/to/payload/file.")
argsRequired.add_argument("-b","--button",help="Button element which will submit form data.")
argParser.add_argument("-P","--proxy",help="IP and port of burpsuite",default="127.0.0.1:8080")
argParser.add_argument("--avoid",help="Input fields and other elements to left untouched, BrowserBruter will avoid them, also useful to avoid csrf field.")
argParser.add_argument("--delay",help="Delay between each brute force attempt.",metavar="0.2", type=float, default=0.2)
argParser.add_argument("-c","--cookie",help="Use it to define cookies to be used while sending initial request, cookies should be in name:value:domain format.", metavar="name:value:domain", nargs="+")
argParser.add_argument("--forceCookie",help="Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server.",action="store_true")
argParser.add_argument("--removeSession",help="Use this switch to remove session data and cookies after each request-response cycle.", action="store_true")
argParser.add_argument("--silent",help="Use this switch to disable output being printed on console and STDLOG file.", action="store_true")
argParser.add_argument("-F","--form",help="Specify the form number to fuzz.", type=int)
argParser.add_argument("--headless",help="Use this switch to run browser in headless mode (No GUI).", action="store_true")
argParser.add_argument("-T","--threads",help="Specifies number of browsers instances to be run, max value is 5, default is 1, lower the instances slower the fuzzing process, more instances - faster fuzzing process.",default=1, type=int)
argParser.add_argument('--values', help='Path to User-configurable attribute values file .json file')
argParser.add_argument("--pause", help="Pause the Browsers on startup, press ENTER to resume",action="store_true")
argParser.add_argument("--iterative",help="Pause the BrowserBruter before fuzzing any element at each payload and wait for user to continue",action="store_true")

# Getting the arguments in args variable
args = argParser.parse_args()

# Check if all required arguments are given and threads are not more than 5
if args.payloads is None or args.target is None or args.elements is None or args.button is None:
	print(f"{RED}Please Enter all required arguments --target, --paylods, --elements, --button{RESET}")
	sys.exit(0)
elif args.threads > 5 or args.threads < 0:
	print(f"{RED}Value of threads must less than 6 and more than 0{RESET}")
	sys.exit(0)
# if forceCookie argument is present withouth --cookie option then throw error 
elif args.forceCookie:
	if args.cookie is None:
		print(f"{RED}You can not use --forceCookie without --cookie option{RESET}")
		sys.exit(0)

### DEFINING AND PARSING COMMAND LINE ARGUMENTS ENDS ###

### DEFINING AND ASSIGNING GLOBAL VARIABLES STARTS ###

# Getting time when script started to name the final report
start_time = datetime.datetime.now()
start_time = start_time.strftime("%Y-%m-%d_%H-%M-%S")

# Getting hostname from target for filtering the output this will work as one kind scope for filtering output to be stored in report
target_url = urlparse(args.target)
hostname = target_url.hostname

# Setting flag which indicates threads to run or stop
terminate = False
# Pause event will be used to pause the threads when user presses the ENTER KEY
pause_event = threading.Event()
# Set Pause event if --pause flag is set
if args.pause:
	pause_event.set()

# Get Payloads from file and store them in list
payloads = []
try:
	with open(args.payloads, "r") as s:
		for i in s:
			i = i.strip()
			payloads.append(i)
except FileNotFoundError:
	print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: The specified payloads file '{args.payloads}' does not exist.\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	sys.exit(1)

# Creating Reports directory in current directory to store reports
os.makedirs("BrowserBruter_Reports",exist_ok=True)
os.makedirs(f"BrowserBruter_Reports/{hostname}/{start_time}",exist_ok=True)

# Non targeted input field value, will update this to allow user specify them, please contribute to add more types and let us know https://github.com/netsquare/BrowserBruter/issues
attribute_values = {
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
	"range":"50"
}
# if user has provided values for above, then override them with user's values
if args.values:
    try:
        with open(args.values, 'r') as values_file:
            attribute_values = json.load(values_file)
    except FileNotFoundError:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: The specified values file '{args.values}' does not exist.\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: Invalid JSON format in the specified values file '{args.values}'.\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        sys.exit(1)


### DEFINING AND ASSIGNING GLOBAL VARIABLES ENDS ###

### FUNCTIONS STARTS ###

# Function to get browser driver specific to the running os
def get_driver_path():
    os_name = platform.system().lower()
    
    if os_name == 'linux':
        return 'res/Drivers/linux/geckodriver' if args.firefox else 'res/Drivers/linux/chromedriver'
    elif os_name == 'windows':
        return 'res/Drivers/Win/chromedriver.exe' if args.firefox else 'res/Drivers/Win/geckodriver.exe'
    elif os_name == 'darwin':  # Mac then use the installed firefox or chrome, no driver support as of now
        return 'darwin'
    else:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: Unsupported operating system: {os_name}\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        sys.exit(1)

# Function to Handle CTRL+C
def signal_handler(signal, frame):
	print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: CTRL+C pressed. Waiting for remaining request/response to stop. Exiting...\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	# Set the global termination flag to True so all threads can stop gracefully
	global terminate
	terminate = True

# Function to run in a separate thread to pause and resume the browserbruter if user presses enter key
def pause_resume():
    global pause_event
    while not terminate:
        userText, timeout = timedKey(prompt="", timeout=3, resetOnInput=True)
        if not (timeout):
            pause_event.set()  # Set the pause even
            print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nWARNING: BROWSERBRUTER IS PAUSED\nPress ENTER to resumse\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
            k = input()				
            pause_event.clear()  # Clear the pause event 
            print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nWARNING: Resuming BROWSERBRUTER\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")

# Function to get BrowserOptions
def get_browser_options(browser_type):
	# Assigning browser options
	options = ChromeOptions()
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--executable-path=res/Drivers/chromedriver')
	options.add_argument("--disable-ipc-flooding-protection")
	options.add_argument("--disable-xss-auditor")
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
	options.add_argument(f"--proxy-server={args.proxy}")
	options.add_argument("--proxy-bypass-list=0.0.0.0")
	options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36"')
	options.add_argument("--ignore-certificate-errors")

	# Check if browser has to be run headless mode
	if args.headless:
		options.add_argument('--headless')
	return options

# Function to add cookies into selenium session
def add_cookies(driver):
	try:
		for cookie_arg in args.cookie:
			# Get the cookie data
			name, value, domain = cookie_arg.split(":")
			# Create cookie dictionary as selenium requires them in dictionary format
			cookie_dict = {
				"name": name,
				"value": value,
				"domain": domain
			}
			driver.add_cookie(cookie_dict)
	except ValueError as e:
		sleep(2)
		log_error(format_exc())
		print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: You have entered arguments in invalid format, please read help message for valid formate of passing cookies. Closing the Fuzzing process\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
		driver.quit()
		sys.exit(0)

# Function to Remove attributes this is created to reduce code in attempt function
def remove_attributes(driver, field):
	driver.execute_script("arguments[0].removeAttribute('pattern');",field)
	driver.execute_script("arguments[0].removeAttribute('min');",field)
	driver.execute_script("arguments[0].removeAttribute('max');",field)
	driver.execute_script("arguments[0].removeAttribute('maxlength');",field)
	driver.execute_script("arguments[0].removeAttribute('minlength');",field)
	driver.execute_script("arguments[0].removeAttribute('readonly');",field)

# Function to log errors 
def log_error(error):
	try:
		with open("logs/Error.txt","a") as log:
				error_time = datetime.datetime.now()
				error_time = error_time.strftime("%Y-%m-%d_%H-%M-%S")
				log.write(f"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
				log.write(f"Error Time - {error_time}")
				log.write("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
				log.write(error)
	except:
		print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: An unknown error has been occured, Please open issue request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")

# Funtion to Generate filename for each differnt thread
def get_filename():
	# Getting current date and time to name the output file accrodingly
	current_datetime = datetime.datetime.now()
	formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
	filename = f"BrowserBruter_Reports/{hostname}/{start_time}/{hostname }-{formatted_datetime}.txt"
	return filename

# Function to Generate Final Report
def generate_final_report():
	print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Genrating Final Report\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	directory = f"BrowserBruter_Reports/{hostname}/{start_time}"
	processed_payloads = f"BrowserBruter_Reports/{hostname}/{start_time}/Processed_Payloads.txt"
	try:
		all_processed_payloads_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
		global payloads

		# Merge the processed payloads file into one
		with open(processed_payloads,'w',newline='') as final_processed_payloads:
			for one_threads_processed_paylods in all_processed_payloads_files:
				file_path = os.path.join(directory,one_threads_processed_paylods)
			
				with open(file_path,'r') as infile:
					for i in infile:
						final_processed_payloads.write(i)
						# keeping track of remaining payloads by removing processed payloads from payload[] list
						payloads.remove(i.strip())
				# Delete the current threads processed payloads file
				os.remove(file_path)
		# Storing remaining payloads in separate file
		remaining_payloads = os.path.join(directory,"Remaining_Payloads.txt")
		with open(remaining_payloads,'w',newline='') as remaining_payloads_file:
			for payload in payloads:
				remaining_payloads_file.write(payload+'\n')
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Processed Payloads (if any) have been stored -> {processed_payloads}\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Remaining Payloads (if any) have been stored -> {remaining_payloads}\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	except FileNotFoundError:
		sys.exit(1)

# Funtion to Run Single Browser instance
def run_browser_instance(payloads, elements, instance_number):
	try:
		# Spawing an instance of browser
		# Assigning browser options
		# Checking whether user has to run fuzzing on firefox or chrome and assigning browser options
		options = get_browser_options('chrome')
		driver = webdriver.Chrome(options=options)

		# If cookies are provided assign them to session
		if args.cookie:
			# first visit the domain so Chrome does not trow InvalidCookieDomainException
			driver.get(args.target)
			add_cookies(driver)

		 ## Set custom headers is not working for BurpBrowserBruter for now, It will be appreciated if you can help in this :)
		#if args.headers:
		#	custom_headers = {}
		#	try:
        #    	# Split the raw string into headers and set each one
		#		for header in args.headers.split(','):
		#			key, value = map(str.strip, header.split(':'))
		#			custom_headers[key] = value
				# Update header_overrides with all custom headers
		#		driver.header_overrides = custom_headers
		#	except ValueError:
		#		print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: Error setting headers. Please provide headers in valid format.\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
		#		driver.quit()
		#		sys.exit(1)

		# Initialize report file and processed payload file
		this_threads_files = get_filename()
 
		# Start the Fuzzing process
		for i in range(len(payloads)):
			for j in range(len(elements)):
					# Fuzz until terminate flag is not set, if it set then exit and close browser
					if not terminate:
						# if iterative option is set stop and wait for user to continue
						if args.iterative:
							pause_event.set()
						# if pause event is set then pause the fuzzing process
						if pause_event.is_set():
							while pause_event.is_set():
								sleep(1)
						attemptToInsertOnePayloadAndFuzzOneElement(elements[j],payloads[i], driver)
						sleep(args.delay)
					j += 1
			# Add the processed payload into the file to keep track of processed payloads by this thread
			with open(this_threads_files,'a',newline='') as processed_payload_file:
				processed_payload_file.write(payloads[i]+'\n')
			i+=i
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Fuzzing completed for Browser Instance number - {instance_number}\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")

	# Handle the exceptions which specific to this thread and does not affects other threads
	except NoSuchWindowException as e:
		sleep(0.5)
		log_error(format_exc())
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	except RemoteDisconnected as e:
		sleep(0.7)
		log_error(format_exc())
		# This exception can be arrived whene user closes browser window
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	except ProtocolError as e:
		sleep(0.9)
		log_error(format_exc())
		# This exception can be arrived whene user closes browser window
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	except MaxRetryError as e:
		sleep(0.3)
		error = format_exc()
		log_error(error)
		# This exception can be arrived whene user closes browser window
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Browsers has reached maximum retries, if you have closed BrowserBruter ignore this else report the issue, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	except WebDriverException as e:
		sleep(1)
		log_error(format_exc())
		# This exception can be arrived whene user closes browser window
		print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}") 
	except:
		sleep(3.5)
		log_error(format_exc())
		# Print Traceback
		print_exc()
		# Ask user to send this to github
		print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: An unkown error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	finally:
		#close the specific thread's driver
		try:
			if driver is not None:
				driver.quit()
		except UnboundLocalError:
			sys.exit(1)

# Function to attempt a single request-response cycle with payload
def attemptToInsertOnePayloadAndFuzzOneElement(element, payload, driver):

	# If --force is set then set the initial cookies
	if args.forceCookie:
		add_cookies(driver)

	# Go to the target website
	driver.get(args.target)

	# Wait for body to be loaded in case of slow response
	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_all_elements_located(("xpath", '//body')))

	# Get the input field of form to be fill them
	# If user has specified the form number 
	if args.form:	
		input_fields = driver.find_elements(By.XPATH,f"//form[{args.form}]//input")
		select_fields = driver.find_elements(By.XPATH,f"//form[{args.form}]//select")
		textarea_fields = driver.find_elements(By.XPATH,f"//form[{args.form}]//textarea")
		input_fields.extend(select_fields)
		input_fields.extend(textarea_fields)
	else:
		input_fields = driver.find_elements(By.XPATH,"//input")
		select_fields = driver.find_elements(By.XPATH,"//select")
		textarea_fields = driver.find_elements(By.XPATH,"//textarea")
		input_fields.extend(select_fields)
		input_fields.extend(textarea_fields)

	# Check if form with specified number exists or not
	if not input_fields:
		print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: Form with specified number does not exists, please verify form number, closing the BrowserBruter\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
		driver.quit()
		sys.exit(0)

	# Remove CSRF and other elements to be excluded to avoid overwriting it
	if args.avoid:
		list_of_elements_to_avoid = args.avoid.split(',')
		input_fields = [
        	field for field in input_fields 
        	if field.get_attribute("name") not in list_of_elements_to_avoid and
        	field.get_attribute("id") not in list_of_elements_to_avoid and
        	field.get_attribute("type") not in ["button", "submit"]
   		 ]
	for field in input_fields:
		# Fill other fields with valid inputs
		# Taking field value appropriate to its type
		fieldType = field.get_attribute("type")
		if fieldType == "checkbox" or fieldType == "radio":
			driver.execute_script("arguments[0].checked = true;",field)
		# Adding support to handle <select> tags
		elif field.tag_name == "select":
        	# Select the second option
			options = field.find_elements(By.TAG_NAME,"option")
			# if there is two options in <select> choose second one as first option can be empty for example <option value="">choose country</option><option value="india">india</option>
			if options[1]:
				options[1].click()
			elif options[0]:
				options[0].click()
		elif field.tag_name =="textarea":
			remove_attributes(driver,field)
			field.clear()  # Clear any existing value
			field.send_keys("randomTextAreaValue")
		else:
			#Removing attribute that can conflict
			remove_attributes(driver,field)
			# Filling the predefined values
			fieldValue = attribute_values.get(fieldType,"defaultValue")
			driver.execute_script("arguments[0].setAttribute('value',arguments[1]);",field,fieldValue)

	# Fill target field which is being fuzzed with current payload	
	# Finding the element either by id, name or class
	try:
		element_being_fuzzed = driver.find_element(By.ID, element)
	except NoSuchElementException:
		try:
			element_being_fuzzed = driver.find_element(By.NAME, element)
		except NoSuchElementException:
			try:
				element_being_fuzzed = driver.find_element(By.CLASS_NAME, element)
			except NoSuchElementException as e:
				sleep(1.2)
				log_error(format_exc())
				print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: Specified element {element} is not found. Please verify the name of element, for more information check Error.txt\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
				driver.quit()
				sys.exit(0)

	# Check if element that is being fuzzed is <select> or not, if it is <select> then set payload to its first <option> tag and mark it as selected option
	if element_being_fuzzed.tag_name == "select":
		options = element_being_fuzzed.find_elements(By.TAG_NAME,"option")
		# if there is two options in <select> choose second one as first option can be empty for example <option value="">choose country</option><option value="india">india</option>
		if options:
			remove_attributes(driver,options[0])
			# Set payload to first option
			driver.execute_script("arguments[0].setAttribute('value',arguments[1]);", options[0], payload)
			options[0].click()
		
	elif element_being_fuzzed.tag_name =="textarea":
		remove_attributes(driver,element_being_fuzzed)
		field.clear()  # Clear any existing value
		field.send_keys(payload)
	else:
		#Removing attribute that can conflict
		remove_attributes(driver,element_being_fuzzed)
		# Setting the payload
		driver.execute_script("arguments[0].setAttribute('type','text');",element_being_fuzzed)
		driver.execute_script("arguments[0].setAttribute('value',arguments[1]);", element_being_fuzzed, payload)
	
	# Press the button
	try:
		driver.find_element(By.ID,args.button).click()
	except NoSuchElementException:
		try:
			driver.find_element(By.NAME,args.button).click()
		except NoSuchElementException:
			try:
				driver.find_element(By.CLASS_NAME,args.button).click()
			except NoSuchElementException as e:
				sleep(1.7)
				log_error(format_exc())
				print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: Button element {args.button} is not found to press, please verify the id or name of the button element, for more information check Error.txt\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
				driver.quit()
				sys.exit(0)

	# Getting current time	
	request_datetime = datetime.datetime.now()

	# Wait for all requests to be completed
	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_all_elements_located(("xpath", '//body')))

	# Note the response time to log it into report
	response_datetime = datetime.datetime.now()

	# Calculating the difference between request - response time in miliseconds
	cycle_time = response_datetime - request_datetime
	cycle_time_in_milliseconds = int(cycle_time.total_seconds() * 1000)
	if not args.silent:
		# Print the request
		print(f'\n{GREEN}---------------------Single Request/Response Cycle-------------------')
		print(f"Fuzzing - " + element)
		print(f"Payload - " + payload)
		print(f"{GREEN}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\nTIME: {cycle_time_in_milliseconds} MiliSeconds ({cycle_time})\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
				
	# Clear the cookies and other data
	if args.removeSession:
		driver.delete_all_cookies() 

### VARIOUS FUNCTIONS ENDS ###

### MAIN EXECUTION BLOCK STARTS ###
# Checking if script is running directly
if __name__ == "__main__":
	try:

		# Redirect stdout to the Tee class, the tee class redirects STDOUT to STDOUT and the log file
		log_file = 'logs/BrowserBruterSTDOUT.txt'  # This file stores console output
		tee_instance = Tee(log_file)
		sys.stdout = tee_instance
	
		# Get the elements to be fuzzed
		elements = args.elements.split(',')

		# Get the number of threads or in other words number of browsers instances to use
		num_threads = args.threads
	
		# Dividing payloads among threads and running the threads
		# Check the number of threads specified in the command line arguments
		num_threads = min(args.threads, 5)

		# Divide the payload data equally among the threads
		payloads_per_thread = len(payloads) // num_threads
		extra_payloads = len(payloads) % num_threads

		 # Create and start the keyboard listener thread which will pause and resume the BrowserBruter
		keyboard_thread = threading.Thread(target=pause_resume)
		keyboard_thread.start()

		# Create and start the threads
		threads = []
		start = 0

		for i in range(num_threads):
			end = start + payloads_per_thread
    		# Distribute extra payloads to the first few threads
			if i < extra_payloads:
				end += 1
    		# Extract the payloads for the current thread
			thread_payloads = payloads[start:end]
    		# Create a thread with the target function and arguments
			thread = threading.Thread(target=run_browser_instance, args=(thread_payloads,elements,i) )
    		# Start the thread
			thread.start()
    		# Add the thread to the list of threads
			threads.append(thread)
    		# Update the starting index for the next thread
			start = end
			# Sleep for 4 seconds for proper resource management
			sleep(4)

		# Wait for all threads to finish
		for thread in threads: 
			thread.join()
		# Set the terminate flag so the keyboard thread stops
		terminate = True
		
	except KeyboardInterrupt:
		signal_handler(signal.SIGINT, None)
		sleep(3)
		log_error(format_exc())
		print(f"{RED}CTRL+C{RESET}")
		sys.exit(0)
	except SystemExit:
		sleep(1.4)
		log_error(format_exc())
		print("")
	except:
		sleep(3.3)
		log_error(format_exc())
		# Print Traceback
		print_exc()
		# Ask user to send this to github
		print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: An unkown error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	finally:
		# Generate report
		generate_final_report()
		# wait for the thread which is responsible for puase-resume mechanism to stop
		keyboard_thread.join()
		# Reset sys.stdout to the console at the end of your script
		sys.stdout = sys.__stdout__ 
else:          
	print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: Please run the script again using python3 BurpBrowserBruter.py, closing the BrowserBruter\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")

### MAIN EXECUTION BLOCK ENDS ###