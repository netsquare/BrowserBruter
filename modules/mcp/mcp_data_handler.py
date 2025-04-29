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
"""
    return JSONResponse(content={"switches": data})

# MCP Server Launcher (as callable module)
def start_mcp_data_handler_server():
    print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}MCP data handler running at http://localhost:9011\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    uvicorn.run(app, host="0.0.0.0", port=9011, log_level="error")