##################################################################
"""
Name  : BrowserBruter.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################
################################################################
"""
This is the main file of the Browser Bruter tool.

Algorithm: 
    1. Import required libraries
    2. Initialize Arguments
    3. Initialize global variable object using singleton class
    4. Check if all required arguments are present and arguments have proper values
    7. Check if script is started as standalone script or imported into another script
    5. Print the banner
    8. Start the keyboard thread for resuming and pausing the script
    9. Handle the verbosity of the script
    10. Print generic console messages
    11. Start the threads and divide the payloads among them
    12. Start the browser
    13. launch the attack
    14. wait for all threads to finish the attack
    15. generate the report
    16. end
"""
##################################################################

##################################################################
"""
The block of code for importing python libraries
as well as custom python code starts here
"""
##################################################################

##################################################################
# Importing Python Libraries
##################################################################
import signal # used for handling CTRL+C key
import threading # used for threads and running multiple browser at same time
import os # used for multiple purpose related to operating system like creating files and directories
from itertools import product # used for creating payloads combination for clusterbomb attack
from traceback import format_exc, print_exc # used for getting the proper exceptions
from time import sleep # used for pausing the script
import warnings
import sys

##################################################################
# Importing Custom Modules
##################################################################
from modules.pause_and_stop.pause_menu import pause_resume
from modules.misc_functions.print_banner import print_banner
from modules.error_handling.error_handling import log_error
from modules.misc_functions.sleep_while_pause import sleep_while_pause
from modules.pause_and_stop.signal_handler import signal_handler
from modules.run_browser.run_browser import run_browser_instance
from modules.threading.slice_dict_for_threads import slice_dict_for_threads
from modules.reporting.final_report import generate_final_report
from modules.error_handling.error_handling import handle_unknown_exception
from modules.global_config_arguments.global_variables import global_variable
# from modules.tee.tee import Tee # res.tee contains code which prints the output of the Browser Bruter on console as well as log file
from modules.automatic_navigation_handler.record_navigation import record_navigation

##################################################################
# Importing various Exceptions
##################################################################
from bs4 import MarkupResemblesLocatorWarning
from bs4 import XMLParsedAsHTMLWarning

##################################################################
"""
The block of code for imports ends here
"""
##################################################################

##################################################################
"""
The block of code for Main Execution starts here

Algorithm ->
    1. check if script is started as standalone or not
    2. Create and start the keyboard listener thread to handle CTRL+C
    3. If verbosity has to implement, then create
      BrowserBruterSTDOUT.txt file and create object of Tee class
      which will redirect the output of the browserbruter to both
      console and log file.
    4. Print generic information console
    5. Get the number of threads and store it in num_threads variable
    6. Initialize threads, start and threads_interval_time variables
    7. If attack is either sniper or battering ram then
        a. divide the payloads equally among threads
        b. start the threads and assign them their respective list of payloads
    8. If attack is pitchfork then
        a. Divide the elements_payloads dictionary combination into smaller dictionaries
        b. start the threads and assign them their respective elements:payloads_list dictionary
    9. If attack is clusterbomb then
        a. first create all possible combination of payloads
        b. Divide this combination of payloads equally among threads into smaller chunks
        c. start the threads and assign them their respective payloads combination chunks
    10. Wait for all threads to finish and after that set the terminate flag so the keyboard thread also stops
    11. Handle any exception
    12. In finally call the generate_final_report() method to generate the report no matter what happens
    13. If the script is not started as standalone script then print generic message and exit
"""
##################################################################

# Algorithm step:1 Checking if script is running directly
if __name__ == "__main__": # Check that the script is started directly and not imported
    try:
        # print banner
        print_banner()
        
        #try:
        # Creating Reports directory in current directory to store reports
        os.makedirs("BrowserBruter_Reports",exist_ok=True) # create BrowserBruter_Reports directory
        os.makedirs(f"BrowserBruter_Reports/{global_variable.hostname}/{global_variable.start_time}",exist_ok=True) # create directory with target hostname and inside that new directory with current time
        os.makedirs("logs",exist_ok=True) # create directory to store the logs
            #if "permission" in e.message:
            #print(e)


        # If --record-navigation is set then start the browser to start recording the navigation
        if global_variable.args.record_navigation:
            record_navigation()
            sys.exit(0)

        # Supress the http encoding and bs prettify warnings
        warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)
        warnings.filterwarnings("ignore", category=UnicodeWarning)
        warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
        # Algorithm step:2 Create and start the keyboard listener thread which will pause and resume the BrowserBruter
        keyboard_thread = threading.Thread(target=pause_resume,daemon=True) # This thread will run independently of browser threads, and will look for key press event console, if key is pressed then this thread will throw and signal to pause the script. Also starting this thread as daemon because we want it close when script's main thread is closed.
        keyboard_thread.start()
        # NOTE: Algorithm step:3 Abandoned, not required now.
        # Algorithm step:3 If only verbose or debug flag is set then track logs else do not track STDOUT console output on logs/BrowserBruterSTDOUT.txt file
        #if global_variable.args.verbose or global_variable.args.print_error:
        #    # Redirect stdout to the Tee class, the tee class redirects STDOUT to STDOUT and the log file only if --verbose flag or --print-error flag is set
        #    log_file = 'logs/BrowserBruterSTDOUT.txt'  # This file stores console output
        #    tee_instance = Tee(log_file) # Tee -> this will print the output on console as well as redirect the STDOUT to logs/BrowserBruterSTDOUT.txt file, This functionality is written in res/tee.py
        #    stdout = tee_instance # Setting Operating System's STDOUT to tee_instance, look -> res/tee.py for more info.
        #    print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Either --verbose or --print-error flag detected creating logs in -> {log_file}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        # Algorithm step:4 Print legal disclaimer and general info about target and payloads
        print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nLegal Warning:{global_variable.RESET} This Browser-Bruter open-source penetration testing tool is Copyrighted Property of Net-Square Solutions PVT LTD. provided for educational and ethical purposes only. Users are solely responsible for ensuring compliance with all applicable laws and regulations, and the developer(s) disclaim any liability for misuse or damage caused by the tool.\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\n{global_variable.RESET}")
        print(f"{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]")
        print(f"{global_variable.BLUE}[+] Start Time : {global_variable.RESET}{global_variable.start_time}") # Print start time
        print(f"{global_variable.BLUE}[+] Target URL : {global_variable.RESET}{global_variable.args.target}") # Print URL
        if global_variable.args.attack == 1: # If attack mode is sniper
            print(f"{global_variable.BLUE}[+] Attack Mode: {global_variable.RESET}SNIPER") # Print attack mode
            print(f"{global_variable.BLUE}[+] Elements   : {global_variable.RESET}{global_variable.args.elements}") # Print elements
            print(f"{global_variable.BLUE}[+] Payloads   : {global_variable.RESET}{global_variable.args.payloads}")
        if global_variable.args.attack == 2:
            print(f"{global_variable.BLUE}[+] Attack Mode: {global_variable.RESET}BATTERING RAM") # Print attack mode
            print(f"{global_variable.BLUE}[+] Elements   : {global_variable.RESET}{global_variable.args.elements}") # Print elements
            print(f"{global_variable.BLUE}[+] Payloads   : {global_variable.RESET}{global_variable.args.payloads}")
        if global_variable.args.attack == 3:
            print(f"{global_variable.BLUE}[+] Attack Mode: {global_variable.RESET}PITCH FORK") # Print attack mode
            for element_payload in global_variable.args.elements_payloads.split(','): # Divide --elements-payloads into elements:payloads
                element, payload_file_path = element_payload.split(':')
                print(f"{global_variable.BLUE}[+] Elements:Payloads: {global_variable.RESET}{element}:{payload_file_path}") # Print elements:payloads
        if global_variable.args.attack == 4:
            print(f"{global_variable.BLUE}[+] Attack Mode: {global_variable.RESET}CLUSTER BOMB") # Print attack mode
            for element_payload in global_variable.args.elements_payloads.split(','): # Divide --elements-payloads into elements:payloads
                element, payload_file_path = element_payload.split(':')
                print(f"{global_variable.BLUE}[+] Elements:Payloads: {global_variable.RESET}{element}:{payload_file_path}") # Print elements:payloads
        print(f"{global_variable.BLUE}[+] Button     : {global_variable.RESET}{global_variable.args.button}")
        print(f"{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]")
        print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Press ENTER to pause the attack.\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\n{global_variable.RESET}")
        # Algorithm step:5 Get the number of threads or in other words number of browsers instances to use supplied by user using --threads argument
        num_threads = global_variable.args.threads
        # Algorithm step:6 Create and start the threads
        threads = [] # Creating empty list variable to store the threads variables
        start = 0 # This variable is used for indicating the start of payloads for all threads, look below examples for better understanding
        threads_interval_time = 2.5 # threads_interval_time indicates the delay or pause before starting new thread (launching new browser instance)
        if global_variable.args.threads: # Check if there is --threads argument
            if global_variable.args.threads > 10:
                threads_interval_time = 6 # If --threads values is more than 10 then set delay before launching new browser to 6 seconds to improve stability
            elif global_variable.args.threads > 5:
                threads_interval_time = 4 # If --threads values is more than 5 then set delay before launching new browser to 4 seconds to improve stability
        if global_variable.args.attack in (1,2): # Algorithm step:7 Below logic for launching new browser instance and fuzzing the application using threads for sniper and battering ram attack because payloads and elements are independent simple list
            # Algorithm step:7.a Divide the payload data equally among the threads
            payloads_per_thread = len(global_variable.payloads) // num_threads # Divide total number of payloads by total number of threads, Example: len(payloads) = 10, num_threads = 3, payloads_per_thread = 10 // 3 = 3
            extra_payloads = len(global_variable.payloads) % num_threads # If total number of payloads is not divisible by total number of threads then count the remainder as extra payloads, Example: len(payloads) = 10, num_threads = 3, extra_payloads = 10 % 3 = 1
            for i in range(num_threads): # Algorithm step:7.b Repeat below code for --threads number of times, Example: num_threads = 3, loop will run with i = 0, 1, 2
                if not global_variable.terminate: # Check if user has pressed the CTRL+C before starting any new thread, if yes then this terminate flag will be set and do not launch any more browsers
                    try:
                        end = start + payloads_per_thread # Example: start = 0, payloads_per_thread = 3, end = 0 + 3 = 3
                        if i < extra_payloads: # Distribute extra payloads to the first few threads
                            end += 1 # Example: i = 0, extra_payloads = 1, end = 3 + 1 = 4 for the first thread
                        thread_payloads = global_variable.payloads[start:end] # Extract the payloads for the current thread
                        # Example: payloads = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
                        # For i = 0, start = 0, end = 4, thread_payloads = [p1, p2, p3, p4]
                        # For i = 1, start = 4, end = 7, thread_payloads = [p5, p6, p7]
                        # For i = 2, start = 7, end = 10, thread_payloads = [p8, p9, p10]
                        thread = threading.Thread(target=run_browser_instance, args=(thread_payloads,i))  # Create a thread with the target function and arguments, Example: i = 0, thread_payloads = [p1, p2, p3, p4], creates a thread with these arguments
                        # Sleep while pause, after starting the thread if the user has paused the script then wait and do not run the script
                        sleep_while_pause()
                        # Start the thread
                        thread.start()
                        # Add the thread to the list of threads
                        threads.append(thread)
                        start = end # Update the starting index for the next thread, Example: start = 4 for the next iteration of the loop
                        # Sleep for 2.5 seconds for proper resource management
                        sleep(threads_interval_time)
                    except KeyboardInterrupt as e: # This exception has raised when user has pressed CTRL+C one time or more than one time.
                        signal_handler(signal.SIGINT, None) # Call the CTRL+C handler
                        log_error(format_exc())
                        sys.exit(0)
        elif global_variable.args.attack == 3: # Algorithm step:8
            threaded_dicts = slice_dict_for_threads(global_variable.elements_payloads, num_threads) # Algorithm step:8.a Call the slice_dict_for_threads to divide the payloads equally among the threads, Example: elements_payloads = {'key1': [v1, v2, ..., v10]}, num_threads = 3, threaded_dicts = [{'key1': [v1, v2, v3]}, {'key1': [v4, v5, v6]}, {'key1': [v7, v8, v9, v10]}]
            try:
                for i, thread_dict in enumerate(threaded_dicts, start=1): # Algorithm step:8.b Iterate through the sliced dictionaries
                    if not global_variable.terminate: # Check termination flag
                        # Create a thread with the target function and arguments
                        thread = threading.Thread(target=run_browser_instance, args=(thread_dict, i))
                        thread.start() # Start the thread
                        threads.append(thread) # Append the thread in threads list
                        sleep(2.5)  # Sleep for 2.5 seconds for proper resource management
            except KeyboardInterrupt as e: # Handle the keyboard interrupt
                signal_handler(signal.SIGINT, None)
                log_error(format_exc())
                sys.exit(0)
        elif global_variable.args.attack == 4: # Algorithm step:9
            payloads_combinations = list(product(*global_variable.elements_payloads.values())) # Algorithm step:9.a Create a list to store all combinations of payloads, Example: elements_payloads = {'key1': [v1, v2], 'key2': [v3, v4]}, payloads_combinations = [(v1, v3), (v1, v4), (v2, v3), (v2, v4)]
            chunk_size = len(payloads_combinations) // num_threads # Algorithm step:9.b Split the workload equally among threads
            chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads - 1)] # Example: len(payloads_combinations) = 4, num_threads = 2, chunk_size = 4 // 2 = 2
            chunks.append(((num_threads - 1) * chunk_size, len(payloads_combinations))) # Example: chunks = [(0, 2)], for the last chunk manually append the range, Example: chunks = [(0, 2), (2, 4)]
            # Algorithm step:9.c Create and start the threads
            for instance_number, (start, end) in enumerate(chunks):  # Iterate through the chunks
                if not global_variable.terminate:
                    thread_combinations = payloads_combinations[start:end] # Slice the combinations for the current thread
                    # Example: for instance_number = 0, thread_combinations = [(v1, v3), (v1, v4)]
                    # Example: for instance_number = 1, thread_combinations = [(v2, v3), (v2, v4)]
                    # Create a thread with the target function and arguments
                    thread = threading.Thread(target=run_browser_instance, args=(thread_combinations, instance_number))
                    # Start the thread
                    thread.start()
                    threads.append(thread)
                    # Sleep for 5 seconds for proper resource management
                    sleep(5)     
        # Algorithm step:10 Wait for all threads to finish
        for thread in threads:
            try:
                thread.join()
            except KeyboardInterrupt:
                log_error(format_exc())
        # Set the terminate flag so the keyboard thread stops
        terminate = True
    # Algorithm step:11
    except PermissionError as e:
        log_error(format_exc())
        if global_variable.args.print_error:
            print_exc()
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}BrowserBruter does not have WRITE PERMISSION to 'BrowserBruter_Reports/' or 'logs/' folder. This is not an issue with Browser Bruter.\nKindly run the following command to solve the issue {global_variable.BLUE}'sudo chmod 777 -R ./BrowserBruter_Reports && sudo chmod 777 -R ./logs'{global_variable.RESET} and the issue will be resolved. If issue still persists then Contact the dev at https://github.com/netsquare/BrowserBruter\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        sys.exit(0)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
        log_error(format_exc())
        sys.exit(0)
    except ConnectionRefusedError as e:
        log_error(format_exc())
        print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    except SystemExit:
        log_error(format_exc())
        print("")
    except Exception as e:
        handle_unknown_exception(e)
    finally: # Algorithm step:12
        # Generate the report
        if not global_variable.args.record_navigation:
            generate_final_report()
        # Reset sys.stdout to the console at the end
        #if global_variable.args.verbose or global_variable.args.print_error:
            #sys.stdout = sys.__stdout__
        # Ensure terminal is in 'echo' mode
        os.system('stty echo')
        sys.exit(0)      
else: # Algorithm step:13
    print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nError:{global_variable.RESET} Please run the script again using python3 BrowserBruter.py, closing the BrowserBruter\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    if global_variable.args.print_error:
        print_exc()
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Refer Above Stack Trace\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")

##################################################################
"""
The block of code for Main Execution ends here
"""
##################################################################

