
### VARIOUS IMPORTS STARTS ###

import time
import argparse
import csv
import datetime
import signal
import sys
import traceback
import threading
import os
from seleniumwire import webdriver
from seleniumwire.utils import decode
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from http.client import RemoteDisconnected
from urllib3.exceptions import ProtocolError
from urllib3.exceptions import MaxRetryError
from bs4 import BeautifulSoup as bs

### VARIOUS IMPORTS ENDS ###

### PRINTING BANNER STARTS ###

print("""
##################################################################################################################################################################################
##################################################################################################################################################################################
##                                                                                                                                                                             ###
## ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░                                                       
## ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗⠀⠀⠀⠀⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣶⣶⣶⣶⣶⣾⣷⣾⣷⣶⠀. . . . . . . . . . . . . . . 
## ██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝⠀⣶⣶⣶⣶⣶⣶⣶⡆⢸⣿⣿⣿⣿⣿⣿⡇⠸⠿⠿⠿⠿⠿⠿⢿⡿⢿⡿⠿⠀. . . . .  . . . . . . . . . . 
## ██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗⠀⣿⣿⣿⣿⣿⣿⣿⡇⠘⠛⢻⠟⠛⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠁⠀⠀                  
## ██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║⠀⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⣸⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  
## ╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝⠀⠀⠀⣆⠀⢶⡆⠀⠀⠀⢀⡟⠀⣼⡇                                 
##                                                                                                                       ⠀⠀⠀⢹⣄⠘⣷⡀⠀⢀⡼⠁⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  
##                                                                                                                       ⠀⠀⠀⠀⠙⠦⡈⠻⢶⣿⣥⡾⠋ by Jafar Pathan & NetSquare Team v1.0 
##                                                                                                                           An Advance Browser Automated Web Form Fuzzing Tool### 
##################################################################################################################################################################################
##################################################################################################################################################################################""")

### PRINTING BANNER ENDS ###

### DEFINING AND PARSING COMMAND LINE ARGUMENTS START ###

argParser = argparse.ArgumentParser(description="BrowserBruter is a python3 script utilizing power of selenium and selenium-wire to automate fuzzing of variout input fields of webpages to test their security against malicious inputs. For contact and more information about project please visit https://github.com/netsquare/BrowserBruter",formatter_class=argparse.RawTextHelpFormatter)
usage_examples = '''
Usage Examples:
	1. Fuzz on login page
	 > python3 BrowserBruter.py -e username,password -p sqli.txt -t http://owasp.com/login -b loginButton
	
	2. Fuzz on login page with csrf enabled
	 > python3 BrowserBruter.py -e username,password -p sqli.txt -t http://owasp.com/login -b loginButton --csrf csrfToken
	
	3. Fuzz on registration page with csrf enabled no output printed on console
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --csrf _token --silent
	
	4. Fuzz on 3rd form of registration page with csrf enabled no output printed on console
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --csrf _token --silent --form 3
	
	5. Fuzz on registration page with csrf and two cookies difficulty and hint
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token
	
	6. Fuzz on registration page with csrf and two cookies difficulty and hint and sent them forcefully on each request
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --forceCookie
	
	7. Fuzz on 3rd form of registration page with csrf and two cookies difficulty and hint and sent them forcefully on each request and remove session data and cookie after each request-response cycle
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie --remove
	
	8. Fuzz on 3rd form of registration page with csrf and two cookies difficulty and hint and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie --remove --headless
	
	9. Fuzz on 3rd form of registration page with csrf and two cookies difficulty and hint and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode and run 5 instances of browser parallely
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie --remove --headless --threads 5
   
   10. Fuzz CheckBox for example '<input type="checkbox" name="hobbies" value="reading" /> <input type="checkbox" name="hobbies" value="writing" />', then
	 > python3 BrowserBruter.py -e hobbies -p paylods.txt -t http://dvwa.com/register -b register
   
   11. Fuzz Radio Button for example '<input type="radio" name="yesno" id="yes" value="yes" required/> <input type="radio" name="yesno" id="no" value="no" required/>', then
	 > python3 BrowserBruter.py -e yesno -p payloads.txt -t http://dvwa.com/register -b register 
	 OR
	 > python3 BrowserBruter.py -e no -p payloads.txt -t http://dvwa.com/register -b register
   
   12. Fuzz CSRF token + don't overwrite it while fuzzing other fields
     > python3 BrowserBruter.py -e csrfToken,username,password -p payloads.txt -t http://dvwa.com/login -b login --csrf csrfToken
   
   13. Fuzz <select> element - for example <select name="selectElement" required> <option value="">Select an option</option> <option value="option1">Option 1</option> </select>, then
     > python3 BrowserBruter.py -e selectElement -p payloads.txt -t http://dvwa.com/selection -b submit
   
   14. Fuzz <textarea> element - for example <textarea name="textareaElement" placeholder="Enter text" required></textarea>, then
     > python3 BrowserBruter.py -e textareaElement -p payloads.txt -t http://dvwa.com/registration -b submit
   
   15. Fuzz colorpicker, datepicker, timepicker - for example <input type="color" name="colorElement" required/> <input type="date" name="dateElement" required/> <input type="time" name="timeElement" required/>, then
     > python3 BrowserBruter.py -e colorElement,dateElement,timeElement -p payloads.txt -t http://localhost/ -b submit
	'''
argParser.description += '\n' + usage_examples
argsRequired = argParser.add_argument_group("required")
argsRequired.add_argument("-t","--target",help="target's url: http://www.owasp.com/index.php, for example python3 BrowserBruter.py -t http://localhost/index.js")
argsRequired.add_argument("-e","--elements", help="Enter input fields in comma separated values for example suppose webpage has following input fields <input name='input1' type='text'/>, <input name='input2' type='number'/> then python3 BrowserBruter.py -e input1,input2")
argsRequired.add_argument("-p","--payloads",help="/path/to/file - for example suppose /tmp/payloads.txt is file containing payloads then python3 BrowserBruter.py -p /tmp/paylods.txt")
argsRequired.add_argument("-b","--button",help="button element, for example suppose web page has following element to submit form <input type='submit' id='submit'> then  python3 brute.py -t http://localhost:3000/ -e username,password -b submit -p payloads.txt --form 1")
argParser.add_argument("-C","--csrf",help="Input field containing CSRF token so BrowserBruter leaves it unmodified for example suppose web page has following hidden field <input type='hidden' name='csrf' value='csrfTOKEN'/>, then python3 BrowserBruter.py --csrf csrf")
argParser.add_argument("-d","--delay",help="Delay between each brute force attempt, for example -d 1 is 1 second delay, -d 0.5 is 0.5 seconds delay, use it make attack more reliable in case fuzzing process crashes due to speed, default delay is 0.2", type=float, default=0.2)
argParser.add_argument("-c","--cookie",help="Use it to define cookies to be used while sending request note cookies will be set only once and they might be changed by browser, cookies should be in name:value:domain format, example python3 BrowseBruter.py -c cookie_name1:cookie_value1:locahost cookie_name2:cookie_value2:example.com", metavar="name:value:domain", nargs="+")
argParser.add_argument("-f","--forceCookie",help="Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server,for example python3 BrowserBruter.py --cookie cookieName:Vlaue1:localhost --forceCookie",action="store_true")
argParser.add_argument("-r","--remove",help="Use this switch to remove session data and cookies after each request-response cycle, this is useful against Authentication pages when you don't want redirection in case of successful login, example python3 BrowserBruter.py --cookie cookieName:Vlaue1:localhost --forceCookie", action="store_true")
argParser.add_argument("-s","--silent",help="Use this switch to disable output being printed on console. for example python3 brute.py -t http://localhost/index.php -e username,password -b submit -p payloads.txt --silent", action="store_true")
argParser.add_argument("-F","--form",help="Specify the form number to fuzz, for example if webpage contains two form and you want to fuzz second form use --form 2, example  python3 brute.py -t http://localhost:3000/ -e username,password -b submit -p payloads.txt --form 3", type=int)
argParser.add_argument("-L","--headless",help="Use this switch to run browser in headless mode (No GUI), this is useful to save resources, though it is recommended to first run browser in GUI mode to verify the fuzzing is working properly, and in headless it is recommended to avoid --silent mode so logs can be printed on console", action="store_true")
argParser.add_argument("-T","--threads",help="Specifies number of browsers instances to be run, max value is 5, default is 1, lower the instances slower the fuzzing process, more instances - faster fuzzing process, In other words --threads 1 slow, --threads 3 fast, --threads 5 faster",default=1, type=int)

# Getting the arguments in args variable
args = argParser.parse_args()

# Check if all required arguments are given and threads are not more than 5
if args.payloads is None or args.target is None or args.elements is None or args.button is None:
	print("Please Enter all required arguments --target, --paylods, --elements, --button")
	sys.exit(0)
elif args.threads > 5 or args.threads < 0:
	print("Value of threads must less than 6 and more than 0")
	sys.exit(0)
elif args.forceCookie:
	if args.cookie is None:
		print("You can not use --forceCookie without --cookie option")
		sys.exit(0)

### DEFINING AND PARSING COMMAND LINE ARGUMENTS ENDS ###

### DEFINING AND ASSIGNING GLOBAL VARIABLES STARTS ###

# Getting hostname from target for filtering the output this will work as one kind scope for filtering output to be stored in report
hostname = args.target
hostname = hostname.split("://",1)[-1]
hostname = hostname.split("/")[0]

# Getting time when script started to name the final report
start_time = datetime.datetime.now()
start_time = start_time.strftime("%Y-%m-%d_%H-%M-%S")

# Setting flag which indicates threads to run or stop
terminate = False

# Creating Reports directory in current directory to store reports
if not os.path.exists("BrowserBruter_Reports"):
	os.makedirs("BrowserBruter_Reports")
if not os.path.exists(f"BrowserBruter_Reports/{hostname}/{start_time}"):
	os.makedirs(f"BrowserBruter_Reports/{hostname}/{start_time}")

# Non targeted input field value, will update this to allow user specify them, please contribute to add more types and let us know https://github.com/netsquare/BrowserBruter/issues
attribute_values = {
	# This allows BrowserBruter to put default valid values into field which are not being fuzzed
	# For example BrowserBruter will send 0123456789 in fields which has type tel and which are not being fuzzed
	"text":"text",
	"number":"1234567890",
	"password":"password",
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

### DEFINING AND ASSIGNING GLOBAL VARIABLES ENDS ###

### FUNCTIONS STARTS ###

# Function to Handle CTRL+C signal
def signal_handler(signal, frame):
	print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: CTRL+C pressed. Waiting for remaining request/response to stop. Exiting...\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	# Set the global termination flag to True so all threads can stop gracefully
	global terminate
	terminate = True

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
		time.sleep(2)
		log_error(traceback.format_exc())
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: You have entered arguments in invalid format, please read help message for valid formate of passing cookies. Closing the Fuzzing process\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		driver.quit()
		sys.exit(0)

# Function to Remove attributes
def remove_attributes(driver, field):
	driver.execute_script("arguments[0].removeAttribute('pattern');",field)
	driver.execute_script("arguments[0].removeAttribute('min');",field)
	driver.execute_script("arguments[0].removeAttribute('max');",field)
	driver.execute_script("arguments[0].removeAttribute('maxlength');",field)
	driver.execute_script("arguments[0].removeAttribute('minlength');",field)
	driver.execute_script("arguments[0].removeAttribute('readonly');",field)

# Function to log errors 
def log_error(error):
	#log_file_lock.acquire()
	try:
		with open("Error.log","a") as log:
				error_time = datetime.datetime.now()
				error_time = error_time.strftime("%Y-%m-%d_%H-%M-%S")
				log.write("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
				log.write(f"Error Time - {error_time}")
				log.write("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
				log.write(error)
	except:
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: An unknown error has been occured, Please open issue request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Funtion to Generate filename for each differnt thread
def get_filename():
	# Getting current date and time to name the output file accrodingly
	current_datetime = datetime.datetime.now()
	formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
	filename = f"BrowserBruter_Reports/{hostname}/{start_time}/{hostname}-{formatted_datetime}.csv"
	return filename

# Function to Generate Final Report
def generate_final_report():
	print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Genrating Final Report\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	directory = f"BrowserBruter_Reports/{hostname}/{start_time}"
	final_report = f"BrowserBruter_Reports/{hostname}/{start_time}/{hostname}-{start_time}.csv"
	all_threads_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

	# Merge other files into single final report
	with open(final_report, 'w',newline='') as final:
		writer = csv.writer(final)

		# Insert columns names or in other words headings
		writer.writerow(['Request Time','Selected','Payload','Web Page Before','Method','URL','Request Headers','Request Body','Response Time','Cycle Time MilliSeconds','Response Status Code','Response Reason','Response Headers','Response Body', 'Web Page After'])
		# Iterate over each CSV file
		for csv_file in all_threads_files:
			file_path = os.path.join(directory, csv_file)

        	# Open the current CSV file in 'r' mode
			with open(file_path, 'r') as infile:
				reader = csv.reader(infile)

            	# Read and write the rows to the output file
				writer.writerows(reader)

        	# Delete the current CSV file
			os.remove(file_path)
	print(f"\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Report Generated -> {final_report}\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Funtion to Run Single Browser instance
def run_browser_instance(payloads, elements, instance_number):
	try:
		options = Options()
		options.add_argument('--disable-dev-shm-usage')
		# Check if browser has to be run headless mode
		if args.headless:
			options.add_argument('--headless')
		driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
	
		# If cookies are provided assign them to session
		if args.cookie:
			# first visit the domain so Chrome does not trow InvalidCookieDomainException
			driver.get(args.target)
			add_cookies(driver)

		# Initialize report file
		this_threads_file = get_filename()

		# Start the Fuzzing process
		for i in range(len(elements)):
			for j in range(len(payloads)):
					if not terminate:
						attempt(elements[i],payloads[j], driver, this_threads_file)
						time.sleep(args.delay)
					j += 1
			i+=i
		print(f"\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Fuzzing completed for Browser Instance number - {instance_number}\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

	# Handle the exceptions which specific to this thread and does not affects other threads
	except NoSuchWindowException as e:
		time.sleep(0.5)
		log_error(traceback.format_exc())
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	except RemoteDisconnected as e:
		time.sleep(0.7)
		log_error(traceback.format_exc())
		# This exception can be arrived whene user closes browser window
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	except ProtocolError as e:
		time.sleep(0.9)
		log_error(traceback.format_exc())
		# This exception can be arrived whene user closes browser window
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	except MaxRetryError as e:
		time.sleep(0.3)
		error = traceback.format_exc()
		log_error(error)
		# This exception can be arrived whene user closes browser window
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Browsers has reached maximum retries, if you have closed BrowserBruter ignore this else report the issue, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	except WebDriverException as e:
		time.sleep(1)
		log_error(traceback.format_exc())
		# This exception can be arrived whene user closes browser window
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
	except:
		time.sleep(3.5)
		log_error(traceback.format_exc())
		# Print Traceback
		traceback.print_exc()
		# Ask user to send this to github
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: An unkown error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	finally:
		# close the specific thread's driver
		driver.quit()

# Function to attempt a single request-response cycle with payload
def attempt(element, payload, driver, filename):

	# If --force is set then set the initial cookies
	if args.forceCookie == True:
		add_cookies()

	# Go to the target website
	driver.get(args.target)

	#Clear previous requests
	del driver.requests

	# Wait for body to be loaded in case of slow response
	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_all_elements_located(("xpath", '//body')))

	# Get web page content before making request
	webpage_before = driver.page_source

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
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: Form with specified number does not exists, please verify form number, closing the BrowserBruter\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		driver.quit()
		sys.exit(0)

	# Remove CSRF token field to avoid overwriting it
	if args.csrf:
		input_fields = [field for field in input_fields if field.get_attribute("name") != args.csrf and field.get_attribute("id") != args.csrf and field.get_attribute("type") != "button" and field.get_attribute("type") != "submit"]
	
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
				time.sleep(1.2)
				log_error(traceback.format_exc())
				print(f"\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: Specified element {element} is not found. Please verify the name of element, for more information check Error.log\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
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
				time.sleep(1.7)
				log_error(traceback.format_exc())
				print(f"\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: Button element {args.button} is not found to press, please verify the id or name of the button element, for more information check Error.log\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
				driver.quit()
				sys.exit(0)

	# Getting current time to log it into report 		
	request_datetime = datetime.datetime.now()
	requestTime = request_datetime.strftime("%H-%M-%S")

	# Wait for all requests to be completed
	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_all_elements_located(("xpath", '//body')))

	# Get web page content after making response
	webpage_after = driver.page_source

	# Note the response time to log it into report
	response_datetime = datetime.datetime.now()
	responseTime = response_datetime.strftime("%H-%M-%S")

	# Calculating the difference between request - response time in miliseconds
	cycle_time = response_datetime - request_datetime
	cycle_time_in_milliseconds = int(cycle_time.total_seconds() * 1000)

	with open(filename,'a', newline='') as report:

		# Filtering request which are in scope
		captured_requests = driver.requests
		filtered_requests = [req for req in captured_requests if hostname in req.url]

		writer = csv.writer(report)
		for request in filtered_requests:
			# Check whether should output be printed on console or not
			if not args.silent:
				# Print the request
				print('\n---------------------Single Request/Response Cycle-------------------')
				print("Fuzzing - " + element)
				print("Payload - " + payload)
				print('----------------------REQUEST---------------------')
				print('Time - '+requestTime+'\n', request.method, request.url)
				# Print in new line
				print(request.headers, request.body)
				# Print the response
				print('----------------------RESPONSE--------------------')
				if request.response:
					print(
						'Time - '+responseTime+'\n',
						request.response.status_code,
						request.response.reason,
						#bs.prettify(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
					)
				print(request.response.headers)
				raw = decode(request.response.body, request.response.headers.get('Content-Encoding','identity'))
				# Using BeutifulSoup4 to reformat the HTML content
				soup = bs(raw,features="html.parser")
				print(soup.prettify())
				# After printing on display write it to report
				row = [value if value else '-' for value in [requestTime, element, payload, webpage_before, request.method, request.url, request.headers, request.body, responseTime, cycle_time_in_milliseconds, request.response.status_code, request.response.reason, request.response.headers, soup.prettify(), webpage_after]]
				writer.writerow(row)
			else:
				# Store the logs in report file
				raw = decode(request.response.body, request.response.headers.get('Content-Encoding','identity'))
				soup = bs(raw,features="html.parser")
				# Substituting blank or no values with N/A then writing it to file
				print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n\n{cycle_time}\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
				row = [value if value else '-' for value in [requestTime, element, payload, webpage_before, request.method, request.url, request.headers, request.body, responseTime, cycle_time_in_milliseconds, request.response.status_code, request.response.reason, request.response.headers, soup.prettify(), webpage_after]]
				writer.writerow(row)
		
	# Clear the cookies and other data
	if args.remove == True:
		driver.delete_all_cookies() 

### VARIOUS FUNCTIONS ENDS ###

### MAIN EXECUTION BLOCK STARTS ###
# Checking if script is running directly
if __name__ == "__main__":
	try:
		# Get Payloads
		payloads = []
		with open(args.payloads, "r") as s:
			for i in s:
				i = i.strip()
				payloads.append(i)

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
			time.sleep(4)

		# Wait for all threads to finish
		for thread in threads: 
			thread.join()

	except KeyboardInterrupt:
		signal_handler(signal.SIGINT, None)
		time.sleep(3)
		log_error(traceback.format_exc())
		print("CTRL+C")
		sys.exit(0)
	except SystemExit:
		time.sleep(1.4)
		log_error(traceback.format_exc())
		print("")
	except:
		time.sleep(3.3)
		log_error(traceback.format_exc())
		# Print Traceback
		traceback.print_exc()
		# Ask user to send this to github
		print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: An unkown error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	finally:
		generate_final_report()
else:          
	print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError: Please run the script again using python3 BrowserBruter.py, closing the BrowserBruter\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

### MAIN EXECUTION BLOCK ENDS ###
