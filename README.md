# The Browser-Bruter

```shell
###############################################################################################################################
###############################################################################################################################                                                             
###                                                                                                                         ###                                                             
### ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░  ###                                                             
### ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗  ###                                                             
### ██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝  ###                                                             
### ██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗  ###                                                             
### ██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║  ###                                                             
### ╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ###                                                             
###                                                                                   by Jafar Pathan(@github/zinja-coder)  ###                                                             
###                                                                                                                         ###                                                             
###                                                                                                                         ###                                                             
###                        The First-Ever Advance Browser Based Automated Web Form Fuzzing Tool                             ###                                                             
###                        Version:  v2024.3                                                                              ###                                                             
###                        Github :  https://github.com/netsquare/BrowserBruter                                             ###                                                             
###                                                                                                                         ###                                                             
###             ..,:dOkxl:.                                                                                                 ###                                                             
###         .,coooooooooooooc,.                                                                                             ###                                                             
###      .,lllllllllllllllllllll,.                                                                                          ###                                                             
###     ;ccccccccccccccccccccccccc;                                                                                         ###                                                             
###   'ccccccccccccccccccccccccccccc.                                                                                       ###                                                             
###  ,ooc::::::::okO0000OOkkkkkkkkkkk:                _____                                                                 ###                                                             
### .ooool;;;;:xK0kxxxxxk0XK0000000000.            .':::::::'.                                                              ###                                                             
### :oooool;,;OKdddddddddddKX000000000d       ___ /:::::::::::\____ _            _.''_                                      ###                                                             
### lllllool;lNdllllllllllldNK000000000    /||   ||`.______.-`||   | |\_\\\\____/_ _.-'\\\\-- -- -- -- -- --                ###                                                             
### llllllllloMdcccccccccccoWK000000000.|-| ||===||           ||===| ||_||||____|_| .-'|||||-- -- -- -- -- --               ###                                                             
### ;cllllllllXXc:::::::::c0X000000000d'|-| ||===||===========||===| ||_||||____|_|`-._|||||-- -- -- -- -- --               ###                                                             
### .ccccllllllONkc;,,,;cxKK0000000000.    \||___||___________||___|_|/ ////   ##  `-._////-- -- -- -- -- --                ###                                                             
### .cccccclllllxOOOOOOkxO0000000000;          )  _____  (                     ##                                           ###                                                             
###   .:cccccccclllllllloO0000000OOO,          / .'| (  '. \                   ##                                           ###                                                             
###     ,:ccccccccclllcd0000OOOOOOl.          (  './    )   )                  ##                                           ###                                                             
###       '::cccccccccdOOOOOOOkx:.             \ '._____.' /                   ##                                           ###                                                             
###         ..,::ccccxOOOkkko;.                 '._______.'                    ##                                           ###                                                             
###             ..,:dOkxl:.                                                    ##                                           ###                                                             
###           ###############                                                  ##                                           ###                                                             
###          #################                                                ####                                          ###                                                             
###         ###################                                              ######                                         ###                                                             
###############################################################################################################################                                                             
###############################################################################################################################   
```

**The Browser-Bruter** is first ever browser based automated web pentesting tool for fuzzing **web forms** by controlling the browser it self. It automates the process of sending **payloads** to input fields of browser and sends them too server. It completely **bypasses** the need of breaking the **encryption** in order to fuzz and insert payloads in BurpSuite scanner and intruder. After fuzzing it generates a **comprehensive report** including all the data and result of the pentest along with HTTP traffic, this report can be viewed by **The Report-Explorer** tool which comes with The Browser-Bruter.

**Handcrafted in India 🇮🇳**

## Table of Contents

- [The Browser-Bruter](#the-browser-bruter)
  - [Table of Contents](#table-of-contents)
  - [What it does](#what-it-does)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Options](#options)
    - [Usage Examples](#usage-examples)
- [The Report-Explorer](#the-report-explorer)
  - [Features](#features-1)
  - [Usage](#usage-1)
    - [Options](#options-1)
    - [Usage Examples](#usage-examples-1)
  - [Contributing](#contributing)
  - [License](#license)

## What it does

- Allows Pentester to fuzz the web application forms when the HTTP body (or part of body) is encrypted making HTTP proxy tools like ZAP and BurpSuite unable to insert payloads in such traffic.
- Creates a way to tackle front end captchas by allowing pentester to manually perform the required human interactions and then proceed to payload insertions.
- Can fuzz front-end when there is no HTTP traffic, for example when Input is utilized on client side, i.e. when you want to bruteforce OTP input which is validated on client side, so there is no HTTP Traffic.
- Removes burden of session management and auth handling while using HTTP proxy tools.

## Features

- Perform Intruder attacks on Browser including:
  - Sniper
  - Battering Ram
  - Pitch Fork
  - Cluster Bomb. 
- Automatically removes front-end HTML input validations.
- Tries its best to automatically remove front-end Javascript input validations.
- Stealthy, evades bot detection.
- Rich session handling mechanism.
- Completely bypasses encryption protections.
- Solution for captchas and invisible captchas.
- Bit-to-Bit log keeping and report generating.
- Professional pentest report generation and report exploration tool to analyse and identify vulnerabilities found during pentesting.
- Tracking of processed payloads progress.
- Can run upto 5 threads increasing fuzzing speed.
- Can take and execute custom javascript code.
- Replace/Modify frontend code on the fly.
- Rich target scope handling mechanism.
- Route traffic to BurpSuite proxy.
- Highly customizable with thousands of possibilities.
- Robust handling of crashes so no testing record is lost

## Prerequisites

Before using BrowserBruter, make sure you have the following prerequisites installed:

- **Python 3**: The tool is written in Python, so you need Python 3 installed.

## Installation

1. Download and install Python3
2. Download the latest release from releases.


## Usage
### Options
   
Navigate to the BrowserBruter executable directory.

Run the executable along with following options:

```
usage: BrowserBruter.py [-h] [--target TARGET_URL] [--button submit] [--attack 2] [--elements username,password,phone,address]
                        [--elements-payloads FIELD:/PATH/TO/FILE,textarea:payloads.txt,data:pay.txt] [--payloads /home/payloads.txt] [--fill e1,elemn3,user,npass,id]
                        [--fill-values /path/to/file.json] [--buttons-to-press-before-fuzz visibleform,ok,confirm,pressthis] [--press-enter-no-click] [--proxy http://proxyaddress:port/]
                        [--delay-before 0.2] [--delay-after 0.2] [--threads 3] [--pause] [--interactive] [--pause-after-submit] [--reload-page] [--form changePasswordForm]
                        [--ignore-popups] [--remove-class cdk-text-field-autofill-monitored] [--headers "Auth: 123","CUSTOME_HEADER: VALUE"] [--cookie name:value,name2:value2]
                        [--force-cookie] [--remove-session] [--auto-remove-javascript-validation] [--javascript "alert(1);"] [--javascript-after JAVASCRIPT_AFTER]
                        [--javascript-file /path/to/javascript/file.js] [--replace-code "alert(1);","alert(0);"] [--replace-files /path/to/validation_file.js] [--headless] [--no-css]
                        [--load-static-media] [--chrome-options blink-settings=imagesEnabled=false,disable-notifications] [--anti-bot] [--no-anti-bot] [--new-instance] [--rows-limit 200]
                        [--scope api1.example.com,bak.example.com] [--include-urls /path/to/file OR "https://api1.example.com/v2/getData","https://bak.example.com/v2/signin"]
                        [--exclude-urls /path/to/file OR "http://10.13.37.3:8080/webgoat/service/hint.mvc","http://10.13.37.3:8080/webgoat/service/solution.mvc"] [--verbose] [--debug]
                        [--help-manual]
options:
  -h, --help            show this help message and exit

Basic:
  --target TARGET_URL   Target's url: https://zinja-coder.github.io/jafarpathan
  --button submit       Button element which will submit form data.
  --attack 2            The attack mode:
                         1. SNIPER
                         2. BATTERING RAM
                         3. PITCH FORK
                         4. CLUSTER BOMB

Sniper and Battering Ram:
  --elements username,password,phone,address
                        Input fields(target elements of form) in comma separated values.
  --payloads /home/payloads.txt
                        /path/to/payload/file.

PitchFork and Cluster Bomb:
  --elements-payloads FIELD:/PATH/TO/FILE,textarea:payloads.txt,data:pay.txt
                        Input fields(target elements of form) and their respective payloads files.

Fuzzing and Browser Options:
  --fill e1,elemn3,user,npass,id
                        Auto fill the specified elements, usefull when web page is complex when you want to target specific fields only.
  --fill-values /path/to/file.json
                        [Optional] Path to User provided elements values file. See sample-file-for-giving-form-values.json
  --buttons-to-press-before-fuzz visibleform,ok,confirm,pressthis
                        Supply list of buttons to be pressed in sequence before filling the form, useful if form submission requires some action or form is invisible until some button is pressed.[Note if the button is not pressable elment, then use --javascript and suppy javascript to click the element.]
  --press-enter-no-click
                        This switch will force the Browser Bruter to send ENTER key instead of clicking the button, useful when form is submitted when pressing entering on text field and there are no buttons to click.
  --proxy http://proxyaddress:port/
                        Set proxy for traffic, for example give IP:PORT of Burpsuite to send traffic to burpsuite.
  --delay-before 0.2    Delay before fuzz attempt.
  --delay-after 0.2     Delay after fuzz attempt.
  --threads 3           Specifies number of browsers instances to be run, max value is 5, default is 1, lower the instances slower the fuzzing process, more instances - faster fuzzing process.
  --pause               Pause the BrowserBruter instances on startup, press ENTER to resume.
  --interactive         Pause the BrowserBruter before fuzzing any element at each payload and wait for user to continue.
  --pause-after-submit  Pause the script after pressing the submit button to allow pentester to interact with the web application.
  --reload-page         This switch tells The Browser Bruter to reload the page before fuzzing the form on each iteration, usefull when result of previous iteration causes the web elements to disappear or which leads to elements not found error, in such case this switch helps to keep browser bruter running.
  --form changePasswordForm
                        Specy id,name,class of form to fuzz in case of muliple forms
  --ignore-popups       Ignore alert and other pop up menus
  --remove-class cdk-text-field-autofill-monitored
                        Provide a list of elements from which you want to remove the class attribute, extremely useful when element is linked to some class with extreme javascript input validation or makes the element not interactable, you can still select this element by providing it's class name.

Session:
  --headers "Auth: 123","CUSTOME_HEADER: VALUE"
                        Comma-separated list of custom headers.
  --cookie name:value,name2:value2
                        Use it to define cookies to be used while sending initial request, cookies should be in name:value:domain comma separated format.
  --force-cookie        Use this switch to force setting of cookies given as argument using --cookie flag regardless of cookies being sent by server.
  --remove-session      Use this switch to remove session data and cookies after each request-response cycle.

JavaScript and Code Handling:
  --auto-remove-javascript-validation
                        This switch will tell The Browser-Bruter to not remove common javascript input validations mechanisms. Useful if removing of javacript validaiton breaks the web app.
  --javascript "alert(1);"
                        Javascript code to run on browser
  --javascript-after JAVASCRIPT_AFTER
                        Javascriptc code to run on browser after pressing and submitting the button.
  --javascript-file /path/to/javascript/file.js
                        Javascritp file containing javascript code to execute
  --replace-code "alert(1);","alert(0);"
                        Replaces the code in response body with the code provided by user in following format - "CODE_TO_REPLACE1","REPLACEMENT_CODE1","CODE_TO_REPLACE2","REPLACEMENT_CODE2"
  --replace-files /path/to/validation_file.js
                        Replace the content of a file in HTTP responses.

Browser Options:
  --headless            Use this switch to run browser in headless mode (No GUI).
  --no-css              This switch will tell Browser Bruter to drop the requests to .css files and it will load .css files
  --load-static-media   This switch tells BrowserBruter to load audio, video and image (.png, .img, .ico, .mp4, .gif, .mp3 etc) files. By default it discards these files to save time and load pages faster.
  --chrome-options blink-settings=imagesEnabled=false,disable-notifications
                        Custom comma separated list of options which will be passed to chrome. [This will override in-built options in Browser-Bruter that are passed to chrome]
  --anti-bot            This switch tells BrowserBruter to use avoid any chrome options and use raw undetected chrome driver to avoid bot detection, by default Browser-Bruter uses custom Chrome options along with undetected chrome driver like disabling xss protection along with undeteced chrome driver
  --no-anti-bot         Completely removes any anti bot detection evasions.
  --new-instance        Start new fresh instance of browser for each new payload [Fuzzing process's iteration] usefull in bypassing the invisible captchas.

Debug Option:
  --verbose             Use this switch to enable HTTP request/response output being printed on console and STDLOG file.
  --debug               Use this switch to print the Stack Trace messages in case of the error! and keep the logs in log file.

Report Generation:
  --rows-limit 200      Specify the number of rows to be included in single file, if not specified, a single report will be generated, if specified, multiple reports with specified rows amount will be generated, useful when test consists of thousands of payloads.
  --scope api1.example.com,bak.example.com
                        Comma separated list of hostnames in scope
  --include-urls /path/to/file OR "https://api1.example.com/v2/getData","https://bak.example.com/v2/signin"
                        Comma-separated list of urls or file containing urls in-scope
  --exclude-urls /path/to/file OR "http://10.13.37.3:8080/webgoat/service/hint.mvc","http://10.13.37.3:8080/webgoat/service/solution.mvc"
                        Comma separated list of urls or file containing urls which are to be excluded from final report

Help:
  --help-manual         Print the Usage Exapmles

```

### Usage Examples

BrowserBruter offers thousands of possibilities to tackle various scenarios, following are a list of just few:

```
Usage Examples:
    1. Perform Bruteforce(ClusterBomb) on login page:
        python3 BrowserBruter.py --elements-payloads username:username.txt,password:passwords.txt --target http://localhost/login.php --button Login --attack 4 --remove-session

    2. Perform PitchFork on login page:
        python3 BrowserBruter.py --elements-payloads username:username.txt,password:passwords.txt --target http://localhost/login.php --button Login --attack 3

    3. Perform BatteringRam on login page:
        python3 BrowserBruter.py --elements username,password --payloads sqli.txt --target http://localhost/login.php --button Login --verbose --attack 2

    4. Fuzz on login page and make it verbose:
        python3 BrowserBruter.py --elements username,password --fill username,password --payloads sqli.txt --target http://localhost/login.php --button Login --verbose --attack 1

    5. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint':
        python3 BrowserBruter.py --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --attack 1

    6. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request becuase the initial cookies might be overridden by new cookies values:
        python3 BrowserBruter.py --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --attack 1

    7. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle [this is useful against Authentication pages when you don't want redirection in case of successful login]:
        python3 BrowserBruter.py --elements name,age,address,phone --fill name,age,address,phone --payloads payloads.txt --target http://localhost/register --button register --cookie difficulty:high,hint:no --force-cookie --remove-session --attack 1

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
        python3 BrowserBruter.py --elements selectElement --payloads payloads.txt --target http://localhost/selection --button submit --attack 1
    
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
        python3 BrowserBruter.py --elements username,password --fill username,password --button login --target http://localhost/login --payloads payloads.txt --replace-code "return false","return true","alert(0)","alert(1)" --javascript "var elmnt = document.getElementById('ClickMe'); elmnt.click();" --attack 1
    
    23. Replace bunch of javascript code into return true:
        python3 BrowserBruter.py --elements-payloads textarea:sqli.txt,data:sqli.txt --button submit --target http://localhost:3000/index.html --attack 3 --replace-code "return false","return true","return regex.test(dateString)","return true","return regex.test(timeString)","return true","return regex.test(colorString)","return true"

    24. Fuzz the search box, when user have to press enter to submit the search query, the user has to click on search icon to make search box appear:
        python3 BrowserBruter.py --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click                                                                                                                                                                             
    
    25. Tell Browser Bruter to remove commong javascript input validation:
        python3 BrowserBruter.py --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --auto-remove-javascript-validation                                                                                                                                         
        
    26. Tell Browser Bruter to ignore pop ups like alert() box:
        python3 BrowserBruter.py --elements search-bar --button search-bar --attack 1 --target http://localhost:3000/#/ --payloads fuzz.txt --buttons-to-press-before-fuzz searchQuery --press-enter-no-click --auto-remove-javascript-validation --ignore-popups                                                                                                                         

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

    32. Route traffic via proxy i.e. BurpSuite and load the static media like images:
        python3 BrowserBruter.py --proxy http://127.0.0.1:8080/ --elements textarea,select,yesno,hobbies,phone,data,time,calendar,color --fill textarea,select,yesno,hobbies,phone,data,time,calendar,color --button submit --payloads payloads.txt --target http://localhost:3000/ --attack 1 --load-static-media

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
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --exclude-urls "http://localhost/webgoat/service/solution.mvc","http://localhost/webgoat/service/lessonprogress.mvc","http://localhost/webgoat/service/lessonmenu.mvc","http://localhost/webgoat/service/solution.mvc"
        
        OR -> Providing list of urls:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --exclude-urls urls.txt

    42. Including only specific urls in final report:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --include-urls "http://localhost/webgoat/attack?Screen=1869022003&menu=100"

        OR -> Prvoding file containing URLs:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/1869022003/100 --elements person --payloads fuzz.txt --button SUBMIT --attack 1 --include-urls urls.txt

    43. Force reload the page before fuzzing the form on each iteration, usefull when result of previous iteration causes the web elements to disappear or which leads to elements not found error, in such case this switch helps to keep browser bruter running:
        python3 BrowserBruter.py --target http://localhost/webgoat/start.mvc#attack/160587164/200 --elements employee_id,password --button submit --attack 1 --cookie ASP.NET_SessionId:fawx1oxcfm0fd4gvzmej5oco,JSESSIONID:1F0E3B20ECEDDF29235853F55C60FC17 --include-urls "http://localhost/webgoat/attack?Screen=160587164&menu=200" --payloads fuzz.txt --delay-before 0.3 --delay-after 0.3 --fill employee_id,password --reload-page                                                                                                                                             
                                                                                                                                                                                             
    44. Print the stack trace for debugging purpose:                                                                                                                                         
        python3 BrowserBruter.py --target http://localhost:13066/ --elements-payloads username:username.txt,password:passwords.txt --button btn-default --attack 4 --debug                   

    45. Execute specific javascript after submitting the form:
        python3 BrowserBruter.py --target http://localhost:8080/webgoat/start.mvc#attack/1778575388/500 --elements pass1,pass2,pass3,pass4,pass5,pass6 --fill pass1,pass2,pass3,pass4,pass5,pass6 --button SUBMIT --attack 1 --payloads fuzz.txt --include-url "http://10.13.37.3:8080/webgoat/attack?Screen=1778575388&menu=500" --cookie ASP.NET_SessionId:fawx1oxcfm0fd4gvzmej5oco,JSESSIONID:1F0E3B20ECEDDF29235853F55C60FC17 --reload-page --javascript-after "alert(123);"

    46. Don't load .css files:
        python3 BrowserBruter.py --target http://localhost:8080/webgoat/start.mvc#attack/1778575388/500 --elements pass1,pass2,pass3,pass4,pass5,pass6 --fill pass1,pass2,pass3,pass4,pass5,pass6 --button SUBMIT --attack 1 --payloads fuzz.txt --no-css

    47. Become psycho and run 20 threads (unstable):
        python3 BrowserBruter.py --target http://localhost/webgoat/login.mvc --attack 4 --elements-payloads exampleInputEmail1:username.txt,exampleInputPassword1:passwords.txt --button "btn.btn-large.btn-primary" --remove-session --threads 20 --exclude-urls urls.txt                                                                                                                
                                                                                                                                                                                             
        OR -> run in headless mode, this is most stable way to run in multple threads (still unstable):                                                                                      
        python3 BrowserBruter.py --target http://localhost/webgoat/login.mvc --attack 4 --elements-payloads exampleInputEmail1:username.txt,exampleInputPassword1:passwords.txt --button "btn.btn-large.btn-primary" --remove-session --threads 20 --exclude-urls urls.txt --headless                                                                                                     
    DVWA Usage Examples:                                                                                                                                                                     

    1. Fuzz the Command Injection page of DVWA, Pause BrowserBruter on startup to manually login and manually set cookies, press ENTER two times to continue:
        python3 BrowserBruter.py --elements ip --button Submit --payloads payloads.txt --target http://localhost/vulnerabilities/exec/ --pause --attack 1    
    
    2. Fuzz the Command Injection page of DVWA, set two cookies, force reuse of these cookies, reset session data each time:
        python3 BrowserBruter.py --elements ip --button Submit --payloads payloads.txt --target http://localhost/vulnerabilities/exec/ --cookie PHPSESSID:jtq7r9fbgf90h2qm9915qk6551,security:low --force-cookie --remove-session --attack 1

    jsdebugging lab - https://hub.docker.com/r/bhattsameer/jsdebugginglab Usage Examples:
        
    1. Perform BruteForce attack on login page:
        python3 BrowserBruter.py --elements-payloads email:username.txt,password:passwords.txt --target http://172.17.0.2/Lab3/login.php --attack 4 --button btn-secondary --remove-session
        
    2. Perform bruteforce attack on otp page, but otp is being checked on frontend client side, so there are no http request-response from server, so perform brute force attack on client side only:
        python3 BrowserBruter.py --elements otp --payloads otps.txt --target http://localhost/Lab3/OTP.php --button button --attack 1 --delay-after 0.3 --cookie PHPSESSID:9u593rhl797n3v6aa5vu8mjj20

    Stock Management System Lab Usage Examples:

    1. Perform brute force attack on login page to bypass authentication:
        python3 BrowserBruter.py --elements-payloads username:username.txt,password:passwords.txt --button btn-default --target http://localhost:13066/ --attack 4 --remove-session
                                                                                                                                                                                             

    2. Perform Sniper attack on form page which is hidden, and requires pressing a button to be revealed, so use --interactive option to manually press the button:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --interactive --delay-after 0.5 --fill editBrandName,brandId,editBrandStatus

    3. Further automate the script by locating and clickng the buttons which enables the form:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 0.3 --fill editBrandName --javascript "document.querySelector('button.btn.btn-default.dropdown-toggle').click(); document.querySelector('a[data-target="#editBrandModel"]').click();" --delay-after 0.3

    4. Provide above javascript code in file:    
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName,brandId --payloads sqli.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 1 --fill editBrandName --javascript-file click.js

    5. Remove input validations form bootstrap.min.js file and press two buttons on web page using --javascript which will enable the web form:
        python3 BrowserBruter.py --elements editBrandStatus,editBrandName --payloads fuzz.txt --button editBrandBtn --target http://localhost:13066/brand.php --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --attack 1 --delay-before 0.7 --fill editBrandName --javascript "document.querySelector('button.btn.btn-default.dropdown-toggle').click();document.querySelector('a[data-target="#editBrandModel"]').click();" --delay-after 0.5 --replace-files "./res/samples/js-files-with-no-input-validation/bootstrap.min.js"++"http://localhost:13066/assests/bootstrap/js/bootstrap.min.js"

    6. Brute force change password form with submit button's class name is 'btn btn-primary':
        python3 BrowserBruter.py --elements-payloads user_id:username.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt --target http://localhost:13066/setting.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button 'btn-primary'                                                                                                              

    7. Brute force change password form by selecting the specific form, because there is other form with same elements:
        python3 BrowserBruter.py --elements-payloads user_id:username.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt --target http://localhost:13066/setting.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button 'btn-primary' --form changePasswordForm                                                                                    
 
    8. Brute force add user form but first press one using --buttons-to-press-before-fuzz to enable this form:
        python3 BrowserBruter.py --elements-payloads userName:fuzz.txt,upassword:fuzz.txt,uemail:fuzz.txt --button createUserBtn --target http://localhost:13066/user.php --attack 4 --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --buttons-to-press-before-fuzz addUserModalBtn

    9. Audit an complex form, replacing jquery-ui with no input validation jquery-ui and replacing bootstrap.min.js too, running 5 threads:
        python3 BrowserBruter.py --form createOrderForm --elements orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace --fill orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace --payloads fuzz.txt --cookie PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 --button createOrderBtn --attack 1 --replace-file ./res/samples/js-files-with-no-input-validation/bootstrap.min.js++http//localhost:13066/assests/bootstrap/bootstrap.min.js,"./res/samples/js-files-with-no-input-validation/jquery-ui.min.js"++"http://localhost:13066/assests/jquery-ui/jquery-ui.min.js" --attack 1 --target "http://localhost:13066/orders.php?o=add" --threads 5                                                                                                                    

    OWASP JuiceShop Usage Examples:
         
    1. Testing SQLi on OWASP JuiceShop's login page by clusterbombing the payloads:
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

    11. Fuzz the write review form of product by first manually login to the application, then automatically click on the image of product to make produc review menu appear:
        python3 BrowserBruter.py --buttons-to-press-before-fuzz img-container --elements "cdk-text-field-autofill-monitored" --button submitButton --target http://localhost:3000/#/ --cookie cookieconsent_status:dismiss,language:en,welcomebanner_status:dismiss --attack 1 --payloads fuzz.txt --remove-class cdk-text-field-autofill-monitored --pause

```
# The Report-Explorer

## Features

- Rich GUI with customizations.
- Filter the logs by specific string.
- Grep and Match specific strings in data.
- Along with HTTP request/response, also provides Web-Page before/after.
- Sort data by clicking on specific columns.
- Copy payloads and data.

## Usage

### Options
```shell
  --help    Show this help message and exit
  --grep    List of Strings to grep from report.
```

### Usage Examples
```                                                                       
    1. Run the tool:
        python ReportExplorer.py
    
    2. Grep the strings and show the counts:
        python ReportExplore.py welcome,success,admin,root,error 

    SPLIT REPORT:
    
    1. Split the final report into small reports of 200 rows:
        python SplitReport.py /path/to/report-file.csv 200
```


## Contributing

Contributions to **The Browser-Bruter** are welcome! If you have any feature requests, bug reports, or suggestions, please open an issue on the GitHub repository.

If we have missed any scenario that **The Browser-Bruter** cannot tackle, we kindly request you to **open an issue** along with the scenario and any possible solution. In the **BrowserBruter.py** script, you'll find global variables and functions that you can adjust to fit your testing needs. Please **open an issue** after you have modified the tool and solved any penetration testing challenge so that the **community** can benefit from it.

To contribute code or improvements:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and test them.
4. Submit a pull request with a clear description of your contribution.

## License

The license