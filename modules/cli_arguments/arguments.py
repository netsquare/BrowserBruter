##################################################################
"""
Name  : arguments.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
import argparse

def get_arguments():
    ##################################################################
    # Getting argument parser to parse and process arguments
    ##################################################################
    argParser = argparse.ArgumentParser(description="BrowserBruter is a python3 script, utilizing power of selenium and selenium-wire to automate fuzzing of various input fields of webpages to test their security against malicious inputs. For contact and more information about project please visit https://github.com/netsquare/BrowserBruter",formatter_class=argparse.RawTextHelpFormatter)

    ##################################################################
    # Adding various command line arguments groups
    ##################################################################
    args_basic = argParser.add_argument_group("Basic") # argument group to hold basic options 
    args_attack1n2 = argParser.add_argument_group("Sniper and Battering Ram") # argument group to hold elements and payloads related options for sniper and battering ram
    args_attack3n4 = argParser.add_argument_group("PitchFork and Cluster Bomb") # argument group to hold elements and payloads related options for pitchfork and cluster bomb
    args_fuzz = argParser.add_argument_group("Fuzzing Options") # argument group to hold options related to fuzzing 
    args_debug = argParser.add_argument_group("Fuzzing via Debugging Options") # argument group to hold options related to debugging module
    args_session = argParser.add_argument_group("Session") # argument group to hold options related to options
    args_python = argParser.add_argument_group("Python Scripting Engine") # argument group to hold options related to python scripting engine
    args_javascript = argParser.add_argument_group("JavaScript Code Handler") # argument group to hold options related to javascript and navigation and handling
    #args_navigation = argParser.add_argument_group("Navigation Handling")
    args_automatic_navigation = argParser.add_argument_group("Automatic Navigation Handler")
    args_input_validation = argParser.add_argument_group("Anti Input Validation")
    args_browser = argParser.add_argument_group("Browser Options") # argument group to hold options related to browser options
    args_verbose = argParser.add_argument_group("Verbose Option") # argument group to hold options related to debug options
    args_report = argParser.add_argument_group("Report Generation") # argument group to hold options related to report generations
    args_gui = argParser.add_argument_group("GUI") # argument group to hold the options for gui related things.
    args_help = argParser.add_argument_group("Help") # argument group to hold options related to help

    ##################################################################
    # Adding the command line arguments
    ##################################################################
    args_basic.add_argument("-t", "--target",help="Target's url: https://zinja-coder.github.io/", metavar="TARGET_URL", type=str)
    args_basic.add_argument("-b", "--button",help="Button element which will submit form data.", metavar="submit", type=str)
    args_basic.add_argument("-a","--attack",help="The attack mode:\n 1. SNIPER\n 2. BATTERING RAM\n 3. PITCH FORK\n 4. CLUSTER BOMB",type=int,metavar="2")
    args_attack1n2.add_argument("-e", "--elements", help="Input fields(target elements of form) in comma separated values.", metavar="username,password,phone,address,projectId++formcontrolname", type=str)
    args_attack3n4.add_argument("-ep", "--elements-payloads",help="Input fields(target elements of form) and their respective payloads files.", metavar="FIELD:/PATH/TO/FILE,textarea:payloads.txt,data:pay.txt", type=str)
    args_attack1n2.add_argument("-p", "--payloads",help="/path/to/payload/file.", metavar="/home/payloads.txt", type=str)
    args_fuzz.add_argument("--fill",help="Auto fill the specified elements, usefull when web page is complex when you want to target specific fields only.",metavar="e1,elemn3,user,npass,id", type=str)
    args_fuzz.add_argument("--fill-values", help="[Optional] Path to User provided elements values file. See sample-file-for-giving-form-values.json", metavar="/path/to/file.json", type=str)
    args_fuzz.add_argument("--buttons-to-press-before-fuzz",help="Supply list of buttons to be pressed in sequence before filling the form, useful if form submission requires some action or form is invisible until some button is pressed.[Note if the button is not pressable elment, then use --javascript and suppy javascript to click the element.]",metavar="visibleform,ok,confirm,pressthis", type=str)
    args_fuzz.add_argument("--press-enter-no-click",help="This switch will force the Browser Bruter to send ENTER key instead of clicking the button, useful when form is submitted when pressing entering on text field and there are no buttons to click.", action="store_true")
    args_fuzz.add_argument("--delay-before",help="Delay before fuzz attempt.",metavar="0.2", type=float, default=0.2)
    args_fuzz.add_argument("--delay-after",help="Delay after fuzz attempt.",metavar="0.2", type=float, default=0.2)
    args_fuzz.add_argument("--threads",help="Specifies number of browsers instances to be run, max value is 20, default is 1, lower the instances slower and stable the fuzzing process, more instances - faster and unstable fuzzing process. Note: The higher amount of threads consumes more system resources.",metavar="3",default=1, type=int)
    args_fuzz.add_argument("--pause", help="Pause the BrowserBruter instances on startup, press ENTER to resume.",action="store_true",default=False)
    args_fuzz.add_argument("--interactive",help="Pause the BrowserBruter before fuzzing any element at each payload and wait for user to continue.",action="store_true",default=False)
    args_fuzz.add_argument("--pause-after-submit",help="Pause the script after pressing the submit button to allow pentester to interact with the web application.",action="store_true")
    args_fuzz.add_argument("--reload-page",help="This switch tells The Browser Bruter to reload the page before fuzzing the form on each iteration, usefull when result of previous iteration causes the web elements to disappear or which leads to elements not found error, in such case this switch helps to keep browser bruter running.", action="store_true")
    args_fuzz.add_argument("--no-reload-page",help="This switch will force the Browser Bruter to not go back to --target URL, instead stay on the same page after submitting the form.", action="store_true", default=False)
    args_fuzz.add_argument("--form",help="Specy id,name,class of form to fuzz in case of muliple forms",metavar="changePasswordForm", type=str)
    args_debug.add_argument("--debug",help="use this to set debug point on the browser", type=str)
    args_debug.add_argument("--debug-code",help="when debug hits, execute this code", type=str)
    args_debug.add_argument("--property",help="COMING SOON....", type=str)
    args_fuzz.add_argument("--pause-on-popup",help="Pauses the Browser Bruter in case of pop up occurs, help full when finding Cross Site Scripting and need to perform manual actions",action="store_true",default=False)
    args_session.add_argument("--headers", help="Comma-separated list of custom headers.",metavar="\"Auth: 123\",\"CUSTOM_HEADER: VALUE\"", type=str)
    args_session.add_argument("--cookie",help="Use it to define cookies to be used while sending initial request, cookies should be in name:value:domain comma separated format.", metavar="name:value,name2:value2", type=str)
    args_session.add_argument("--force-cookie",help="Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server.",action="store_true")
    args_session.add_argument("--remove-session",help="Use this switch to remove session data and cookies after each request-response cycle.", action="store_true")
    args_session.add_argument("--add-storage",help="Use this switch to add local storage in browser as a key:value pair.", metavar="key:value++key2:value2", type=str)
    args_session.add_argument("--add-session-storage",help="Use this switch to add session storage in browser as a key:value pair.", metavar="key:value++key2:value2", type=str)
    args_session.add_argument("--force-storage",help="This switch will prevent overriding of data set using --add-storage option by web application.",action="store_true",default=False)
    args_session.add_argument("--force-session-storage",help="This switch will prevent overriding of data set using --add-session-storage option by web application.",action="store_true",default=False)
    args_python.add_argument("--python",help="Executes provided python code.", type=str)
    args_python.add_argument("--python-after",help="Executes provided python code after single fuzzing attempt of form.", type=str)
    args_python.add_argument("--python-file",help="Reads and Executes provided python code from file.", type=str)
    args_python.add_argument("--python-request",help="Python code which will modify the HTTP Request.", type=str)
    args_python.add_argument("--python-request-file",help="File containing python code to manipulate HTTP Request.", type=str)
    args_python.add_argument("--python-response",help="Python code to manipulate HTTP Response.", type=str)
    args_python.add_argument("--python-response-file",help="File containing python code to manipulate HTTP response.", type=str)
    args_automatic_navigation.add_argument("--record-navigation",help="This option will let user record their mouse clicks and keyboard key strokes, which can be replicated to navigate around the web page.", action="store_true", default=False)
    args_automatic_navigation.add_argument("--load-navigation-before",help="This switch will load the previously recorded navigation and will replicate it to automatically do the navigation around the web page.", metavar="/path/to/navigation/file.json", type=str)
    args_automatic_navigation.add_argument("--load-navigation-after",help="This switch will load the previously recorded navigation and will replicate it to automatically do the navigation around the web page after submitting the form.", metavar="/path/to/navigation/file.json", type=str)
    args_input_validation.add_argument("--auto-remove-javascript-validation",help="This switch will tell The Browser-Bruter to not remove common javascript input validations mechanisms. Useful if removing of javacript validaiton breaks the web app.", action="store_true",default=False)
    args_input_validation.add_argument("--disable-events", help="Disables specified javascript events, for example onClick, etc. Provide comma separated list of events.", metavar="keypress,keydown,change,keyup", type=str)
    args_input_validation.add_argument("--remove-class",help="Provide a list of elements from which you want to remove the class attribute, extremely useful when element is linked to some class with extreme javascript input validation or makes the element not interactable, you can still select this element by providing it's class name.", metavar="cdk-text-field-autofill-monitored", type=str)
    args_javascript.add_argument("--javascript",help="Javascript code to run on browser", metavar="\"alert(1);\"", type=str)
    args_javascript.add_argument("--javascript-after",help="Javascript code to run on browser after pressing and submitting the button.", type=str)
    args_javascript.add_argument("--javascript-file",help="Javascript file containing javascript code to execute", metavar="/path/to/javascript/file.js", type=str)
    args_input_validation.add_argument("--replace-code",help="Replaces the code in response body with the code provided by user in following format - \"CODE_TO_REPLACE1\"::\"REPLACEMENT_CODE1\"+++\"CODE_TO_REPLACE2\"::\"REPLACEMENT_CODE2\"",metavar="\"alert(1);\"::\"alert(0);\"", type=str)
    args_input_validation.add_argument("--replace-files", help="Replace the content of a file in HTTP responses.", metavar="/path/to/validation_file.js", type=str)
    args_browser.add_argument("--chrome-binary",help="Use this switch to provide your local/custom chrome browser.", metavar="/path/to/chrome", type=str)
    args_browser.add_argument("--chrome-driver",help="Use this switch to use your local/custom chromedriver.", metavar="/path/to/chromedriver", type=str)
    args_browser.add_argument("--headless",help="Use this switch to run browser in headless mode (No GUI).", action="store_true")
    args_browser.add_argument("--no-css",help="This switch will tell Browser Bruter to drop the requests to .css files and it will not load .css files and remove <style> tag.",action="store_true")
    args_browser.add_argument("--proxy",help="Set proxy for traffic, for example give IP:PORT of Burpsuite to send traffic to burpsuite.",metavar="http://proxyaddress:port/", type=str)
    args_browser.add_argument("--remove-images",help="This switch tells BrowserBruter not to load audio, video and image (.png, .img, .ico, .mp4, .gif, .mp3 etc) files. By default it loads these files.",action="store_true",default=False)
    args_browser.add_argument("--chrome-options",help="Custom comma separated list of options which will be passed to chrome. [This will override in-built options in Browser-Bruter that are passed to chrome]",metavar="blink-settings=imagesEnabled=false,disable-notifications", type=str)
    args_browser.add_argument("--anti-bot",help="This switch tells BrowserBruter to use avoid any chrome options and use raw undetected chrome driver to avoid bot detection, by default Browser-Bruter uses custom Chrome options along with undetected chrome driver like disabling xss protection along with undeteced chrome driver",action="store_true",default=False)
    args_browser.add_argument("--no-anti-bot",help="Completely removes any anti bot detection evasions.",action="store_true",default=False)
    args_browser.add_argument("--new-instance",help="Start new fresh instance of browser for each new payload [Fuzzing process's iteration] usefull in bypassing the invisible captchas.",action="store_true")
    args_report.add_argument("--rows-limit",help="Specify the number of rows to be included in single file, if not specified, a single report will be generated, if specified, multiple reports with specified rows amount will be generated, useful when test consists of thousands of payloads.", type=int, metavar="200")
    args_report.add_argument("--scope",help="Comma separated list of hostnames in scope",metavar="api1.example.com,bak.example.com", type=str)
    args_report.add_argument("--inscope-urls",help="Comma-separated list of urls or file containing urls in-scope", metavar="/path/to/file OR \"https://api1.example.com/v2/getData\",\"https://bak.example.com/v2/signin\"", type=str)
    args_report.add_argument("--outofscope-urls",help="Comma separated list of urls or file containing urls which are to be excluded from final report", metavar="/path/to/file OR \"http://10.13.37.3:8080/webgoat/service/hint.mvc\",\"http://10.13.37.3:8080/webgoat/service/solution.mvc\"", type=str)
    args_verbose.add_argument("--verbose",help="Use this switch to enable HTTP request/response output being printed on console and STDLOG file.", action="store_true",default=False)
    args_verbose.add_argument("--print-error",help="Use this switch to print the Stack Trace messages in case of the error! and keep the logs in log file.",action="store_true")
    args_gui.add_argument("--gui",help="Use this switch to run Browser Bruter in GUI",action="store_true",default=False)
    args_help.add_argument("--help-manual",help="Print the Usage Examples",action="store_true")

    # Getting the arguments in args variable
    args = argParser.parse_args()
    # Return the args object containing all the arguments
    return args
