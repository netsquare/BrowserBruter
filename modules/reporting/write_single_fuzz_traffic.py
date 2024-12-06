##################################################################
"""
Name  : write_single_fuzz_traffic.py 
Date  : 13/03/2023
Author: Jafar Pathan 
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
import csv # importing csv which will be used in reporting
import urllib.parse # used to decode the HTTP response and request
import gzip # used for gzip decompression of http response
import zlib # used for zlib decompression of http response
import brotli # used for brotli decompression of http response
import zstandard # used for zstd decompression of http response
import base64 # used to encode the raw http request and response
from traceback import format_exc
from bs4 import BeautifulSoup as bs # used to make html into pretty format
from urllib.parse import urlparse # used to parse the url

##################################################################
"""
Name          -> write_http_request_response
Functionality -> Function to write single http request/response into specific thread's file
Algorithm     -> 
    1. Open the Current threads specific temporary report file in append mode
    2. Get the requests and store them in captured_requests
    3. if --inscope-urls options is there then remove all Requests to url which are not included in --inscope-urls
    4. else remove requests which are for different hosts, or which are out of scope
        a. remove the requests for static files
        b. remove the requests which does not contains urls present in list_of_urls_to_be_excluded_from_final_report list
    5. Get the csv writer object
    6. for each request do following
        a. decode the request body into UTF-8 from binary
        b. get the request and response time
        c. Get the response body and store it in raw binary format
        d. convert the binary response body from raw binary to proper encoding or decompress it if required
        e. URL decode the request and response
        f. define and initialize the BeautifulSoup4 object
        g. Refactor the HTML of response into pretty format
        h. Create a row object which will hold all the values for csv report's single row
        i. write this row into report
        j. if --verbose flag is present then print this HTTP request/response on console as well
        k. If there is an AttributeError then place '0' and "N/A" in the fields that causes this issue and move on
Parameters    -> element(element), this_threads_file(string), driver(webdriver.Chrome),
 payload(string), webpage_before(string), webpage_after(string)
Return        -> 
"""
################################################################## 

def write_http_request_response(element, this_threads_file, driver, payload, webpage_before, webpage_after):
    # Algorithm step: 1 open the temporary report file to write the data
    with open(this_threads_file, 'a', newline='') as report:
        # Algorithm step: 2 Filtering requests that are in scope
        captured_requests = driver.requests
        # Algorithm step: 3 filter the request based on --inscope-urls option
        if global_variable.args.inscope_urls:
            filtered_requests = [single_request for single_request in captured_requests if any([single_request.url in global_variable.list_of_urls_to_be_included_in_final_report])]    
        else: # Algorithm step: 4 filter the requests
            filtered_requests = [single_request for single_request in captured_requests if # Filtering request based on hostname and out of scope 
                         urlparse(single_request.url).hostname == global_variable.hostname or
                         any(urlparse(single_request.url).hostname == scope_hostname for scope_hostname in global_variable.scope_hostnames)]
            filtered_requests = [single_request for single_request in filtered_requests if all(extension not in single_request.url for extension in global_variable.forbidden_extensions)] # # Algorithm step: 4.a removing static files
            filtered_requests = [single_request for single_request in filtered_requests if all(extension not in single_request.url for extension in ['.js', '.css', '.txt','.woff2','.woff'])] # Algorithm step: 4.a remove static files
            filtered_requests = [single_request for single_request in filtered_requests if all([single_request.url not in global_variable.list_of_urls_to_be_excluded_from_final_report])] # Algorithm step: 4.b
        # Algorithm step: 5 get the csv writer
        writer = csv.writer(report)
        # Algorithm step: 6. 
        for request in filtered_requests: # For each request
            try:
                base64_request = None
                base64_response = None
                # Converting request into base64
                request_headers_for_bs64 = "\r\n".join(f"{header}: {value}" for header, value in request.headers.items())
    
                # Combine headers and raw body
                if request.body:
                    raw_data_request = f"{request.method} {request.path} HTTP/1.1\r\n{request_headers_for_bs64}\r\n\r\n".encode('utf-8') + request.body
                else:
                    raw_data_request = f"{request.method} {request.path} HTTP/1.1\r\n{request_headers_for_bs64}\r\n\r\n".encode('utf-8')

                # Encode the raw data in Base64
                base64_request = base64.b64encode(raw_data_request).decode('utf-8')

                # Converting response into base64
                response_headers_for_bs64 = "\r\n".join(f"{header}: {value}" for header, value in request.response.headers.items())
                # Combine headers and raw body
                if request.response.body:
                    raw_data_response = f"HTTP/1.1 {request.response.status_code} {request.response.reason}\r\n{response_headers_for_bs64}\r\n\r\n".encode('utf-8') + request.response.body
                else:
                    raw_data_response = f"HTTP/1.1 {request.response.status_code} {request.response.reason}\r\n{response_headers_for_bs64}\r\n\r\n".encode('utf-8')
                # Encode the raw data in Base64
                base64_response = base64.b64encode(raw_data_response).decode('utf-8')
            except Exception as e:
                log_error(format_exc())
                if global_variable.args.debug:
                    print(e)
                    pass
                else:
                    pass
                
            try: # Algorithm step: 6.a decode the request body
                request_body = request.body.decode("UTF-8")
            except UnicodeDecodeError:
                request_body = request.body
            try:
                # Check if the base64 request or base64 response are not none
                if base64_response is None:
                    base64_response = "N/A"
                if base64_request is None:
                    base64_request = "N/A"
                # Algorithm step: 6.b Get request response time
                request_time = request.date
                response_time = request.response.date
                # Calculate the cycle time in milliseconds
                cycle_time_in_milliseconds = int((response_time - request_time).total_seconds() * 1000)
                # Algorithm step: 6.c decode the response body
                raw = request.response.body
                # Algorithm step: 6.d here getting the value of 'Content-Encoding' response header to know how to decode the response
                encoding = request.response.headers.get('Content-Encoding', 'UTF-8')
                if encoding.lower() == 'gzip': # if 'Content-Encoding' is gzip then decompress it using gzip
                    raw = gzip.decompress(raw)
                elif encoding.lower() == 'br': # brtoli decompression
                    raw = brotli.decompress(raw)
                elif encoding.lower() == 'deflate': # deflate decompression
                    raw = zlib.decompress(raw, -zlib.MAX_WBITS)
                elif encoding.lower() == 'zstd': # zstd decompression
                    zdecompressor = zstandard.ZstdDecompressor()
                    raw = zdecompressor.decompress(raw)    
                else:
                    raw = raw.decode(encoding, errors='replace') # Else if the 'Content-Encoding' contains some other encoding then decode to that specific decoding
                # Algorithm step: 6.e URL Decode the request and response bodies
                request_body = urllib.parse.unquote(request_body)
                try:
                    raw = urllib.parse.unquote(raw) # URL decode 
                except Exception as e:
                    log_error(format_exc())
                    pass
                # Algorithm step: 6.f prettifying the html in response
                soup = bs(raw, features="html.parser") # creating object of beautiful soup
                response_body = soup.prettify() if hasattr(soup, 'prettify') else raw.decode("UTF-8", errors="replace") # Algorithm step: 6.g prettifying the html 
                # Algorithm step: 6.h create a row variable holding all the data of single row to be written in report
                row = [value if value else ' ' for value in
                    [request_time.strftime('%Y-%m-%d %H:%M:%S'), str(element), str(payload), request.method, urllib.parse.unquote(request.url), request.headers, request_body, response_time.strftime('%Y-%m-%d %H:%M:%S'), 
                    cycle_time_in_milliseconds, request.response.status_code, request.response.reason, request.response.headers, response_body,
                    len(request.response.body), bs(webpage_before,features="html.parser").prettify(), 
                    bs(webpage_after,features="html.parser").prettify(), base64_request, base64_response]]
                # Algorithm step: 6.i write the row in report
                writer.writerow(row)
                # Algorithm step: 6.j Check whether the output should be printed on the console or not
                if global_variable.args.verbose:
                    # Print the request
                    print(f'\n{global_variable.GREEN}[+]---------------------Single Request/Response Cycle-------------------[+]')
                    print(f"Fuzzing - " + str(element))
                    print(f"Payload - " + str(payload))
                    print(f'[+]----------------------REQUEST---------------------[+]{global_variable.RESET}')
                    print('Time - ' + request_time.strftime('%Y-%m-%d %H:%M:%S') + '\n', request.method, urllib.parse.unquote(request.url))
                    # Print in a new line
                    print(request.headers, request_body)
                    # Print the response
                    print(f'{global_variable.GREEN}[+]----------------------RESPONSE--------------------[+]{global_variable.RESET}')
                    if request.response:
                        print(
                            'Time - ' + response_time.strftime('%Y-%m-%d %H:%M:%S') + '\n',
                            request.response.status_code,
                            request.response.reason
                        )
                    print(request.response.headers)
                    print(response_body)
                    print(f"{global_variable.GREEN}[+]--------------------------------------------------------------------------------------------------------------------------[+]\n\nTIME: {cycle_time_in_milliseconds} MilliSeconds \n\n[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
            # Algorithm step: 6.k handle the AttributeError
            except AttributeError as e:
                # Code to handle if no request has been made and there is no response
                if global_variable.args.verbose:
                    print(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} No response is received skipping report row!\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                # recreate the row and fill '0' and "N/A" in place of fields which causes this exceptions
                row = [value if value else ' ' for value in 
                    [request_time.strftime('%Y-%m-%d %H:%M:%S'), str(element), str(payload), request.method, urllib.parse.unquote(request.url), request.headers, request_body, request_time.strftime('%Y-%m-%d %H:%M:%S'), 
                    '0', '0', "N/A", "N/A", "N/A",
                    '0', bs(webpage_before,features="html.parser").prettify(), 
                    bs(webpage_after,features="html.parser").prettify(), base64_request, base64_response]]
                # write the row to report
                writer.writerow(row)