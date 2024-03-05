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
from res.tee import Tee
from time import sleep
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from seleniumwire import webdriver
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
from http.client import RemoteDisconnected
from urllib3.exceptions import ProtocolError
from urllib3.exceptions import MaxRetryError
from bs4 import BeautifulSoup as bs
from bs4 import MarkupResemblesLocatorWarning
from bs4 import XMLParsedAsHTMLWarning
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
##################################################################################################################################################################
##################################################################################################################################################################
##                                                                                                                                                             ###
## {YELLOW}██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░                                                       
{GREEN}## {YELLOW}██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗⠀⠀⠀⠀{RED}⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣶⣶⣶⣶⣶⣾⣷⣾⣷⣶{YELLOW}. . . .
{GREEN}## {YELLOW}██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝⠀{RED}⣶⣶⣶⣶⣶⣶⣶⡆⢸⣿⣿⣿⣿⣿⣿⡇⠸⠿⠿⠿⠿⠿⠿⢿⡿⢿⡿⠿{YELLOW}. . . . . 
{GREEN}## {YELLOW}██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗⠀{RED}⣿⣿⣿⣿⣿⣿⣿⡇⠘⠛⢻⠟⠛⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠁⠀⠀                  
{GREEN}## {YELLOW}██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║⠀{RED}⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⣸⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  
{GREEN}## {YELLOW}╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝⠀⠀⠀{RED}⣆⠀⢶⡆⠀⠀⠀⢀⡟⠀⣼⡇                                 
{GREEN}##                                                                                                                       ⠀⠀⠀{RED}⢹⣄⠘⣷⡀⠀⢀⡼⠁⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                  
{GREEN}##                                                                                                                       ⠀⠀⠀⠀{RED}⠙⠦⡈⠻⢶⣿⣥⡾⠋ {YELLOW}by Jafar Pathan 
{GREEN}##                                                                                                           {YELLOW}The First-Ever Advance Browser Based Automated Web Form Fuzzing Tool{GREEN}### 
{GREEN}##################################################################################################################################################################
{GREEN}##################################################################################################################################################################{RESET}""")


### DEFINING AND PARSING COMMAND LINE ARGUMENTS START ###
# Getting argument parser to parse and process arguments
argParser = argparse.ArgumentParser(description="BrowserBruter is a python3 script, utilizing power of selenium and selenium-wire to automate fuzzing of various input fields of webpages to test their security against malicious inputs. For contact and more information about project please visit https://github.com/netsquare/BrowserBruter",formatter_class=argparse.RawTextHelpFormatter)
# Defining the epilog message which will be displayed with help message
argParser.epilog = f'''
Usage Examples:
    1. Perform Bruteforce(ClusterBomb) on login page:
        {YELLOW}BrowserBruter --elements-payloads username:username.txt,password:passwords.txt --target http://localhost/login.php --button Login --attack 4 --remove-session{RESET}

    2. Perform PitchFork on login page:
        {YELLOW}BrowserBruter --elements-payloads username:username.txt,password:passwords.txt --target http://localhost/login.php --button Login --attack 3{RESET}

    3. Perform BatteringRam on login page:
        {YELLOW}BrowserBruter --elements username,password --payloads sqli.txt --target http://localhost/login.php --button Login --verbose --attack 2{RESET}

    4. Fuzz on login page and make it verbose:
        {YELLOW}BrowserBruter --elements username,password --fill username,password --payloads sqli.txt --target http://localhost/login.php --button Login --verbose --attack 1{RESET}

    5. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint':
        {YELLOW}BrowserBruter --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --attack 1{RESET}
	
    6. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request becuase the initial cookies might be overridden by new cookies values:
        {YELLOW}BrowserBruter --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --attack 1{RESET}
	
    7. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle [this is useful against Authentication pages when you don't want redirection in case of successful login]:
        {YELLOW}BrowserBruter --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --remove-session --attack 1{RESET}
	
    8. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode:
        {YELLOW}BrowserBruter --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --remove-session --headless --attack 1{RESET}
	
    9. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode and run 5 instances of browser parallely:
        {YELLOW}BrowserBruter --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --remove-session --headless --threads 5 --attack 1{RESET}
   
    10. Fuzz CheckBox for example '<input type="checkbox" name="hobbies" value="reading" /> <input type="checkbox" name="hobbies" value="writing" />':
        {YELLOW}BrowserBruter --elements hobbies --payloads paylods.txt --target http://localhost/register --button register --attack 1{RESET}
   
    11. Fuzz Radio Button for example '<input type="radio" name="yesno" id="yes" value="yes" required/> <input type="radio" name="yesno" id="no" value="no" required/>':
        {YELLOW}BrowserBruter --elements yesno --payloads payloads.txt --target http://localhost/register --button register --attack 1{RESET}
    OR
        {YELLOW}BrowserBruter --elements no --payloads payloads.txt --target http://localhost/register --button register --attack 1{RESET}
   
    12. Fuzz <select> element - for example <select name="selectElement" required> <option value="">Select an option</option> <option value="option1">Option 1</option> </select>:
        {YELLOW}BrowserBruter --elements selectElement --payloads payloads.txt --target http://dvwa.com/selection --button submit --attack 1{RESET}
    
    13. Fuzz <textarea> element - for example <textarea name="textareaElement" placeholder="Enter text" required></textarea>:
        {YELLOW}BrowserBruter --elements textareaElement --payloads payloads.txt --target http://dvwa.com/registration --button submit --attack 1{RESET}
   
    14. Fuzz colorpicker, datepicker, timepicker - for example <input type="color" name="colorElement" required/> <input type="date" name="dateElement" required/> <input type="time" name="timeElement" required/>:
        {YELLOW}BrowserBruter --elements colorElement,dateElement,timeElement --fill colorElement,dateElement,timeElement --payloads payloads.txt --target http://localhost/ --button submit --attack 1{RESET}

    15. Define API domain in scope for proper report generation and logging:
        {YELLOW}BrowserBruter --elements username,password --fill username,password --button button --target http://net-square.com/login --payloads payloads.txt --attack 1 --scope api.net-square.com,dev.api.net-square.com{RESET}

    16. Add Authorization headers with bearer token for valid authorization:
        {YELLOW}BrowserBruter --elements username,password --fill username,password --button button --target http://net-square.com/login --payloads payloads.txt --headers "Auth: 123","Auth1: Bearer emluamFjb2Rlcgo=" {RESET}
	   
    17. Provide custom values for each form field types, content of the file should be in JSON format and it should contain all of the field types, see example values.json for better understanding:
        {YELLOW}BrowserBruter --elements username,password --fill username,password --fill-values fields.json --button button --target http://net-square.com/login --payloads payloads.txt" {RESET}

    18. Pause the BrowserBruter on each iteration of fuzzing, so user can manually perform any task, complete captcha before BrowserBruter fuzzes the form, press ENTER two times to continue:
        {YELLOW}BrowserBruter --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --threads 5 --fill-values values.json --interacitve --attack 1{RESET}

    19. Replace the content of a file in HTTP responses and specify the replacement file URL:
        {YELLOW}BrowserBruter --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-files "input-validation.js"++"http://localhost/assets/js/input-validation.js" --attack 1{RESET}

    20. Replace the content of a file in HTTP responses and run JavaScript:
        {YELLOW}BrowserBruter --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-files "input-validation.js"++"http://localhost/assets/js/input-validation.js" --javascript "var elmnt = document.getElementById('ClickMe'); elmnt.click();" --attack 1{RESET}

    21. Replace the content of a file in HTTP responses and run JavaScript code by providing the code in file:
        {YELLOW}BrowserBruter --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-files "input-validation.js"++"http://localhost/assets/js/input-validation.js" --javascript-file element-click.js --attack 1{RESET}
    
    22. Replace every "return false" statement with "return true" and replace every "alert(0)" with "alert(1)":
        {YELLOW}BrowserBruter --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-code "return false","return true","alert(0)","alert(1)" --javascript "var elmnt = document.getElementById('ClickMe'); elmnt.click();" --attack 1{RESET}
    
    23. Replace bunch of javascript code into return true:
        {YELLOW}BrowserBruter --elements-payloads textarea:sqli.txt,data:sqli.txt --button submit --target http://localhost:3000/index.html --attack 3 --replace-code "return false","return true","return regex.test(dateString)","return true","return regex.test(timeString)","return true","return regex.test(colorString)","return true"{RESET}

    24. Fuzz the search box, when user have to press enter to submit the search query, the user has to click on search icon to make search box appear:
        {YELLOW}BrowserBruter --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click{RESET}
    
    25. Tell Browser Bruter to remove commong javascript input validation:
        {YELLOW}BrowserBruter --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --auto-remove-javascript-validation{RESET}
        
    26. Tell Browser Bruter to ignore pop ups like alert() box:
        {YELLOW}BrowserBruter --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --auto-remove-javascript-validation --ignore-popups{RESET}

    27. Tell Browser Bruter to select the elements under the specified form only, in case there are two forms and multiple elements have same name and ids:
        {YELLOW}BrowserBruter --form changePasswordForm --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --attack 1{RESET}

    28. Pause the Browser Bruter on startup to manually login to the application:
        {YELLOW}BrowserBruter --pause --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1{RESET}

    29. Pause the Browser Bruter on startup to manually login to the application then run Browser Bruter in interactive mode to solve the captcha before inserting the payloads:
        {YELLOW}BrowserBruter --pause --interactive --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1{RESET}
        
    30. Pause the Browser Bruter on startup to manually login to the application then run Browser Bruter in interactive mode to solve the captcha before inserting the payloads, pause the Browser Bruter after submitting the form to perform some manual human interaction:
        {YELLOW}BrowserBruter --pause --interactive --pause-after-submit --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1{RESET}
    
    31. Wait for 1 seconds before and after submission of the form:
        {YELLOW}BrowserBruter --delay-before 1 --delay-after 1 --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1{RESET}

    32. Route traffic via proxy i.e. BurpSuite and load the static media like images:
        {YELLOW}BrowserBruter --proxy http://127.0.0.1:8080/ --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1 --load-static-media{RESET}

    33. Add custom chrome options which will be passed to chrome browser:
        {YELLOW}BrowserBruter --elements id --button Submit --payloads sqli.txt --target http://localhost/ --attack 1 --chrome-options ignore-certificate-errors,disable-dev-shm-usage{RESET}

    34. Override all chrome options and use raw anti bot detection evasions:
        {YELLOW}BrowserBruter --elements id --button Submit --payloads sqli.txt --target http://localhost/ --attack 1 --anti-bot{RESET}

    35. Brute force login page and try to bypass authentication and also do not try to evade anti bot defences:
        {YELLOW}BrowserBruter --elements-payloads username:userid.txt,password:passwords.txt --button Login --target http://localhost/login.php --attack 4 --proxy http://127.0.0.1:8080/ --no-anti-bot --remove-session{RESET}

    36. Perform BatteringRam attack on web page which has invisible captcha so start each payload insertion on new fresh instance of browser:
        {YELLOW}BrowserBruter --elements name,email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 2 --new-instance{RESET}

    37. Perform BatteringRam attack on web page which has invisible captcha so start each payload insertion on new fresh instance of browser and restore the previous session:
        {YELLOW}BrowserBruter --elements name,email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 2 --new-instance --new-instance-restore-session{RESET}
	
    38. There is field called name that you don't want to fuzz but it requires to be filled while submitting the form:
        {YELLOW}BrowserBruter --elements email,phone --fill name --payloads payloads.txt --target http://example.com/signup --button submit --attack 1{RESET}
          
    39. There is input validation that is preventing the payloads, try to remove the class attribute from these elements to see if payloads are correctly inserted:
        {YELLOW}BrowserBruter --elements email,phone --fill name --remove-class email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 1{RESET}

    40. Split the final report into smaller chunks by specifying the rows limit in each report to make report review process faster in ReportExplorer:
        {YELLOW}BrowserBruter --elements email,phone --fill name --remove-class email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 1 --rows-limit 200{RESET}

    DVWA Usage Examples:

    1. Fuzz the Command Injection page of DVWA, Pause BrowserBruter on startup to manually login and manually set cookies, press ENTER two times to continue:
        {YELLOW}BrowserBruter --elements ip --button Submit --payloads payloads.txt --target http://localhost/vulnerabilities/exec/ --pause --attack 1{RESET}    
    
    2. Fuzz the Command Injection page of DVWA, set two cookies, force reuse of these cookies, reset session data each time:
        {YELLOW}BrowserBruter --elements ip --button Submit --payloads payloads.txt --target http://localhost/vulnerabilities/exec/ --cookie PHPSESSID:jtq7r9fbgf90h2qm9915qk6551,security:low --force-cookie --remove-session --attack 1{RESET}
       

    {RED}jsdebugging lab - https://hub.docker.com/r/bhattsameer/jsdebugginglab Usage Examples:{RESET}
        
    1. Perform BruteForce attack on login page:
        {YELLOW}BrowserBruter --elements-payloads email:username.txt,password:passwords.txt --target http://172.17.0.2/Lab3/login.php --attack 4 --button btn-secondary --remove-session{RESET}
        
    2. Perform bruteforce attack on otp page, but otp is being checked on frontend client side, so there are no http request-response from server, so perform brute force attack on client side only:
        {YELLOW}BrowserBruter --elements otp --payloads otps.txt --target http://localhost/Lab3/OTP.php --button button --attack 1 --delay-after 0.3 --cookie PHPSESSID:9u593rhl797n3v6aa5vu8mjj20{RESET}

    {RED}Stock Management System Lab Usage Examples:{RESET}

    1. Perform brute force attack on login page to bypass authentication:
        {YELLOW}python3 BrowserBruter.py --elements-payloads username:username.txt,password:passwords.txt --button btn-default --target http://localhost:13066/ --attack 4 --remove-session
{RESET}

    2. Perform Sniper attack on form page which is hidden, and requires pressing a button to be revealed, so use --interactive option to manually press the button:
        {YELLOW}BrowserBruter --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --interactive --delay-after 0.5 --fill editBrandName,brandId,editBrandStatus

    3. Further automate the script by locating and clickng the buttons which enables the form:
        {YELLOW}BrowserBruter --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 0.3 --fill editBrandName --javascript "document.querySelector('button.btn.btn-default.dropdown-toggle').click(); document.querySelector('a[data-target=\"#editBrandModel\"]').click();" --delay-after 0.3{RESET}

    4. Provide above javascript code in file:    
        {YELLOW}BrowserBruter --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 1 --fill editBrandName --javascript-file click.js{RESET}

    5. Remove input validations form bootstrap.min.js file and press two buttons on web page using --javascript which will enable the web form:
        {YELLOW}BrowserBruter --elements editBrandStatus,editBrandName --payloads fuzz.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 0.7 --fill editBrandName --javascript "document.querySelector('button.btn.btn-default.dropdown-toggle').click();document.querySelector('a[data-target=\"#editBrandModel\"]').click();" --delay-after 0.5 --replace-files "js-files-with-no-input-validation/bootstrap.min.js"++"http://localhost:13066/assests/bootstrap/js/bootstrap.min.js"{RESET}

    6. Brute force change password form with submit button's class name is 'btn btn-primary':
        {YELLOW}BrowserBruter --elements-payloads user_id:username.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt --target http://localhost:13066/setting.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button 'btn-primary'{RESET}

    7. Brute force change password form by selecting the specific form, because there is other form with same elements:
        {YELLOW}BrowserBruter --elements-payloads user_id:username.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt --target http://localhost:13066/setting.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button 'btn-primary' --form changePasswordForm{RESET}
 
    8. Brute force add user form but first press one using --buttons-to-press-before-fuzz to enable this form:
        {YELLOW}BrowserBruter --elements-payloads userName:fuzz.txt,upassword:fuzz.txt,uemail:fuzz.txt --button createUserBtn --target http://localhost:13066/user.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --buttons-to-press-before-fuzz addUserModalBtn{RESET}

    9. Audit an complex form, replacing jquery-ui with no input validation jquery-ui and replacing bootstrap.min.js too, running 5 threads:
        {YELLOW}BrowserBruter --form createOrderForm --elements orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace --fill orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace --payloads fuzz.txt --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button createOrderBtn --attack 1 --replace-file js-files-with-no-input-validation/bootstrap.min.js++http//localhost:13066/assests/bootstrap/bootstrap.min.js,"js-files-with-no-input-validation/jquery-ui.min.js"++"http://localhost:13066/assests/jquery-ui/jquery-ui.min.js" --attack 1 --target "http://localhost:13066/orders.php?o=add" --threads 5{RESET}

    {RED}OWASP JuiceShop Usage Examples:{RESET}
         
    1. Testing SQLi on OWASP JuiceShop's login page by clusterbombing the payloads:
        {YELLOW}BrowserBruter --elements-payloads email:sqli.txt,password:sqli.txt --target http://localhost:3000/#/login --attack 4 --button loginButton --proxy http://127.0.0.1:8080/ --cookie welcomebanner_status:dismiss --remove-session{RESET}

    2. Fuzzing registration page of OWASP JuiceShop:
        {YELLOW}BrowserBruter --elements emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl --button registerButton --attack 1 --fill emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl --payloads fuzz.txt --target http://localhost:3000/#/register --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/{RESET}

    3. Fuzz the email field for various vulnerabilities of OWASP JuiceShop and split the final report into 100 rows of multiples reports:
        {YELLOW}BrowserBruter --elements emailControl --button registerButton --attack 1 --fill emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl --payloads sqli.txt --target http://localhost:3000/#/register --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --rows-limit 100{RESET}

    4. Fuzz the file upload functionality of OWASP JuiceShop's complaint page:
        {YELLOW}BrowserBruter --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file{RESET}

    5. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable:
        {YELLOW}BrowserBruter --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file --remove-class cdk-text-field-autofill-monitored{RESET}

    6. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable and include the auth cookies and Authorization header to be able fuzz while being authenticated:
        {YELLOW}BrowserBruter --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file --remove-class cdk-text-field-autofill-monitored --headers "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI"
{RESET}

    7. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable and include the auth cookies and Authorization header to be able fuzz while being authenticated and split the final report into smaller reports containing 200 rows each:
        {YELLOW}BrowserBruter --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file --remove-class cdk-text-field-autofill-monitored --headers "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI"
{RESET}

    8. Fuzz the global search functionality of the OWASP JuiceShop while authenticated by sending ENTER key instead of click:
        {YELLOW}BrowserBruter --elements mat-input-0 --button mat-input-0 --attack 1 --target http://localhost:3000/#/ --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --payloads fuzz.txt --headers "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" --buttons-to-press-before-fuzz searchQuery --press-enter-no-click
{RESET}

        OR -> following removes class attribute so the script does no throw element not intreactable error:
        {YELLOW}BrowserBruter --elements mat-input-0 --button mat-input-0 --attack 1 --target http://localhost:3000/#/ --cookie welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --payloads fuzz.txt --headers "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --remove-class mat-input-0
{RESET}

    9. Fuzz the Customer Feedback form of OWASP JuiceShop:
        {YELLOW}BrowserBruter --button submitButton --proxy http://127.0.0.1:8080/ --target http://localhost:3000/#/contact --cookie welcomebanner_status:dismiss --payloads fuzz.txt --attack 1 --elements userId,cdk-text-field-autofill-monitored,comment,rating --fill cdk-text-field-autofill-monitored,comment,rating --remove-class userId,cdk-text-field-autofill-monitored,comment,rating --interactive --rows-limit 200{RESET}

        OR -> Fuzz the captcha field too:
        {YELLOW}BrowserBruter --button submitButton --proxy http://127.0.0.1:8080/ --target http://localhost:3000/#/contact --cookie welcomebanner_status:dismiss --payloads fuzz.txt --attack 1 --elements userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --fill cdk-text-field-autofill-monitored,comment,rating --remove-class userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --interactive --rows-limit 200{RESET}

        OR -> Fuzz the captcha field and auto fill too:
        {YELLOW}BrowserBruter --button submitButton --proxy http://127.0.0.1:8080/ --target http://localhost:3000/#/contact --cookie welcomebanner_status:dismiss --headers "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" --payloads fuzz.txt --attack 1 --elements userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --fill cdk-text-field-autofill-monitored,comment,rating,captchaControl --remove-class userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --rows-limit 200{RESET}

    10. Fuzz the chatbot of OWASP JuiceShop by first manually sign-in into the application:
        {YELLOW}BrowserBruter --button message-input --elements message-input --press-enter-no-click --proxy http://127.0.0.1:8080/ --target http://localhost:3000/#/chatbot --cookie test:working,welcomebanner_status:dismiss,language:en --pause --payloads fuzz.txt --attack 1 --rows-limit 200{RESET}

    11. Fuzz the write review form of product by first manually login to the application, then automatically click on the image of product to make produc review menu appear:
        {YELLOW}BrowserBruter --buttons-to-press-before-fuzz img-container --elements "cdk-text-field-autofill-monitored" --button submitButton --target http://localhost:3000/#/ --cookie cookieconsent_status:dismiss,language:en,welcomebanner_status:dismiss --proxy http://127.0.0.1:8080/ --attack 1 --payloads fuzz.txt --remove-class cdk-text-field-autofill-monitored --pause{RESET}
'''
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
args_fuzz.add_argument("--scope",help="Comma-separated list of in-scope domains.", metavar="api1.example.com,bak.example.com")
args_fuzz.add_argument("--delay-before",help="Delay before fuzz attempt.",metavar="0.2", type=float, default=0.2)
args_fuzz.add_argument("--delay-after",help="Delay after fuzz attempt.",metavar="0.2", type=float, default=0.2)
args_fuzz.add_argument("--threads",help="Specifies number of browsers instances to be run, max value is 5, default is 1, lower the instances slower the fuzzing process, more instances - faster fuzzing process.",metavar="3",default=1, type=int)
args_fuzz.add_argument("--pause", help="Pause the BrowserBruter instances on startup, press ENTER to resume.",action="store_true",default=False)
args_fuzz.add_argument("--interactive",help="Pause the BrowserBruter before fuzzing any element at each payload and wait for user to continue.",action="store_true",default=False)
args_fuzz.add_argument("--pause-after-submit",help="Pause the script after pressing the submit button to allow pentester to interact with the web application.",action="store_true")
args_fuzz.add_argument("--form",help="Specy id,name,class of form to fuzz in case of muliple forms",metavar="changePasswordForm")
args_fuzz.add_argument("--ignore-popups",help="Ignore alert and other pop up menus",action="store_true",default=False)
args_fuzz.add_argument("--remove-class",help="Provide a list of elements from which you want to remove the class attribute, extremely useful when element is linked to some class with extreme javascript input validation or makes the element not interactable, you can still select this element by providing it's class name.", metavar="cdk-text-field-autofill-monitored")
args_session.add_argument("--headers", help="Comma-separated list of custom headers.",metavar="\"Auth: 123\",\"CUSTOME_HEADER: VALUE\"")
args_session.add_argument("--cookie",help="Use it to define cookies to be used while sending initial request, cookies should be in name:value:domain comma separated format.", metavar="name:value,name2:value2")
args_session.add_argument("--force-cookie",help="Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server.",action="store_true")
args_session.add_argument("--remove-session",help="Use this switch to remove session data and cookies after each request-response cycle.", action="store_true")
args_javascript.add_argument("--auto-remove-javascript-validation",help="This switch will tell The Browser-Bruter to not remove common javascript input validations mechanisms. Useful if removing of javacript validaiton breaks the web app.", action="store_true",default=False)
args_javascript.add_argument("--javascript",help="Javascript code to run on browser", metavar="\"alert(1);\"")
args_javascript.add_argument("--javascript-file",help="Javascritp file containing javascript code to execute", metavar="/path/to/javascript/file.js")
args_javascript.add_argument("--replace-code",help="Replaces the code in response body with the code provided by user in following format - \"CODE_TO_REPLACE1\",\"REPLACEMENT_CODE1\",\"CODE_TO_REPLACE2\",\"REPLACEMENT_CODE2\"",metavar="\"alert(1);\",\"alert(0);\"")
args_javascript.add_argument("--replace-files", help="Replace the content of a file in HTTP responses.", metavar="/path/to/validation_file.js")
args_browser.add_argument("--headless",help="Use this switch to run browser in headless mode (No GUI).", action="store_true")
args_browser.add_argument("--load-static-media",help="This switch tells BrowserBruter to load audio, video and image (.png, .img, .ico, .mp4, .gif, .mp3 etc) files. By default it discards these files to save time and load pages faster.",action="store_true",default=False)
args_browser.add_argument("--chrome-options",help="Custom comma separated list of options which will be passed to chrome. [This will override in-built options in Browser-Bruter that are passed to chrome]",metavar="blink-settings=imagesEnabled=false,disable-notifications")
args_browser.add_argument("--anti-bot",help="This switch tells BrowserBruter to use avoid any chrome options and use raw undetected chrome driver to avoid bot detection, by default Browser-Bruter uses custom Chrome options along with undetected chrome driver like disabling xss protection along with undeteced chrome driver",action="store_true",default=False)
args_browser.add_argument("--no-anti-bot",help="Completely removes any anti bot detection evasions.",action="store_true",default=False)
args_browser.add_argument("--new-instance",help="Start new fresh instance of browser for each new payload [Fuzzing process's iteration] usefull in bypassing the invisible captchas.",action="store_true")
args_browser.add_argument("--new-instance-restore-session",help="Start new fresh browser instance but restore the cookies", action="store_true")
args_report.add_argument("--rows-limit",help="Specify the number of rows to be included in single file, if not specified, a single report will be generated, if specified, multiple reports with specified rows amount will be generated, useful when test consists of thousands of payloads.", type=int, metavar="200")
args_debug.add_argument("--verbose",help="Use this switch to enable HTTP request/response output being printed on console and STDLOG file.", action="store_true",default=False)
# Getting the arguments in args variable
args = argParser.parse_args()

# Check if all required arguments are given and threads are not more than 5
if ((args.payloads is None or args.elements is None) and (args.elements_payloads is None)) or args.target is None or args.button is None or args.attack is None:
	print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Please Enter all required arguments --attack, --target, --button, --payloads, --elements or --elements-payloads\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	sys.exit(0)
elif args.threads > 5 or args.threads < 0:
	print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Value of threads must less than 6 and more than 0\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
	sys.exit(0)
elif (args.elements and args.elements_payloads):
    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}--elements and --elements--payloads can't be used together\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
    sys.exit(0)
# if forceCookie argument is present withouth --cookie option then throw error 
elif args.force_cookie:
	if args.cookie is None:
		print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}You can not use --forceCookie without --cookie option\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
		sys.exit(0)

### DEFINING AND PARSING COMMAND LINE ARGUMENTS ENDS ###

### DEFINING AND ASSIGNING GLOBAL VARIABLES STARTS ###	

# Getting hostname from target for filtering the output this will work as one kind scope for filtering output to be stored in report
target_url = urlparse(args.target)
hostname = target_url.hostname
# Get the scope hostnames from the command-line arguments
scope_hostnames = args.scope.split(',') if args.scope else []
# Getting time when script started to name the final report
start_time = datetime.datetime.now()
start_time = start_time.strftime("%Y-%m-%d_%H-%M-%S")
# Get the javascript code to be executed
javascript_to_execute = '\0'
if args.javascript:
    javascript_to_execute = args.javascript
elif args.javascript_file:
    if args.javascript:	
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The --javascript-file option can not be used with --javascript option\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        sys.exit(0)
    try:
        with open(args.javascript_file, 'rb') as file:
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Trying to read the replacement file.\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
            javascript_to_execute = file.read()
            javascript_to_execute = javascript_to_execute.decode('utf-8')
    except FileNotFoundError:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The specified replacement file '{args.replace_files}' does not exist.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
forbidden_extensions = ('.ico', '.png', '.img', '.jpg', '.svg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.gif', '.apng', '.avif', '.webp', '.bmp', '.cur', '.tif', '.tiff', '.mp3', '.mp4', '.avi', '.mkv', '.webm', 'ogv')
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
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The specified payloads file '{args.payloads}' does not exist.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The specified payloads file '{args.payloads}' does not exist.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        sys.exit(0)

# Get the content, Replace the response body with the content of the file provided by the user
file_contents = {}
if args.replace_files:
    try:
        replace_files = args.replace_files.split(',')
        for replace_file in replace_files:
            file_name, file_url = replace_file.split('++')
            with open(file_name, 'r') as file:
                print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Trying to read the replacement file. -> {file_name}\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                file_contents[file_name] = file.read()
    except FileNotFoundError:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The specified replacement file '{file_name}' does not exist.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The specified values file '{args.values}' does not exist.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        sys.exit(0)
    except json.JSONDecodeError:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Invalid JSON format in the specified values file '{args.values}'.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        print_exc()
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Refer Above Stack Trace\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
        if args.ignore_popups:
            try:
                alert = driver.switch_to.alert
                alert.accept()
            except NoAlertPresentException:
                pass
        else:
            print(f"\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Alert Pupup please interact with popup or use --ignore-popup option\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
            input(f"\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}press ENTER after intracting with popup\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")

# Handle Unknown Exception
def handle_unknown_exception(exception):
    print(exception)
    print_exc()
    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}An unknown error has been occured, Please open issue request at https://github.com/netsquare/BrowserBruter/issues and paste above message there, we are glad to help\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The specified payloads file '{file_path}' does not exist.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        log_error(format_exc())
        sys.exit(0)

# Function to Handle CTRL+C
def signal_handler(signal, frame):
    sleep(3)
    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}CTRL+C pressed. Waiting for remaining request/response to stop. Exiting...\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
                print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nWARNING: {RESET}BROWSERBRUTER IS PAUSED\npress ENTER to resume\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                k = input()				
                pause_event.clear()  # Clear the pause event 
                print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nWARNING: {RESET}Resuming BROWSERBRUTER\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Please download The Browser-Bruter from releases.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
            try:
                driver.add_cookie(cookie_dict)  
            except InvalidCookieDomainException as e:
                print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError:{RESET} Cookie Domain is invalid -> {cookie_dict} -> Skipping\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                log_error(format_exc())       
    except ValueError as e:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError:{RESET} You have entered arguments in invalid format -> {args.cookie} please read help message for valid format of passing cookies. Closing the Fuzzing process\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
        if response_body_encoding.lower() == 'gzip':
            response_body_str = gzip.decompress(request.response.body)
        else:
            response_body_str = request.response.body.decode(response_body_encoding,errors='ignore')
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
                request.response.body = file_contents[file_name]#response_content
                request.response.headers['Content-Length'] = len(request.response.body)

# Function to get and initialize the driver
def get_and_initialize_chrome_driver():
    options = get_browser_options()
    if args.no_anti_bot:
        options=get_browser_options()
        driver = webdriver.Chrome(executable_path="res/chrome/chromedriver", options=options, seleniumwire_options={'proxy': {'http': args.proxy, 'https': args.proxy}} if args.proxy else {})
    else:
        options = get_browser_options()
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
            print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR:{RESET} Error setting headers. Please provide headers in valid format.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
            driver.quit()
            log_error(format_exc())
            sys.exit(0)
    return driver
            
# Function to Remove attributes this is created to reduce code in attempt function
def remove_attributes_and_get_focus(driver, element):
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

# Function to log errors 
def log_error(error):
    try:
        #with log_error_lock:
        with open("logs/Error.txt","a") as error_log_file:
            error_time = datetime.datetime.now()
            error_time = error_time.strftime("%Y-%m-%d_%H-%M-%S")
            error_log_file.write(f"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            error_log_file.write(f"Error Time - {error_time}")
            error_log_file.write("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
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
    cookies_to_be_restored = driver.get_cookies()
    driver.quit()
    driver = get_and_initialize_chrome_driver()
    if args.new_instance_restore_session:
        for cookie in cookies_to_be_restored:
            driver.add_cookie(cookie)
    return driver

# Function to press the button
def press_button(driver,button,from_buttons_to_press):
    try:
        if args.press_enter_no_click and not from_buttons_to_press:
            button.send_keys("\n")
        else:
            button.click()
    except ElementClickInterceptedException as e:
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}The button -> {button} is not clickable or click has been intercepted by some other element, there might be some javascript being executed on web page which is preventing the click. Please remove the code intercepting the click.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        print_exc()
        log_error(format_exc())
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Refer Above Stack Trace\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        driver.quit()
        sys.exit(0)

# Function to perform generic initial operations before filling the form
def initial_operations_before_filling_the_form(driver):
    # If --forceCookie is set then set the initial cookies
    if args.force_cookie:
        add_cookies(driver)
    # Wait for body to be loaded in case of slow response
    wait_and_handle_popup(driver) 
    # Clear previous requests
    del driver.requests
    # Go to the target website
    if not args.interactive:
        try:
            driver.get(args.target)
        except TimeoutException as e:
            print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
            print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Specified Element is not interactable -> {input_field}\nFollowings are the possible reason:\n 1. Either tool is running too fast, make it slow using --delay-* options\n 2. May be the {input_field} requires some action like clicking on button to make it interactable, in such case, provide a javascript using --javascript option to execute javascript.\n Skipping filling this {input_field}\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
            
def write_http_request_response(element, this_threads_file, driver, payload, webpage_before, webpage_after):
    with open(this_threads_file, 'a', newline='') as report:
        # Filtering requests that are in scope
        captured_requests = driver.requests
        filtered_requests = [single_request for single_request in captured_requests if
                     urlparse(single_request.url).hostname == hostname or
                     any(urlparse(single_request.url).hostname == scope_hostname for scope_hostname in scope_hostnames)]
        filtered_requests = [single_request for single_request in filtered_requests if all(extension not in single_request.url for extension in forbidden_extensions)]
        filtered_requests = [single_request for single_request in filtered_requests if all(extension not in single_request.url for extension in ['.js', '.css', '.txt'])]
        writer = csv.writer(report)
        for request in filtered_requests:
            try:
                request_body = request.body.decode("UTF-8")
            except UnicodeDecodeError:
                request_body = request.body
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
                soup = bs(raw, features="html.parser")
                response_body = soup.prettify() if hasattr(soup, 'prettify') else raw.decode("UTF-8", errors="replace")
                # After printing on the display, write it to the report
                row = [value if value else ' ' for value in
                    [request_time.strftime('%Y-%m-%d %H:%M:%S'), str(element), str(payload), request.method, request.url, request.headers, request_body, response_time.strftime('%Y-%m-%d %H:%M:%S'), 
                    cycle_time_in_milliseconds, request.response.status_code, request.response.reason, request.response.headers, response_body,
                    len(request.response.body), bs(webpage_before,features="html.parser").prettify(), 
                    bs(webpage_after,features="html.parser").prettify()]]
                writer.writerow(row)
                # Check whether the output should be printed on the console or not
                if args.verbose:
                    # Print the request
                    print(f'\n{GREEN}---------------------Single Request/Response Cycle-------------------')
                    print(f"Fuzzing - " + str(element))
                    print(f"Payload - " + str(payload))
                    print(f'----------------------REQUEST---------------------{RESET}')
                    print('Time - ' + request_time.strftime('%Y-%m-%d %H:%M:%S') + '\n', request.method, request.url)
                    # Print in a new line
                    print(request.headers, request_body)
                    # Print the response
                    print(f'{GREEN}----------------------RESPONSE--------------------{RESET}')
                    if request.response:
                        print(
                            'Time - ' + response_time.strftime('%Y-%m-%d %H:%M:%S') + '\n',
                            request.response.status_code,
                            request.response.reason
                        )
                    print(request.response.headers)
                    print(response_body)
                    print(f"{GREEN}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\nTIME: {cycle_time_in_milliseconds} MilliSeconds \n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
  
            except AttributeError as e:
                # Code to handle if no request has been made and there is no response
                if args.verbose:
                    print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO:{RESET} No response is received not skipping report row!\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                row = [value if value else ' ' for value in
                    [request_time.strftime('%Y-%m-%d %H:%M:%S'), str(element), str(payload), request.method, request.url, request.headers, request_body, request_time.strftime('%Y-%m-%d %H:%M:%S'), 
                    '0', '0', "N/A", "N/A", "N/A",
                    "N/A", bs(webpage_before,features="html.parser").prettify(), 
                    bs(webpage_after,features="html.parser").prettify()]]
                writer.writerow(row)

# Function to Generate Final Report
def generate_final_report():
    # Increase the field size limit
    csv.field_size_limit(sys.maxsize)
    print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO:{RESET} Generating Final Report\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
                            print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nWARNING:{RESET} Field size is too large to handle, replacing field with 'BROWSER-BRUTER-DISCARDED-EXTREMELY-LARGE' - Skipping row {index_counter} in file {csv_file}: {str(e)}\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
                            payloads.remove(i.strip())
                # Delete the current thread's processed payloads file
                os.remove(file_path)
        if args.attack in (1, 2):
            # Storing remaining payloads in a separate file
            remaining_payloads = os.path.join(directory, "Remaining_Payloads.txt")
            with open(remaining_payloads, 'w', newline='') as remaining_payloads_file:
                for payload in payloads:
                    remaining_payloads_file.write(payload + '\n')
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO:{RESET} Remaining Payloads (if any) have been stored -> {remaining_payloads}\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Processed Payloads (if any) have been stored -> {processed_payloads}\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO:{RESET} Report Generated -> {final_report}\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
    except ConnectionRefusedError as e:
        log_error(format_exc())
        print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
                print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError:{RESET} Specified element {element} is not found. Please verify the name of the element. For more information, check Error.txt\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                print_exc()
                print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Refer Above Stack Trace\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                driver.quit()
                log_error(format_exc())
                sys.exit(0)

# Function to get element to be fuzzed
def get_element(driver,element,coming_from_initial_operations_method):
    if args.form and not coming_from_initial_operations_method:
        selector = get_form(driver,args.form)
    else:
        selector = driver    
    try:
        element = selector.find_element(By.ID, element)
    except NoSuchElementException:
        try:
            element = selector.find_element(By.NAME, element)
        except NoSuchElementException:
            try:
                element = selector.find_element(By.CLASS_NAME, element)
            except NoSuchElementException:
                try:
                    element = selector.find_element(By.XPATH,f"//input[@value='{element}']")
                except NoSuchElementException:
                    try:
                        element = selector.find_element(By.XPATH,f"//input[@Type='{element}']")
                    except NoSuchElementException:
                        try:
                            element = selector.find_element(By.XPATH,f"//textarea[@value='{element}']")
                        except NoSuchElementException:    
                            try:
                                element = selector.find_element(By.XPATH,f"//button[@value='{element}']")
                            except NoSuchElementException:
                                try:
                                    element = selector.find_element(By.XPATH,f"//button[@Type='{element}']")
                                except NoSuchElementException as e:
                                    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError:{RESET} Specified element {element} is not found. Please verify the name of the element. For more information, check Error.txt\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                                    print_exc()
                                    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Refer Above Stack Trace\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
                                    driver.quit()
                                    log_error(format_exc())
                                    sys.exit(0)
    remove_attributes_and_get_focus(driver, element)
    return element

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
        print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Specified Element is not interactable -> {element_being_fuzzed}\nFollowings are the possible reason:\n 1. Either tool is running too fast, make it slow using --delay-* options\n 2. May be the {element_being_fuzzed} requires some action like clicking on button to make it interactable, in such case, provide a javascript using --javascript option to execute javascript.\n Skipping filling this {element_being_fuzzed}\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")

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
                    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
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
            if args.attack == 1:
                if not terminate:
                    sniper(payloads, elements, instance_number, this_threads_files, driver)
            elif args.attack == 2:
                if not terminate:
                    battering_ram(payloads, elements, instance_number, this_threads_files, driver)
            elif args.attack == 3:
                if not terminate:
                    pitchfork(payloads,instance_number,this_threads_files,driver)
            elif args.attack == 4:
                if not terminate:
                    attempt_clusterbomb_fuzz(payloads,driver,this_threads_files,instance_number)
        # Handle the exceptions which are specific to this thread and do not affect other threads
        except NoSuchWindowException as e:
            log_error(format_exc())
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        except ConnectionRefusedError as e:
            log_error(format_exc())
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        except RemoteDisconnected as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        except ProtocolError as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        except MaxRetryError as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed or Browsers has reached maximum retries, if you have closed BrowserBruter ignore this else report the issue, check error log if this is unintentional\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        except WebDriverException as e:
            log_error(format_exc())
            # This exception can be arrived when the user closes the browser window
            print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed or Remote connection lost with following message\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
            print_exc()
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

def sniper(payloads,elements,instance_number,this_threads_files,driver):
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
    initial_operations_before_filling_the_form(driver)
    # Get web page content before making request
    webpage_before = driver.page_source
    # Automatically handle and fill the form
    if args.fill:
        fill_the_form(driver)
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    element_being_fuzzed = get_element(driver,element,False)
    if element in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed)
    # Fill the payload in element
    fill_payload_in_element(driver,element_being_fuzzed,payload)
    # Press the button
    button_to_press = get_element(driver,args.button,False)
    if args.button in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press)
    press_button(driver,button_to_press,False)
    operations_after_pressing_the_button(element,driver,webpage_before,this_threads_file,payload)
    
def battering_ram(payloads,elements,instance_number,this_threads_files,driver):
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
    initial_operations_before_filling_the_form(driver)
    # Get web page content before making request
    webpage_before = driver.page_source
    # Automatically handle and fill the form
    if args.fill:
        fill_the_form(driver)
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    for element in elements:
        element_being_fuzzed = get_element(driver,element,False)
        if element in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed)
        # Fill the payload in element
        fill_payload_in_element(driver,element_being_fuzzed,payload)
    # Press the button
    button_to_press = get_element(driver,args.button,False)
    if args.button in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",button_to_press)
    press_button(driver,button_to_press,False)
    operations_after_pressing_the_button(element,driver,webpage_before,this_threads_file,payload)

def pitchfork(elements_payloads,instance_number,this_threads_files,driver):
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
    initial_operations_before_filling_the_form(driver)
    # Get web page content before making request
    webpage_before = driver.page_source
    # Automatically handle and fill the form
    if args.fill:
        fill_the_form(driver)
    # Fill the target field being fuzzed with the current payload
    # Finding the element either by id, name, or class
    for element, payload_list in elements_payloads.items():
        element_being_fuzzed = get_element(driver,element,False)
        if element in remove_class_elements:
            driver.execute_script("arguments[0].removeAttribute('class');",element_being_fuzzed)
        # Fill the payload in element
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
                initial_operations_before_filling_the_form(driver)
                # Get web page content before making request
                webpage_before = driver.page_source
                if terminate:
                    break
                # Automatically handle and fill the form
                if args.fill:
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
                    fill_payload_in_element(driver,element_being_fuzzed,payload)
                # Press the button
                if not terminate:
                    button_to_press = get_element(driver,args.button,False)
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
                    handle_new_instance(driver)
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
        # Redirect stdout to the Tee class, the tee class redirects STDOUT to STDOUT and the log file
        log_file = 'logs/BrowserBruterSTDOUT.txt'  # This file stores console output
        tee_instance = Tee(log_file)
        sys.stdout = tee_instance
        # Get the number of threads or in other words number of browsers instances to use
        num_threads = args.threads
        # Print legal disclaimer
        print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nLegal Warning:{RESET} This Browser-Bruter open-source penetration testing tool is provided for educational and ethical purposes only. Users are solely responsible for ensuring compliance with all applicable laws and regulations, and the developer(s) disclaim any liability for misuse or damage caused by the tool.\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO:{RESET} press ENTER to puase the attack.\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
        # Create and start the threads
        threads = []
        start = 0
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
                        # Start the thread
                        thread.start()
                        # Add the thread to the list of threads
                        threads.append(thread)
                        # Update the starting index for the next thread
                        start = end
                        # Sleep for 2.5 seconds for proper resource management
                        sleep(2.5)
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
                    sleep(2.5)     
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
        print(f"\n\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nINFO: {RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{YELLOW}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
    except SystemExit:
        log_error(format_exc())
        print("")
    except Exception as e:
        handle_unknown_exception(e)
    finally:
        # Generate the report
        generate_final_report()
        # Reset sys.stdout to the console at the end of your script
        sys.stdout = sys.__stdout__
        sys.exit(0)      
else:
    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nError:{RESET} Please run the script again using python3 BrowserBruter.py, closing the BrowserBruter\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")
    print_exc()
    print(f"\n\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\nERROR: {RESET}Refer Above Stack Trace\n{RED}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}")

### MAIN EXECUTION BLOCK ENDS ###