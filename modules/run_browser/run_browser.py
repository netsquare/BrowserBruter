##################################################################
"""
Name  : run_browser.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import handle_unknown_exception, log_error
from modules.attacks.battering_ram import battering_ram_loop
from modules.attacks.sniper import sniper_loop
from modules.attacks.pitchfork import pitchfork_loop
from modules.attacks.cluster_bomb import attempt_clusterbomb_fuzz
from modules.misc_functions.sleep_while_pause import sleep_while_pause
from modules.run_browser.add_cookies import add_cookies
from modules.run_browser.get_and_initialize_driver import get_and_initialize_chrome_driver
from modules.run_browser.add_local_storage import add_local_storage
from modules.run_browser.add_session_storage import add_session_storage
from modules.run_browser.set_debug_point import set_debug_breakpoint
from modules.run_browser.monitor_breakpoint_hit import monitor_breakpoint_hit

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # Used to pause the script
from traceback import format_exc# used for getting the proper exceptions
import datetime # used for getting current time and working with time
from sys import exit # used to close the script
import threading

##################################################################
# Importing Exception
##################################################################
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import ProtocolError
from urllib3.exceptions import MaxRetryError
from http.client import RemoteDisconnected


##################################################################
"""
Name          -> get_filename
Functionality -> Function to Generate filename for each different thread
Algorithm     -> 
    1. Ge the current time
    2. format the current time
    3. create file name inside Browser Bruter reports directory, create directory of hostname which is the target for example, if the target is https://net-square.com then directory will be net-square.
    4. return the filename
Parameters    -> 
Return        -> filename(string)
"""
################################################################## 

def get_filename():
	# Getting current date and time to name the output file accordingly
	current_datetime = datetime.datetime.now() # Algorithm step: 1 Get the current time
	formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") # Algorithm step: 2 format the current time
	filename = [f"BrowserBruter_Reports/{global_variable.hostname}/{global_variable.start_time}/{global_variable.hostname}-{formatted_datetime}.csv",f"BrowserBruter_Reports/{global_variable.hostname}/{global_variable.start_time}/{global_variable.hostname }-{formatted_datetime}.txt"] # Algorithm step: 3 create report filename
	return filename # Algorithm step: 4 return filename

##################################################################
"""
Name          -> run_browser_instance
Functionality -> Function to Run Single Browser instance, This function first initializes the webdriver.Chrome object which is called 'driver' throughout the script
Algorithm     ->
    1. Check the termination flag
    2. Call the get_and_initialize_chrome_driver() method to get the webdriver.Chrome object
    3. if --cookies were given, call add_cookie() and add the cookies
    4. Get the temporary report for this thread and store it in this_threads_files
    5. if --pause is set then pause the script on startup
    6. Launch the specified attack
    7. if there is --threads option and there was an issue retry the step 6
    8. Handle various exceptions
    9. Close the browser after attack is finished
                
Parameters    -> payloads(list of string), instance_number(int)
Return        -> 
"""
################################################################## 

def run_browser_instance(payloads, instance_number):
    if not global_variable.terminate: # Algorithm step: 1 Check the global_variable.terminate flag
        try:
            driver = get_and_initialize_chrome_driver() # Algorithm step: 2 Spawning an instance of browser, Assigning browser options
            if global_variable.args.add_storage:
                try:
                    driver.get(global_variable.args.target)
                    add_local_storage(driver)
                except TimeoutException as e: # For any reason if there is a timeout, ask user whether they want to continue or not
                    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                    global_variable.pause_event.set()
                    sleep_while_pause()
                except Exception as e:
                    handle_unknown_exception(e)
                    driver.quit()
                    exit(0)
            if global_variable.args.add_session_storage:
                try:
                    driver.get(global_variable.args.target)
                    add_session_storage(driver)
                except TimeoutException as e: # For any reason if there is a timeout, ask user whether they want to continue or not
                    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                    global_variable.pause_event.set()
                    sleep_while_pause()
                except Exception as e:
                    handle_unknown_exception(e)
                    driver.quit()
                    exit(0)
            if global_variable.args.cookie: # Algorithm step: 3 If cookies are provided assign them to session, Get the initial cookie
                try:
                    driver.get(global_variable.args.target) # first visit the domain so Chrome does not trow InvalidCookieDomainException
                    add_cookies(driver) # Call add_cookies() function to assign cookies
                except TimeoutException as e: # For any reason if there is a timeout, ask user whether they want to continue or not
                    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}HTTP Response Timeout has been reached. Do you want to wait for server to response? Press ENTER to continue to wait, press CTRL+C to stop the process and generate the report.\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                    global_variable.pause_event.set()
                    sleep_while_pause()
                except Exception as e:
                    handle_unknown_exception(e)
                    driver.quit()
                    exit(0)
#            if global_variable.args.debug: # Setting the debug breakpoint
#                for debug_point in global_variable.args.debug.split('++'):
#                    file_url, loc = debug_point.split(',',1)
#                    if ',' in loc:
#                        loc, column = loc.split(',')
#                        set_debug_breakpoint(driver, file_url, loc, column)
#                    else:
#                        set_debug_breakpoint(driver, file_url, loc)
#                debug_thread = threading.Thread(target=monitor_breakpoint_hit, args=(driver,global_variable.args.debug_code),  daemon=True)
#                debug_thread.start()
            this_threads_files = get_filename() # Algorithm step: 4 Initialize report file and processed payload file 
            if global_variable.args.pause: # Algorithm step: 5 If pause flag is set then go to target page and pause until user continues
                driver.get(global_variable.args.target)
                global_variable.pause_event.set()
            try: # Algorithm step: 6 Launch the attack
                if global_variable.args.attack == 1: # SNIPER ATTACK
                    if not global_variable.terminate: # Check the global_variable.terminate flag before starting the browser, This global_variable.terminate check is at so many places to improve to stability of the script. This prevents any further action to take place in case user has pressed CTRL+C
                        sniper_loop(payloads, global_variable.elements, instance_number, this_threads_files, driver) # Call the SNIPER ATTACK loop 
                elif global_variable.args.attack == 2: # BATTERING RAM ATTACK
                    if not global_variable.terminate:
                        battering_ram_loop(payloads, global_variable.elements, instance_number, this_threads_files, driver) # Call the Battering ram loop
                elif global_variable.args.attack == 3: # PITCHFORK ATTACK
                    if not global_variable.terminate:
                        pitchfork_loop(payloads,instance_number,this_threads_files,driver) # Call the Pitchfork loop
                elif global_variable.args.attack == 4: # CLUSTER BOMB ATTACK
                    if not global_variable.terminate:
                        attempt_clusterbomb_fuzz(payloads,driver,this_threads_files,instance_number) # Call the Cluster bomb attack directly without any loop, this is because cluster bomb's loop logic is written in attempt function it self
            except: # Algorithm step: 7
                if global_variable.args.threads:  # If there are multiple threads, then and only then retry in case of exception on first try of launching the browser
                    sleep(6) # As there will be an exception on previous try wait for 6 seconds before attempting again
                    try:
                        if global_variable.args.attack == 1: # SNIPER ATTACK
                            if not global_variable.terminate: # Check the global_variable.terminate flag before starting the browser, This global_variable.terminate check is at so many places to improve to stability of the script. This prevents any further action to take place in case user has pressed CTRL+C
                                sniper_loop(payloads, global_variable.elements, instance_number, this_threads_files, driver) # Call the SNIPER ATTACK loop 
                        elif global_variable.args.attack == 2: # BATTERING RAM ATTACK
                            if not global_variable.terminate:
                                battering_ram_loop(payloads, global_variable.elements, instance_number, this_threads_files, driver) # Call the Battering ram loop
                        elif global_variable.args.attack == 3: # PITCHFORK ATTACK
                            if not global_variable.terminate:
                                pitchfork_loop(payloads,instance_number,this_threads_files,driver) # Call the Pitchfork loop
                        elif global_variable.args.attack == 4: # CLUSTER BOMB ATTACK
                            if not global_variable.terminate:
                                attempt_clusterbomb_fuzz(payloads,driver,this_threads_files,instance_number) # Call the Cluster bomb attack directly without any loop, this is because cluster bomb's loop logic is written in attempt function it self
                    except: # Incase there was again an error even after waiting for 6 seconds, perform third attempt
                        sleep(10) # In third attempt, wait for 10 seconds before 
                        if global_variable.args.attack == 1: # SNIPER ATTACK
                            if not global_variable.terminate: # Check the global_variable.terminate flag before starting the browser, This global_variable.terminate check is at so many places to improve to stability of the script. This prevents any further action to take place in case user has pressed CTRL+C
                                sniper_loop(payloads, global_variable.elements, instance_number, this_threads_files, driver) # Call the SNIPER ATTACK loop 
                        elif global_variable.args.attack == 2: # BATTERING RAM ATTACK
                            if not global_variable.terminate:
                                battering_ram_loop(payloads, global_variable.elements, instance_number, this_threads_files, driver) # Call the Battering ram loop
                        elif global_variable.args.attack == 3: # PITCHFORK ATTACK
                            if not global_variable.terminate:
                                pitchfork_loop(payloads,instance_number,this_threads_files,driver) # Call the Pitchfork loop
                        elif global_variable.args.attack == 4: # CLUSTER BOMB ATTACK
                            if not global_variable.terminate:
                                attempt_clusterbomb_fuzz(payloads,driver,this_threads_files,instance_number) # Call the Cluster bomb attack directly without any loop, this is because cluster bomb's loop logic is written in attempt function it self
                else:
                    raise # Even after three attempts of launching the browser, if there is still error, then raise the exception
        # Algorithm step: 8 Below are Exception handling code, Handle the exceptions which are specific to this thread and do not affect other threads
        except NoSuchWindowException as e: # This exception can be arrived when the user closes the browser window
            log_error(format_exc())
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        except ConnectionRefusedError as e: # This exception can be arrived when the user closes the browser window
            log_error(format_exc())
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        except RemoteDisconnected as e: # This exception can be arrived when the user closes the browser window
            log_error(format_exc())
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        except ProtocolError as e: # This exception can be arrived when the user closes the browser window
            log_error(format_exc())
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed or Remote connection lost, check error log if this is unintentional\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        except MaxRetryError as e: # This exception can be arrived when the user closes the browser window
            log_error(format_exc())
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed or Browsers has reached maximum retries, if you have closed BrowserBruter ignore this else report the issue, check error log if this is unintentional\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        except WebDriverException as e: # This exception can be arrived when there is issue from webdriver object
            log_error(format_exc())
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed or Remote connection lost with following message\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        except SystemExit as e: # This exception is raised when sys.exit() is called
            log_error(format_exc())
        except Exception as e: # Handle the unknown exception
            handle_unknown_exception(e)
        finally: # Algorithm step: 9
            # close the specific thread's driver
            try:
                if driver is not None: # Check if the webdriver.Chrome is null or not, if it is null means driver is not initialized, in case it is not initialized no need to close(if we close it then there will be an exception), else close it.
                    driver.quit() # Close the browser
            except UnboundLocalError: # If there is an error in closing the browser it-self then close the script
                exit(0)