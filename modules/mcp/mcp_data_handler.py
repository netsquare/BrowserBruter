##################################################################
"""
Name : mcp_data_handler.py
Date : 04/29/2025
Author: Jafar Pathan
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
import base64
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from selenium.webdriver.common.by import By

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.run_browser.get_and_initialize_driver import get_and_initialize_chrome_driver
from modules.run_browser.add_cookies import add_cookies
from modules.run_browser.add_local_storage import add_local_storage
from modules.run_browser.add_session_storage import add_session_storage

# Global driver instance
driver = None

# Lifespan event: manages driver lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    global driver
    driver = get_and_initialize_chrome_driver()
    driver.get(global_variable.args.target)
    if global_variable.args.add_storage:
        add_local_storage(driver)
    if global_variable.args.add_session_storage:
        add_session_storage(driver)
    if global_variable.args.cookie:
        add_cookies(driver)
        driver.get(global_variable.args.target)
    yield
    if driver:
        driver.quit()

# FastAPI App Initialization
app = FastAPI(lifespan=lifespan)

# DOM Snapshot
@app.get("/dom_snapshot")
async def dom_snapshot():
    return JSONResponse(content={"url": driver.page_source})

# Get ScreenShot
@app.get("/screenshot")
async def screenshot():
    # Get PNG bytes from Selenium
    png_data = driver.get_screenshot_as_png()
    
    # Encode to base64 and format as data URI
    base64_image = base64.b64encode(png_data).decode('utf-8')
    data_uri = f"data:image/png;base64,{base64_image}"
    
    # Return in JSON
    return JSONResponse(content={"image": data_uri})

# Current URL
@app.get("/current_url")
async def current_url():
    return JSONResponse(content={"url": driver.current_url})

# Parsed Switches (Arguments)
@app.get("/browser_bruter_switches_and_arguments")
async def browser_bruter_switches_and_arguments():
    data = """
usage: BrowserBruter.py [-h] [-t TARGET_URL] [-b submit] [-a 2] [-e username,password,phone,address,projectId++formcontrolname]
                        [-ep FIELD:/PATH/TO/FILE,textarea:payloads.txt,data:pay.txt] [-p /home/payloads.txt] [--mcp] [--fill e1,elemn3,user,npass,id] [--fill-values /path/to/file.json]
                        [--buttons-to-press-before-fuzz visibleform,ok,confirm,pressthis] [--press-enter-no-click] [--delay-before 0.2] [--delay-after 0.2] [--threads 3] [--pause]
                        [--interactive] [--pause-after-submit] [--reload-page] [--no-reload-page] [--form changePasswordForm] [--debug DEBUG] [--debug-code DEBUG_CODE]
                        [--property PROPERTY] [--pause-on-popup] [--headers "Auth: 123","CUSTOM_HEADER: VALUE"] [--cookie name:value,name2:value2] [--force-cookie] [--remove-session]
                        [--add-storage key:value++key2:value2] [--add-session-storage key:value++key2:value2] [--force-storage] [--force-session-storage] [--python PYTHON]
                        [--python-after PYTHON_AFTER] [--python-file PYTHON_FILE] [--python-request PYTHON_REQUEST] [--python-request-file PYTHON_REQUEST_FILE]
                        [--python-response PYTHON_RESPONSE] [--python-response-file PYTHON_RESPONSE_FILE] [--record-navigation] [--load-navigation-before /path/to/navigation/file.json]
                        [--load-navigation-after /path/to/navigation/file.json] [--auto-remove-javascript-validation] [--disable-events keypress,keydown,change,keyup]
                        [--remove-class cdk-text-field-autofill-monitored] [--javascript "alert(1);"] [--javascript-after JAVASCRIPT_AFTER] [--javascript-file /path/to/javascript/file.js]
                        [--replace-code "alert(1);"::"alert(0);"] [--replace-files /path/to/validation_file.js] [--chrome-binary /path/to/chrome] [--chrome-driver /path/to/chromedriver]
                        [--headless] [--no-css] [--proxy http://proxyaddress:port/] [--remove-images] [--chrome-options blink-settings=imagesEnabled=false,disable-notifications]
                        [--anti-bot] [--no-anti-bot] [--new-instance] [--rows-limit 200] [--scope api1.example.com,bak.example.com]
                        [--inscope-urls /path/to/file OR "https://api1.example.com/v2/getData","https://bak.example.com/v2/signin"]
                        [--outofscope-urls /path/to/file OR "http://10.13.37.3:8080/webgoat/service/hint.mvc","http://10.13.37.3:8080/webgoat/service/solution.mvc"] [--verbose]
                        [--print-error] [--gui] [--help-manual]

BrowserBruter is a python3 script, utilizing power of selenium and selenium-wire to automate fuzzing of various input fields of webpages to test their security against malicious inputs. For contact and more information about project please visit https://github.com/netsquare/BrowserBruter

options:
  -h, --help            show this help message and exit

Basic:
  -t, --target TARGET_URL
                        Target's url: https://zinja-coder.github.io/
  -b, --button submit   Button element which will submit form data.
  -a, --attack 2        The attack mode:
                         1. SNIPER
                         2. BATTERING RAM
                         3. PITCH FORK
                         4. CLUSTER BOMB

Sniper and Battering Ram:
  -e, --elements username,password,phone,address,projectId++formcontrolname
                        Input fields(target elements of form) in comma separated values.
  -p, --payloads /home/payloads.txt
                        /path/to/payload/file.

PitchFork and Cluster Bomb:
  -ep, --elements-payloads FIELD:/PATH/TO/FILE,textarea:payloads.txt,data:pay.txt
                        Input fields(target elements of form) and their respective payloads files.

AI and MCP Options:
  --mcp                 Spawn Browser and analyze the target using AI via MCP Server.

Fuzzing Options:
  --fill e1,elemn3,user,npass,id
                        Auto fill the specified elements, useful when web page is complex when you want to target specific fields only.
  --fill-values /path/to/file.json
                        [Optional] Path to User provided elements values file. See sample-file-for-giving-form-values.json
  --buttons-to-press-before-fuzz visibleform,ok,confirm,pressthis
                        Supply list of buttons to be pressed in sequence before filling the form, useful if form submission requires some action or form is invisible until some button is pressed.[Note if the button is not pressable element, then use --javascript and supply javascript to click the element.]
  --press-enter-no-click
                        This switch will force the Browser Bruter to send ENTER key instead of clicking the button, useful when form is submitted when pressing entering on text field and there are no buttons to click.
  --delay-before 0.2    Delay before fuzz attempt.
  --delay-after 0.2     Delay after fuzz attempt.
  --threads 3           Specifies number of browsers instances to be run, max value is 20, default is 1, lower the instances slower and stable the fuzzing process, more instances - faster and unstable fuzzing process. Note: The higher amount of threads consumes more system resources.
  --pause               Pause the BrowserBruter instances on startup, press ENTER to resume.
  --interactive         Pause the BrowserBruter before fuzzing any element at each payload and wait for user to continue.
  --pause-after-submit  Pause the script after pressing the submit button to allow pentester to interact with the web application.
  --reload-page         This switch tells The Browser Bruter to reload the page before fuzzing the form on each iteration, useful when result of previous iteration causes the web elements to disappear or which leads to elements not found error, in such case this switch helps to keep browser bruter running.
  --no-reload-page      This switch will force the Browser Bruter to not go back to --target URL, instead stay on the same page after submitting the form.
  --form changePasswordForm
                        Specify id,name,class of form to fuzz in case of multiple forms
  --pause-on-popup      Pauses the Browser Bruter in case of pop up occurs, help full when finding Cross Site Scripting and need to perform manual actions

Fuzzing via Debugging Options:
  --debug DEBUG         use this to set debug point on the browser
  --debug-code DEBUG_CODE
                        when debug hits, execute this code
  --property PROPERTY   COMING SOON....

Session:
  --headers "Auth: 123","CUSTOM_HEADER: VALUE"
                        Comma-separated list of custom headers.
  --cookie name:value,name2:value2
                        Use it to define cookies to be used while sending initial request, cookies should be in name:value:domain comma separated format.
  --force-cookie        Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server.
  --remove-session      Use this switch to remove session data and cookies after each request-response cycle.
  --add-storage key:value++key2:value2
                        Use this switch to add local storage in browser as a key:value pair.
  --add-session-storage key:value++key2:value2
                        Use this switch to add session storage in browser as a key:value pair.
  --force-storage       This switch will prevent overriding of data set using --add-storage option by web application.
  --force-session-storage
                            This switch will prevent overriding of data set using --add-session-storage option by web application.

Python Scripting Engine:
  --python PYTHON       Executes provided python code.
  --python-after PYTHON_AFTER
                        Executes provided python code after single fuzzing attempt of form.
  --python-file PYTHON_FILE
                        Reads and Executes provided python code from file.
  --python-request PYTHON_REQUEST
                        Python code which will modify the HTTP Request.
  --python-request-file PYTHON_REQUEST_FILE
                        File containing python code to manipulate HTTP Request.
  --python-response PYTHON_RESPONSE
                        Python code to manipulate HTTP Response.
  --python-response-file PYTHON_RESPONSE_FILE
                        File containing python code to manipulate HTTP response.

JavaScript Code Handler:
  --javascript "alert(1);"
                        Javascript code to run on browser
  --javascript-after JAVASCRIPT_AFTER
                        Javascript code to run on browser after pressing and submitting the button.
  --javascript-file /path/to/javascript/file.js
                        Javascript file containing javascript code to execute

Automatic Navigation Handler:
  --record-navigation   This option will let user record their mouse clicks and keyboard key strokes, which can be replicated to navigate around the web page.
  --load-navigation-before /path/to/navigation/file.json
                        This switch will load the previously recorded navigation and will replicate it to automatically do the navigation around the web page.
  --load-navigation-after /path/to/navigation/file.json
                        This switch will load the previously recorded navigation and will replicate it to automatically do the navigation around the web page after submitting the form.

Anti Input Validation:
  --auto-remove-javascript-validation
                        This switch will tell The Browser-Bruter to not remove common javascript input validations mechanisms. Useful if removing of javacript validaiton breaks the web app.
  --disable-events keypress,keydown,change,keyup
                        Disables specified javascript events, for example onClick, etc. Provide comma separated list of events.
  --remove-class cdk-text-field-autofill-monitored
                        Provide a list of elements from which you want to remove the class attribute, extremely useful when element is linked to some class with extreme javascript input validation or makes the element not interactable, you can still select this element by providing it's class name.
  --replace-code "alert(1);"::"alert(0);"
                        Replaces the code in response body with the code provided by user in following format - "CODE_TO_REPLACE1"::"REPLACEMENT_CODE1"+++"CODE_TO_REPLACE2"::"REPLACEMENT_CODE2"
  --replace-files /path/to/validation_file.js
                        Replace the content of a file in HTTP responses.

Browser Options:
  --chrome-binary /path/to/chrome
                        Use this switch to provide your local/custom chrome browser.
  --chrome-driver /path/to/chromedriver
                        Use this switch to use your local/custom chromedriver.
  --headless            Use this switch to run browser in headless mode (No GUI).
  --no-css              This switch will tell Browser Bruter to drop the requests to .css files and it will not load .css files and remove <style> tag.
  --proxy http://proxyaddress:port/
                        Set proxy for traffic, for example give IP:PORT of Burpsuite to send traffic to burpsuite.
  --remove-images       This switch tells BrowserBruter not to load audio, video and image (.png, .img, .ico, .mp4, .gif, .mp3 etc) files. By default it loads these files.
  --chrome-options blink-settings=imagesEnabled=false,disable-notifications
                        Custom comma separated list of options which will be passed to chrome. [This will override in-built options in Browser-Bruter that are passed to chrome]
  --anti-bot            This switch tells BrowserBruter to use avoid any chrome options and use raw undetected chrome driver to avoid bot detection, by default Browser-Bruter uses custom Chrome options along with undetected chrome driver like disabling xss protection along with undeteced chrome driver
  --no-anti-bot         Completely removes any anti bot detection evasions.
  --new-instance        Start new fresh instance of browser for each new payload [Fuzzing process's iteration] usefull in bypassing the invisible captchas.

Verbose Option:
  --verbose             Use this switch to enable HTTP request/response output being printed on console and STDLOG file.
  --print-error         Use this switch to print the Stack Trace messages in case of the error! and keep the logs in log file.

Report Generation:
  --rows-limit 200      Specify the number of rows to be included in single file, if not specified, a single report will be generated, if specified, multiple reports with specified rows amount will be generated, useful when test consists of thousands of payloads.
  --scope api1.example.com,bak.example.com
                        Comma separated list of hostnames in scope
  --inscope-urls /path/to/file OR "https://api1.example.com/v2/getData","https://bak.example.com/v2/signin"
                        Comma-separated list of urls or file containing urls in-scope
  --outofscope-urls /path/to/file OR "http://10.13.37.3:8080/webgoat/service/hint.mvc","http://10.13.37.3:8080/webgoat/service/solution.mvc"
                        Comma separated list of urls or file containing urls which are to be excluded from final report

GUI:
  --gui                 Use this switch to run Browser Bruter in GUI

Help:
  --help-manual         Print the Usage Examples
  
Usage Examples:
    1. Perform Bruteforce(ClusterBomb) on login page:
        python3 BrowserBruter.py --elements-payloads username:usernames.txt,password:passwords.txt --target http://localhost/login.php --button Login --attack 4 --remove-session

    2. Perform PitchFork on login page:
        python3 BrowserBruter.py -ep username:usernames.txt,password:passwords.txt -t http://localhost/login.php -b Login -a 3

    3. Perform BatteringRam on login page:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login.php --button Login --verbose --attack 2

    4. Fuzz on login page and make it verbose:
        python3 BrowserBruter.py -e username,password --fill username,password -p sqli.txt -t http://localhost/login.php -b Login --verbose -a 1

    5. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint':
        python3 BrowserBruter.py --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --attack 1

    6. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request becuase the initial cookies might be overridden by new cookies values:
        python3 BrowserBruter.py --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --attack 1

    7. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle [this is useful against Authentication pages when you don't want redirection in case of successful login]:
        python3 BrowserBruter.py -e name,age,address,phone --fill name,age,address,phone -p payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --remove-session --attack 1

    8. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode:
        python3 BrowserBruter.py --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --remove-session --headless --attack 1

    9. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode and run 5 instances of browser parallely:
        python3 BrowserBruter.py --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --remove-session --headless --threads 5 --attack 1
   
    10. Fuzz CheckBox for example '<input type="checkbox" name="hobbies" value="reading" /> <input type="checkbox" name="hobbies" value="writing" />':
        python3 BrowserBruter.py --elements hobbies --payloads paylods.txt --target http://localhost/register --button register --attack 1
   
    11. Fuzz Radio Button for example '<input type="radio" name="yesno" id="yes" value="yes" required/> <input type="radio" name="yesno" id="no" value="no" required/>':
        python3 BrowserBruter.py --elements yesno --payloads payloads.txt --target http://localhost/register --button register --attack 1
    OR
        python3 BrowserBruter.py --elements no --payloads payloads.txt --target http://localhost/register --button register --attack 1
   
    12. Fuzz <select> element - for example <select name="selectElement" required> <option value="">Select an option</option> <option value="option1">Option 1</option> </select>:
        python3 BrowserBruter.py -e selectElement -p payloads.txt -t http://localhost/selection -b submit -a 1
    
    13. Fuzz <textarea> element - for example <textarea name="textareaElement" placeholder="Enter text" required></textarea>:
        python3 BrowserBruter.py --elements textareaElement --payloads payloads.txt --target http://localhost/registration --button submit --attack 1
   
    14. Fuzz colorpicker, datepicker, timepicker - for example <input type="color" name="colorElement" required/> <input type="date" name="dateElement" required/> <input type="time" name="timeElement" required/>:
        python3 BrowserBruter.py --elements colorElement,dateElement,timeElement --fill colorElement,dateElement,timeElement --payloads payloads.txt --target http://localhost/ --button submit --attack 1

    15. Define API domain in scope for proper report generation and logging:
        python3 BrowserBruter.py --elements username,password --fill username,password --button button --target http://net-square.com/login --payloads payloads.txt --attack 1 --scope api.net-square.com,dev.api.net-square.com

    16. Add Authorization headers with bearer token for valid authorization:
        python3 BrowserBruter.py --elements username,password --fill username,password --button button --target http://net-square.com/login --payloads payloads.txt --header "Auth: 123","Auth1: Bearer emluamFjb2Rlcgo=" 
           
    17. Provide custom values for each form field types, content of the file should be in JSON format and it should contain all of the field types, see example values.json for better understanding:
        python3 BrowserBruter.py --elements username,password --fill username,password --fill-values fields.json --button button --target http://net-square.com/login --payloads payloads.txt"                                                                                                                                                          

    18. Pause the BrowserBruter on each iteration of fuzzing, so user can manually perform any task, complete captcha before BrowserBruter fuzzes the form, press ENTER two times to continue:
        python3 BrowserBruter.py --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --threads 5 --fill-values values.json --interacitve --attack 1

    19. Replace the content of a file in HTTP responses and specify the replacement file URL:
        python3 BrowserBruter.py --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-files "input-validation.js"++"http://localhost/assets/js/input-validation.js" --attack 1                                                                                        

    20. Replace the content of a file in HTTP responses and run JavaScript:
        python3 BrowserBruter.py --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-files "input-validation.js"++"http://localhost/assets/js/input-validation.js" --javascript "var elmnt = document.getElementById('ClickMe'); elmnt.click();" --attack 1          

    21. Replace the content of a file in HTTP responses and run JavaScript code by providing the code in file:
        python3 BrowserBruter.py --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-files "input-validation.js"++"http://localhost/assets/js/input-validation.js" --javascript-file element-click.js --attack 1                                                     
    
    22. Replace every "return false" statement with "return true" and replace every "alert(0)" with "alert(1)":
        python3 BrowserBruter.py --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-code "return false"::"return true"+++"alert(0)"::"alert(1)" --javascript "var elmnt = document.getElementById('ClickMe'); elmnt.click();" --attack 1
    
    23. Replace bunch of javascript code into return true:
        python3 BrowserBruter.py --elements-payloads textarea:sqli.txt,data:sqli.txt --button submit --target http://localhost:3000/index.html --attack 3 --replace-code "return false"::"return true"+++"return regex.test(dateString)"::"return true"+++"return regex.test(timeString)"::"return true"+++"return regex.test(colorString)"::"return true"

    24. Fuzz the search box, when user have to press enter to submit the search query, the user has to click on search icon to make search box appear:
        python3 BrowserBruter.py --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click                                                                                                                                           
    
    25. Tell Browser Bruter to remove common javascript input validation:
        python3 BrowserBruter.py --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --auto-remove-javascript-validation                                                                                                       
        
    26. Tell Browser Bruter to ignore pop ups like alert() box:
        python3 BrowserBruter.py --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --auto-remove-javascript-validation                                                                                                       

    27. Tell Browser Bruter to select the elements under the specified form only, in case there are two forms and multiple elements have same name and ids:
        python3 BrowserBruter.py --form changePasswordForm --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --attack 1

    28. Pause the Browser Bruter on startup to manually login to the application:
        python3 BrowserBruter.py --pause --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1

    29. Pause the Browser Bruter on startup to manually login to the application then run Browser Bruter in interactive mode to solve the captcha before inserting the payloads:
        python3 BrowserBruter.py --pause --interactive --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1
        
    30. Pause the Browser Bruter on startup to manually login to the application then run Browser Bruter in interactive mode to solve the captcha before inserting the payloads, pause the Browser Bruter after submitting the form to perform some manual human interaction:
        python3 BrowserBruter.py --pause --interactive --pause-after-submit --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1
    
    31. Wait for 1 seconds before and after submission of the form:
        python3 BrowserBruter.py --delay-before 1 --delay-after 1 --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1

    32. Route traffic via proxy i.e. BurpSuite and remove the static media like images:
        python3 BrowserBruter.py --proxy http://127.0.0.1:8080/ --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1 --remove-images

    33. Add custom chrome options which will be passed to chrome browser:
        python3 BrowserBruter.py --elements id --button Submit --payloads sqli.txt --target http://localhost/ --attack 1 --chrome-options ignore-certificate-errors,disable-dev-shm-usage

    34. Override all chrome options and use raw anti bot detection evasions:
        python3 BrowserBruter.py --elements id --button Submit --payloads sqli.txt --target http://localhost/ --attack 1 --anti-bot

    35. Brute force login page and try to bypass authentication and also do not try to evade anti bot defences and route traffic via proxy:
        python3 BrowserBruter.py --elements-payloads username:userid.txt,password:passwords.txt --button Login --target http://localhost/login.php --attack 4 --proxy http://127.0.0.1:8080/ --no-anti-bot --remove-session

    36. Perform BatteringRam attack on web page which has invisible captcha so start each payload insertion on new fresh instance of browser:
        python3 BrowserBruter.py --elements name,email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 2 --new-instance

    37. Perform BatteringRam attack on web page which has invisible captcha so start each payload insertion on new fresh instance of browser and force restore the cookie:
        python3 BrowserBruter.py --elements name,email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 2 --new-instance --force-cookie                                                                                                                                                                        

    38. There is field called name that you don't want to fuzz but it requires to be filled while submitting the form:
        python3 BrowserBruter.py --elements email,phone --fill name --payloads payloads.txt --target http://example.com/signup --button submit --attack 1
          
    39. There is input validation that is preventing the payloads, try to remove the class attribute from these elements to see if payloads are correctly inserted:
        python3 BrowserBruter.py --elements email,phone --fill name --remove-class email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 1                                                                                                                                                                    

    40. Split the final report into smaller chunks by specifying the rows limit in each report to make report review process faster in ReportExplorer:
        python3 BrowserBruter.py --elements email,phone --fill name --remove-class email,phone --payloads payloads.txt --target http://example.com/signup --button submit --attack 1 --rows-limit 200                                                                                                                                                   

    41. Excluding urls from final report:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --outofscope-urls "http://localhost/webgoat/service/solution.mvc","http://localhost/webgoat/service/lessonprogress.mvc","http://localhost/webgoat/service/lessonmenu.mvc","http://localhost/webgoat/service/solution.mvc"
        
        OR -> Providing list of urls:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --outofscope-urls urls.txt                                                                                                                                                          

    42. Including only specific urls in final report:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --inscope-urls "http://localhost/webgoat/attack?Screen=1869022003&menu=100"                                                                                                         

        OR -> Providing file containing URLs:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --inscope-urls urls.txt                                                                                                                                                             

    43. Force reload the page before fuzzing the form on each iteration, usefull when result of previous iteration causes the web elements to disappear or which leads to elements not found error, in such case this switch helps to keep browser bruter running:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/160587164/200 --elements employee_id,password --button submit --attack 1 --cookie ASP.NET_SessionId:fawx1oxcfm0fd4gvzmej5oco,JSESSIONID:1F0E3B20ECEDDF29235853F55C60FC17 --inscope-urls "http://localhost/webgoat/attack?Screen=160587164&menu=200" --payloads fuzz.txt --delay-before 0.3 --delay-after 0.3 --fill employee_id,password --reload-page
                                                                                                                                                                            
    44. Print the stack trace for debugging purpose:                                                                                                                        
        python3 BrowserBruter.py --target http://localhost/ --elements-payloads username:usernames.txt,password:passwords.txt --button btn-default --attack 4 --print-error 

    45. Execute specific javascript after submitting the form:
        python3 BrowserBruter.py --target http://localhost:8080/webgoat/start.mvc#attack/1778575388/500 --elements pass1,pass2,pass3,pass4,pass5,pass6 --fill pass1,pass2,pass3,pass4,pass5,pass6 --button SUBMIT --attack 1 --payloads fuzz.txt --include-url "http://10.13.37.3:8080/webgoat/attack?Screen=1778575388&menu=500" --cookie ASP.NET_SessionId:fawx1oxcfm0fd4gvzmej5oco,JSESSIONID:1F0E3B20ECEDDF29235853F55C60FC17 --reload-page --javascript-after "alert(123);"

    46. Don't load .css files:
        python3 BrowserBruter.py --target http://localhost:8080/webgoat/start.mvc#attack/1778575388/500 --elements pass1,pass2,pass3,pass4,pass5,pass6 --fill pass1,pass2,pass3,pass4,pass5,pass6 --button SUBMIT --attack 1 --payloads fuzz.txt --no-css

    47. Become psycho and run 20 threads (unstable):
        python3 BrowserBruter.py --target http://localhost/webgoat/login.mvc --attack 4 --elements-payloads exampleInputEmail1:usernames.txt,exampleInputPassword1:passwords.txt --button "btn.btn-large.btn-primary" --remove-session --threads 20 --outofscope-urls urls.txt

        OR -> run in headless mode, this is most stable way to run in multiple threads (still unstable):
        python3 BrowserBruter.py --target http://localhost/webgoat/login.mvc --attack 4 --elements-payloads exampleInputEmail1:usernames.txt,exampleInputPassword1:passwords.txt --button "btn.btn-large.btn-primary" --remove-session --threads 20 --outofscope-urls urls.txt --headless

    48. Get the element using CSS SELECTOR, here using css selector for '--button' option:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login3.php --button button.btn.btn-default --attack 1 --fill username,password   

    49. Execute the python using Python Scripting Engine:
        python3 BrowserBruter.py --elements text-center --button font-semibold --payloads usernames.txt --target http://localhost/ --attack 1 --scope api.localhost --python "e1 = driver.find_element(By.CSS_SELECTOR, 'input.w-full.text-center'); e1.send_keys('1234567890'); driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.mt-6.w-full.font-semibold').click(); sleep(2)"

    50. Execute the python using Python Scripting Engine - provide python file:
        python3 BrowserBruter.py --elements text-center --button font-semibold --payloads usernames.txt --target http://localhost/ --attack 1 --scope api.localhost --python-file captcha_cracker.py                                                                                                                                                    

    51. Execute the python code after filling the form using Python Scripting Engine:
        python3 BrowserBruter.py --elements text-center --button font-semibold --payloads usernames.txt --target http://localhost/ --attack 1 --scope api.localhost --python-after "e1 = driver.find_element(By.CSS_SELECTOR, 'input.w-full.text-center'); e1.send_keys('1234567890'); driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.mt-6.w-full.font-semibold').click(); sleep(2)"

    52. Execute the python code to Add custom header in HTTP request using Python Scripting Engine:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login3.php --button "button.btn.btn-default" --attack 1 --fill username,password --python-request "request.headers['python-added'] = 'added-by-python'"    

    53. Execute the python code to Add custom header in HTTP response using Python Scripting Engine:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login3.php --button "button.btn.btn-default" --attack 1 --fill username,password --python-response "response.headers['python-added'] = 'added-by-python'"    

    54. Execute the python code to Add custom header in HTTP request using Python Scripting Engine using python file:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login3.php --button "button.btn.btn-default" --attack 1 --fill username,password --python-request-file sample-python-code.py

    55. Execute the python code to Add custom header in HTTP response using Python Scripting Engine using python file:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login3.php --button "button.btn.btn-default" --attack 1 --fill username,password --python-response-file sample-python-code.py

    56. Disable keypress,keydown and keyup events using --disable-events method:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login3.php --button "button.btn.btn-default" --attack 1 --fill username,password --disable-events keypress,keydown,keyup

    57. Record the navigation:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost/brand.php --cookie PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 --attack 1 --fill editBrandName --record-navigation

    58. Play the navigation before fuzzing the form:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost/brand.php --cookie PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 --attack 1 --fill editBrandName --load-navigation-before path/to/navigation.json

    59. Play the navigation after fuzzing the form:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost/brand.php --cookie PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 --attack 1 --fill editBrandName --load-navigation-after path/to/navigation.json
        
    60. You can also specify the element via custom identifier using '++' operator. For example for most angular based application, there is a attribute in element called formcontrolname, now suppose there is a element which don't have id and name, but have formcontrolname attribute with projectId value like following -> <input _ngcontent-ng-c1723137943="" formcontrolname="projectId" placeholder="Enter project Id" required="" class="form-control ng-untouched ng-pristine ng-invalid"> we can identify this as follows:
        python3 BrowserBruter.py --elements projectId++formcontrolname 

    Damn Vulnerable Web Application Lab Usage Examples:   

    1. Fuzz the Command Injection page of DVWA, Pause BrowserBruter on startup to manually login and manually set cookies, press ENTER two times to continue:
        python3 BrowserBruter.py --elements ip --button Submit --payloads payloads.txt --target http://localhost/vulnerabilities/exec/ --pause --attack 1    
    
    2. Fuzz the Command Injection page of DVWA, set two cookies, force reuse of these cookies, reset session data each time:
        python3 BrowserBruter.py --elements ip --button Submit --payloads payloads.txt --target http://localhost/vulnerabilities/exec/ --cookie PHPSESSID:jtq7r9fbgf90h2qm9915qk6551,security:low --force-cookie --remove-session --attack 1

    jsdebugging lab - https://hub.docker.com/r/bhattsameer/jsdebugginglab Usage Examples:
        
    1. Perform BruteForce attack on login page:
        python3 BrowserBruter.py --elements-payloads email:usernames.txt,password:passwords.txt --target http://172.17.0.2/Lab3/login.php --attack 4 --button btn-secondary --remove-session                                                                                                                                                            
        
    2. Perform bruteforce attack on otp page, but otp is being checked on frontend client side, so there are no http request-response from server, so perform brute force attack on client side only:
        python3 BrowserBruter.py --elements otp --payloads otps.txt --target http://localhost/Lab3/OTP.php --button button --attack 1 --delay-after 0.3 --cookie PHPSESSID:9u593rhl797n3v6aa5vu8mjj20

    Stock Management System Lab Usage Examples:

    1. Perform brute force attack on login page to bypass authentication:
        python3 BrowserBruter.py --elements-payloads username:usernames.txt,password:passwords.txt --button btn-default --target http://localhost/login3.php --attack 4 --remove-session                                                                                                                                                                
                                                                                                                                                                            

    2. Perform Sniper attack on form page which is hidden, and requires pressing a button to be revealed, so use --interactive option to manually press the button:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --interactive --delay-after 0.5 --fill editBrandName,brandId,editBrandStatus

    3. Further automate the script by locating and clickng the buttons which enables the form:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 0.3 --fill editBrandName --javascript "document.querySelector('button.btn.btn-default.dropdown-toggle').click(); document.querySelector('a[data-target=\"#editBrandModel\"]').click();" --delay-after 0.3

    4. Provide above javascript code in file:    
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 1 --fill editBrandName --javascript-file click.js

    5. Remove input validations form bootstrap.min.js file and press two buttons on web page using --javascript which will enable the web form:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName --payloads fuzz.txt --button editBrandBtn --target http://localhost/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 0.7 --fill editBrandName --javascript "document.querySelector('button.btn.btn-default.dropdown-toggle').click();document.querySelector('a[data-target=\"#editBrandModel\"]').click();" --delay-after 0.5 --replace-files "./res/samples/js-files-with-no-input-validation/bootstrap.min.js"++"http://localhost/assests/bootstrap/js/bootstrap.min.js"

    6. Brute force change password form with submit button's class name is 'btn btn-primary':
        python3 BrowserBruter.py --elements-payloads user_id:usernames.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt --target http://localhost/setting.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button 'btn-primary'

    7. Brute force change password form by selecting the specific form, because there is other form with same elements:
        python3 BrowserBruter.py --elements-payloads user_id:usernames.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt --target http://localhost/setting.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button 'btn-primary' --form changePasswordForm
 
    8. Brute force add user form but first press one using --buttons-to-press-before-fuzz to enable this form:
        python3 BrowserBruter.py --elements-payloads userName:fuzz.txt,upassword:fuzz.txt,uemail:fuzz.txt --button createUserBtn --target http://localhost/user.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --buttons-to-press-before-fuzz addUserModalBtn

    9. Audit an complex form, replacing jquery-ui with no input validation jquery-ui and replacing bootstrap.min.js too, running 5 threads:
        python3 BrowserBruter.py --form createOrderForm --elements orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace --fill orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace --payloads fuzz.txt --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button createOrderBtn --attack 1 --replace-file ./res/samples/js-files-with-no-input-validation/bootstrap.min.js++http//localhost/assests/bootstrap/bootstrap.min.js,"./res/samples/js-files-with-no-input-validation/jquery-ui.min.js"++"http://localhost/assests/jquery-ui/jquery-ui.min.js" --attack 1 --target "http://localhost/orders.php?o=add" --threads 5

    10. Fuzz the report page of the Stock Management System:
        python3 BrowserBruter.py --elements startDate,endDate --fill startDate,endDate --button generateReportBtn --target http://localhost/report.php --attack 1 --payloads fuzz.txt --form getOrderReportForm --cookie PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 --replace-files res/samples/js-files-with-no-input-validation/bootstrap.min.js++http//localhost/assests/bootstrap/bootstrap.min.js,"res/samples/js-files-with-no-input-validation/jquery-ui.min.js"++"http://localhost/assests/jquery-ui/jquery-ui.min.js" --delay-before 0.5                                                                                                                                                                     

    OWASP JuiceShop Usage Examples:
         
    1. Testing SQLi on OWASP JuiceShop's login page by cluster bombing the payloads:
        python3 BrowserBruter.py --elements-payloads email:sqli.txt,password:sqli.txt --target http://localhost:3000/#/login --attack 4 --button loginButton --cookie welcomebanner_status:dismiss --remove-session

    2. Fuzzing registration page of OWASP JuiceShop:
        python3 BrowserBruter.py --elements emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl --button registerButton --attack 1 --fill emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl --payloads fuzz.txt --target http://localhost:3000/#/register --cookie welcomebanner_status:dismiss                                                                                                                                       

    3. Fuzz the email field for various vulnerabilities of OWASP JuiceShop and split the final report into 100 rows of multiples reports:
        python3 BrowserBruter.py --elements emailControl --button registerButton --attack 1 --fill emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl --payloads sqli.txt --target http://localhost:3000/#/register --cookie welcomebanner_status:dismiss --rows-limit 100

    4. Fuzz the file upload functionality of OWASP JuiceShop's complaint page:
        python3 BrowserBruter.py --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file

    5. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable:
        python3 BrowserBruter.py --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file --remove-class cdk-text-field-autofill-monitored

    6. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable and include the auth cookies and Authorization header to be able fuzz while being authenticated:
        python3 BrowserBruter.py --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file --remove-class cdk-text-field-autofill-monitored --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI"


    7. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable and include the auth cookies and Authorization header to be able fuzz while being authenticated and split the final report into smaller reports containing 200 rows each:
        python3 BrowserBruter.py --elements cdk-text-field-autofill-monitored,complaintMessage,file --button submitButton --attack 1 --target http://localhost:3000/#/complain --cookie welcomebanner_status:dismiss --payloads fuzz.txt --fill cdk-text-field-autofill-monitored,complaintMessage,file --remove-class cdk-text-field-autofill-monitored --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI"


    8. Fuzz the global search functionality of the OWASP JuiceShop while authenticated by sending ENTER key instead of click:
        python3 BrowserBruter.py --elements mat-input-0 --button mat-input-0 --attack 1 --target http://localhost:3000/#/ --cookie welcomebanner_status:dismiss --payloads fuzz.txt --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" --buttons-to-press-before-fuzz searchQuery --press-enter-no-click 


        OR -> following removes class attribute so the script does no throw element not intreactable error:
        python3 BrowserBruter.py --elements mat-input-0 --button mat-input-0 --attack 1 --target http://localhost:3000/#/ --cookie welcomebanner_status:dismiss --payloads fuzz.txt --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --remove-class mat-input-0


    9. Fuzz the Customer Feedback form of OWASP JuiceShop:
        python3 BrowserBruter.py --button submitButton --target http://localhost:3000/#/contact --cookie welcomebanner_status:dismiss --payloads fuzz.txt --attack 1 --elements userId,cdk-text-field-autofill-monitored,comment,rating --fill cdk-text-field-autofill-monitored,comment,rating --remove-class userId,cdk-text-field-autofill-monitored,comment,rating --interactive --rows-limit 200

        OR -> Fuzz the captcha field too:
        python3 BrowserBruter.py --button submitButton --target http://localhost:3000/#/contact --cookie welcomebanner_status:dismiss --payloads fuzz.txt --attack 1 --elements userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --fill cdk-text-field-autofill-monitored,comment,rating --remove-class userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --interactive --rows-limit 200

        OR -> Fuzz the captcha field and auto fill too:
        python3 BrowserBruter.py --button submitButton --target http://localhost:3000/#/contact --cookie welcomebanner_status:dismiss --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" --payloads fuzz.txt --attack 1 --elements userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --fill cdk-text-field-autofill-monitored,comment,rating,captchaControl --remove-class userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl --rows-limit 200

    10. Fuzz the chatbot of OWASP JuiceShop by first manually sign-in into the application:
        python3 BrowserBruter.py --button message-input --elements message-input --press-enter-no-click --target http://localhost:3000/#/chatbot --cookie test:working,welcomebanner_status:dismiss,language:en --pause --payloads fuzz.txt --attack 1 --rows-limit 200

    11. Fuzz the write review form of product by first manually login to the application, then automatically click on the image of product to make product review menu appear:
        python3 BrowserBruter.py --buttons-to-press-before-fuzz img-container --elements "cdk-text-field-autofill-monitored" --button submitButton --target http://localhost:3000/#/ --cookie cookieconsent_status:dismiss,language:en,welcomebanner_status:dismiss --attack 1 --payloads fuzz.txt --remove-class cdk-text-field-autofill-monitored --pause                                                                                                                                                                         

    USAGE EXAMPLES OF THE REPORT EXPLORER:
                                                                                                                                                                            
    REPORT EXPLORER:                                                                                                                                                        
    
    1. Run the tool:
        python ReportExplorer.py
    
    2. Open the report using --report option:
        python3 ReportExplorer.py --report BrowserBruter_Reports/localhost/2024-03-20_03-24-37/localhost-2024-03-20_03-24-37.csv

    2. Grep the strings and show the counts:
        python ReportExplore.py --grep welcome,success,admin,root,error

    3. Combine both --report and --grep option:
        python3 ReportExplorer.py --report BrowserBruter_Reports/localhost/2024-03-20_03-24-37/localhost-2024-03-20_03-24-37.csv --grep error,exception,success,"login Successful","welcome admin"

    4. Split the report for efficient review:
        python ReportExplorer.py --split /path/to/report-file.csv,200

"""
    return JSONResponse(content={"switches": data})
  
  
##################################################################
# Form Analysis and Intelligence Endpoints
##################################################################

@app.get("/analyze_forms")
async def analyze_forms():
    """Analyze all forms on the current page and extract detailed information"""
    forms_info = []
    try:
        forms = driver.find_elements(By.TAG_NAME, "form")
        for i, form in enumerate(forms):
            form_info = {
                "form_index": i,
                "id": form.get_attribute("id") or "",
                "class": form.get_attribute("class") or "",
                "action": form.get_attribute("action") or "",
                "method": form.get_attribute("method") or "GET",
                "inputs": [],
                "buttons": []
            }
            
            # Analyze input fields
            inputs = form.find_elements(By.TAG_NAME, "input")
            for input_elem in inputs:
                input_info = {
                    "name": input_elem.get_attribute("name") or "",
                    "id": input_elem.get_attribute("id") or "",
                    "type": input_elem.get_attribute("type") or "text",
                    "placeholder": input_elem.get_attribute("placeholder") or "",
                    "required": input_elem.get_attribute("required") is not None,
                    "maxlength": input_elem.get_attribute("maxlength"),
                    "pattern": input_elem.get_attribute("pattern") or "",
                    "value": input_elem.get_attribute("value") or ""
                }
                form_info["inputs"].append(input_info)
            
            # Analyze textarea fields
            textareas = form.find_elements(By.TAG_NAME, "textarea")
            for textarea in textareas:
                textarea_info = {
                    "name": textarea.get_attribute("name") or "",
                    "id": textarea.get_attribute("id") or "",
                    "type": "textarea",
                    "placeholder": textarea.get_attribute("placeholder") or "",
                    "required": textarea.get_attribute("required") is not None,
                    "maxlength": textarea.get_attribute("maxlength"),
                    "value": textarea.get_attribute("value") or ""
                }
                form_info["inputs"].append(textarea_info)
            
            # Analyze buttons
            buttons = form.find_elements(By.TAG_NAME, "button") + form.find_elements(By.XPATH, ".//input[@type='submit' or @type='button']")
            for button in buttons:
                button_info = {
                    "name": button.get_attribute("name") or "",
                    "id": button.get_attribute("id") or "",
                    "type": button.get_attribute("type") or "",
                    "value": button.get_attribute("value") or "",
                    "text": button.text or ""
                }
                form_info["buttons"].append(button_info)
            
            forms_info.append(form_info)
            
        return JSONResponse(content={"forms": forms_info})
    except Exception as e:
        return JSONResponse(content={"error": str(e), "forms": []})

@app.get("/detect_validation_mechanisms")
async def detect_validation_mechanisms():
    """Detect client-side validation mechanisms that might interfere with fuzzing"""
    validation_info = {
        "javascript_events": [],
        "validation_patterns": [],
        "required_fields": [],
        "client_side_validations": []
    }
    
    try:
        # Detect JavaScript events on form elements
        form_elements = driver.find_elements(By.XPATH, "//input | //textarea | //select")
        for element in form_elements:
            events_detected = []
            common_events = ['onchange', 'onkeyup', 'onkeydown', 'onblur', 'oninput']
            for event in common_events:
                if element.get_attribute(event):
                    events_detected.append(event)
            
            if events_detected:
                validation_info["javascript_events"].append({
                    "element": element.get_attribute("name") or element.get_attribute("id") or "unnamed",
                    "events": events_detected
                })
            
            # Check for HTML5 validation patterns
            pattern = element.get_attribute("pattern")
            if pattern:
                validation_info["validation_patterns"].append({
                    "element": element.get_attribute("name") or element.get_attribute("id"),
                    "pattern": pattern
                })
            
            # Check for required fields
            if element.get_attribute("required"):
                validation_info["required_fields"].append(
                    element.get_attribute("name") or element.get_attribute("id")
                )
        
        # Look for common validation libraries
        page_source = driver.page_source.lower()
        validation_libraries = ['jquery.validate', 'parsley', 'joi', 'yup', 'formik']
        for lib in validation_libraries:
            if lib in page_source:
                validation_info["client_side_validations"].append(lib)
        
        return JSONResponse(content=validation_info)
    except Exception as e:
        return JSONResponse(content={"error": str(e)})
    
##################################################################
# Hashing Logic Detection Endpoint
##################################################################
# @app.get("/fetch_hashing_logic")
# async def fetch_hashing_logic():


##################################################################
# Encryption Logic Detection Endpoint
##################################################################

@app.get("/fetch_encryption_logic")
async def fetch_encryption_logic():
    """Detect and fetch client-side encryption logic from the current page"""
    try:
        encryption_info = {
            "encryption_functions": [],
            "crypto_libraries": [],
            "encoding_functions": [],
            "suspicious_patterns": [],
            "javascript_sources": []
        }
        
        # JavaScript to extract encryption-related functions and code
        js_extraction_script = """
        const encryptionInfo = {
            encryption_functions: [],
            crypto_libraries: [],
            encoding_functions: [],
            suspicious_patterns: [],
            javascript_sources: []
        };
        
        // Common encryption/crypto keywords to search for
        const encryptKeywords = [
            'encrypt', 'decrypt', 'cipher', 'aes', 'rsa', 'blowfish',
            'crypto', 'cryptojs', 'sjcl', 'forge', 'webcrypto', 'subtle', 'scrypt', 'bcrypt',
            'encr', 'decr'
        ];
        
        // Function to extract function source code
        function getFunctionSource(func) {
            try {
                return func.toString();
            } catch (e) {
                return 'Unable to extract source';
            }
        }
        
        // Search in global window object
        function searchInObject(obj, path = 'window') {
            try {
                for (const key in obj) {
                    if (typeof obj[key] === 'function') {
                        const funcName = key.toLowerCase();
                        const funcSource = getFunctionSource(obj[key]);
                        
                        // Check if function name contains encryption keywords
                        for (const keyword of encryptKeywords) {
                            if (funcName.includes(keyword.toLowerCase())) {
                                encryptionInfo.encryption_functions.push({
                                    name: key,
                                    path: path + '.' + key,
                                    source: funcSource,
                                    keyword_matched: keyword
                                });
                                break;
                            }
                        }
                        
                        // Check if function source contains encryption patterns
                        const sourceLower = funcSource.toLowerCase();
                        for (const keyword of encryptKeywords) {
                            if (sourceLower.includes(keyword)) {
                                encryptionInfo.suspicious_patterns.push({
                                    name: key,
                                    path: path + '.' + key,
                                    source: funcSource,
                                    pattern_found: keyword,
                                    type: 'function_content'
                                });
                                break;
                            }
                        }
                    } else if (typeof obj[key] === 'object' && obj[key] !== null && obj[key] !== window) {
                        // Recursively search in nested objects (limited depth)
                        if (path.split('.').length < 4) {
                            searchInObject(obj[key], path + '.' + key);
                        }
                    }
                }
            } catch (e) {
                // Skip objects that can't be enumerated
            }
        }
        
        // Search for crypto libraries
        const commonCryptoLibs = {
            'CryptoJS': window.CryptoJS,
            'sjcl': window.sjcl,
            'forge': window.forge,
            'crypto': window.crypto,
            'msCrypto': window.msCrypto,
            'webcrypto': window.crypto && window.crypto.subtle,
            'jQuery.md5': window.jQuery && window.jQuery.md5,
            'SparkMD5': window.SparkMD5,
            'JSEncrypt': window.JSEncrypt
        };
        
        for (const [libName, libObj] of Object.entries(commonCryptoLibs)) {
            if (libObj) {
                encryptionInfo.crypto_libraries.push({
                    name: libName,
                    available: true,
                    methods: Object.getOwnPropertyNames(libObj).filter(prop => 
                        typeof libObj[prop] === 'function'
                    ).slice(0, 20) // Limit to first 20 methods
                });
            }
        }
        
        // Search in window object
        searchInObject(window);
        
        // Extract inline script content from DOM
        const scripts = document.querySelectorAll('script');
        scripts.forEach((script, index) => {
            if (script.textContent) {
                const scriptContent = script.textContent;
                const scriptLower = scriptContent.toLowerCase();
                
                // Check for encryption patterns in script content
                for (const keyword of encryptKeywords) {
                    if (scriptLower.includes(keyword)) {
                        encryptionInfo.javascript_sources.push({
                            script_index: index,
                            src: script.src || 'inline',
                            content_snippet: scriptContent.substring(0, 1000), // First 1000 chars
                            keyword_found: keyword,
                            full_content: scriptContent.length > 1000 ? '[Truncated]' : scriptContent
                        });
                        break;
                    }
                }
            }
        });
        
        // Check for common hash/encoding functions
       // const hashFunctions = ['btoa', 'atob', 'encodeURIComponent', 'decodeURIComponent'];
       // hashFunctions.forEach(funcName => {
         //   if (window[funcName]) {
           //     encryptionInfo.encoding_functions.push({
       //             name: funcName,
         //           available: true,
           //         source: getFunctionSource(window[funcName])
             //   });
     //       }
       // });
        
        return encryptionInfo;
        """
        
        # Execute the JavaScript extraction script
        encryption_data = driver.execute_script(js_extraction_script)
        
        # Additional server-side analysis of page source
        page_source = driver.page_source.lower()
        
        # Search for encryption-related patterns in HTML/JS
        encryption_patterns = {
            'base64_patterns': [],
            'hex_patterns': [],
            'crypto_constants': [],
            'key_variables': []
        }
        
        import re
        
        # Look for Base64 patterns
        base64_pattern = r'[A-Za-z0-9+/]{20,}={0,2}'
        base64_matches = re.findall(base64_pattern, driver.page_source)
        encryption_patterns['base64_patterns'] = base64_matches[:10]  # Limit to first 10
        
        # Look for hex patterns (common in crypto)
        hex_pattern = r'[0-9a-fA-F]{32,}'
        hex_matches = re.findall(hex_pattern, driver.page_source)
        encryption_patterns['hex_patterns'] = hex_matches[:10]  # Limit to first 10
        
        # Look for common crypto variable names
        crypto_var_patterns = [
            r'var\s+(\w*key\w*)\s*=',
            r'var\s+(\w*secret\w*)\s*=',
            r'var\s+(\w*salt\w*)\s*=',
            r'var\s+(\w*iv\w*)\s*=',
            r'var\s+(\w*cipher\w*)\s*='
        ]
        
        for pattern in crypto_var_patterns:
            matches = re.findall(pattern, driver.page_source, re.IGNORECASE)
            encryption_patterns['key_variables'].extend(matches)
        
        # Analyze network requests for encryption endpoints
        network_crypto_endpoints = []
        if hasattr(driver, 'requests'):
            for request in driver.requests[-50:]:  # Check last 50 requests
                url_lower = request.url.lower()
                if any(keyword in url_lower for keyword in ['encrypt', 'decrypt', 'crypto', 'auth', 'token']):
                    network_crypto_endpoints.append({
                        'url': request.url,
                        'method': request.method,
                        'status_code': request.response.status_code if request.response else None
                    })
        
        # Combine all findings
        final_result = {
            'client_side_analysis': encryption_data,
            'pattern_analysis': encryption_patterns,
            'network_endpoints': network_crypto_endpoints,
            'summary': {
                'crypto_functions_found': len(encryption_data.get('encryption_functions', [])),
                'crypto_libraries_detected': len(encryption_data.get('crypto_libraries', [])),
                'suspicious_patterns': len(encryption_data.get('suspicious_patterns', [])),
                'javascript_sources_with_crypto': len(encryption_data.get('javascript_sources', [])),
                'base64_patterns_found': len(encryption_patterns['base64_patterns']),
                'hex_patterns_found': len(encryption_patterns['hex_patterns']),
                'crypto_variables_found': len(encryption_patterns['key_variables']),
                'network_crypto_endpoints': len(network_crypto_endpoints)
            },
            'recommendations': []
        }
        
        # Generate recommendations based on findings
        if encryption_data.get('crypto_libraries'):
            final_result['recommendations'].append("Crypto libraries detected - analyze for weak implementations")
        
        if encryption_data.get('encryption_functions'):
            final_result['recommendations'].append("Custom encryption functions found - review for vulnerabilities")
        
        if encryption_patterns['base64_patterns']:
            final_result['recommendations'].append("Base64 encoded data found - check for sensitive information")
        
        if network_crypto_endpoints:
            final_result['recommendations'].append("Crypto-related network endpoints detected - test for vulnerabilities")
        
        if not encryption_data.get('crypto_libraries') and not encryption_data.get('encryption_functions'):
            final_result['recommendations'].append("No obvious client-side encryption detected - data may be transmitted in plaintext")
        
        return JSONResponse(content=final_result)
        
    except Exception as e:
        return JSONResponse(content={
            "error": str(e),
            "client_side_analysis": {},
            "pattern_analysis": {},
            "network_endpoints": [],
            "summary": {}
        })

##################################################################
# Additional Helper Endpoint for Deep Encryption Analysis
##################################################################

@app.post("/analyze_specific_function")
async def analyze_specific_function(function_name: str):
    """Analyze a specific JavaScript function for encryption patterns"""
    try:
        #function_name = function_data.get("function_name")
        #if not function_name:
        #    return JSONResponse(content={"error": "Function name required"})
        
        # JavaScript to get detailed function analysis
        analysis_script = f"""
        const funcName = '{function_name}';
        const analysis = {{
            exists: false,
            source: '',
            calls_made: [],
            dependencies: [],
            parameters: [],
            return_analysis: ''
        }};
        
        try {{
            const func = eval(funcName);
            if (typeof func === 'function') {{
                analysis.exists = true;
                analysis.source = func.toString();
                
                // Extract parameters
                const paramMatch = analysis.source.match(/function[^\\(]*\\(([^\\)]*)\\)/);
                if (paramMatch) {{
                    analysis.parameters = paramMatch[1].split(',').map(p => p.trim()).filter(p => p);
                }}
                
                // Look for function calls within the source
                const callPattern = /\\b([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\\(/g;
                let match;
                const calls = new Set();
                while ((match = callPattern.exec(analysis.source)) !== null) {{
                    calls.add(match[1]);
                }}
                analysis.calls_made = Array.from(calls);
            }}
        }} catch (e) {{
            analysis.error = e.message;
        }}
        
        return analysis;
        """
        function_analysis = driver.execute_script(analysis_script)
        # Additional static analysis
        if function_analysis.get('source'):
            source = function_analysis['source'].lower()
            crypto_indicators = {
                'encryption_keywords': [],
                'crypto_operations': [],
                'security_concerns': []
            }
            
            # Check for encryption keywords
            keywords = ['encrypt', 'decrypt', 'cipher', 'key', 'salt', 'iv', 'aes', 'rsa']
            for keyword in keywords:
                if keyword in source:
                    crypto_indicators['encryption_keywords'].append(keyword)
            
            # Check for crypto operations
            operations = ['btoa', 'atob', 'crypto.', 'cryptojs', 'math.random', 'date.now']
            for op in operations:
                if op in source:
                    crypto_indicators['crypto_operations'].append(op)
            
            # Security concerns
            if 'math.random' in source:
                crypto_indicators['security_concerns'].append('Uses Math.random() - not cryptographically secure')
            
            if 'date.now' in source:
                crypto_indicators['security_concerns'].append('Uses Date.now() - potentially predictable')
            
            function_analysis['crypto_analysis'] = crypto_indicators
        
        return JSONResponse(content=function_analysis)
        
    except Exception as e:
        return JSONResponse(content={"error": str(e)})

# MCP Server Launcher (as callable module)
def start_mcp_data_handler_server():
    print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}MCP data handler running at http://localhost:9011\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    uvicorn.run(app, host="0.0.0.0", port=9011, log_level="error")