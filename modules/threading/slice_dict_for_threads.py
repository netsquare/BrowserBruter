##################################################################
"""
Name  : slice_dict_for_threads.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
"""
Name          -> slice_dict_for_threads
Functionality -> This function is used to slice the dictionary to support multi threading  
Algorithm     ->
    1. create result variable which will store list
    2. Create loop which will iterate for each threads which will do following
        a. Create this threads unique dictionary which will store combination of payloads and elements
        b. Create one more loop which will iterate over each input_dictionary item
            1.   Get total elements
            2.   Divide elements per thread
            3.   Assign the start_index
            4.   Assign end_index
            5.   Assign the values from start_index to end_index to this thread's dictionary
        c. append the inner loops result
    3. Return the dictionary
Parameters    -> input_dict(dictionary), num_threads(int)
Return        -> result(list of dictionaries)
"""
##################################################################

def slice_dict_for_threads(input_dict, num_threads):
    result = [] # Algorithm step: 1 This variable will store list of dictionaries
    for i in range(num_threads): # Algorithm step: 2 Loop to create dictionary slices for each thread
        thread_dict = {} # Algorithm step: 2.a This variable will store single dictionaries for specific thread and will be appended into result list
        for key, values in input_dict.items(): # Algorithm step: 2.b Iterate through each key-value pair in the input dictionary
            total_elements = len(values) # Algorithm step: 2.b.1 Get the total number of elements for the current key, Example: total_elements = 10
            elements_per_thread = total_elements // num_threads # Algorithm step: 2.b.2 Divide the total elements by number of threads, Example: num_threads = 3, elements_per_thread = 10 // 3 = 3
            start_index = i * elements_per_thread # Algorithm step: 2.b.3 Calculate the starting index for the current thread, Example: i = 0, start_index = 0 * 3 = 0
            end_index = (i + 1) * elements_per_thread if i < num_threads - 1 else total_elements # Algorithm step: 2.b.4 Calculate the end index, Example: i = 0, end_index = (0 + 1) * 3 = 3, for the last thread end_index = total_elements
            thread_dict[key] = values[start_index:end_index] # Algorithm step: 2.b.5 Slice the values for the current thread, Example: values = [v1, v2, ..., v10], for i = 0, thread_dict[key] = [v1, v2, v3]
        result.append(thread_dict) # Algorithm step: 2.c Append the dictionary slice to the result list
    return result # Algorithm step: 3 Return the list of dictionary slices