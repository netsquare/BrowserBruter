##################################################################
"""
Name  : final_report.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import log_error

##################################################################
# Importing Python Libraries
##################################################################
import pandas as pd # used to manipulate and handle csv data
import csv # importing csv which will be used in reporting
import datetime # used for getting current time and working with time
import os # used for multiple purpose related to operating system like creating files and directories
from traceback import format_exc # used to format exceptions
from sys import maxsize # This is constant, it defines the maximum bytes a single cell in csv data can hold which is set by system
from sys import exit # used to close the script

##################################################################
"""
Name          -> generate_final_report
Functionality -> Function to Generate Final Report
Algorithm     ->
    1. Set the csv field size limit to maximum size that can be handle by operating system, we need to do this because http request/response can be longer than the max default limit of the data per field of csv.
    2. Get the directory and final_report file path
    3. get the processed payloads file path
    4. get the all temporary report files generated by threads
    5. get the all temporary processed payload files generated by threads
    6. Get the global payloads variable -> get the reference of global variable payloads ( this variable hold all the payloads, when we do the fuzzing, when the payload is used, we remove that payload from this variables, that is how we keep track of remaining payloads)
    7. initialize the index counter called index_counter
    8. open the main final report file in write mode
    9. get the csv writer object on final report file
    10. Insert the columns names which is first raw of the report in other words add field names
    11. for each temporary report generated by threads do following
        a. get that temporary file
        b. open that temporary report file
        c. read its data (report generated by thread)
        d. add all rows present in temporary report to final report one by one
        e. if there is any size limit error then skip that row and continue with other rows
        f. else raise the exception
        g. after all rows from has been copied from temporary file to final report, delete this temporary report file 
    12. if there --row-limit option is present, then split the final report into smaller chunks specified by user
    13. Same as we merged the temporary reports into final report, merge the processed payloads
    14. if attack mode sniper or battering ram, then also add merge final remaining payloads file
    15. print generic information message
    16. Handle the errors
Parameters    -> 
Return        -> 
"""
################################################################## 

def generate_final_report():
    # Algorithm step: 1 Increase the field size limit
    csv.field_size_limit(maxsize)
    print(f"\n\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Generating Final Report\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    # Algorithm step: 2 Get the path path of final report
    directory = f"BrowserBruter_Reports/{global_variable.hostname}/{global_variable.start_time}" # path of directory
    final_report = f"BrowserBruter_Reports/{global_variable.hostname}/{global_variable.start_time}/{global_variable.hostname}-{global_variable.start_time}.csv" # path of final report
    try:
        # Algorithm step: 3 Get the path of processed payload file
        processed_payloads = f"BrowserBruter_Reports/{global_variable.hostname}/{global_variable.start_time}/Processed_Payloads.txt" 
        # Algorithm step: 4 get all temporary reports
        all_threads_files = [file for file in os.listdir(directory) if file.endswith('.csv')]
        # Algorithm step: 5 get all temporary processed payloads files
        all_processed_payloads_files = [file for file in os.listdir(directory) if file.endswith('.txt')]
        # Algorithm step: 6 get the reference of global payloads variable
        # Algorithm step: 7 Initialize index counter
        index_counter = 0
        # Algorithm step: 8 Merge other files into a single final report
        with open(final_report, 'w', newline='') as final: # Open the final report file
            # Algorithm step: 9 get the csv writer object which writes csv data into report
            writer = csv.writer(final)
            # Algorithm step: 10 Insert column names or, in other words, headings
            writer.writerow(['Index', 'Request Time', 'Fuzzing', 'Payload', 'Method', 'URL', 'Request Headers', 'Request Body', 'Response Time', 'Cycle Time MilliSeconds', 'Response Status Code', 'Response Reason', 'Response Headers', 'Response Body', 'Response Length', 'Web Page Before', 'Web Page After'])
            # Algorithm step: 11 Iterate over each CSV file
            for csv_file in all_threads_files: 
                # Algorithm step: 11.a get the temporary file
                file_path = os.path.join(directory, csv_file)
                # Algorithm step: 11.b Open the current temporary CSV file in 'r' mode
                with open(file_path, 'r') as infile:
                    # Algorithm step: 11.c read the temporary csv file and store it in reader object
                    reader = csv.reader(infile)
                    # Algorithm step: 11.d Read and write the rows to the output file
                    try:
                        for row in reader: # For each row present in reader object which holds the rows of temporary csv report file
                            # Insert the index value at the beginning of each row
                            row.insert(0, index_counter)
                            writer.writerow(row) # insert the row
                            # Increment the index counter
                            index_counter += 1 # so if we have written data at row 2, increase the values so next row will be row 3
                    except csv.Error as e: # Algorithm step: 11.e handle the size limit error
                        if "field larger than field limit" in str(e):
                            print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nWARNING:{global_variable.RESET} Field size is too large to handle, replacing field with 'BROWSER-BRUTER-DISCARDED-EXTREMELY-LARGE' - Skipping row {index_counter} in file {csv_file}: {str(e)}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                            # If a row exceeds the field limit, skip writing that row and write a placeholder value instead
                            log_error(f"Skipping row {index_counter} in file {csv_file}: {str(e)}") # Skip the row
                            writer.writerow(['BROWSER-BRUTER-DISCARDED-EXTREMELY-LARGE']) # Write generic message in place of values skipped
                            # Increment the index counter
                            index_counter += 1
                        else: # Algorithm step: 11.f raise exception to handle unknown error
                            raise
                # Algorithm step: 11.g Delete the current CSV file
                os.remove(file_path) 
        # Algorithm step: 12 handle --row-limit option
        if global_variable.args.rows_limit:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(final_report)
            # Split the DataFrame into chunks
            chunks = [df[i:i+global_variable.args.rows_limit] for i in range(0, len(df), global_variable.args.rows_limit)]
            # Write each chunk to a new CSV file
            for i, chunk in enumerate(chunks): # iterate over chunks
                output_file = f"{final_report}_{i}.csv" # create a file
                chunk.to_csv(output_file, index=False) # write to that file
        # Algorithm step: 13 Merge the processed payloads file into one; logic is the same as above
        with open(processed_payloads, 'w', newline='') as final_processed_payloads:
            for one_threads_processed_payloads in all_processed_payloads_files:
                file_path = os.path.join(directory, one_threads_processed_payloads)
                with open(file_path, 'r') as infile:
                    for i in infile:
                        final_processed_payloads.write(i)
                        if global_variable.args.attack in (1, 2):
                            # keeping track of remaining payloads by removing processed payloads from payload[] list
                            try:
                                global_variable.payloads.remove(i.strip())
                            except ValueError:
                                pass
                # Delete the current thread's processed payloads file
                os.remove(file_path)
        # Algorithm step: 14 for sniper and battering ram attack mode, also create file for remaining payloads
        if global_variable.args.attack in (1, 2):
            # Storing remaining payloads in a separate file, logic is same as above, we do this as global payloads variable only holds the remaining payloads after the attack, the processed payload has been removed from this list
            remaining_payloads = os.path.join(directory, "Remaining_Payloads.txt")
            with open(remaining_payloads, 'w', newline='') as remaining_payloads_file:
                for payload in global_variable.payloads: # iterate over each remaining payload
                    remaining_payloads_file.write(payload + '\n')
            print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Remaining Payloads (if any) have been stored -> {remaining_payloads}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        # Algorithm step: 15 print generic messages
        print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Processed Payloads (if any) have been stored -> {processed_payloads}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Report Generated -> {final_report}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        end_time_int = datetime.datetime.now() # Get the time when script is finished
        end_time_str = end_time_int.strftime("%Y-%m-%d_%H-%M-%S") # format the end time
        total_time = end_time_int - global_variable.start_time_int # End time - start time = total time
        total_time_str = str(total_time).split('.')[0] # get the first part of the total time
        print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Fuzzing end time ->  {end_time_str} Total Running time -> {total_time_str}\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    # Algorithm step: 16 handle the exceptions
    except ConnectionRefusedError as e:
        log_error(format_exc())
        print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO: {global_variable.RESET}Browser's window has been closed, closing the BrowserBruter, check error log if this is unintentional\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
    except FileNotFoundError:
        log_error(format_exc())
        exit(0)

##################################################################
"""
The block of code for reporting logic ends here
"""
##################################################################
