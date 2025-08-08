# /// script
# dependencies = [ "fastmcp", "httpx", "logging" ]
# ///

import httpx
import logging
import argparse

from typing import Union
from fastmcp import FastMCP

# Logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create fastmcp object
mcp = FastMCP("Browser Bruter MCP Server")
MCP_DATA_HANDLER_BASE = "http://127.0.0.1:9011" # FastAPI Server

parser = argparse.ArgumentParser("MCP Server for Browser Bruter.")
parser.add_argument("--http", help="Serve MCP Server over HTTP stream.", action="store_true", default=False)
parser.add_argument("--port", help="Specify the port number for --http to serve on. (default:8652)", default=8652, type=int)
args = parser.parse_args()

async def get_from_data_handler(endpoint: str, params: dict = {}) -> Union[str, dict, list]:
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{MCP_DATA_HANDLER_BASE}/{endpoint}", params=params, timeout=120)
            resp.raise_for_status()
            content_type = resp.headers.get("content-type", "")
            return resp.text
        
    except httpx.HTTPStatusError as e:
        msg = f"HTTP error {e.response.status_code}: {e.response.text}"
        logger.error(msg)
        return {"error": msg}
    except httpx.RequestError as e:
        msg = f"Request failed: {str(e)}"
        logger.error(msg)
        return {"error": msg}
    except Exception as e:
        msg = f"Unexptected error: {str(e)}"
        logger.error(msg)
        return {"error": msg}
    
# MCP Tools
@mcp.tool(name="get_current_url", description="Fetch the current browser URL and page title.")
async def get_current_url() -> str:
    """ Fetch the current browser url and page title.
    
    Args: None

    Returns:
        Dictionary containing current url.
    """
    return await get_from_data_handler("current_url")

@mcp.tool(name="get_dom_snapshot", description="Get the current DOM snapshot. In other words, get the current web page's source code.")
async def get_dom_snapshot() -> str:
    """ Fetch the current web pages's source code.
    
    Args: None

    Returns:
        Dictionary containing current web page's source code.
    """
    return await get_from_data_handler("dom_snapshot")


@mcp.tool(name="get_browser_bruter_switches_and_arguments", description="Fetch the available switches and arguments in BrowserBruter to know it's functionality and build a cli command.")
async def get_browser_bruter_switches_and_arguments() -> str:
    """ Fetch the available switches and arguments in BrowserBruter to know it's functionality and build a cli command.
    
    Args: None

    Returns:
        Dictionary containing options of BrowserBruter
    """
    return await get_from_data_handler("browser_bruter_switches_and_arguments")

@mcp.tool(name="get_screenshot", description="Fetch the screenshot of the currently opened web page in browser.")
async def get_screenshot() -> str:
    """ Fetch the screenshot of the currently opened web page in browser.
    
    Args: None

    Returns:
        Dictionary containing screenshot image of currently opened web page in browser bruter
    """
    return await get_from_data_handler("screenshot")

##################################################################
# Form Analysis and Intelligence Tools
##################################################################

@mcp.tool(name="analyze_page_forms", description="Analyze all forms on the current page and extract detailed information about inputs, buttons, and validation mechanisms.")
async def analyze_page_forms() -> str:
    """Analyze all forms on the current page including input fields, buttons, and validation mechanisms.
    
    Returns:
        Dictionary containing detailed form analysis including field types, validation patterns, and submit buttons.
    """
    return await get_from_data_handler("analyze_forms")

@mcp.tool(name="fetch_encryption_logic", description="Detect and fetch the client-side encryption logic of HTTP traffic.")
async def fetch_encryption_logic() -> str:
    """
    Detect encryption mechanism.
    
    Args:
        None
    
    Returns:
        Dictionary containing code of methods that has encrypt keyword in their name.
    """
    return await get_from_data_handler("fetch_encryption_logic")

@mcp.tool(name="analyze_specific_function", description="Fetch and analyze specific function.")
async def analyze_specific_function(function_name: str) -> str:
    """
    Fetch and analyze specific by their name.
    
    Args:
        function_name: name of the function to analyze
    
    Returns:
        Dictionary containing analysis of specific function.
    """
    return await get_from_data_handler("analyze_specific_function")

@mcp.tool(name="detect_validation_mechanisms", description="Detect client-side validation mechanisms that might interfere with fuzzing attempts.")
async def detect_validation_mechanisms() -> str:
    """Detect JavaScript validation, HTML5 patterns, required fields, and validation libraries.
    
    Returns:
        Dictionary containing validation mechanisms that need to be bypassed for effective fuzzing.
    """
    return await get_from_data_handler("detect_validation_mechanisms")

@mcp.tool(name="suggest_payloads_for_inputs", description="Analyze input fields and suggest appropriate payloads based on field types and names.")
async def suggest_payloads_for_inputs() -> str:
    """Suggest appropriate fuzzing payloads based on detected input field types and characteristics.
    
    Returns:
        Dictionary mapping field names to suggested payloads for different vulnerability types (XSS, SQLi, etc.).
    """
    return await get_from_data_handler("suggest_payloads")

# MCP Prompt to build browser bruter command
@mcp.prompt(name="Build Browser Bruter Command", description="Builds the cli command to run the Browser Bruter")
async def build_browser_bruter_cli_command() -> str:
    return """
    Focus on the web page structure and the elements by:
    1. call the current_url() to know the target url
    2. call the analyze_page_forms() to find and analyze forms in current page
    3. call the browser_bruter_switches_and_arguments() to analyze the available options and switches in browser bruter. 
    
    Then Provide:
     - Command with `python3 BrowserBruter.py` prefix to run and fuzz the target web page.
    """

@mcp.prompt(name="Build Browser Bruter Command using dom snapshot", description="Builds the cli command to run the Browser Bruter by providing dom snap shot to llm")
async def build_browser_bruter_cli_command() -> str:
    return """
    Focus on the web page structure and the elements by:
    1. call the current_url() to know the target url
    2. call the analyze_page_forms() to find and analyze forms in current page
    4. call the dom_snapshot() to analyze the dom structure of the web page.
    3. call the browser_bruter_switches_and_arguments() to analyze the available options and switches in browser bruter. 
    
    Then Provide:
     - Command with `python3 BrowserBruter.py` prefix to run and fuzz the target web page.
    """
    
if __name__ == "__main__":
    if args.http:
        if args.port:
            mcp.run(transport="http",port=args.port)
        else:
            mcp.run(transport="http",port=8651)
    else:
        mcp.run(transport="stdio")
