##################################################################
"""
Name  : request_interceptor.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.global_config_arguments.global_variables import global_variable
from modules.error_handling.error_handling import handle_unknown_exception
import re

##################################################################
"""
Name          -> intercept_request
Functionality -> Function to intercept requests
Algorithm     ->
    1. if --remove-images is there then abort the requests for static media
    2. if there is python to execute on HTTP request then 
        a. create a dictionary to hold HTTP request
        b. execute the python code provided by user using exec() method and pass the HTTP request to this method
        c. if there is any error and this is first round of fuzzing, then stop the script
        d. else handle the unknown exceptions
Parameters    -> request(request)
Return        -> 
"""
##################################################################


def intercept_request(request):
    try:
        # Algorithm step: 1 if --remove-images is there then abort the requests for static media
        if global_variable.args.remove_images:
            if any(extension in request.path.lower() for extension in global_variable.forbidden_extensions):
                request.abort()  # drop the request

        # Algorithm step: 2 if there is python to execute on HTTP request then
        if global_variable.args.python_request or global_variable.args.python_request_file:
            # Algorithm step: 2.a create a dictionary to hold HTTP request
            pass_request_object = {'request': request}

            try:
                # Extract import statements
                import_statements = re.findall(r'^\s*(import .+|from .+ import .+)$', global_variable.python_http_request, re.MULTILINE)

                # Execute import statements in the global scope
                for statement in import_statements:
                    exec(statement, globals())

                # Remove import statements from the original python_code
                code_without_imports = re.sub(r'^\s*(import .+|from .+ import .+)$', '', global_variable.python_http_request, flags=re.MULTILINE)

                # Execute the remaining code using exec() method and pass the request object to it
                exec(code_without_imports, globals(), pass_request_object)
            except Exception as e:
                if global_variable.first_payload:
                    global_variable.terminate = True
                    handle_unknown_exception(e)
    except Exception as e:
        handle_unknown_exception(e)


##################################################################
"""
The block of code for Python Scripting Engine and HTTP interceptor
ends here
"""
##################################################################
