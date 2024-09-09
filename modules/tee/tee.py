##################################################################
"""
Name  : tee.py 
Date  : 12/11/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
"""
Algorithm -> 
1. Define a class 'Tee' with methods '__init__', 'write', and 'flush'.
2. In the '__init__' method:
   - Accept a 'log_file' argument, which is the path to the log file.
   - Store the 'log_file' path in an instance variable 'self.log_file'.
   - Store the original standard output stream in an instance variable 'self.stdout_orig'.
3. In the 'write' method:
   - Accept a 'text' argument, which is the text to be written.
   - Write the 'text' to the original standard output stream using 'self.stdout_orig.write(text)'.
   - Open the log file in append mode using a 'with' statement and write the 'text' to the log file.
4. In the 'flush' method:
   - Flush the buffer of the original standard output stream using 'self.stdout_orig.flush()'.

This file is used to replicate the functionality of the tee tool.
This will print the script output to console as well as logs file
"""
##################################################################

import sys

class Tee:  # Creating a class called Tee
    def __init__(self, log_file):  # Defining the constructor method, which initializes the class instance
        self.log_file = log_file  # Assigning the log file name/path to an instance variable
        self.stdout_orig = sys.stdout  # Storing the original standard output stream in an instance variable

    def write(self, text):  # Defining a method to write text to both the standard output and the log file
        self.stdout_orig.write(text)  # Writing the text to the original standard output stream
        with open(self.log_file, 'a') as log:  # Opening the log file in append mode
            log.write(text)  # Writing the text to the log file

    def flush(self):  # Defining a method to flush the output stream buffers
        self.stdout_orig.flush()  # Flushing the buffer of the original standard output stream

