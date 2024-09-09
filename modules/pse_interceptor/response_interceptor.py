
##################################################################
"""
Name  : response_interceptor.py 
Date  : 13/03/2023
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import handle_unknown_exception

##################################################################
# Importing Python Libraries
##################################################################
import gzip # used for gzip decompression of http response
import zlib # used for zlib decompression of http response
import brotli # used for brotli decompression of http response
import zstandard # used for zstd decompression of http response
import re # used to fetch the import statements

##################################################################
"""
Name          -> intercept_response
Functionality -> Function to intercept response and replace HTTP response body, and execute python code
Algorithm     ->
    1. delete the 'Content-Length' header from response as we are going to update it later
    2. if --replace-code option is there then
        a. if 'Content-Encoding' option does not exist then set the decoding as 'utf-8'
        b. else set the response encoding specified in 'Content-Encoding' header
        c. if there is a key error then set the response encoding as 'utf-8' again
        d. decode the response body as per the encoding
        e. for each string which are to be replaced in response present in replacement_pairs, replace it with the string specified by user
        f. delete the 'Content-Encoding' header
        g. Set the 'Content-Encoding' as 'utf-8' 
        h. Add the new response body in HTTP response
        i. update the 'Content-Length' header
    3. if --replace-files options is present then
        a. for each file to be replaced:
            1. get the filename and file url from user supplied value
            2. if file url matches the current HTTP response's url then 
                a. delete the 'Content-Encoding' header
                b. set content encoding as 'utf-8'
                c. replace the HTTP response body with replacement file's content
                d. update the HTTP response 'content-length' header
    4. if there python code to execute on HTTP response then
        a. if 'Content-Encoding' option does not exist then set the decoding as 'utf-8'
        b. else set the response encoding specified in 'Content-Encoding' header
        c. if there is a key error then set the response encoding as 'utf-8' again
        d. decode the response body as per the encoding
        e. create dictionary of objects which are to be passed to the python scripting engine 
        f. execute the python using exec() method and pass the request, response and response_body to the exec() method
        g. if there is any error then check if this is first round of fuzzing, if yes then global_variable.terminate the script else move on
Parameters    -> request(request), response(response)
Return        -> 
"""
##################################################################

def intercept_response(request, response):
    # Algorithm step: 1 Delete the content length header, because we will update it later.
    del request.response.headers['Content-Length']
    if global_variable.args.replace_code:
        try:
            # Algorithm step: 2.a. if 'Content-Encoding' option does not exist then set the decoding as 'utf-8'
            if response.headers['Content-Encoding'] == None:
                response_body_encoding = 'utf-8'  # setting encoding as 'utf-8'
            else:
                # Algorithm 2.b. else set the response encoding specified in 'Content-Encoding' header
                response_body_encoding = response.headers['Content-Encoding']
        except KeyError:
            # Algorithm step: 2.c. if there is a key error then set the response encoding as 'utf-8' again
            response_body_encoding = 'utf-8'
        # Algorithm step: 2.d. decode the response body as per the encoding
        if response_body_encoding.lower() == 'gzip':  # if gzip then decompress gzip
            response_body_str = gzip.decompress(request.response.body)
        elif response_body_encoding.lower() == 'br':
            response_body_str = brotli.decompress(request.response.body)  # brotli decompression
        elif response_body_encoding.lower() == 'deflate':
            response_body_str = zlib.decompress(request.response.body, -zlib.MAX_WBITS)  # deflate decompression
        elif response_body_encoding.lower() == 'zstd':
            zdecompressor = zstandard.ZstdDecompressor()  # create zstd object
            response_body_str = zdecompressor.decompress(request.response.body)  # zstd decompression
        else:
            # if decode the response body as per the value given in 'Content-Encoding' or specified in response_body_encoding variable
            response_body_str = request.response.body.decode(response_body_encoding, errors='ignore')
        # Algorithm step: 2.e. for each string which are to be replaced in response present in replacement_pairs, replace it with the string specified by user
        for to_be_replaced, to_be_replaced_with in global_variable.replacement_pairs:
            # Replace bytes in response body
            new_response_body_str = response_body_str.replace(to_be_replaced, to_be_replaced_with)
        # Update the content length header and content encoding header
        # Algorithm step: 2.f. delete the 'Content-Encoding' header
        del request.response.headers['Content-Encoding']
        # Algorithm step: 2.g set the 'content-encoding' header
        request.response.headers['Content-Encoding'] = 'utf-8'
        # Algorithm step: 2.h. Add the new response body in HTTP response
        request.response.body = new_response_body_str.encode('utf-8')
        # Algorithm step: 2.i. update the 'Content-Length' header
        request.response.headers['Content-Length'] = len(request.response.body)
    # Algorithm step:3 Check if the request URL matches the filename provided by the user
    if global_variable.args.replace_files:
        for replace_file in global_variable.replace_files:
            # Algorithm step: 3.a for each file to be replaced do following
            file_name, file_url = replace_file.split('++')
            # Algorithm step: 3.a.1. get the filename and file url from user supplied value
            if file_url == request.url:
                # Algorithm step:3.a.2 if file url matches the current HTTP response's url then
                # Update the response content using replace method
                del request.response.headers['Content-Encoding']
                # Algorithm step: 3.a.2.a delete the 'Content-Encoding' header
                request.response.headers['Content-Encoding'] = 'utf-8'
                # Algorithm step: 3.a.2.b set content encoding as 'utf-8'
                request.response.body = global_variable.file_contents[file_name]
                # Algorithm step: 3.a.2.c replace the HTTP response body with replacement file's content
                request.response.headers['Content-Length'] = len(request.response.body)
                # Algorithm step: 3.a.2.d update the HTTP response 'content-length' header
    # Algorithm step: 4 if there python code to execute then Execute python code to manipulate response
    if global_variable.args.python_response or global_variable.args.python_response_file:
        try:
            # Algorithm step: 4.a if 'Content-Encoding' option does not exist then set the decoding as 'utf-8'
            if response.headers['Content-Encoding'] == None:
                response_body_encoding = 'utf-8'
            else:
                # Algorithm step: 4.b else set the response encoding specified in 'Content-Encoding' header
                response_body_encoding = response.headers['Content-Encoding']
        except KeyError:
            # Algorithm step: 4.c if there is a key error then set the response encoding as 'utf-8' again
            response_body_encoding = 'utf-8'
        # Algorithm step: 4.d decode the response body as per the encoding
        if response_body_encoding.lower() == 'gzip':  # gzip decompression
            response_body_str = gzip.decompress(request.response.body)
        elif response_body_encoding.lower() == 'br':
            response_body_str = brotli.decompress(request.response.body)  # brotli decompression
        elif response_body_encoding.lower() == 'deflate':
            response_body_str = zlib.decompress(request.response.body, -zlib.MAX_WBITS)  # deflate decompression
        elif response_body_encoding.lower() == 'zstd':
            zdecompressor = zstandard.ZstdDecompressor()  # create object of zstd
            response_body_str = zdecompressor.decompress(request.response.body)  # zstd decompression
        else:
            # if decode the response body as per the value given in 'Content-Encoding' or specified in response_body_encoding variable
            response_body_str = request.response.body.decode(response_body_encoding, errors='ignore')
        # Algorithm step: 4.e create dictionary of objects which are to be passed to the python scripting engine
        pass_response_object = {
            'request': request,
            'response': response,
            'response_body': response_body_str
        }
        try:
            # Extract import statements
            import_statements = re.findall(r'^\s*(import .+|from .+ import .+)$', global_variable.python_http_response, re.MULTILINE)

            # Execute import statements in the global scope
            for statement in import_statements:
                exec(statement, globals())

            # Remove import statements from the original python_code
            code_without_imports = re.sub(r'^\s*(import .+|from .+ import .+)$', '', global_variable.python_http_response, flags=re.MULTILINE)

            # Execute the remaining code using exec() method and pass the request, response and response_body to the exec() method
            exec(code_without_imports, globals(), pass_response_object)
        except Exception as e:
            # Algorithm step: 4.g if there is any error then check if this is first round of fuzzing, if yes then global_variable.terminate the script else move on
            if global_variable.first_payload:
                # check if this is first round of fuzzing
                global_variable.terminate = True
                # set the global termination flag to indicate that script has to close
                handle_unknown_exception(e)  # handle the exception
