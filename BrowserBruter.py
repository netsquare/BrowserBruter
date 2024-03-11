### VARIOUS IMPORTS STARTS ###

import argparse
import csv
import datetime
import signal 
import sys
import threading
import os
import json
import gzip
import warnings
import pandas as pd
from itertools import product
from tqdm import tqdm
from pytimedinput import timedKey
from traceback import format_exc, print_exc
from time import sleep
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import InvalidCookieDomainException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import JavascriptException
from http.client import RemoteDisconnected
from urllib3.exceptions import ProtocolError
from urllib3.exceptions import MaxRetryError
from urllib3.util import Retry
from threading import Lock
from bs4 import BeautifulSoup as bs
from bs4 import MarkupResemblesLocatorWarning
from bs4 import XMLParsedAsHTMLWarning
from urllib.parse import urlparse
import urllib.parse
from colorama import Fore

# Custom python files
from res.tee import Tee
from res.usage_manual import print_manual

### VARIOUS IMPORTS ENDS ###

# Defining color contants #
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE

### PRINTING BANNER ###
print(f"""
{GREEN}###############################################################################################################################
{GREEN}###############################################################################################################################
{GREEN}###                                                                                                                         ###
{GREEN}### {YELLOW}██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░  {GREEN}###
{GREEN}### {YELLOW}██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗  {GREEN}###
{GREEN}### {YELLOW}██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝  {GREEN}###
{GREEN}### {YELLOW}██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗  {GREEN}###
{GREEN}### {YELLOW}██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║  {GREEN}###
{GREEN}### {YELLOW}╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  {GREEN}###
{GREEN}###                                                                                   {YELLOW}by Jafar Pathan(@github/zinja-coder)  {GREEN}###
{GREEN}###                                                                                                                         {GREEN}###
{GREEN}###                                                                                                                         {GREEN}###
{GREEN}### 	                   {YELLOW}The First-Ever Advance Browser Based Automated Web Form Fuzzing Tool                             {GREEN}###
{GREEN}### 	                   {YELLOW}Version: {BLUE} v2024.3.1                                                                              {GREEN}###
{GREEN}###                        {YELLOW}Github : {BLUE} https://github.com/netsquare/BrowserBruter                                             {GREEN}###
{GREEN}###                                                                                                                         {GREEN}###
{GREEN}###        {RED}     ..,:dOkxl:.                                                                                                 {GREEN}###
{GREEN}###         {RED}.,coooooooooooooc,.                                                                                             {GREEN}###
{GREEN}###      {RED}.,lllllllllllllllllllll,.                                                                                          {GREEN}###
{GREEN}###     {RED};ccccccccccccccccccccccccc;                                                                                         {GREEN}###
{GREEN}###   {RED}'ccccccccccccccccccccccccccccc.                                                                                       {GREEN}###
{GREEN}### {GREEN} ,ooc::::::::ok{RESET}O0000{YELLOW}OOkkkkkkkkkkk:                _____                                                                 {GREEN}###
{GREEN}### {GREEN}.ooool;;;;:x{RESET}K0{BLUE}kxxxxxk{RESET}0X{YELLOW}K0000000000.            .'{RED}:::::::{YELLOW}'.                                                              {GREEN}###
{GREEN}### {GREEN}:oooool;,;O{RESET}K{BLUE}ddddddddddd{RESET}KX{YELLOW}000000000d       ___ /{RED}:::::::::::{YELLOW}\\____ _            {GREEN}_.''_                                      ###
{GREEN}### {GREEN}lllllool;l{RESET}N{BLUE}dllllllllllld{RESET}N{YELLOW}K000000000    {RESET}/{YELLOW}||   ||`.______.-`||   | |\\_{BLUE}\\\\\\\\{YELLOW}____/_{GREEN} _.-'{BLUE}\\\\\\\\{RED}-- -- -- -- -- --                {GREEN}###
{GREEN}### {GREEN}lllllllllo{RESET}M{BLUE}dccccccccccco{RESET}W{YELLOW}K000000000.{RESET}|-|{YELLOW} ||===||           ||===| ||_{BLUE}||||{YELLOW}____|_|{GREEN} .-'{BLUE}|||||{RED}-- -- -- -- -- --               {GREEN}###
{GREEN}### {GREEN};cllllllllX{RESET}X{BLUE}c:::::::::c{RESET}0X{YELLOW}000000000d'{RESET}|-|{YELLOW} ||===||===========||===| ||_{BLUE}||||{YELLOW}____|_|{GREEN}`-._{BLUE}|||||{RED}-- -- -- -- -- --               {GREEN}###
{GREEN}### .ccccllllllO{RESET}Nk{BLUE}c;,,,;cx{RESET}KK{YELLOW}0000000000.    {RESET}\{YELLOW}||___||___________||___|_|/ {BLUE}////{YELLOW}   {RESET}##{GREEN}  `-._{BLUE}////{RED}-- -- -- -- -- --                {GREEN}###
{GREEN}### .cccccclllllxOO{RESET}OOOOkx{YELLOW}O0000000000;          )  _____  (                     {RESET}##                                           {GREEN}###
{GREEN}###   {GREEN}.:ccccccccllllllllo{YELLOW}O0000000OOO,          / .'| {RESET}({YELLOW}  '. \\                   {RESET}##                                           {GREEN}###
{GREEN}###     {GREEN},:ccccccccclllcd{YELLOW}0000OOOOOOl.          (  './    )   )                  {RESET}##                                           {GREEN}###
{GREEN}###       {GREEN}'::ccccccccc{YELLOW}dOOOOOOOkx:.             \ '._____.' /                   {RESET}##                                           {GREEN}###
{GREEN}###         {GREEN}..,::cccc{YELLOW}xOOOkkko;.                 '._______.'                    {RESET}##                                           {GREEN}###
{GREEN}###             {GREEN}..,:{YELLOW}dOkxl:.                                                    {RESET}##                                           {GREEN}###
{GREEN}###           {RESET}###############                                                  {RESET}##                                           {GREEN}###
{GREEN}###          {RESET}#################                                                {RESET}####                                          {GREEN}###
{GREEN}###         {RESET}###################                                              {RESET}######                                         {GREEN}###
{GREEN}###############################################################################################################################
{GREEN}###############################################################################################################################{RESET}""")


### DEFINING AND PARSING COMMAND LINE ARGUMENTS START ###
# Getting argument parser to parse and process arguments
argParser = argparse.ArgumentParser(description="BrowserBruter is a python3 script, utilizing power of selenium and selenium-wire to automate fuzzing of various input fields of webpages to test their security against malicious inputs. For contact and more information about project please visit https://github.com/netsquare/BrowserBruter",formatter_class=argparse.RawTextHelpFormatter)

# Adding various command line arguments
args_basic = argParser.add_argument_group("Basic")
args_attack1n2 = argParser.add_argument_group("Sniper and Battering Ram")
args_attack3n4 = argParser.add_argument_group("PitchFork and Cluster Bomb")
args_fuzz = argParser.add_argument_group("Fuzzing and Browser Options")
args_session = argParser.add_argument_group("Session")
args_javascript = argParser.add_argument_group("JavaScript and Code Handling")
args_browser = argParser.add_argument_group("Browser Options")
args_debug = argParser.add_argument_group("Debug Option")
args_report = argParser.add_argument_group("Report Generation")
args_help = argParser.add_argument_group("Help")

# Adding CLI arguments
args_basic.add_argument("--target",help="Target's url: https://zinja-coder.github.io/jafarpathan", metavar="TARGET_URL")
args_basic.add_argument("--button",help="Button element which will submit form data.", metavar="submit")
args_basic.add_argument("--attack",help="The attack mode:\n 1. SNIPER\n 2. BATTERING RAM\n 3. PITCH FORK\n 4. CLUSTER BOMB",type=int,metavar="2")
args_attack1n2.add_argument("--elements", help="Input fields(target elements of form) in comma separated values.", metavar="username,password,phone,address")
args_attack3n4.add_argument("--elements-payloads",help="Input fields(target elements of form) and their respective payloads files.", metavar="FIELD:/PATH/TO/FILE,textarea:payloads.txt,data:pay.txt")
args_attack1n2.add_argument("--payloads",help="/path/to/payload/file.", metavar="/home/payloads.txt")
args_fuzz.add_argument("--fill",help="Auto fill the specified elements, usefull when web page is complex when you want to target specific fields only.",metavar="e1,elemn3,user,npass,id")
args_fuzz.add_argument("--fill-values", help="[Optional] Path to User provided elements values file. See sample-file-for-giving-form-values.json", metavar="/path/to/file.json")
args_fuzz.add_argument("--buttons-to-press-before-fuzz",help="Supply list of buttons to be pressed in sequence before filling the form, useful if form submission requires some action or form is invisible until some button is pressed.[Note if the button is not pressable elment, then use --javascript and suppy javascript to click the element.]",metavar="visibleform,ok,confirm,pressthis")
args_fuzz.add_argument("--press-enter-no-click",help="This switch will force the Browser Bruter to send ENTER key instead of clicking the button, useful when form is submitted when pressing entering on text field and there are no buttons to click.", action="store_true")
args_fuzz.add_argument("--proxy",help="Set proxy for traffic, for example give IP:PORT of Burpsuite to send traffic to burpsuite.",metavar="http://proxyaddress:port/")
args_fuzz.add_argument("--delay-before",help="Delay before fuzz attempt.",metavar="0.2", type=float, default=0.2)
args_fuzz.add_argument("--delay-after",help="Delay after fuzz attempt.",metavar="0.2", type=float, default=0.2)
args_fuzz.add_argument("--threads",help="Specifies number of browsers instances to be run, max value is 5, default is 1, lower the instances slower the fuzzing process, more instances - faster fuzzing process.",metavar="3",default=1, type=int)
args_fuzz.add_argument("--pause", help="Pause the BrowserBruter instances on startup, press ENTER to resume.",action="store_true",default=False)
args_fuzz.add_argument("--interactive",help="Pause the BrowserBruter before fuzzing any element at each payload and wait for user to continue.",action="store_true",default=False)
args_fuzz.add_argument("--pause-after-submit",help="Pause the script after pressing the submit button to allow pentester to interact with the web application.",action="store_true")
args_fuzz.add_argument("--reload-page",help="This switch tells The Browser Bruter to reload the page before fuzzing the form on each iteration, usefull when result of previous iteration causes the web elements to disappear or which leads to elements not found error, in such case this switch helps to keep browser bruter running.", action="store_true")
args_fuzz.add_argument("--form",help="Specy id,name,class of form to fuzz in case of muliple forms",metavar="changePasswordForm")
args_fuzz.add_argument("--ignore-popups",help="Ignore alert and other pop up menus",action="store_true",default=False)
args_fuzz.add_argument("--remove-class",help="Provide a list of elements from which you want to remove the class attribute, extremely useful when element is linked to some class with extreme javascript input validation or makes the element not interactable, you can still select this element by providing it's class name.", metavar="cdk-text-field-autofill-monitored")
args_session.add_argument("--headers", help="Comma-separated list of custom headers.",metavar="\"Auth: 123\",\"CUSTOME_HEADER: VALUE\"")
args_session.add_argument("--cookie",help="Use it to define cookies to be used while sending initial request, cookies should be in name:value:domain comma separated format.", metavar="name:value,name2:value2")
args_session.add_argument("--force-cookie",help="Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server.",action="store_true")
args_session.add_argument("--remove-session",help="Use this switch to remove session data and cookies after each request-response cycle.", action="store_true")
args_javascript.add_argument("--auto-remove-javascript-validation",help="This switch will tell The Browser-Bruter to not remove common javascript input validations mechanisms. Useful if removing of javacript validaiton breaks the web app.", action="store_true",default=False)
args_javascript.add_argument("--javascript",help="Javascript code to run on browser", metavar="\"alert(1);\"")
args_javascript.add_argument("--javascript-after",help="Javascriptc code to run on browser after pressing and submitting the button.")
args_javascript.add_argument("--javascript-file",help="Javascritp file containing javascript code to execute", metavar="/path/to/javascript/file.js")
args_javascript.add_argument("--replace-code",help="Replaces the code in response body with the code provided by user in following format - \"CODE_TO_REPLACE1\",\"REPLACEMENT_CODE1\",\"CODE_TO_REPLACE2\",\"REPLACEMENT_CODE2\"",metavar="\"alert(1);\",\"alert(0);\"")
args_javascript.add_argument("--replace-files", help="Replace the content of a file in HTTP responses.", metavar="/path/to/validation_file.js")
args_browser.add_argument("--headless",help="Use this switch to run browser in headless mode (No GUI).", action="store_true")
args_browser.add_argument("--no-css",help="This switch will tell Browser Bruter to drop the requests to .css files and it will load .css files",action="store_true")
args_browser.add_argument("--load-static-media",help="This switch tells BrowserBruter to load audio, video and image (.png, .img, .ico, .mp4, .gif, .mp3 etc) files. By default it discards these files to save time and load pages faster.",action="store_true",default=False)
args_browser.add_argument("--chrome-options",help="Custom comma separated list of options which will be passed to chrome. [This will override in-built options in Browser-Bruter that are passed to chrome]",metavar="blink-settings=imagesEnabled=false,disable-notifications")
args_browser.add_argument("--anti-bot",help="This switch tells BrowserBruter to use avoid any chrome options and use raw undetected chrome driver to avoid bot detection, by default Browser-Bruter uses custom Chrome options along with undetected chrome driver like disabling xss protection along with undeteced chrome driver",action="store_true",default=False)
args_browser.add_argument("--no-anti-bot",help="Completely removes any anti bot detection evasions.",action="store_true",default=False)
args_browser.add_argument("--new-instance",help="Start new fresh instance of browser for each new payload [Fuzzing process's iteration] usefull in bypassing the invisible captchas.",action="store_true")
args_report.add_argument("--rows-limit",help="Specify the number of rows to be included in single file, if not specified, a single report will be generated, if specified, multiple reports with specified rows amount will be generated, useful when test consists of thousands of payloads.", type=int, metavar="200")
args_report.add_argument("--scope",help="Comma separated list of hostnames in scope",metavar="api1.example.com,bak.example.com")
args_report.add_argument("--include-urls",help="Comma-separated list of urls or file containing urls in-scope", metavar="/path/to/file OR \"https://api1.example.com/v2/getData\",\"https://bak.example.com/v2/signin\"")
args_report.add_argument("--exclude-urls",help="Comma separated list of urls or file containing urls which are to be excluded from final report", metavar="/path/to/file OR \"http://10.13.37.3:8080/webgoat/service/hint.mvc\",\"http://10.13.37.3:8080/webgoat/service/solution.mvc\"")
args_debug.add_argument("--verbose",help="Use this switch to enable HTTP request/response output being printed on console and STDLOG file.", action="store_true",default=False)
args_debug.add_argument("--debug",help="Use this switch to print the Stack Trace messages in case of the error! and keep the logs in log file.",action="store_true")
args_help.add_argument("--help-manual",help="Print the Usage Exapmles",action="store_true")

# Getting the arguments in args variable
args = argParser.parse_args()

# If user has enter --manual then print the manual and exit
if args.help_manual:
    print_manual()
    sys.exit(0)

# Check if all required arguments are given and threads are not more than 5
if ((args.payloads is None or args.elements is None) and (args.elements_payloads is None)) or args.target is None or args.button is None or args.attack is None:
	print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Please Enter all required arguments --attack, --target, --button, --payloads, --elements or --elements-payloads or --help for help.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
	sys.exit(0)
elif args.threads > 20 or args.threads < 0:
	print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Value of threads must less than 8 and more than 0\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
	sys.exit(0)
elif (args.elements and args.elements_payloads):
    print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}--elements and --elements--payloads can't be used together\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    sys.exit(0)
# if force-cookie argument is present withouth --cookie option then throw error 
elif args.force_cookie:
	if args.cookie is None:
		print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}You can not use --forceCookie without --cookie option\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
		sys.exit(0)

### DEFINING AND PARSING COMMAND LINE ARGUMENTS ENDS ###

### DEFINING AND ASSIGNING GLOBAL VARIABLES STARTS ###	

# Getting hostname from target for filtering the output this will work as one kind scope for filtering output to be stored in report
target_url = urlparse(args.target)
hostname = target_url.hostname
# Get the scope hostnames from the command-line arguments
scope_hostnames = args.scope.split(',') if args.scope else []
# Get the urls to be excluded from final report
list_of_urls_to_be_excluded_from_final_report = []
if args.exclude_urls:
    try:
        with open(args.exclude_urls,"r") as urls_excluded_file:
                for line in urls_excluded_file:
                    line = line.strip()
                    list_of_urls_to_be_excluded_from_final_report.append(line)
    except FileNotFoundError:
        list_of_urls_to_be_excluded_from_final_report = args.exclude_urls.split(',')
    except Exception as e:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}There is a problem with -> {args.exclude_urls}\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        if args.debug:
            print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}{print_exc()}\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)
# Get the urls in scope
list_of_urls_to_be_included_in_final_report = []
if args.include_urls:
    try:
        with open(args.include_urls,"r") as urls_included_file:
                for line in urls_included_file:
                    line = line.strip()
                    list_of_urls_to_be_included_in_final_report.append(line)
    except FileNotFoundError:
        list_of_urls_to_be_included_in_final_report = args.include_urls.split(',')
    except Exception as e:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}There is a problem with -> {args.exclude_urls}\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        if args.debug:
            print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}{print_exc()}\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)
# Set the urllib max retry count to 50 to make this script stable as f
max_retry = Retry(total=50, backoff_factor=1)
# Creating chrome driver synchronization lock for multithreading
driver_lock = Lock()
# Getting time when script started to name the final report
start_time_int = datetime.datetime.now()
start_time = start_time_int.strftime("%Y-%m-%d_%H-%M-%S")
# Get the javascript code to be executed
javascript_to_execute = '\0'
if args.javascript:
    javascript_to_execute = args.javascript
elif args.javascript_file:
    if args.javascript:	
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The --javascript-file option can not be used with --javascript option\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)
    try:
        with open(args.javascript_file, 'rb') as file:
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Trying to read the replacement file.\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
            javascript_to_execute = file.read()
            javascript_to_execute = javascript_to_execute.decode('utf-8')
    except FileNotFoundError:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The specified replacement file '{args.replace_files}' does not exist.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)
# Setting flag which indicates threads to run or stop
terminate = False
# Pause event will be used to pause the threads when user presses the ENTER KEY
pause_event = threading.Event()
# if there is code to replace, get the code
if args.replace_code:
    # Split the replace_code argument into individual strings
    replace_codes = args.replace_code.split(',')
    # Create pairs of replacement codes
    replacement_pairs = []
    i = 0
    while i < len(replace_codes):
        if i + 1 < len(replace_codes):
            to_be_replaced = replace_codes[i]
            to_be_replaced_with = replace_codes[i + 1]
            replacement_pairs.append((to_be_replaced, to_be_replaced_with))
        i += 2
# Abort request with following extensions
forbidden_extensions = ['.ico', '.png', '.img', '.jpg', '.svg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.gif', '.apng', '.avif', '.webp', '.bmp', '.cur', '.tif', '.tiff', '.mp3', '.mp4', '.avi', '.mkv', '.webm', 'ogv']
if args.no_css:
    forbidden_extensions.append('.css')
# Get the payloads
payloads = []
elements_payloads = {}
if args.attack in (1, 2):
    # Get the elements to be fuzzed
    elements = args.elements.split(',')
    # Get Payloads from file and store them in a list
    try:
        with open(args.payloads, "r") as payload_file:
            for line in payload_file:
                line = line.strip()
                payloads.append(line)
    except FileNotFoundError:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The specified payloads file '{args.payloads}' does not exist.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)
elif args.attack in (3, 4):
    try:
        for element_payload in args.elements_payloads.split(','):
            element, payload_file_path = element_payload.split(':')
            # Initialize the list if it doesn't exist
            elements_payloads.setdefault(element, [])
            with open(payload_file_path, 'r') as payload_file:
                for line in payload_file:
                    line = line.strip()
                    elements_payloads[element].append(line)
        if args.attack == 3:
            # Check if all lists have the same length
            if len(set(len(payloads) for payloads in elements_payloads.values())) > 1:
                # Find the maximum length of lists in the dictionary
                max_length = max(len(payloads) for payloads in elements_payloads.values())
                # Loop through each element in the dictionary and extend the lists to match the maximum length
                for element in elements_payloads:
                    current_length = len(elements_payloads[element])
                    if current_length < max_length:
                        # Calculate how many elements are needed to reach the maximum length
                        needed_elements = max_length - current_length
                        # Duplicate the list and append elements from the original list until the desired length is reached
                        extended_list = elements_payloads[element].copy()
                        while len(extended_list) < max_length:
                            extended_list += elements_payloads[element]
                        # Trim the list to the maximum length
                        extended_list = extended_list[:max_length]
                        # Update the dictionary with the extended list
                        elements_payloads[element] = extended_list
    except FileNotFoundError:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The specified payloads file '{args.payloads}' does not exist.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)

# Get the content, Replace the response body with the content of the file provided by the user
file_contents = {}
if args.replace_files:
    try:
        replace_files = args.replace_files.split(',')
        for replace_file in replace_files:
            file_name, file_url = replace_file.split('++')
            with open(file_name, 'r') as file:
                print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Trying to read the replacement file. -> {file_name}\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                file_contents[file_name] = file.read()
    except FileNotFoundError:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The specified replacement file '{file_name}' does not exist.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)

# Creating Reports directory in current directory to store reports
os.makedirs("BrowserBruter_Reports",exist_ok=True)
os.makedirs(f"BrowserBruter_Reports/{hostname}/{start_time}",exist_ok=True)
os.makedirs("logs",exist_ok=True)

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
	"range":"50",
    "textarea":"AtextForTextArea"
}

# Create list of elements whose class attribute needs to be removed
remove_class_elements = []
if args.remove_class:
    remove_class_elements = args.remove_class.split(',')

# If user has provided list of buttons to press, get those buttons.
if args.buttons_to_press_before_fuzz:
    buttons_to_press_before_fuzz = args.buttons_to_press_before_fuzz.split(',')

# If user has provided values for above, then override them with user's values
if args.fill_values:
    try:
        with open(args.fill_values, 'r') as values_file:
            attribute_values = json.load(values_file)
    except FileNotFoundError:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The specified values file '{args.values}' does not exist.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)
    except json.JSONDecodeError:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Invalid JSON format in the specified values file '{args.values}'.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        if args.debug:
            print_exc()
            print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Refer Above Stack Trace\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        sys.exit(0)
# Supress the http encoding and bs prettify warnings
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)
warnings.filterwarnings("ignore", category=UnicodeWarning)
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

### DEFINING AND ASSIGNING GLOBAL VARIABLES ENDS ###

### FUNCTIONS STARTS ###

# This function will handle the alert popup    
def wait_and_handle_popup(driver):
    wait = WebDriverWait(driver, 500)
    try:
        wait.until(EC.presence_of_all_elements_located(("xpath", '//body')))
    except UnexpectedAlertPresentException:
        #if args.ignore_popups:
            try:
                alert = driver.switch_to.alert
                alert.accept()
            except NoAlertPresentException:
                pass
        #else:
        #    print(f"\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Alert Pupup please interact with popup or use --ignore-popup option\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        #    input(f"\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}press ENTER after intracting with popup\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")

# Handle Unknown Exception
def handle_unknown_exception(exception):
    if args.debug:
        print_exc()
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}An unknown error has been occured, Please open issue request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    else:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}An unknown error has been occured, Please refer logs/Error.txt or use --debug flag.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    log_error(format_exc(exception))
    sys.exit(0)

# function to handle multi threading for cluster bomb       
def slice_combinations_for_threads(payload_combinations, num_threads):
    # Calculate the number of combinations per thread
    combinations_per_thread = len(payload_combinations) // num_threads
    extra_combinations = len(payload_combinations) % num_threads
    # Initialize a list to store sliced combinations
    sliced_combinations = []
    # Iterate over the threads
    start = 0
    for i in range(num_threads):
        end = start + combinations_per_thread
        # Distribute extra combinations to the first few threads
        if i < extra_combinations:
            end += 1
        # Slice the combinations for the current thread
        sliced_combinations.append(payload_combinations[start:end])
        # Update the starting index for the next thread
        start = end
    return sliced_combinations

# This function is used to slice the dictionary to support multi threading
def slice_dict_for_threads(input_dict, num_threads):
    result = []
    for i in range(num_threads):
        thread_dict = {}
        for key, values in input_dict.items():
            total_elements = len(values)
            elements_per_thread = total_elements // num_threads
            start_index = i * elements_per_thread
            end_index = (i + 1) * elements_per_thread if i < num_threads - 1 else total_elements
            thread_dict[key] = values[start_index:end_index]
        result.append(thread_dict)
    return result

# simple read file function, this function is only for generating dictionary based payloads
def read_file(file_path):
    try:
        with open(file_path,'r') as file:
              return file.read().splitlines()
    except FileNotFoundError as e:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The specified payloads file '{file_path}' does not exist.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        log_error(format_exc())
        sys.exit(0)

# Function to Handle CTRL+C
def signal_handler(signal, frame):
    sleep(3)
    print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}CTRL+C pressed. Waiting for remaining request/response to stop. Exiting...\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    # Set the global termination flag to True so all threads can stop gracefully
    global terminate
    terminate = True

# Function to run in a separate thread to pause and resume the browserbruter if user presses enter key
def pause_resume():
    global pause_event
    try:
        while not terminate:
            userText, timeout = timedKey(prompt="", timeout=-1, resetOnInput=True)
            if not (timeout):
                pause_event.set()  # Set the pause event
                print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nWARNING: {RESET}BROWSERBRUTER IS PAUSED\npress ENTER to resume\nPress y to Enter Interactive Mode\nPress n to Exit Interactive Mode\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                k = input()
                if k == 'Y' or k == 'y':
                    args.interactive = True
                elif k == 'N' or k == 'n':
                    args.interactive = False
                pause_event.clear()  # Clear the pause event 
                print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nWARNING: {RESET}Resuming BROWSERBRUTER\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    except KeyboardInterrupt as e:
        signal_handler(signal.SIGINT, None)
        log_error(format_exc())
        sys.exit(0)

# Function to get BrowserOptions
def get_browser_options():
    options = ChromeOptions()
    try:
        # NOTE for contributors, the chrome executable is not present at github repo for the sake of repo size limit, it is included in releases, with each new release, the appropriate chrome will be shipped along with the tool
        options.binary_location = "res/chrome/chrome"
    except FileNotFoundError:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Please download The Browser-Bruter from releases.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    if args.chrome_options:
        list_of_options = args.chrome_options.split(',')
        for option in list_of_options:
            options.add_argument(f"--{option}")
    elif args.anti_bot:
        return options
    else:
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
        options.add_argument("--proxy-bypass-list=0.0.0.0")
        options.add_argument("--ignore-certificate-errors")
        # add below option to prevent use of shared memory
        options.add_argument('--disable-dev-shm-usage')
        # adding below to hide that browser is automatically controlled which can be detected by some websites
        options.add_argument('--disable-blink-features=AutomationControlled')
    if args.headless:
        options.add_argument('--headless')
    return options

# Function to add cookies into selenium session
def add_cookies(driver):
    try:
        # Delete any existing cookies and assign initial cookies
        driver.delete_all_cookies()
        cookies_list = args.cookie.split(',')
        for cookie_arg in cookies_list:
            # Get the cookie data
            name, value = cookie_arg.split(":")
            # Create cookie dictionary as selenium requires them in dictionary format
            cookie_dict = {
                "name": name,
                "value": value,
                "domain": hostname
            }
            driver.add_cookie(cookie_dict)  
    except InvalidArgumentException as e:
            if "invalid argument: invalid 'domain'" in str(e):
                cookie_dict = {
                    "name": name,
                    "value": value
                }
                driver.add_cookie(cookie_dict)
            else:
                handle_unknown_exception(e)
    except InvalidCookieDomainException as e:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{RESET} Cookie Domain is invalid -> {cookie_dict} -> Skipping adding domain\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        cookie_dict = {
                    "name": name,
                    "value": value
                }
        driver.add_cookie(cookie_dict)
        log_error(format_exc())                
    except ValueError as e:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{RESET} You have entered arguments in invalid format -> {args.cookie} please read help message for valid format of passing cookies. Closing the Fuzzing process\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        driver.quit()
        log_error(format_exc())
        sys.exit(0)
	
# Function to intercept requests
def intercept_request(request):
    try:
        if any(extension in request.path.lower() for extension in forbidden_extensions):
            request.abort()
    except Exception as e:
        handle_unknown_exception(e)

def replace_response_content(request, response):
    global response_content
    # Delete the content length header, because we will update it later.
    del request.response.headers['Content-Length']
    if args.replace_code:
        try:
            response_body_encoding = request.response.headers['Content-Encoding']
        except KeyError:
            response_body_encoding = 'utf-8'
        if response_body_encoding and response_body_encoding.lower() == 'gzip':
            response_body_str = gzip.decompress(request.response.body)
        elif response_body_encoding:
            response_body_str = request.response.body.decode(response_body_encoding,errors='ignore')
        else:
            response_body_str = request.response.body.decode('utf-8',errors='ignore')
        for to_be_replaced, to_be_replaced_with in replacement_pairs:
            # Replace bytes in response body
            new_response_body_str = response_body_str.replace(to_be_replaced, to_be_replaced_with)
        # Update the content length header and content encoding header
        del request.response.headers['Content-Encoding']
        request.response.headers['Content-Encoding'] = 'utf-8'
        request.response.body = new_response_body_str.encode('utf-8')
        request.response.headers['Content-Length'] = len(request.response.body)
    # Check if the request URL matches the filename provided by the user
    if args.replace_files:
        for replace_file in replace_files:
            file_name, file_url = replace_file.split('++')
            if file_url == request.url:
                # Update the response content using replace method
                del request.response.headers['Content-Encoding']
                request.response.headers['Content-Encoding'] = 'utf-8'
                request.response.body = file_contents[file_name]
                request.response.headers['Content-Length'] = len(request.response.body)

# Function to get and initialize the driver
def get_and_initialize_chrome_driver():
    with driver_lock:
        options = get_browser_options()
        # try to get chrome driver and retry this three times, in case of exceptions, increases the stablility in case of multiples threads
        try:
            if args.no_anti_bot:
                service = Service(executable_path="res/chrome/chromedriver")
                driver = webdriver.Chrome(service=service, options=options, retries=max_retry, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
            else:
                driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, retries=max_retry, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
        except:
            sleep(10)
            options = get_browser_options()
            try:
                if args.no_anti_bot:
                    service = Service(executable_path="res/chrome/chromedriver")
                    driver = webdriver.Chrome(service=service, options=options, retries=max_retry, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
                else:
                    driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, retries=max_retry, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
            except:
                sleep(10)
                options = get_browser_options()
                try:
                    if args.no_anti_bot:
                        service = Service(executable_path="res/chrome/chromedriver")
                        driver = webdriver.Chrome(service=service, options=options, retries=max_retry, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
                    else:
                        driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, retries=max_retry, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
                except:
                    sleep(10)
                    options = get_browser_options()
                    if args.no_anti_bot:
                        service = Service(executable_path="res/chrome/chromedriver")
                        driver = webdriver.Chrome(service=service, options=options, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
                    else:
                        driver = Chrome(executable_path="res/chrome/chromedriver", version_main=122, options=options, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
        # Set request interceptor
        if not args.load_static_media:
            driver.request_interceptor = intercept_request
        if args.replace_code or args.replace_files:
        # Intercept HTTP responses to modify the http response body if required
            driver.response_interceptor = replace_response_content
        # Set the timeout limit to 5 minutes
        driver.set_page_load_timeout(300)
        # Set custom headers
        if args.headers:
            custom_headers = {}
            try:
            # Split the raw string into headers and set each one
                for header in args.headers.split(','):
                    key, value = map(str.strip, header.split(':'))
                    custom_headers[key] = value
                    # Update header_overrides with all custom headers
                    driver.header_overrides = custom_headers
            except ValueError:
                print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR:{RESET} Error setting headers. Please provide headers in valid format.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                driver.quit()
                log_error(format_exc())
                sys.exit(0)
        return driver
            
# Function to Remove attributes this is created to reduce code in attempt function
def remove_attributes_and_get_focus(driver, element):
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
        driver.execute_script("arguments[0].focus();", element)
    except StaleElementReferenceException:
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
            driver.execute_script("arguments[0].focus();", element)
        except StaleElementReferenceException:
            pass

# Function to log errors 
def log_error(error):
    try:
        #with log_error_lock:
        with open("logs/Error.txt","a") as error_log_file:
            error_time = datetime.datetime.now()
            error_time = error_time.strftime("%Y-%m-%d_%H-%M-%S")
            error_log_file.write(f"\n[+]--------------------------------------------------------------------------------------------------------------------------[+]\n")
            error_log_file.write(f"Error Time - {error_time}")
            error_log_file.write("\n[+]--------------------------------------------------------------------------------------------------------------------------[+]\n")
            error_log_file.write(error)
    except FileNotFoundError as e:
        print("Error: Logging file not found.")

# Function to sleep while pause
def sleep_while_pause():
    if pause_event.is_set():
        while pause_event.is_set():
            sleep(1)

# Function to remove javascript input validation by overriding common methods
def remove_javascript_validation(driver):
    sleep(0.3)
    # Get the last segment (file name) from the URL
    driver.execute_script("""
        String.prototype.match = function() {
            return ["123"];
        };
        String.prototype.replace = function() {
            return true;
        };
        String.prototype.replace = function(String,String) {
            return true;
        };
        String.prototype.replace = function(RegExp,String) {
            return true;
        };
        String.prototype.replace = function(RegExp,RegExp) {
            return true;                
        };
        RegExp.prototype.test = function() {
            return true;    
        };
        Number.isInteger = function(value) {
            return true;
        };
        Number.isNaN = function(value) {
            return false;
        };
""")

# Function to Generate filename for each different thread
def get_filename():
	# Getting current date and time to name the output file accordingly
	current_datetime = datetime.datetime.now()
	formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
	filename = [f"BrowserBruter_Reports/{hostname}/{start_time}/{hostname}-{formatted_datetime}.csv",f"BrowserBruter_Reports/{hostname}/{start_time}/{hostname }-{formatted_datetime}.txt"]
	return filename

# Function to handle --new-instance option
def handle_new_instance(driver):
    driver.quit()
    driver = get_and_initialize_chrome_driver()
    # Following lines solves the bug in which the --new-instace was not working
    driver.get(args.target)
    return driver

# Function to press the button
def press_button(driver,button,from_buttons_to_press):
    try:
        if args.press_enter_no_click and not from_buttons_to_press:
            button.send_keys("\n")
        else:
            button.click()
    except ElementClickInterceptedException as e:
        sleep(3)
        try:
            if args.press_enter_no_click and not from_buttons_to_press:
                button.send_keys("\n")
            else:
                button.click()
        except ElementClickInterceptedException as e:
            sleep(6)
            try:
                if args.press_enter_no_click and not from_buttons_to_press:
                    button.send_keys("\n")
                else:
                    button.click()
            except ElementClickInterceptedException as e:
                print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}The button -> {button} is not clickable or click has been intercepted by some other element, there might be some javascript being executed on web page which is preventing the click. Please remove the code intercepting the click.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                if args.debug:
                    print_exc()
                    print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Refer Above Stack Trace\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                log_error(format_exc())
                driver.quit()
                sys.exit(0)

# Function to perform generic initial operations before filling the form
def initial_operations_before_filling_the_form(driver):
    # If --force-cookie is set then set the initial cookies
    if args.force_cookie:
        add_cookies(driver)
    # Wait for body to be loaded in case of slow response
    wait_and_handle_popup(driver)
    # if args.reload_page then reload the current page
    if args.reload_page:
        # Force reload the page
        driver.execute_script("location.reload(true);")
        wait_and_handle_popup(driver)
        sleep(0.5)
    # Clear previous requests
    del driver.requests
    # Go to the target website
    if not args.interactive:
        try:
            driver.get(args.target)
        except TimeoutException as e:
            print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
            pause_event.set()
            sleep_while_pause()
    if args.delay_before:
        sleep(args.delay_before)
    if args.buttons_to_press_before_fuzz:
        for button_to_press in buttons_to_press_before_fuzz:
            press_button(driver,get_element(driver,button_to_press,True),True)
            sleep(0.3)
    # Remove common javascript validation
    if args.auto_remove_javascript_validation:
        remove_javascript_validation(driver)
    # Execute custom javascript code
    if not javascript_to_execute == '\0':
        sleep(0.3)
        try:
            driver.execute_script(javascript_to_execute)
        except JavascriptException:
            sleep(5)
            try:
                driver.execute_script(javascript_to_execute)
            except JavascriptException:
                sleep(7)
                driver.execute_script(javascript_to_execute)
    # Handle alert if it is present
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass

# Function to perform common operations after pressing the button
def operations_after_pressing_the_button(element,driver,webpage_before,this_threads_file,payload):
    # if pause after submit is present then pause the fuzzing process
    if args.pause_after_submit:
        pause_event.set()
        sleep_while_pause()
    # delay before making new request
    if args.delay_after:
        sleep(args.delay_after)
    # Wait for all requests to be completed
    wait_and_handle_popup(driver)
    if args.javascript_after:
        sleep(0.2)
        driver.execute_script(args.javascript_after)
    # Get web page content after making the response
    webpage_after = driver.page_source
    write_http_request_response(element,this_threads_file,driver,payload,webpage_before,webpage_after)
    # Clear the cookies and other data
    if args.remove_session:
        driver.delete_all_cookies()

def fill_the_form(driver):
    if args.delay_before:
        sleep(args.delay_before)
    input_fields = args.fill.split(',')
    # fill the form
    for input_field in input_fields:
        try:
            field = get_element(driver,input_field,False)
            if input_field in remove_class_elements:
                driver.execute_script("arguments[0].removeAttribute('class');",field)
                driver.execute_script("arguments[0].setAttribute('name',arguments[1]);",field,input_field)
            # Fill other fields with valid inputs
            # Adding support to handle <select> tags
            if field.tag_name == "select":
                # Select the second option
                options = field.find_elements(By.TAG_NAME, "option")
                # if there are two options in <select>, choose the second one as the first option can be empty, for example, <option value="">choose country</option><option value="india">india</option>
                if len(options) == 1:
                    remove_attributes_and_get_focus(driver, options[0])
                    # Set payload to the first option
                    options[0].click()
                else:
                    remove_attributes_and_get_focus(driver,options[1])
                    options[1].click()
            else:
                # Taking field value appropriate to its type
                fieldType = field.get_attribute("type")
                if fieldType == "checkbox" or fieldType == "radio":
                    driver.execute_script("arguments[0].checked = true;", field)
                else:
                    # Filling the predefined values
                    if field.tag_name == "textarea":
                        fieldValue = attribute_values.get("textarea","defaultValue")
                        field.clear()
                        driver.execute_script("arguments[0].value = arguments[1];", field, fieldValue)
                        field.send_keys(fieldValue)
                    else:
                        try:
                            fieldValue = attribute_values.get(fieldType, "defaultValue")
                            driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", field, fieldValue)
                            driver.execute_script("arguments[0].setAttribute('type','text');", field)
                            field.clear()
                            field.send_keys(fieldValue)
                        except InvalidElementStateException:
                            driver.execute_script("""
                                                // Create a new <input> element
                                                var inputElement = document.createElement('input');

                                                // Copy attributes
                                                for (var i = 0; i < arguments[0].attributes.length; i++) {
                                                    var attr = arguments[0].attributes[i];
                                                    inputElement.setAttribute(attr.name, attr.value);
                                                }
                                                // set the values
                                                inputElement.value = arguments[1];

                                                // Replace element with <input> in the DOM
                                                arguments[0].parentNode.replaceChild(inputElement, arguments[0]);
                                              """,field,fieldValue)
        except ElementNotInteractableException:
            print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Specified Element is not interactable -> {input_field}\nFollowings are the possible reason:\n 1. Either tool is running too fast, make it slow using --delay-* options\n 2. May be the {input_field} requires some action like clicking on button to make it interactable, in such case, provide a javascript using --javascript option to execute javascript.\n Skipping filling this {input_field}\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
            
def write_http_request_response(element, this_threads_file, driver, payload, webpage_before, webpage_after):
    with open(this_threads_file, 'a', newline='') as report:
        # Filtering requests that are in scope
        captured_requests = driver.requests
        if args.include_urls:
            filtered_requests = [single_request for single_request in captured_requests if any([single_request.url in list_of_urls_to_be_included_in_final_report])]    
        else:
            filtered_requests = [single_request for single_request in captured_requests if
                         urlparse(single_request.url).hostname == hostname or
                         any(urlparse(single_request.url).hostname == scope_hostname for scope_hostname in scope_hostnames)]
            filtered_requests = [single_request for single_request in filtered_requests if all(extension not in single_request.url for extension in forbidden_extensions)]
            filtered_requests = [single_request for single_request in filtered_requests if all(extension not in single_request.url for extension in ['.js', '.css', '.txt','.woff2','.woff'])]
            filtered_requests = [single_request for single_request in filtered_requests if all([single_request.url not in list_of_urls_to_be_excluded_from_final_report])]
        writer = csv.writer(report)
        for request in filtered_requests:
            try:
                request_body = request.body.decode("UTF-8")
            except UnicodeDecodeError:
                request_body = request.body#.body
            try:
                # Get request response time
                request_time = request.date
                response_time = request.response.date
                # Calculate the cycle time in milliseconds
                cycle_time_in_milliseconds = int((response_time - request_time).total_seconds() * 1000)
                # Store the logs in the report file
                raw = request.response.body
                encoding = request.response.headers.get('Content-Encoding', 'UTF-8')
                if encoding.lower() == 'gzip':
                    raw = gzip.decompress(raw)
                else:
                    raw = raw.decode(encoding, errors='replace')
                # URL Decode the request and response bodies
                request_body = urllib.parse.unquote(request_body)
                try:
                    raw = urllib.parse.unquote(raw)
                except Exception as e:
                    log_error(format_exc())
                    pass
                soup = bs(raw, features="html.parser")
                response_body = soup.prettify() if hasattr(soup, 'prettify') else raw.decode("UTF-8", errors="replace")
                # After printing on the display, write it to the report
                row = [value if value else ' ' for value in
                    [request_time.strftime('%Y-%m-%d %H:%M:%S'), str(element), str(payload), request.method, urllib.parse.unquote(request.url), request.headers, request_body, response_time.strftime('%Y-%m-%d %H:%M:%S'), 
                    cycle_time_in_milliseconds, request.response.status_code, request.response.reason, request.response.headers, response_body,
                    len(request.response.body), bs(webpage_before,features="html.parser").prettify(), 
                    bs(webpage_after,features="html.parser").prettify()]]
                writer.writerow(row)
                # Check whether the output should be printed on the console or not
                if args.verbose:
                    # Print the request
                    print(f'\n{GREEN}[+]---------------------Single Request/Response Cycle-------------------[+]')
                    print(f"Fuzzing - " + str(element))
                    print(f"Payload - " + str(payload))
                    print(f'[+]----------------------REQUEST---------------------[+]{RESET}')
                    print('Time - ' + request_time.strftime('%Y-%m-%d %H:%M:%S') + '\n', request.method, urllib.parse.unquote(request.url))
                    # Print in a new line
                    print(request.headers, request_body)
                    # Print the response
                    print(f'{GREEN}[+]----------------------RESPONSE--------------------[+]{RESET}')
                    if request.response:
                        print(
                            'Time - ' + response_time.strftime('%Y-%m-%d %H:%M:%S') + '\n',
                            request.response.status_code,
                            request.response.reason
                        )
                    print(request.response.headers)
                    print(response_body)
                    print(f"{GREEN}[+]--------------------------------------------------------------------------------------------------------------------------[+]\n\nTIME: {cycle_time_in_milliseconds} MilliSeconds \n\n[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
  
            except AttributeError as e:
                # Code to handle if no request has been made and there is no response
                if args.verbose:
                    print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{RESET} No response is received skipping report row!\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                row = [value if value else ' ' for value in
                    [request_time.strftime('%Y-%m-%d %H:%M:%S'), str(element), str(payload), request.method, urllib.parse.unquote(request.url), request.headers, request_body, request_time.strftime('%Y-%m-%d %H:%M:%S'), 
                    '0', '0', "N/A", "N/A", "N/A",
                    '0', bs(webpage_before,features="html.parser").prettify(), 
                    bs(webpage_after,features="html.parser").prettify()]]
                writer.writerow(row)

# Function to Generate Final Report
def generate_final_report():
    # sleep for 3 seconds so console progress bars are properly rendered
    #sleep(3)
    # Increase the field size limit
    csv.field_size_limit(sys.maxsize)
    print(f"\n\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{RESET} Generating Final Report\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    directory = f"BrowserBruter_Reports/{hostname}/{start_time}"
    final_report = f"BrowserBruter_Reports/{hostname}/{start_time}/{hostname}-{start_time}.csv"
    try:
        processed_payloads = f"BrowserBruter_Reports/{hostname}/{start_time}/Processed_Payloads.txt"
        all_threads_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
        all_processed_payloads_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
        global payloads
        # Initialize index counter
        index_counter = 0
        # Merge other files into a single final report
        with open(final_report, 'w', newline='') as final:
            writer = csv.writer(final)
            # Insert column names or, in other words, headings
            writer.writerow(['Index', 'Request Time', 'Fuzzing', 'Payload', 'Method', 'URL', 'Request Headers', 'Request Body', 'Response Time', 'Cycle Time MilliSeconds', 'Response Status Code', 'Response Reason', 'Response Headers', 'Response Body', 'Response Length', 'Web Page Before', 'Web Page After'])
            # Iterate over each CSV file
            for csv_file in all_threads_files:
                file_path = os.path.join(directory, csv_file)
                # Open the current CSV file in 'r' mode
                with open(file_path, 'r') as infile:
                    reader = csv.reader(infile)
                    # Read and write the rows to the output file
                    try:
                        for row in reader:
                            # Insert the index value at the beginning of each row
                            row.insert(0, index_counter)
                            writer.writerow(row)
                            # Increment the index counter
                            index_counter += 1
                    except csv.Error as e:
                        if "field larger than field limit" in str(e):
                            print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nWARNING:{RESET} Field size is too large to handle, replacing field with 'BROWSER-BRUTER-DISCARDED-EXTREMELY-LARGE' - Skipping row {index_counter} in file {csv_file}: {str(e)}\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                            # If a row exceeds the field limit, skip writing that row and write a placeholder value instead
                            log_error(f"Skipping row {index_counter} in file {csv_file}: {str(e)}")
                            writer.writerow(['BROWSER-BRUTER-DISCARDED-EXTREMELY-LARGE'])
                            # Increment the index counter
                            index_counter += 1
                        else:
                            raise
                # Delete the current CSV file
                os.remove(file_path) 
        if args.rows_limit:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(final_report)
            # Split the DataFrame into chunks
            chunks = [df[i:i+args.rows_limit] for i in range(0, len(df), args.rows_limit)]
            # Write each chunk to a new CSV file
            for i, chunk in enumerate(chunks):
                output_file = f"{final_report}_{i}.csv"
                chunk.to_csv(output_file, index=False)

        # Merge the processed payloads file into one; logic is the same as above
        with open(processed_payloads, 'w', newline='') as final_processed_payloads:
            for one_threads_processed_payloads in all_processed_payloads_files:
                file_path = os.path.join(directory, one_threads_processed_payloads)
                with open(file_path, 'r') as infile:
                    for i in infile:
                        final_processed_payloads.write(i)
                        if args.attack in (1, 2):
                            # keeping track of remaining payloads by removing processed payloads from payload[] list
                            try:
                                payloads.remove(i.strip())
                            except ValueError:
                                pass
                # Delete the current thread's processed payloads file
                os.remove(file_path)
        if args.attack in (1, 2):
            # Storing remaining payloads in a separate file
            remaining_payloads = os.path.join(directory, "Remaining_Payloads.txt")
            with open(remaining_payloads, 'w', newline='') as remaining_payloads_file:
                for payload in payloads:
                    remaining_payloads_file.write(payload + '\n')
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{RESET} Remaining Payloads (if any) have been stored -> {remaining_payloads}\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Processed Payloads (if any) have been stored -> {processed_payloads}\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{RESET} Report Generated -> {final_report}\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        end_time_int = datetime.datetime.now()
        end_time_str = end_time_int.strftime("%Y-%m-%d_%H-%M-%S")
        total_time = end_time_int - start_time_int
        total_time_str = str(total_time).split('.')[0]
        print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{RESET} Fuzzing end time ->  {end_time_str} Total Running time -> {total_time_str}\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    except ConnectionRefusedError as e:
        log_error(format_exc())
        print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    except FileNotFoundError:
        log_error(format_exc())
        sys.exit(0)

# Function to get the form
def get_form(driver,form):
    try:
        return driver.find_element(By.ID, form)
    except NoSuchElementException:
        try:
            return driver.find_element(By.NAME, form)
        except NoSuchElementException:
            try:
                return driver.find_element(By.CLASS_NAME, form)
            except NoSuchElementException as e:
                print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{RESET} Specified element {element} is not found. Please verify the name of the element. For more information, check Error.txt or use --debug flag.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                if args.debug:
                    print_exc()
                    print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Refer Above Stack Trace\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                driver.quit()
                log_error(format_exc())
                sys.exit(0)

# Function to get element to be fuzzed
def get_element(driver,element,coming_from_initial_operations_method):
    if args.form and not coming_from_initial_operations_method:
        selector = get_form(driver,args.form)
    else:
        selector = driver    
    found = False
    for i in range(30): # retry ten times
        # First try
        found, element = single_find_element_try(selector,element)
        if found:
            break
        else:
            sleep(5)
    if not found:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{RESET} Specified element {element} is not found. Please verify the name of the element. For more information, check Error.txt or use --debug flag.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        if args.debug:
            print_exc()
            print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Refer Above Stack Trace\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        driver.quit()
        log_error(format_exc())
        sys.exit(0)
    remove_attributes_and_get_focus(driver, element)
    return element

# This function is created two call this two times in case of slow loading of web page
def single_find_element_try(selector,element):
    try:
        element = selector.find_element(By.ID, element)
    except (NoSuchElementException, StaleElementReferenceException):
        try:
            element = selector.find_element(By.NAME, element)
        except (NoSuchElementException, StaleElementReferenceException):
            try:
                element = selector.find_element(By.CLASS_NAME, element)
            except (NoSuchElementException, StaleElementReferenceException):
                try:
                    element = selector.find_element(By.XPATH,f"//input[@value='{element}']")
                except (NoSuchElementException, StaleElementReferenceException):
                    try:
                        element = selector.find_element(By.XPATH,f"//input[@Type='{element}']")
                    except (NoSuchElementException, StaleElementReferenceException):
                        try:
                            element = selector.find_element(By.XPATH,f"//textarea[@value='{element}']")
                        except (NoSuchElementException, StaleElementReferenceException):    
                            try:
                                element = selector.find_element(By.XPATH,f"//button[@value='{element}']")
                            except (NoSuchElementException, StaleElementReferenceException):
                                try:
                                    element = selector.find_element(By.XPATH,f"//button[@Type='{element}']")
                                except (NoSuchElementException, StaleElementReferenceException):
                                    return False, element
    return True, element
                                
# Function to fill the payload in selected input field
def fill_payload_in_element(driver,element_being_fuzzed,payload):
    try:
        # Check if the element that is being fuzzed is <select> or not, if it is <select>, then set payload to its first <option> tag and mark it as the selected option
        if element_being_fuzzed.tag_name in ["select","mat-select"]:
            options = element_being_fuzzed.find_elements(By.TAG_NAME, "option")
            # if there are two options in <select>, choose the second one as the first option can be empty, for example, <option value="">choose country</option><option value="india">india</option>
            if options:
                remove_attributes_and_get_focus(driver, options[0])
                # Set payload to the first option
                driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", options[0], payload)
                options[0].click()
        else:
            if element_being_fuzzed.tag_name == "textarea":
                element_being_fuzzed.clear()
                driver.execute_script("arguments[0].value = arguments[1];", element_being_fuzzed, payload)
            else:
                # Setting the payload
                driver.execute_script("arguments[0].setAttribute('type','text');", element_being_fuzzed)
                driver.execute_script("arguments[0].setAttribute('value',arguments[1]);", element_being_fuzzed, payload)
                try:
                    element_being_fuzzed.clear()
                    element_being_fuzzed.send_keys(payload)
                except InvalidElementStateException:
                    driver.execute_script("""
                                                // Create a new <input> element
                                                var inputElement = document.createElement('input');

                                                // Copy attributes
                                                for (var i = 0; i < arguments[0].attributes.length; i++) {
                                                    var attr = arguments[0].attributes[i];
                                                    inputElement.setAttribute(attr.name, attr.value);
                                                }
                                                // set the values
                                                inputElement.value = arguments[1];

                                                // Replace element with <input> in the DOM
                                                arguments[0].parentNode.replaceChild(inputElement, arguments[0]);
                                              """,element_being_fuzzed,payload)
                except WebDriverException as e:
                    if "ChromeDriver only supports characters in the BMP" in str(e):
                        pass
                    else:
                        raise
    except ElementNotInteractableException:
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Specified Element is not interactable -> {element_being_fuzzed}\nFollowings are the possible reason:\n 1. Either tool is running too fast, make it slow using --delay-* options\n 2. May be the {element_being_fuzzed} requires some action like clicking on button to make it interactable, in such case, provide a javascript using --javascript option to execute javascript.\n Skipping filling this {element_being_fuzzed}\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")

# Function to Run Single Browser instance
def run_browser_instance(payloads, instance_number):
    if not terminate:
        try:
            # Spawning an instance of browser
            # Assigning browser options
            driver = get_and_initialize_chrome_driver()
            # If cookies are provided assign them to session
            # Get the initial cookie
            if args.cookie:
                # first visit the domain so Chrome does not trow InvalidCookieDomainException
                try:
                    driver.get(args.target)
                    add_cookies(driver)
                except TimeoutException as e:
                    print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
                    pause_event.set()
                    sleep_while_pause()
                except Exception as e:
                    handle_unknown_exception(e)
            # Initialize report file and processed payload file
            this_threads_files = get_filename()
            # If pause flag is set then go to target page and puase for one time
            if args.pause:
                driver.get(args.target)
                pause_event.set()
            # Retry count = 3
            try:
                if args.attack == 1:
                    if not terminate:
                        sniper_loop(payloads, elements, instance_number, this_threads_files, driver)
                elif args.attack == 2:
                    if not terminate:
                        battering_ram_loop(payloads, elements, instance_number, this_threads_files, driver)
                elif args.attack == 3:
                    if not terminate:
                        pitchfork_loop(payloads,instance_number,this_threads_files,driver)
                elif args.attack == 4:
                    if not terminate:
                        attempt_clusterbomb_fuzz(payloads,driver,this_threads_files,instance_number)
            except:
                # If there are multiple threads, then and only then retry
                if args.threads:
                    sleep(6)
                    try:
                        if args.attack == 1:
                            if not terminate:
                                sniper_loop(payloads, elements, instance_number, this_threads_files, driver)
                        elif args.attack == 2:
                            if not terminate:
                                battering_ram_loop(payloads, elements, instance_number, this_threads_files, driver)
                        elif args.attack == 3:
                            if not terminate:
                                pitchfork_loop(payloads,instance_number,this_threads_files,driver)
                        elif args.attack == 4:
                            if not terminate:
                                attempt_clusterbomb_fuzz(payloads,driver,this_threads_files,instance_number)
                    except:
                        sleep(10)
                        if args.attack == 1:
                            if not terminate:
                                sniper_loop(payloads, elements, instance_number, this_threads_files, driver)
                        elif args.attack == 2:
                            if not terminate:
                                battering_ram_loop(payloads, elements, instance_number, this_threads_files, driver)
                        elif args.attack == 3:
                            if not terminate:
                                pitchfork_loop(payloads,instance_number,this_threads_files,driver)
                        elif args.attack == 4:
                            if not terminate:
                                attempt_clusterbomb_fuzz(payloads,driver,this_threads_files,instance_number)
                else:
                    raise
        # Handle the exceptions which are specific to this thread and do not affect other threads
        except NoSuchWindowException as e:
            log_error(format_exc())
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        except ConnectionRefusedError as e:
            log_error(format_exc())
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        except RemoteDisconnected as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        except ProtocolError as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        except MaxRetryError as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed or Browsers has reached maximum retries, if you have closed BrowserBruter ignore this else report the issue, check error log if this is unintentional\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        except WebDriverException as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed or Remote connection lost with following message\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        except SystemExit as e:
            log_error(format_exc())
        except Exception as e:
            handle_unknown_exception(e)
        finally:
            # close the specific thread's driver
            try:
                if driver is not None:
                    driver.quit()
            except UnboundLocalError:
                sys.exit(0)

def sniper_loop(payloads,elements,instance_number,this_threads_files,driver):
    progress_bar = tqdm(total=len(payloads) * len(elements), desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration",dynamic_ncols=True,colour='blue')
    # Start the Fuzzing process
    for i in range(len(payloads)):
        for j in range(len(elements)):
            # Fuzz until terminate flag is not set, if it set then exit and close browser
            if not terminate:
                # if interactive option is set stop and wait for user to continue
                if args.interactive:
                    driver.get(args.target)
                    pause_event.set()
                # if pause event is set then pause the fuzzing process
                sleep_while_pause()
                try:
                    attempt_sniper_fuzz(elements[j],payloads[i], driver, this_threads_files[0])
                except StaleElementReferenceException:
                    sleep(4)
                    attempt_sniper_fuzz(elements[j],payloads[i], driver, this_threads_files[0])
                if args.new_instance:
                    driver = handle_new_instance(driver)
            if not terminate:
                # Update the progress bar
                progress_bar.update(1)
            j += 1
        # Add the processed payload into the file to keep track of processed payloads by this thread
        with open(this_threads_files[1],'a',newline='') as processed_payload_file:
            processed_payload_file.write(payloads[i]+'\n')
        i+=i
    progress_bar.close()

# Function to attempt a single request-response cycle with payload
def attempt_sniper_fuzz(element, payload, driver, this_threads_file):
    # Call the initial_operations_before_filling_the_form
    try:
        initial_operations_before_filling_the_form(driver)
    except StaleElementReferenceException:
        sleep(5)
        initial_operations_before_filling_the_form(driver)
    # Get web page content before making request
    webpage_before = driver.page_source
    # Automatically handle and fill the form
    if args.fill:
        try:
            fill_the_form(driver)
        except StaleElementReferenceException:
            driver.get(args.target)
            wait_and_handle_popup(driver)
            sleep(5)
            try:
                fill_the_form(driver)
            except StaleElementReferenceException:
                driver.get(args.target)
                wait_and_handle_popup(driver)
                sleep(5)
                fill_the_form(driver)
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    element_being_fuzzed = get_element(driver,element,False)
    if element in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed)
    # Fill the payload in element
    try:
        fill_payload_in_element(driver,element_being_fuzzed,payload)
    except StaleElementReferenceException:
        sleep(6)
        try:
            fill_payload_in_element(driver,element_being_fuzzed,payload)
        except StaleElementReferenceException:
            sleep(6)
            try:
                fill_payload_in_element(driver,element_being_fuzzed,payload)
            except StaleElementReferenceException:
                sleep(10)
                try:
                    fill_payload_in_element(driver,element_being_fuzzed,payload)
                except StaleElementReferenceException:
                    sleep(20)
                    fill_payload_in_element(driver,element_being_fuzzed,payload)
    # Press the button
    button_to_press = get_element(driver,args.button,False)
    if args.button in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press)
    press_button(driver,button_to_press,False)
    operations_after_pressing_the_button(element,driver,webpage_before,this_threads_file,payload)
    
def battering_ram_loop(payloads,elements,instance_number,this_threads_files,driver):
    progress_bar = tqdm(total=len(payloads), desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration",dynamic_ncols=True,colour='blue')
    # Start the Fuzzing process
    for i in range(len(payloads)):
        # Fuzz until terminate flag is not set, if it set then exit and close browser
        if not terminate:
        # if interactive option is set stop and wait for user to continue
            if args.interactive:
                driver.get(args.target)
                pause_event.set()
            sleep_while_pause()
            try:
                attempt_battering_ram_fuzz(elements,payloads[i], driver, this_threads_files[0])
            except StaleElementReferenceException:
                sleep(4)
                attempt_battering_ram_fuzz(elements,payloads[i], driver, this_threads_files[0])
            if args.new_instance:
                handle_new_instance(driver)
            if not terminate:
                # Update the progress bar
                progress_bar.update(1)
        # Add the processed payload into the file to keep track of processed payloads by this thread
        with open(this_threads_files[1],'a',newline='') as processed_payload_file:
            processed_payload_file.write(payloads[i]+'\n')
        i+=i
    progress_bar.close()
	
# Function to attempt to fuzz battering ram
def attempt_battering_ram_fuzz(elements, payload, driver, this_threads_file):
    # Call the initial_operations_before_filling_the_form
    try:
        initial_operations_before_filling_the_form(driver)
    except StaleElementReferenceException:
        sleep(5)
        initial_operations_before_filling_the_form(driver)
    # Get web page content before making request
    webpage_before = driver.page_source
    # Automatically handle and fill the form
    if args.fill:
        try:
            fill_the_form(driver)
        except StaleElementReferenceException:
            driver.get(args.target)
            wait_and_handle_popup(driver)
            sleep(10)
            try:
                fill_the_form(driver)
            except StaleElementReferenceException:
                driver.get(args.target)
                wait_and_handle_popup(driver)
                sleep(10)
                fill_the_form(driver)
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    for element in elements:
        element_being_fuzzed = get_element(driver,element,False)
        if element in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed)
        # Fill the payload in element
        try:
            fill_payload_in_element(driver,element_being_fuzzed,payload)
        except StaleElementReferenceException:
            sleep(6)
            try:
                fill_payload_in_element(driver,element_being_fuzzed,payload)
            except StaleElementReferenceException:
                sleep(6)
                try:
                    fill_payload_in_element(driver,element_being_fuzzed,payload)
                except StaleElementReferenceException:
                    sleep(10)
                    try:
                        fill_payload_in_element(driver,element_being_fuzzed,payload)
                    except StaleElementReferenceException:
                        sleep(20)
                        fill_payload_in_element(driver,element_being_fuzzed,payload)
    # Press the button
    button_to_press = get_element(driver,args.button,False)
    if args.button in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press)
    press_button(driver,button_to_press,False)
    operations_after_pressing_the_button(element,driver,webpage_before,this_threads_file,payload)

def pitchfork_loop(elements_payloads,instance_number,this_threads_files,driver):
    # Determine the number of iterations based on the maximum length of test data files
    num_iterations = max(len(payload_list) for payload_list in elements_payloads.values())
    progress_bar = tqdm(total=num_iterations, desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration", dynamic_ncols=True, colour='blue')
    processed_payloads = []
    for i in range(num_iterations):
        # Fuzz until terminate flag is not set, if it is set then exit and close the browser
        if not terminate:
            # if interactive option is set stop and wait for user to continue
            if args.interactive:
                driver.get(args.target)
                pause_event.set()
            # If the pause event is set, then pause the fuzzing process
            sleep_while_pause()
            try:
                attempt_pitchfork_fuzz(elements_payloads, i, driver, this_threads_files[0])
            except StaleElementReferenceException:
                sleep(4)
                attempt_pitchfork_fuzz(elements_payloads, i, driver, this_threads_files[0])
            if args.new_instance:
                handle_new_instance(driver)
            for element, payload_list in elements_payloads.items():
                processed_payloads.append(payload_list[i])
            if not terminate:
                # Update the progress bar
                progress_bar.update(1)
        # Add the processed payload into the file to keep track of processed payloads by this thread
        with open(this_threads_files[1], 'w', newline='') as processed_payload_file:
            processed_payload_file.write(str(processed_payloads) + '\n')
    # Close the progress bar
    progress_bar.close()
		
def attempt_pitchfork_fuzz(elements_payloads,index,driver,this_threads_file):
    payloads = []
    for element, payload_list in elements_payloads.items():
        payloads.append(payload_list[index])
    # Call the initial_operations_before_filling_the_form
    try:
        initial_operations_before_filling_the_form(driver)
    except StaleElementReferenceException:
        sleep(5)
        initial_operations_before_filling_the_form(driver)
    # Get web page content before making request
    webpage_before = driver.page_source
    # Automatically handle and fill the form
    if args.fill:
        try:
            fill_the_form(driver)
        except StaleElementReferenceException:
            driver.get(args.target)
            wait_and_handle_popup(driver)
            sleep(5)
            try:
                fill_the_form(driver)
            except StaleElementReferenceException:
                driver.get(args.target)
                wait_and_handle_popup(driver)
                sleep(5)
                fill_the_form(driver)
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    for element, payload_list in elements_payloads.items():
        element_being_fuzzed = get_element(driver,element,False)
        if element in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed)
        # Fill the payload in element
        try:
            fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
        except StaleElementReferenceException:
            sleep(6)
            try:
                fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
            except StaleElementReferenceException:
                sleep(6)
                try:
                    fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
                except StaleElementReferenceException:
                    sleep(10)
                    try:
                        fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
                    except StaleElementReferenceException:
                        sleep(20)
                        fill_payload_in_element(driver,element_being_fuzzed,payload_list[index])
    # Press the button
    button_to_press = get_element(driver,args.button,False)
    if args.button in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press)
    press_button(driver,button_to_press,False)
    operations_after_pressing_the_button(list(elements_payloads.keys()),driver,webpage_before,this_threads_file,payloads)

def attempt_clusterbomb_fuzz(payloads_combinations, driver,this_threads_files, instance_number):#index, driver, this_threads_files):
    try:
        # Create a list to store all combinations of payloads
        progress_bar = tqdm(total=len(payloads_combinations), desc=f"Fuzzing Progress for Browser -> {instance_number}", unit="iteration",dynamic_ncols=True,colour='blue')
        # Iterate through each combination
        for payloads in payloads_combinations:
            if not terminate:
                # if interactive option is set stop and wait for user to continue
                if args.interactive:
                    driver.get(args.target)
                    pause_event.set()
                # If the pause event is set, then pause the fuzzing process
                sleep_while_pause()
                # Call the initial_operations_before_filling_the_form
                try:
                    initial_operations_before_filling_the_form(driver)
                except StaleElementReferenceException:
                    sleep(5)
                    initial_operations_before_filling_the_form(driver)
                # Get web page content before making request
                webpage_before = driver.page_source
                if terminate:
                    break
                # Automatically handle and fill the form
                if args.fill:
                    try:
                        fill_the_form(driver)
                    except StaleElementReferenceException:
                        driver.get(args.target)
                        wait_and_handle_popup(driver)
                        sleep(5)
                        try:
                            fill_the_form(driver)
                        except StaleElementReferenceException:
                            driver.get(args.target)
                            wait_and_handle_popup(driver)
                            sleep(5)
                            fill_the_form(driver)
                if terminate:
                    break
                # Iterate through each element and set its value
                for element, payload in zip(elements_payloads.keys(), payloads):
                    if terminate:
                        break
                    # Find the element to be fuzzed
                    element_being_fuzzed = get_element(driver,element,False)
                    if element in remove_class_elements:
                        driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed)
                    # Fill the payload in element
                    try:
                        fill_payload_in_element(driver,element_being_fuzzed,payload)
                    except StaleElementReferenceException:
                        sleep(4)
                        try:
                            fill_payload_in_element(driver,element_being_fuzzed,payload)
                        except StaleElementReferenceException:
                            sleep(10)
                            try:    
                                fill_payload_in_element(driver,element_being_fuzzed,payload)
                            except StaleElementReferenceException:
                                sleep(20)
                                fill_payload_in_element(driver,element_being_fuzzed,payload)
                # Press the button
                if not terminate:
                    button_to_press = get_element(driver,args.button,False)
                    try:
                        if args.button in remove_class_elements:
                            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press)
                        press_button(driver,button_to_press,False)
                    except StaleElementReferenceException:
                        sleep(4)
                        if args.button in remove_class_elements:
                            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press)
                        press_button(driver,button_to_press,False)
                else:
                    break
                if not terminate:
                    # update progress bar
                    progress_bar.update(1)
                operations_after_pressing_the_button(list(elements_payloads.keys()),driver,webpage_before,this_threads_files[0],payloads)
                # Add the processed payload into the file to keep track of processed payloads by this thread
                with open(this_threads_files[1], 'w', newline='') as processed_payload_file:
                    processed_payload_file.write(str(payloads) + '\n')
                if args.new_instance:
                    driver = handle_new_instance(driver)
        # Close the progress bar
        progress_bar.close()
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
        log_error(format_exc())
        sys.exit(0)

### VARIOUS FUNCTIONS ENDS ###

### MAIN EXECUTION BLOCK STARTS ###
# Checking if script is running directly
if __name__ == "__main__":
    try:
        # Create and start the keyboard listener thread which will pause and resume the BrowserBruter
        keyboard_thread = threading.Thread(target=pause_resume,daemon=True) 
        keyboard_thread.start()
        # If only verbose or debug flag is set then track logs
        if args.verbose or args.debug:
            # Redirect stdout to the Tee class, the tee class redirects STDOUT to STDOUT and the log file only if --verbose flag or --debug flag is set
            log_file = 'logs/BrowserBruterSTDOUT.txt'  # This file stores console output
            tee_instance = Tee(log_file)
            sys.stdout = tee_instance
            print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Either --verbose or --debug flag detected creating logs in -> {log_file}\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
        # Get the number of threads or in other words number of browsers instances to use
        num_threads = args.threads
        # Print legal disclaimer and general info about target and payloads
        print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nLegal Warning:{RESET} This Browser-Bruter open-source penetration testing tool is provided for educational and ethical purposes only. Users are solely responsible for ensuring compliance with all applicable laws and regulations, and the developer(s) disclaim any liability for misuse or damage caused by the tool.\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\n{RESET}")
        print(f"{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]")
        print(f"{BLUE}[+] Start Time : {RESET}{start_time}")
        print(f"{BLUE}[+] Target URL : {RESET}{args.target}")
        if args.attack == 1:
            print(f"{BLUE}[+] Attack Mode: {RESET}SNIPER")
            print(f"{BLUE}[+] Elements   : {RESET}{args.elements}")
            print(f"{BLUE}[+] Payloads   : {RESET}{args.payloads}")
        if args.attack == 2:
            print(f"{BLUE}[+] Attack Mode: {RESET}BATTERING RAM")
            print(f"{BLUE}[+] Elements   : {RESET}{args.elements}")
            print(f"{BLUE}[+] Payloads   : {RESET}{args.payloads}")
        if args.attack == 3:
            print(f"{BLUE}[+] Attack Mode: {RESET}PITCH FORK")
            for element_payload in args.elements_payloads.split(','):
                element, payload_file_path = element_payload.split(':')
                print(f"{BLUE}[+] Elements:Payloads: {RESET}{element}:{payload_file_path}")
        if args.attack == 4:
            print(f"{BLUE}[+] Attack Mode: {RESET}CLUSTER BOMB")
            for element_payload in args.elements_payloads.split(','):
                element, payload_file_path = element_payload.split(':')
                print(f"{BLUE}[+] Elements:Payloads: {RESET}{element}:{payload_file_path}")
        print(f"{BLUE}[+] Button     : {RESET}{args.button}")
        print(f"{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]")
        print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{RESET} Press ENTER to puase the attack.\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\n{RESET}")
        # Create and start the threads
        threads = []
        start = 0
        threads_interval_time = 2.5
        if args.threads:
            if args.threads > 10:
                threads_interval_time = 6
            elif args.threads > 5:
                threads_interval_time = 4
        if args.attack in (1,2):
            # Divide the payload data equally among the threads
            payloads_per_thread = len(payloads) // num_threads
            extra_payloads = len(payloads) % num_threads
            for i in range(num_threads):
                if not terminate:
                    try:
                        end = start + payloads_per_thread
                        # Distribute extra payloads to the first few threads
                        if i < extra_payloads:
                            end += 1
                        # Extract the payloads for the current thread
                        thread_payloads = payloads[start:end]
                        # Create a thread with the target function and arguments
                        thread = threading.Thread(target=run_browser_instance, args=(thread_payloads,i)) #elements, i))
                        # Sleep while puase
                        sleep_while_pause()
                        # Start the thread
                        thread.start()
                        # Add the thread to the list of threads
                        threads.append(thread)
                        # Update the starting index for the next thread
                        start = end
                        # Sleep for 2.5 seconds for proper resource management
                        sleep(threads_interval_time)
                    except KeyboardInterrupt as e:
                        signal_handler(signal.SIGINT, None)
                        log_error(format_exc())
                        sys.exit(0)
        elif args.attack == 3:
            threaded_dicts = slice_dict_for_threads(elements_payloads, num_threads)
            try:
                for i, thread_dict in enumerate(threaded_dicts, start=1):
                    if not terminate:
                        # Create a thread with the target function and arguments
                        thread = threading.Thread(target=run_browser_instance, args=(thread_dict, i))
                        thread.start()
                        threads.append(thread)
                        # Sleep for 2.5 seconds for proper resource management
                        sleep(2.5)
            except KeyboardInterrupt as e:
                signal_handler(signal.SIGINT, None)
                log_error(format_exc())
                sys.exit(0)
        elif args.attack == 4:
            # Create a list to store all combinations of payloads
            payloads_combinations = list(product(*elements_payloads.values()))
            # Split the workload equally among threads
            chunk_size = len(payloads_combinations) // num_threads
            chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads - 1)]
            chunks.append(((num_threads - 1) * chunk_size, len(payloads_combinations)))
            # Create and start the threads
            for instance_number, (start, end) in enumerate(chunks):
                if not terminate:
                    thread_combinations = payloads_combinations[start:end]
                    # Create a thread with the target function and arguments
                    thread = threading.Thread(target=run_browser_instance, args=(thread_combinations, instance_number))
                    # Start the thread
                    thread.start()
                    threads.append(thread)
                    # Sleep for 2.5 seconds for proper resource management
                    sleep(5)     
        # Wait for all threads to finish
        for thread in threads:
            try:
                thread.join()
            except KeyboardInterrupt:
                log_error(format_exc())
        # Set the terminate flag so the keyboard thread stops
        terminate = True
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
        log_error(format_exc())
        sys.exit(0)
    except ConnectionRefusedError as e:
        log_error(format_exc())
        print(f"\n\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    except SystemExit:
        log_error(format_exc())
        print("")
    except Exception as e:
        handle_unknown_exception(e)
    finally:
        # Generate the report
        generate_final_report()
        # Reset sys.stdout to the console at the end
        if args.verbose or args.debug:
            sys.stdout = sys.__stdout__
        sys.exit(0)      
else:
    print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{RESET} Please run the script again using python3 BrowserBruter.py, closing the BrowserBruter\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")
    if args.debug:
        print_exc()
        print(f"\n\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {RESET}Refer Above Stack Trace\n{RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{RESET}")

### MAIN EXECUTION BLOCK ENDS ###
