import time
import argparse
import csv
import datetime
import signal
import sys
import ast
import traceback
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
from bs4 import BeautifulSoup as bs


# Print logo because why not!
print("""
██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡀⠀⠀
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗⠀⠀⠀⠀⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣶⣶⣶⣶⣶⣾⣷⣾⣷⣶⠀. . . . .
██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝⠀⣶⣶⣶⣶⣶⣶⣶⡆⢸⣿⣿⣿⣿⣿⣿⡇⠸⠿⠿⠿⠿⠿⠿⢿⡿⢿⡿⠿⠀. . . . .
██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗⠀⣿⣿⣿⣿⣿⣿⣿⡇⠘⠛⢻⠟⠛⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠁⠀⠀
██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║⠀⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⣸⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝⠀⠀⠀⣆⠀⢶⡆⠀⠀⠀⢀⡟⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                                                                                                                      ⠀⠀⠀⢹⣄⠘⣷⡀⠀⢀⡼⠁⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                      ⠀⠀⠀⠀⠙⠦⡈⠻⢶⣿⣥⡾⠋ by Jafar Pathan & NetSquare Team""")

# Parse Command Line Arguments
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
	5. Fuzz on 3rd form of registration page with csrf and two cookies difficulty and hint
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3
	6. Fuzz on 3rd form of registration page with csrf and two cookies difficulty and hint and sent them forcefully on each request
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie
	7. Fuzz on 3rd form of registration page with csrf and two cookies difficulty and hint and sent them forcefully on each request and remove session data and cookie after each request-response cycle
	 > python3 BrowserBruter.py -e name,age,address,phone -p payloads.txt -t http://dvwa.com/register -b register --cookie difficulty:high:dvwa.com hint:no:dvwa.com --csrf _token --form 3 --forceCookie --remove
	'''
argParser.description += '\n' + usage_examples
argsRequired = argParser.add_argument_group("required")
argsRequired.add_argument("-t","--target",help="target's url: http://www.owasp.com/index.php, for example python3 BrowserBruter.py -t http://localhost/index.js")
argsRequired.add_argument("-e","--elements", help="Enter input fields in comma separated values for example suppose webpage has following input fields <input name='input1' type='text'/>, <input name='input2' type='number'/> then python3 BrowserBruter.py -e input1,input2")
argsRequired.add_argument("-p","--payloads",help="/path/to/file - for example suppose /tmp/payloads.txt is file containing payloads then python3 BrowserBruter.py -p /tmp/paylods.txt")
argsRequired.add_argument("-b","--button",help="button element, for example suppose web page has following element to submit form <input type='submit' id='submit'> then  python3 brute.py -t http://localhost:3000/ -e username,password -b submit -p payloads.txt --form 1")
argParser.add_argument("-C","--csrf",help="Input field containing CSRF token so BrowserBruter leaves it unmodified for example suppose web page has following hidden field <input type='hidden' name='csrf' value='csrfTOKEN'/>, then python3 BrowserBruter.py --csrf csrf")
argParser.add_argument("-d","--delay",help="Delay between each brute force attempt, for example -d 1 is 1 second delay, -d 0.5 is 0.5 seconds delay, use it make attack more reliable in case fuzzing process crashes due to speed, default delay is 0.2", type=float, default="0.2")
argParser.add_argument("-c","--cookie",help="Use it to define cookies to be used while sending request note cookies will be set only once and they might be changed by browser, cookies should be in name:value:domain format, example python3 BrowseBruter.py -c cookie_name1:cookie_value1:locahost cookie_name2:cookie_value2:example.com", metavar="name:value:domain", nargs="+")
argParser.add_argument("-f","--forceCookie",help="Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server,for example python3 BrowserBruter.py --cookie cookieName:Vlaue1:localhost --forceCookie",action="store_true")
argParser.add_argument("-r","--remove",help="Use this switch to remove session data and cookies after each request-response cycle, this is useful against Authentication pages when you don't want redirection in case of successful login, example python3 BrowserBruter.py --cookie cookieName:Vlaue1:localhost --forceCookie", action="store_true")
argParser.add_argument("-s","--silent",help="Use this switch to disable output being printed on console. for example python3 brute.py -t http://localhost/index.php -e username,password -b submit -p payloads.txt --silent", action="store_true")
argParser.add_argument("-F","--form",help="Specify the form number to fuzz, for example if webpage contains two form and you want to fuzz second form use --form 2, by default it fuzzes first form, this is necessary to avoid overhead, example  python3 brute.py -t http://localhost:3000/ -e username,password -b submit -p payloads.txt --form 3", default="1", type=int)
argParser.add_argument("-j","--javascript",help="This option lets you replace the webpage's javascript with specified code, for example 'var pass = 123$$$var pass = 321', this will replace javascript code before $$$ with javascript after $$$ delimiter, if you want to remove it put blank space after $$$, Please take note that this functionality is still in testing process and may not work even may result in crashing, also this only supports replacing javascript which is embedded, javascript loaded from external source is to be implemented", metavar="'existing$$$replacer'")

# Getting the arguments in args variable
args = argParser.parse_args()

# Check if all required arguments are given
if args.payloads is None or args.target is None or args.elements is None or args.button is None:
	argParser.print_help()
	sys.exit(0)

# Configure the driver
try:
	options = Options()
	options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
except:
	# Print Traceback
	traceback.print_exc()
	# Ask user to send this to github
	print("An error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/pulls and paste above message there, we are glad to help")
	driver.quit()
	sys.exit(0)

# Function to Replace Java script Note: this is still to be fully developed and further testing is required
def replace_javascript():
	# Retrieve whole webpage code 
	javascript_code = driver.execute_script("return document.documentElement.innerHTML")
	
	# Get string to remove and replacer string
	code_to_remove, replacer = args.javascript.split("$$$")

	# Search for the string in code
	if code_to_remove in javascript_code:
		
		# replace it
		modified_code = javascript_code.replace(code_to_remove,replacer)

		# Place it in browser
		driver.execute_script("document.documentElement.innerHTML = arguments[0];",modified_code)

# Non targeted input field value, will update this to allow user specify them, please contribute to add more types and let us know https://github.com/netsquare/BrowserBruter/pulls
attribute_values = {
	# This allows BrowserBruter to put default valid values into field which are not being fuzzed
	# For example BrowserBruter will send 0123456789 in fields which has type tel and which are not being fuzzed
	"text":"text",
	"number":"12",
	"password":"password",
	"email":"email@email.com",
	"url":"http://nvlkjdpfapdo.com/",
	"file":"name.txt",
	"tel":"0123456789",
	"date":"2023-06-17",
	"datetime":"2023-07-17T10:30",
	"time":"10:30",
	"month":"2023-07",
	"week":"2023-W25",
	"color":"#ff0000",
	"range":"50"

}


# Function to Handle CTRL+C signal
def signal_handler(signal, frame):
	print("\nCTRL+C pressed. Exiting...")
	driver.quit()
	sys.exit(0)

# Getting hostname from target for filtering the output this will work as one kind scope for filtering output to be stored in report
hostname = args.target
hostname = hostname.split("://",1)[-1]
hostname = hostname.split("/")[0]

# Getting current date and time to name the output file accrodingly
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{hostname}-{formatted_datetime}.csv"


# Functino to add cookies into selenium session
def add_cookies():
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
	except ValueError:
		print("Error: You have entered arguments in invalid format, please read help message for valid formate of passing cookies. Closing the Fuzzing process")
		driver.quit()
		sys.exit(0)
	except: 
		# Print Traceback
		traceback.print_exc()
		# Ask user to send this to github
		print("An error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/pulls and paste above message there, we are glad to help")
		driver.quit()
		sys.exit(0)
 	

# If cookies are provided assign them to session
if args.cookie:
	# first visit the domain so Chrome does not trow InvalidCookieDomainException
	driver.get(args.target)
	add_cookies()

# Function to attempt a single request-response cycle with payload
def attempt(element,payload):

	#Clear previous requests
	del driver.requests

	# If --force is set then set the initial cookies
	if args.forceCookie == True:
		add_cookies()

	# Go to the target website
	driver.get(args.target)

	# Replace Java script 
	if args.javascript:
		# Wait for body to be loaded in case of slow response
		wait = WebDriverWait(driver, 10)
		wait.until(EC.presence_of_all_elements_located(("xpath", '//body')))
		# Call replace_javascript
		replace_javascript()

	# Get the input field of form to be fill them
	input_fields = driver.find_elements("xpath",f"//form[{args.form}]//input")

	# Check if form with specified number exists or not
	if not input_fields:
		print("Form with specified number does not exists, please verify form number, closing the BrowserBruter")
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
		else:
			fieldValue = attribute_values.get(fieldType,"defaultValue")
			driver.execute_script("arguments[0].setAttribute('value',arguments[1]);",field,fieldValue)
			driver.execute_script("arguments[0].removeAttribute('pattern');",field)

	# Fill target field which is being fuzzed with current payload	
	# Finding the element either by id, name or class
	try:
		inputField = driver.find_element("id", element)
	except NoSuchElementException:
		try:
			inputField = driver.find_element("name", element)
		except NoSuchElementException:
			try:
				inputField = driver.find_element(By.CLASS_NAME, element)
			except NoSuchElementException:
				print("Error: Specified element is not found. Please verify the name of element")
				driver.quit()
				sys.exit(0)

	# Remove pattern attribute from input field cause it may conflict with payload
	if inputField.get_attribute("pattern"):
			driver.execute_script("arguments[0].removeAttribute('pattern');",inputField)
	# Setting the payload
	driver.execute_script("arguments[0].setAttribute('type','text');",inputField)
	driver.execute_script("arguments[0].setAttribute('value',arguments[1]);", inputField, payload)

	# Press the button
	try:
		driver.find_element("id",args.button).click()
	except NoSuchElementException:
		try:
			driver.find_element("name",args.button).click()
		except NoSuchElementException:
			try:
				driver.find_element(By.CLASS_NAME,args.button).click()
			except NoSuchElementException:
				print("Error: No Button element is found to press, please verify the id or name of the button element")
				driver.quit()
				sys.exit(0)

	# Getting current time to log it into report 		
	current_datetime = datetime.datetime.now()
	requestTime = current_datetime.strftime("%H-%M-%S")

	# Wait for all requests to be completed
	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_all_elements_located(("xpath", '//body')))

	# Note the response time to log it into report
	current_datetime = datetime.datetime.now()
	responseTime = current_datetime.strftime("%H-%M-%S")

	with open(filename,"w") as report:

		# Filtering request which are in scope
		captured_requests = driver.requests
		filtered_requests = [req for req in captured_requests if hostname in req.url]

		writer = csv.writer(report)
		writer.writerow(['Request Time','Element','Payload','Method','URL','Request Headers','Request Body','Response Time','Response Status Code','Response Reason','Response Headers','Response Body'])
		for request in filtered_requests:
			# Check whether should output be printed on console or not
			if not args.silent:
				# Print the request
				print('---------------------An Attempt-------------------')
				print("Element - " + element)
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
				writer.writerow([requestTime,element,payload,request.method,request.url,request.headers,request.body,responseTime,request.response.status_code,request.response.reason,request.response.headers,soup.prettify()])
			else:
				# Store the logs in report file
				raw = decode(request.response.body, request.response.headers.get('Content-Encoding','identity'))
				soup = bs(raw,features="html.parser")
				writer.writerow([requestTime,element,payload,request.method,request.url,request.headers,request.body,responseTime,request.response.status_code,request.response.reason,request.response.headers,soup.prettify()])
		
	# Clear the cookies and other data
	if args.remove == True:
		driver.delete_all_cookies() 

# Perform attempts
try:
	# Get Payloads
	payloads = []
	with open(args.payloads, "r") as s:
		for i in s:
			i = i.strip()
			payloads.append(i)

	# Get the elements to be fuzzed
	elements = args.elements.split(',')

	# Start the Fuzzing process
	for i in range(len(elements)):
		for j in range(len(payloads)):
			attempt(elements[i],payloads[j])
			time.sleep(args.delay)
			j += 1
		i+=i
	driver.quit()
	print("Fuzzing completed, check generated report")

# Handle the exceptions
except KeyboardInterrupt:
	signal_handler(signal.SIGINT, None)
except NoSuchWindowException:
	print("Browser's window has been closed, closing the BrowserBruter, check generated report")
	driver.quit()
	sys.exit(0)
except WebDriverException as e:
	if "target frame detached" in str(e) or "received Inspector.detached event" in str(e):
		print("Browser's window has been closed, closing the BrowserBruter, check generated report")
		driver.quit()
		sys.exit(0)
	else:
		# Print Traceback
		traceback.print_exc()
	
		# Ask user to send this to github
		print("An error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/pulls and paste above message there, we are glad to help")
		
except SystemExit:
	print("")
except:
	# Print Traceback
	traceback.print_exc()
	
	# Ask user to send this to github
	print("An error has been occured, Please open pull request at https://github.com/netsquare/BrowserBruter/pulls and paste above message there, we are glad to help")
	
