##################################################################
"""
Name  : usage_manual.py
Date  : 08/03/2024
CopyRight: Net-Square Solutions PVT LTD.
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
This file is used to print the in-built help usage examples
"""
##################################################################

from colorama import Fore

# Defining color contants #
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE

# Defining the user manual
def print_manual():
    print(f'''
Usage Examples:
    1. Perform Bruteforce(ClusterBomb) on login page:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} username:usernames.txt,password:passwords.txt {GREEN}--target{RESET} http://localhost/login.php {GREEN}--button{RESET} Login {GREEN}--attack{RESET} 4 {GREEN}--remove-session{RESET}

    2. Perform PitchFork on login page:
        {YELLOW}python3 BrowserBruter.py{GREEN} -ep{RESET} username:usernames.txt,password:passwords.txt {GREEN}-t{RESET} http://localhost/login.php {GREEN}-b{RESET} Login {GREEN}-a{RESET} 3

    3. Perform BatteringRam on login page:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/login.php {GREEN}--button{RESET} Login {GREEN}--verbose{RESET} {GREEN}--attack{RESET} 2{RESET}

    4. Fuzz on login page and make it verbose:
        {YELLOW}python3 BrowserBruter.py{GREEN} -e{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}-p{RESET} sqli.txt {GREEN}-t{RESET} http://localhost/login.php {GREEN}-b{RESET} Login {GREEN}--verbose{RESET} {GREEN}-a{RESET} 1{RESET}

    5. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint':
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} name,age,address,phone {GREEN}--fill{RESET} name,age,address,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--cookie{RESET} difficulty:high,hint:no {GREEN}--attack{RESET} 1{RESET}
	
    6. Fuzz on registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request becuase the initial cookies might be overridden by new cookies values:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} name,age,address,phone {GREEN}--fill{RESET} name,age,address,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--cookie{RESET} difficulty:high,hint:no {GREEN}--force-cookie {GREEN}--attack{RESET} 1{RESET}
	
    7. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle [this is useful against Authentication pages when you don't want redirection in case of successful login]:
        {YELLOW}python3 BrowserBruter.py{GREEN} -e{RESET} name,age,address,phone {GREEN}--fill{RESET} name,age,address,phone {GREEN}-p{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--cookie{RESET} difficulty:high,hint:no {GREEN}--force-cookie {GREEN}--remove-session {GREEN}--attack{RESET} 1{RESET}
	
    8. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} name,age,address,phone {GREEN}--fill{RESET} name,age,address,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--cookie{RESET} difficulty:high,hint:no {GREEN}--force-cookie {GREEN}--remove-session {GREEN}--headless {GREEN}--attack{RESET} 1{RESET}
	
    9. Fuzz registration page with two cookies 1)'difficulty' and 2)'hint' and sent them forcefully on each request and remove session data and cookie after each request-response cycle and run browser in headless mode and run 5 instances of browser parallely:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} name,age,address,phone {GREEN}--fill{RESET} name,age,address,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--cookie{RESET} difficulty:high,hint:no {GREEN}--force-cookie {GREEN}--remove-session {GREEN}--headless {GREEN}--threads{RESET} 5 {GREEN}--attack{RESET} 1{RESET}
   
    10. Fuzz CheckBox for example '<input type="checkbox" name="hobbies" value="reading" /> <input type="checkbox" name="hobbies" value="writing" />':
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} hobbies {GREEN}--payloads{RESET} paylods.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--attack{RESET} 1{RESET}
   
    11. Fuzz Radio Button for example '<input type="radio" name="yesno" id="yes" value="yes" required/> <input type="radio" name="yesno" id="no" value="no" required/>':
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} yesno {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--attack{RESET} 1{RESET}
    OR
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} no {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/register {GREEN}--button{RESET} register {GREEN}--attack{RESET} 1{RESET}
   
    12. Fuzz <select> element - for example <select name="selectElement" required> <option value="">Select an option</option> <option value="option1">Option 1</option> </select>:
        {YELLOW}python3 BrowserBruter.py{GREEN} -e{RESET} selectElement {GREEN}-p{RESET} payloads.txt {GREEN}-t{RESET} http://localhost/selection {GREEN}-b{RESET} submit {GREEN}-a{RESET} 1{RESET}
    
    13. Fuzz <textarea> element - for example <textarea name="textareaElement" placeholder="Enter text" required></textarea>:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} textareaElement {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/registration {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 1{RESET}
   
    14. Fuzz colorpicker, datepicker, timepicker - for example <input type="color" name="colorElement" required/> <input type="date" name="dateElement" required/> <input type="time" name="timeElement" required/>:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} colorElement,dateElement,timeElement {GREEN}--fill{RESET} colorElement,dateElement,timeElement {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/ {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 1{RESET}

    15. Define API domain in scope for proper report generation and logging:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--button{RESET} button {GREEN}--target{RESET} http://net-square.com/login {GREEN}--payloads{RESET} payloads.txt {GREEN}--attack{RESET} 1 {GREEN}--scope{RESET} api.net-square.com,dev.api.net-square.com{RESET}

    16. Add Authorization headers with bearer token for valid authorization:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--button{RESET} button {GREEN}--target{RESET} http://net-square.com/login {GREEN}--payloads{RESET} payloads.txt {GREEN}--header{RESET} "Auth: 123","Auth1: Bearer emluamFjb2Rlcgo=" {RESET}
	   
    17. Provide custom values for each form field types, content of the file should be in JSON format and it should contain all of the field types, see example values.json for better understanding:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--fill-values{RESET} fields.json {GREEN}--button{RESET} button {GREEN}--target{RESET} http://net-square.com/login {GREEN}--payloads{RESET} payloads.txt" {RESET}

    18. Pause the BrowserBruter on each iteration of fuzzing, so user can manually perform any task, complete captcha before BrowserBruter fuzzes the form, press ENTER two times to continue:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--fill{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--button{RESET} submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost:3000/ {GREEN}--threads{RESET} 5 {GREEN}--fill-values{RESET} values.json {GREEN}--interacitve {GREEN}--attack{RESET} 1{RESET}

    19. Replace the content of a file in HTTP responses and specify the replacement file URL:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--button{RESET} login {GREEN}--target{RESET} http://localhost/login {GREEN}--payloads{RESET} payloads.txt {GREEN}--replace-files{RESET} "input-validation.js"++"http://localhost/assets/js/input-validation.js" {GREEN}--attack{RESET} 1{RESET}

    20. Replace the content of a file in HTTP responses and run JavaScript:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--button{RESET} login {GREEN}--target{RESET} http://localhost/login {GREEN}--payloads{RESET} payloads.txt {GREEN}--replace-files{RESET} "input-validation.js"++"http://localhost/assets/js/input-validation.js" {GREEN}--javascript{RESET} "var elmnt = document.getElementById('ClickMe'); elmnt.click();" {GREEN}--attack{RESET} 1{RESET}

    21. Replace the content of a file in HTTP responses and run JavaScript code by providing the code in file:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--button{RESET} login {GREEN}--target{RESET} http://localhost/login {GREEN}--payloads{RESET} payloads.txt {GREEN}--replace-files{RESET} "input-validation.js"++"http://localhost/assets/js/input-validation.js" {GREEN}--javascript-file{RESET} element-click.js {GREEN}--attack{RESET} 1{RESET}
    
    22. Replace every "return false" statement with "return true" and replace every "alert(0)" with "alert(1)":
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--button{RESET} login {GREEN}--target{RESET} http://localhost/login {GREEN}--payloads{RESET} payloads.txt {GREEN}--replace-code{RESET} "return false","return true","alert(0)","alert(1)" {GREEN}--javascript{RESET} "var elmnt = document.getElementById('ClickMe'); elmnt.click();" {GREEN}--attack{RESET} 1{RESET}
    
    23. Replace bunch of javascript code into return true:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} textarea:sqli.txt,data:sqli.txt {GREEN}--button{RESET} submit {GREEN}--target{RESET} http://localhost:3000/index.html {GREEN}--attack{RESET} 3 {GREEN}--replace-code{RESET} "return false","return true","return regex.test(dateString)","return true","return regex.test(timeString)","return true","return regex.test(colorString)","return true"{RESET}

    24. Fuzz the search box, when user have to press enter to submit the search query, the user has to click on search icon to make search box appear:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} search-bar {GREEN}--button{RESET} search-bar {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/ {GREEN}--payloads{RESET} fuzz.txt {GREEN}--buttons-to-press-before-fuzz searchQuery {GREEN}--press-enter-no-click{RESET}
    
    25. Tell Browser Bruter to remove common javascript input validation:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} search-bar {GREEN}--button{RESET} search-bar {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/ {GREEN}--payloads{RESET} fuzz.txt {GREEN}--buttons-to-press-before-fuzz searchQuery {GREEN}--press-enter-no-click{RESET} {GREEN}--auto-remove-javascript-validation{RESET}
        
    26. Tell Browser Bruter to ignore pop ups like alert() box:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} search-bar {GREEN}--button{RESET} search-bar {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/ {GREEN}--payloads{RESET} fuzz.txt {GREEN}--buttons-to-press-before-fuzz searchQuery {GREEN}--press-enter-no-click{RESET} {GREEN}--auto-remove-javascript-validation {RESET}

    27. Tell Browser Bruter to select the elements under the specified form only, in case there are two forms and multiple elements have same name and ids:
        {YELLOW}python3 BrowserBruter.py{GREEN} --form{RESET} changePasswordForm {GREEN}--elements{RESET} username,password {GREEN}--fill{RESET} username,password {GREEN}--button{RESET} login {GREEN}--target{RESET} http://localhost/login {GREEN}--payloads{RESET} payloads.txt {GREEN}--attack{RESET} 1{RESET}

    28. Pause the Browser Bruter on startup to manually login to the application:
        {YELLOW}python3 BrowserBruter.py{GREEN} --pause {GREEN}--elements{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--fill{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--button{RESET} submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost:3000/ {GREEN}--attack{RESET} 1{RESET}

    29. Pause the Browser Bruter on startup to manually login to the application then run Browser Bruter in interactive mode to solve the captcha before inserting the payloads:
        {YELLOW}python3 BrowserBruter.py{GREEN} --pause {GREEN}--interactive {GREEN}--elements{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--fill{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--button{RESET} submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost:3000/ {GREEN}--attack{RESET} 1{RESET}
        
    30. Pause the Browser Bruter on startup to manually login to the application then run Browser Bruter in interactive mode to solve the captcha before inserting the payloads, pause the Browser Bruter after submitting the form to perform some manual human interaction:
        {YELLOW}python3 BrowserBruter.py{GREEN} --pause {GREEN}--interactive {GREEN}--pause-after-submit {GREEN}--elements{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--fill{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--button{RESET} submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost:3000/ {GREEN}--attack{RESET} 1{RESET}
    
    31. Wait for 1 seconds before and after submission of the form:
        {YELLOW}python3 BrowserBruter.py{GREEN} --delay-before{RESET} 1 {GREEN}--delay-after{RESET} 1 {GREEN}--elements{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--fill{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--button{RESET} submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost:3000/ {GREEN}--attack{RESET} 1{RESET}

    32. Route traffic via proxy i.e. BurpSuite and remove the static media like images:
        {YELLOW}python3 BrowserBruter.py{GREEN} --proxy{RESET} http://127.0.0.1:8080/ {GREEN}--elements{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--fill{RESET} textarea,select,yesno,hobbies,phone,data,time,calendar,color {GREEN}--button{RESET} submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost:3000/ {GREEN}--attack{RESET} 1 {GREEN}--remove-images{RESET}

    33. Add custom chrome options which will be passed to chrome browser:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} id {GREEN}--button{RESET} Submit {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/ {GREEN}--attack{RESET} 1 {GREEN}--chrome-options{RESET} ignore-certificate-errors,disable-dev-shm-usage{RESET}

    34. Override all chrome options and use raw anti bot detection evasions:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} id {GREEN}--button{RESET} Submit {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/ {GREEN}--attack{RESET} 1 {GREEN}--anti-bot{RESET}

    35. Brute force login page and try to bypass authentication and also do not try to evade anti bot defences and route traffic via proxy:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} username:userid.txt,password:passwords.txt {GREEN}--button{RESET} Login {GREEN}--target{RESET} http://localhost/login.php {GREEN}--attack{RESET} 4 {GREEN}--proxy{RESET} http://127.0.0.1:8080/ {GREEN}--no-anti-bot {GREEN}--remove-session{RESET}

    36. Perform BatteringRam attack on web page which has invisible captcha so start each payload insertion on new fresh instance of browser:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} name,email,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://example.com/signup {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 2 {GREEN}--new-instance{RESET}

    37. Perform BatteringRam attack on web page which has invisible captcha so start each payload insertion on new fresh instance of browser and force restore the cookie:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} name,email,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://example.com/signup {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 2 {GREEN}--new-instance {GREEN}--force-cookie{RESET}
	
    38. There is field called name that you don't want to fuzz but it requires to be filled while submitting the form:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} email,phone {GREEN}--fill{RESET} name {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://example.com/signup {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 1{RESET}
          
    39. There is input validation that is preventing the payloads, try to remove the class attribute from these elements to see if payloads are correctly inserted:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} email,phone {GREEN}--fill{RESET} name {GREEN}--remove-class{RESET} email,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://example.com/signup {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 1{RESET}

    40. Split the final report into smaller chunks by specifying the rows limit in each report to make report review process faster in ReportExplorer:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} email,phone {GREEN}--fill{RESET} name {GREEN}--remove-class{RESET} email,phone {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://example.com/signup {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 1 {GREEN}--rows-limit{RESET} 200{RESET}

    41. Excluding urls from final report:
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost/webgoat/start.mvc#attack/1869022003/100 {GREEN}--elements{RESET} person {GREEN}--payloads{RESET} fuzz.txt {GREEN}--button{RESET} SUBMIT {GREEN}--attack{RESET} 1 {GREEN}--outofscope-urls{RESET} "http://localhost/webgoat/service/solution.mvc","http://localhost/webgoat/service/lessonprogress.mvc","http://localhost/webgoat/service/lessonmenu.mvc","http://localhost/webgoat/service/solution.mvc"
        
        {RESET}OR -> Providing list of urls:
        {YELLOW}python3 BrowserBruter.py {GREEN}--target{RESET} http://localhost/webgoat/start.mvc#attack/1869022003/100 {GREEN}--elements{RESET} person {GREEN}--payloads{RESET} fuzz.txt {GREEN}--button{RESET} SUBMIT {GREEN}--attack{RESET} 1 {GREEN}--outofscope-urls{RESET} urls.txt

    42. Including only specific urls in final report:
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost/webgoat/start.mvc#attack/1869022003/100 {GREEN}--elements{RESET} person {GREEN}--payloads{RESET} fuzz.txt {GREEN}--button{RESET} SUBMIT {GREEN}--attack{RESET} 1 {GREEN}--inscope-urls{RESET} "http://localhost/webgoat/attack?Screen=1869022003&menu=100"

        {RESET}OR -> Providing file containing URLs:
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost/webgoat/start.mvc#attack/1869022003/100 {GREEN}--elements{RESET} person {GREEN}--payloads{RESET} fuzz.txt {GREEN}--button{RESET} SUBMIT {GREEN}--attack{RESET} 1 {GREEN}--inscope-urls{RESET} urls.txt

    43. Force reload the page before fuzzing the form on each iteration, usefull when result of previous iteration causes the web elements to disappear or which leads to elements not found error, in such case this switch helps to keep browser bruter running:
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost/webgoat/start.mvc#attack/160587164/200 {GREEN}--elements{RESET} employee_id,password {GREEN}--button{RESET} submit {GREEN}--attack{RESET} 1 {GREEN}--cookie{RESET} ASP.NET_SessionId:fawx1oxcfm0fd4gvzmej5oco,JSESSIONID:1F0E3B20ECEDDF29235853F55C60FC17 {GREEN}--inscope-urls{RESET} "http://localhost/webgoat/attack?Screen=160587164&menu=200" {GREEN}--payloads{RESET} fuzz.txt {GREEN}--delay-before{RESET} 0.3 {GREEN}--delay-after{RESET} 0.3 {GREEN}--fill{RESET} employee_id,password {GREEN}--reload-page

    44. Print the stack trace for debugging purpose:
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost/ {GREEN}--elements-payloads{RESET} username:usernames.txt,password:passwords.txt {GREEN}--button{RESET} btn-default {GREEN}--attack{RESET} 4 {GREEN}--debug{RESET}

    45. Execute specific javascript after submitting the form:
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost:8080/webgoat/start.mvc#attack/1778575388/500 {GREEN}--elements{RESET} pass1,pass2,pass3,pass4,pass5,pass6 {GREEN}--fill{RESET} pass1,pass2,pass3,pass4,pass5,pass6 {GREEN}--button{RESET} SUBMIT {GREEN}--attack{RESET} 1 {GREEN}--payloads{RESET} fuzz.txt {GREEN}--include-url{RESET} "http://10.13.37.3:8080/webgoat/attack?Screen=1778575388&menu=500" {GREEN}--cookie{RESET} ASP.NET_SessionId:fawx1oxcfm0fd4gvzmej5oco,JSESSIONID:1F0E3B20ECEDDF29235853F55C60FC17 {GREEN}--reload-page --javascript-after{RESET} "alert(123);"

    46. Don't load .css files:
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost:8080/webgoat/start.mvc#attack/1778575388/500 {GREEN}--elements{RESET} pass1,pass2,pass3,pass4,pass5,pass6 {GREEN}--fill{RESET} pass1,pass2,pass3,pass4,pass5,pass6 {GREEN}--button{RESET} SUBMIT {GREEN}--attack{RESET} 1 {GREEN}--payloads{RESET} fuzz.txt {GREEN}--no-css{RESET}

    47. Become psycho and run 20 threads (unstable):
        {YELLOW}python3 BrowserBruter.py{GREEN} --target{RESET} http://localhost/webgoat/login.mvc {GREEN}--attack{RESET} 4 {GREEN}--elements-payloads{RESET} exampleInputEmail1:usernames.txt,exampleInputPassword1:passwords.txt {GREEN}--button{RESET} "btn.btn-large.btn-primary" {GREEN}--remove-session --threads {RESET}20 {GREEN}--outofscope-urls{RESET} urls.txt

        OR -> run in headless mode, this is most stable way to run in multiple threads (still unstable):
        {YELLOW}python3 BrowserBruter.py {GREEN}--target{RESET} http://localhost/webgoat/login.mvc {GREEN}--attack{RESET} 4 {GREEN}--elements-payloads{RESET} exampleInputEmail1:usernames.txt,exampleInputPassword1:passwords.txt {GREEN}--button {RESET}"btn.btn-large.btn-primary" {GREEN}--remove-session --threads {RESET}20 {GREEN}--outofscope-urls {RESET}urls.txt {GREEN}--headless{RESET}

    48. Get the element using CSS SELECTOR, here using css selector for '--button' option:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} username,password {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/login3.php {GREEN}--button{RESET} button.btn.btn-default {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} username,password   

    49. Execute the python using Python Scripting Engine:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} text-center {GREEN}--button{RESET} font-semibold {GREEN}--payloads{RESET} usernames.txt {GREEN}--target{RESET} http://localhost/ {GREEN}--attack{RESET} 1 {GREEN}--scope{RESET} api.localhost {GREEN}--python{RESET} "e1 = driver.find_element(By.CSS_SELECTOR, 'input.w-full.text-center'); e1.send_keys('1234567890'); driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.mt-6.w-full.font-semibold').click(); sleep(2)"

    50. Execute the python using Python Scripting Engine - provide python file:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} text-center {GREEN}--button{RESET} font-semibold {GREEN}--payloads{RESET} usernames.txt {GREEN}--target{RESET} http://localhost/ {GREEN}--attack{RESET} 1 {GREEN}--scope{RESET} api.localhost {GREEN}--python-file{RESET} captcha_cracker.py

    51. Execute the python code after filling the form using Python Scripting Engine:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} text-center {GREEN}--button{RESET} font-semibold {GREEN}--payloads{RESET} usernames.txt {GREEN}--target{RESET} http://localhost/ {GREEN}--attack{RESET} 1 {GREEN}--scope{RESET} api.localhost {GREEN}--python-after{RESET} "e1 = driver.find_element(By.CSS_SELECTOR, 'input.w-full.text-center'); e1.send_keys('1234567890'); driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.mt-6.w-full.font-semibold').click(); sleep(2)"

    52. Execute the python code to Add custom header in HTTP request using Python Scripting Engine:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} username,password {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/login3.php {GREEN}--button{RESET} "button.btn.btn-default" {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} username,password {GREEN}--python-request{RESET} "request.headers['python-added'] = 'added-by-python'"    

    53. Execute the python code to Add custom header in HTTP response using Python Scripting Engine:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} username,password {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/login3.php {GREEN}--button{RESET} "button.btn.btn-default" {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} username,password {GREEN}--python-response{RESET} "response.headers['python-added'] = 'added-by-python'"    

    54. Execute the python code to Add custom header in HTTP request using Python Scripting Engine using python file:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} username,password {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/login3.php {GREEN}--button{RESET} "button.btn.btn-default" {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} username,password {GREEN}--python-request-file{RESET} sample-python-code.py

    55. Execute the python code to Add custom header in HTTP response using Python Scripting Engine using python file:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} username,password {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/login3.php {GREEN}--button{RESET} "button.btn.btn-default" {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} username,password {GREEN}--python-response-file{RESET} sample-python-code.py

    56. Disable keypress,keydown and keyup events using --disable-events method:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} username,password {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost/login3.php {GREEN}--button{RESET} "button.btn.btn-default" {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} username,password {GREEN}--disable-events{RESET} keypress,keydown,keyup

    57. Record the navigation:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} editBrandStatus,editBrandName,brandId {GREEN}--payloads{RESET} sqli.txt {GREEN}--button{RESET} editBrandBtn {GREEN}--target{RESET} http://localhost/brand.php {GREEN}--cookie{RESET} PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} editBrandName {GREEN}--record-navigation{RESET}

    58. Play the navigation before fuzzing the form:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} editBrandStatus,editBrandName,brandId {GREEN}--payloads{RESET} sqli.txt {GREEN}--button{RESET} editBrandBtn {GREEN}--target{RESET} http://localhost/brand.php {GREEN}--cookie{RESET} PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} editBrandName {GREEN}--load-navigation-before{RESET} path/to/navigation.json

    59. Play the navigation after fuzzing the form:
        {YELLOW}python3 BrowserBruter.py {GREEN}--elements{RESET} editBrandStatus,editBrandName,brandId {GREEN}--payloads{RESET} sqli.txt {GREEN}--button{RESET} editBrandBtn {GREEN}--target{RESET} http://localhost/brand.php {GREEN}--cookie{RESET} PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} editBrandName {GREEN}--load-navigation-after{RESET} path/to/navigation.json
        
    {RED}Damn Vulnerable Web Application Lab Usage Examples:{RESET}   

    1. Fuzz the Command Injection page of DVWA, Pause BrowserBruter on startup to manually login and manually set cookies, press ENTER two times to continue:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} ip {GREEN}--button{RESET} Submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/vulnerabilities/exec/ {GREEN}--pause {GREEN}--attack{RESET} 1{RESET}    
    
    2. Fuzz the Command Injection page of DVWA, set two cookies, force reuse of these cookies, reset session data each time:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} ip {GREEN}--button{RESET} Submit {GREEN}--payloads{RESET} payloads.txt {GREEN}--target{RESET} http://localhost/vulnerabilities/exec/ {GREEN}--cookie{RESET} PHPSESSID:jtq7r9fbgf90h2qm9915qk6551,security:low {GREEN}--force-cookie {GREEN}--remove-session {GREEN}--attack{RESET} 1{RESET}

    {RED}jsdebugging lab - https://hub.docker.com/r/bhattsameer/jsdebugginglab Usage Examples:{RESET}
        
    1. Perform BruteForce attack on login page:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} email:usernames.txt,password:passwords.txt {GREEN}--target{RESET} http://172.17.0.2/Lab3/login.php {GREEN}--attack{RESET} 4 {GREEN}--button{RESET} btn-secondary {GREEN}--remove-session{RESET}
        
    2. Perform bruteforce attack on otp page, but otp is being checked on frontend client side, so there are no http request-response from server, so perform brute force attack on client side only:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} otp {GREEN}--payloads{RESET} otps.txt {GREEN}--target{RESET} http://localhost/Lab3/OTP.php {GREEN}--button{RESET} button {GREEN}--attack{RESET} 1 {GREEN}--delay-after{RESET} 0.3 {GREEN}--cookie{RESET} PHPSESSID:9u593rhl797n3v6aa5vu8mjj20{RESET}

    {RED}Stock Management System Lab Usage Examples:{RESET}

    1. Perform brute force attack on login page to bypass authentication:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} username:usernames.txt,password:passwords.txt {GREEN}--button{RESET} btn-default {GREEN}--target{RESET} http://localhost/login3.php {GREEN}--attack{RESET} 4 {GREEN}--remove-session
{RESET}

    2. Perform Sniper attack on form page which is hidden, and requires pressing a button to be revealed, so use --interactive option to manually press the button:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} editBrandStatus,editBrandName,brandId {GREEN}--payloads{RESET} sqli.txt {GREEN}--button{RESET} editBrandBtn {GREEN}--target{RESET} http://localhost/brand.php {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--attack{RESET} 1 {GREEN}--interactive {GREEN}--delay-after{RESET} 0.5 {GREEN}--fill{RESET} editBrandName,brandId,editBrandStatus

    3. Further automate the script by locating and clickng the buttons which enables the form:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} editBrandStatus,editBrandName,brandId {GREEN}--payloads{RESET} sqli.txt {GREEN}--button{RESET} editBrandBtn {GREEN}--target{RESET} http://localhost/brand.php {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--attack{RESET} 1 {GREEN}--delay-before{RESET} 0.3 {GREEN}--fill{RESET} editBrandName {GREEN}--javascript{RESET} "document.querySelector('button.btn.btn-default.dropdown-toggle').click(); document.querySelector('a[data-target=\\"#editBrandModel\\"]').click();" {GREEN}--delay-after{RESET} 0.3{RESET}

    4. Provide above javascript code in file:    
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} editBrandStatus,editBrandName,brandId {GREEN}--payloads{RESET} sqli.txt {GREEN}--button{RESET} editBrandBtn {GREEN}--target{RESET} http://localhost/brand.php {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--attack{RESET} 1 {GREEN}--delay-before{RESET} 1 {GREEN}--fill{RESET} editBrandName {GREEN}--javascript-file{RESET} click.js{RESET}

    5. Remove input validations form bootstrap.min.js file and press two buttons on web page using --javascript which will enable the web form:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} editBrandStatus,editBrandName {GREEN}--payloads{RESET} fuzz.txt {GREEN}--button{RESET} editBrandBtn {GREEN}--target{RESET} http://localhost/brand.php {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--attack{RESET} 1 {GREEN}--delay-before{RESET} 0.7 {GREEN}--fill{RESET} editBrandName {GREEN}--javascript{RESET} "document.querySelector('button.btn.btn-default.dropdown-toggle').click();document.querySelector('a[data-target=\\"#editBrandModel\\"]').click();" {GREEN}--delay-after{RESET} 0.5 {GREEN}--replace-files{RESET} "./res/samples/js-files-with-no-input-validation/bootstrap.min.js"++"http://localhost/assests/bootstrap/js/bootstrap.min.js"{RESET}

    6. Brute force change password form with submit button's class name is 'btn btn-primary':
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} user_id:usernames.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt {GREEN}--target{RESET} http://localhost/setting.php {GREEN}--attack{RESET} 4 {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--button{RESET} 'btn-primary'{RESET}

    7. Brute force change password form by selecting the specific form, because there is other form with same elements:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} user_id:usernames.txt,password:passwords.txt,npassword:passwords.txt,cpassword:passwords.txt {GREEN}--target{RESET} http://localhost/setting.php {GREEN}--attack{RESET} 4 {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--button{RESET} 'btn-primary' {GREEN}--form{RESET} changePasswordForm{RESET}
 
    8. Brute force add user form but first press one using --buttons-to-press-before-fuzz to enable this form:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} userName:fuzz.txt,upassword:fuzz.txt,uemail:fuzz.txt {GREEN}--button{RESET} createUserBtn {GREEN}--target{RESET} http://localhost/user.php {GREEN}--attack{RESET} 4 {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--buttons-to-press-before-fuzz{RESET} addUserModalBtn{RESET}

    9. Audit an complex form, replacing jquery-ui with no input validation jquery-ui and replacing bootstrap.min.js too, running 5 threads:
        {YELLOW}python3 BrowserBruter.py{GREEN} --form{RESET} createOrderForm {GREEN}--elements{RESET} orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace {GREEN}--fill{RESET} orderDate,clientName,clientContact,productName1,rate1,rateValue1,quantity1,total1,totalValue1,subTotal,subTotalValue,totalAmount,totalAmountValue,discount,grandTotal,grandTotalValue,vat,vatValue,paid,due,dueValue,paymentType,paymentStatus,paymentPlace {GREEN}--payloads{RESET} fuzz.txt {GREEN}--cookie{RESET} PHPSESSID:lqiqsdi8trjfeijdf8i2s2qru1 {GREEN}--button{RESET} createOrderBtn {GREEN}--attack{RESET} 1 {GREEN}--replace-file{RESET} ./res/samples/js-files-with-no-input-validation/bootstrap.min.js++http//localhost/assests/bootstrap/bootstrap.min.js,"./res/samples/js-files-with-no-input-validation/jquery-ui.min.js"++"http://localhost/assests/jquery-ui/jquery-ui.min.js" {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} "http://localhost/orders.php?o=add" {GREEN}--threads{RESET} 5{RESET}

    10. Fuzz the report page of the Stock Management System:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} startDate,endDate {GREEN}--fill{RESET} startDate,endDate {GREEN}--button{RESET} generateReportBtn {GREEN}--target{RESET} http://localhost/report.php {GREEN}--attack{RESET} 1 {GREEN}--payloads{RESET} fuzz.txt {GREEN}--form{RESET} getOrderReportForm {GREEN}--cookie{RESET} PHPSESSID:gpe4qjanmp01ldltdgdnb9nep0 {GREEN}--replace-files{RESET} res/samples/js-files-with-no-input-validation/bootstrap.min.js++http//localhost/assests/bootstrap/bootstrap.min.js,"res/samples/js-files-with-no-input-validation/jquery-ui.min.js"++"http://localhost/assests/jquery-ui/jquery-ui.min.js" {GREEN}--delay-before{RESET} 0.5

    {RED}OWASP JuiceShop Usage Examples:{RESET}
         
    1. Testing SQLi on OWASP JuiceShop's login page by cluster bombing the payloads:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements-payloads{RESET} email:sqli.txt,password:sqli.txt {GREEN}--target{RESET} http://localhost:3000/#/login {GREEN}--attack{RESET} 4 {GREEN}--button{RESET} loginButton {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--remove-session{RESET}

    2. Fuzzing registration page of OWASP JuiceShop:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl {GREEN}--button{RESET} registerButton {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl {GREEN}--payloads{RESET} fuzz.txt {GREEN}--target{RESET} http://localhost:3000/#/register {GREEN}--cookie{RESET} welcomebanner_status:dismiss

    3. Fuzz the email field for various vulnerabilities of OWASP JuiceShop and split the final report into 100 rows of multiples reports:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} emailControl {GREEN}--button{RESET} registerButton {GREEN}--attack{RESET} 1 {GREEN}--fill{RESET} emailControl,passwordControl,repeatPasswordControl,mat-slide-toggle-1-input,securityAnswerControl {GREEN}--payloads{RESET} sqli.txt {GREEN}--target{RESET} http://localhost:3000/#/register {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--rows-limit{RESET} 100{RESET}

    4. Fuzz the file upload functionality of OWASP JuiceShop's complaint page:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} cdk-text-field-autofill-monitored,complaintMessage,file {GREEN}--button{RESET} submitButton {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/complain {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--fill{RESET} cdk-text-field-autofill-monitored,complaintMessage,file{RESET}

    5. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} cdk-text-field-autofill-monitored,complaintMessage,file {GREEN}--button{RESET} submitButton {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/complain {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--fill{RESET} cdk-text-field-autofill-monitored,complaintMessage,file {GREEN}--remove-class{RESET} cdk-text-field-autofill-monitored{RESET}

    6. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable and include the auth cookies and Authorization header to be able fuzz while being authenticated:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} cdk-text-field-autofill-monitored,complaintMessage,file {GREEN}--button{RESET} submitButton {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/complain {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--fill{RESET} cdk-text-field-autofill-monitored,complaintMessage,file {GREEN}--remove-class{RESET} cdk-text-field-autofill-monitored {GREEN}--header{RESET} "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI"
{RESET}

    7. Fuzz the file upload functionality of OWASP JuiceShop's complain page and remove the class attribute from the email field to make it intractable and include the auth cookies and Authorization header to be able fuzz while being authenticated and split the final report into smaller reports containing 200 rows each:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} cdk-text-field-autofill-monitored,complaintMessage,file {GREEN}--button{RESET} submitButton {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/complain {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--fill{RESET} cdk-text-field-autofill-monitored,complaintMessage,file {GREEN}--remove-class{RESET} cdk-text-field-autofill-monitored {GREEN}--header{RESET} "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI"
{RESET}

    8. Fuzz the global search functionality of the OWASP JuiceShop while authenticated by sending ENTER key instead of click:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} mat-input-0 {GREEN}--button{RESET} mat-input-0 {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/ {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--header{RESET} "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" {GREEN}--buttons-to-press-before-fuzz{RESET} searchQuery {GREEN}--press-enter-no-click{RESET} 
{RESET}

        OR -> following removes class attribute so the script does no throw element not intreactable error:
        {YELLOW}python3 BrowserBruter.py{GREEN} --elements{RESET} mat-input-0 {GREEN}--button{RESET} mat-input-0 {GREEN}--attack{RESET} 1 {GREEN}--target{RESET} http://localhost:3000/#/ {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--header{RESET} "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" {GREEN}--buttons-to-press-before-fuzz{RESET} searchQuery {GREEN}--press-enter-no-click{RESET} {GREEN}--remove-class{RESET} mat-input-0
{RESET}

    9. Fuzz the Customer Feedback form of OWASP JuiceShop:
        {YELLOW}python3 BrowserBruter.py{GREEN} --button{RESET} submitButton {GREEN}--target{RESET} http://localhost:3000/#/contact {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--attack{RESET} 1 {GREEN}--elements{RESET} userId,cdk-text-field-autofill-monitored,comment,rating {GREEN}--fill{RESET} cdk-text-field-autofill-monitored,comment,rating {GREEN}--remove-class{RESET} userId,cdk-text-field-autofill-monitored,comment,rating {GREEN}--interactive {GREEN}--rows-limit{RESET} 200{RESET}

        OR -> Fuzz the captcha field too:
        {YELLOW}python3 BrowserBruter.py{GREEN} --button{RESET} submitButton {GREEN}--target{RESET} http://localhost:3000/#/contact {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--payloads{RESET} fuzz.txt {GREEN}--attack{RESET} 1 {GREEN}--elements{RESET} userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl {GREEN}--fill{RESET} cdk-text-field-autofill-monitored,comment,rating {GREEN}--remove-class{RESET} userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl {GREEN}--interactive {GREEN}--rows-limit{RESET} 200{RESET}

        OR -> Fuzz the captcha field and auto fill too:
        {YELLOW}python3 BrowserBruter.py{GREEN} --button{RESET} submitButton {GREEN}--target{RESET} http://localhost:3000/#/contact {GREEN}--cookie{RESET} welcomebanner_status:dismiss {GREEN}--header{RESET} "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MTI3LCJ1c2VybmFtZSI6IiIsImVtYWlsIjoiemluamFAMTIzLmNvbSIsInBhc3N3b3JkIjoiZjViYjBjOGRlMTQ2YzY3YjQ0YmFiYmY0ZTY1ODRjYzAiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTAzLTA0IDE0OjEzOjIzLjQ2NCArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MDk1NjE2MTV9.oWlMbKjqEk2kxamx5lIgIrnFyXd4vV01xZXPUWLywB-FEfVk6SIx7NA9iNSCjCAwqjKcbKOZIqevIGdvkgiGQw6TpjZhs8_fGtlGIfU7Ud3kjk0MyoXauws9mC1LT9Zn5V2ik2GcuEi-xLgrWi6fNM34F6PQA2c1naeQ_mHkqVI" {GREEN}--payloads{RESET} fuzz.txt {GREEN}--attack{RESET} 1 {GREEN}--elements{RESET} userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl {GREEN}--fill{RESET} cdk-text-field-autofill-monitored,comment,rating,captchaControl {GREEN}--remove-class{RESET} userId,cdk-text-field-autofill-monitored,comment,rating,captchaControl {GREEN}--rows-limit{RESET} 200{RESET}

    10. Fuzz the chatbot of OWASP JuiceShop by first manually sign-in into the application:
        {YELLOW}python3 BrowserBruter.py{GREEN} --button{RESET} message-input {GREEN}--elements{RESET} message-input {GREEN}--press-enter-no-click --target{RESET} http://localhost:3000/#/chatbot {GREEN}--cookie{RESET} test:working,welcomebanner_status:dismiss,language:en {GREEN}--pause {GREEN}--payloads{RESET} fuzz.txt {GREEN}--attack{RESET} 1 {GREEN}--rows-limit{RESET} 200{RESET}

    11. Fuzz the write review form of product by first manually login to the application, then automatically click on the image of product to make product review menu appear:
        {YELLOW}python3 BrowserBruter.py{GREEN} --buttons-to-press-before-fuzz{RESET} img-container {GREEN}--elements{RESET} "cdk-text-field-autofill-monitored" {GREEN}--button{RESET} submitButton {GREEN}--target{RESET} http://localhost:3000/#/ {GREEN}--cookie{RESET} cookieconsent_status:dismiss,language:en,welcomebanner_status:dismiss {GREEN}--attack{RESET} 1 {GREEN}--payloads{RESET} fuzz.txt {GREEN}--remove-class{RESET} cdk-text-field-autofill-monitored {GREEN}--pause{RESET}

    {RED}USAGE EXAMPLES OF THE REPORT EXPLORER:

    {BLUE}REPORT EXPLORER{RESET}:
    
    1. Run the tool:
        {YELLOW}python ReportExplorer.py{RESET}
    
    2. Open the report using --report option:
        {YELLOW}python3 ReportExplorer.py {GREEN}--report{RESET} BrowserBruter_Reports/localhost/2024-03-20_03-24-37/localhost-2024-03-20_03-24-37.csv

    2. Grep the strings and show the counts:
        {YELLOW}python ReportExplore.py {GREEN}--grep{RESET} welcome,success,admin,root,error

    3. Combine both --report and --grep option:
        {YELLOW}python3 ReportExplorer.py {GREEN}--report {RESET}BrowserBruter_Reports/localhost/2024-03-20_03-24-37/localhost-2024-03-20_03-24-37.csv {GREEN}--grep{RESET} error,exception,success,"login Successful","welcome admin"

    4. Split the report for efficient review:
        {YELLOW}python ReportExplorer.py {GREEN}--split{RESET} /path/to/report-file.csv,200
''')