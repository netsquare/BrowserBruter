##################################################################
"""
Name  : show_request_response.py 
Date  : 21/06/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
CopyRight: Net-Square Solutions PVT LTD
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.report_explorer.global_variables.global_variables import re_global_variable

##################################################################
"""
Name          -> show_request_response
Functionality -> Function to show request/response details when a Treeview item is selected
Algorithm     ->
    1. Get the selected item from the Treeview
    2. Define required columns for request/response details
    3. Check if required columns are present in the DataFrame
    4. Extract details from the DataFrame based on the selected index
    5. Build full request and response strings
    6. Display request and response details in the respective Text widgets
    7. Display web page before and after details in the respective Text widgets
    8. Handle missing columns error
Parameters    -> event,tree,tk,request_text,response_text,web_page_before_text,web_page_after_text,messagebox
Return        -> 
"""
##################################################################

def show_request_response(event, tree, tk, request_text, response_text, web_page_before_text, web_page_after_text, request_text_base64, response_text_base64, messagebox):
    # Allow time for selection to change
    tree.after(1, lambda: _process_selection(tree, tk, request_text, response_text, web_page_before_text, web_page_after_text, request_text_base64, response_text_base64, messagebox))

def _process_selection(tree, tk, request_text, response_text, web_page_before_text, web_page_after_text, request_text_base64, response_text_base64, messagebox):
    # Get the newly selected item from the Treeview
    selected_item = tree.selection()
    if selected_item:
        iid = selected_item[0]
        index = tree.index(iid)

        # Define required columns for request/response details
        required_columns = ['Method', 'URL', 'Request Headers', 'Response Status Code', 'Web Page Before', 'Web Page After', 'Response Body', 'Request Body', 'Base64 Request', 'Base64 Response']

        # Check if required columns are present in the DataFrame
        if all(col in re_global_variable.df.columns for col in required_columns):
            if index in re_global_variable.df.index:
                # Extract details from the DataFrame based on the selected index
                method = re_global_variable.df.at[index, 'Method']
                url = re_global_variable.df.at[index, 'URL']
                request_headers = re_global_variable.df.at[index, 'Request Headers']
                request_body = re_global_variable.df.at[index, 'Request Body']

                response_status = re_global_variable.df.at[index, 'Response Status Code']
                response_reason = re_global_variable.df.at[index, 'Response Reason']
                response_headers = re_global_variable.df.at[index, 'Response Headers']
                response_body = re_global_variable.df.at[index, 'Response Body']

                web_page_before = re_global_variable.df.at[index, 'Web Page Before']
                web_page_after = re_global_variable.df.at[index, 'Web Page After']

                request_base64 = re_global_variable.df.at[index, 'Base64 Request']
                response_base64 = re_global_variable.df.at[index, 'Base64 Response']

                # Build full request and response strings
                full_request = f"{method} {url}\n{request_headers}\n{request_body}"
                full_response = f"HTTP/1.1 {response_status} {response_reason}\n{response_headers}\n{response_body}"

                # Display request and response details in the respective Text widgets
                request_text.delete(1.0, tk.END)
                response_text.delete(1.0, tk.END)
                request_text.insert(tk.END, full_request)
                response_text.insert(tk.END, full_response)
                
                # Display the base64 data
                request_text_base64.delete(1.0, tk.END)
                response_text_base64.delete(1.0, tk.END)
                request_text_base64.insert(tk.END, request_base64)
                response_text_base64.insert(tk.END, response_base64)
            
                # Display web page before and after details in the respective Text widgets
                web_page_before_text.delete(1.0, tk.END)
                web_page_after_text.delete(1.0, tk.END)
                web_page_before_text.insert(tk.END, web_page_before)
                web_page_after_text.insert(tk.END, web_page_after)
        else:
            # Handle missing columns error
            messagebox.showerror("Error", "Required columns are missing in the DataFrame.")
