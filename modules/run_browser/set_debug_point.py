
#import traceback
##################################################################
"""
Name  : get_and_initialize_driver.py 
Date  : 1/01/2025
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Exceptions
##################################################################
from selenium.common.exceptions import WebDriverException

##################################################################
# Importing Custom Modules
##################################################################
from modules.error_handling.error_handling import handle_unknown_exception

def set_debug_breakpoint(driver, file_url, line_number, column_number=None):
    
    try:
        # Enable debugging
        driver.execute_cdp_cmd("Debugger.enable", {})
        
        # Prepare the breakpoint request
        breakpoint_request = {
            "lineNumber": int(line_number),  # Line number (0-indexed)
            "url": file_url  # URL or path to the script file
        }
        
        # Include columnNumber only if it is provided
        if column_number is not None:
            breakpoint_request["columnNumber"] = int(column_number)
        
        # Set the breakpoint
        response = driver.execute_cdp_cmd("Debugger.setBreakpointByUrl", breakpoint_request)
        
        # Optional: return the response for further processing or logging
        return response
    
    except WebDriverException as ex:
        if "Breakpoint at specified location already exists" in str(ex):
            pass
        else:
            handle_unknown_exception(ex)
    except Exception as e:
        handle_unknown_exception(e)
