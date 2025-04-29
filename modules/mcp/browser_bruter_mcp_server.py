# /// script
# dependencies = [ "fastmcp", "httpx", "logging" ]
# ///

import httpx
import logging

from typing import Union
from mcp.server.fastmcp import FastMCP

# Logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Create fastmcp object
mcp = FastMCP("Browser Bruter MCP Server")
MCP_DATA_HANDLER_BASE = "http://127.0.0.1:9011" # FastAPI Server

async def get_from_data_handler(endpoint: str, params: dict = {}) -> Union[str, dict, list]:
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{MCP_DATA_HANDLER_BASE}/{endpoint}", params=params, timeout=120)
            resp.raise_for_status()
            content_type = resp.headers.get("content-type", "")
            try:
                if "application/json" in content_type:
                    return resp.join()
            except Exception as e:
                 if "Expecting value" in str(e):  # from JSON decode errors
                    return resp.text
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
@mcp.tool(name="get_browser_bruter_current_url", description="Fetch the current browser URL and page title.")
async def get_current_url() -> dict:
    """ Fetch the current browser url and page title.
    
    Args: None

    Returns:
        Dictionary containing current url.
    """
    return await get_from_data_handler("current_url")

@mcp.tool(name="get_browser_bruter_dom_snapshot", description="Get the current DOM snapshot. In other words, get the current web page's source code.")
async def dom_snapshot() -> dict:
    """ Fetch the current web pages's source code.
    
    Args: None

    Returns:
        Dictionary containing current web page's source code.
    """
    return await get_from_data_handler("dom_snapshot")


@mcp.tool(name="browser_bruter_switches_and_arguments", description="Fetch the available switches and arguments in BrowserBruter to know it's functionality and build a cli command.")
async def browser_bruter_switches_and_arguments() -> dict:
    """ Fetch the available switches and arguments in BrowserBruter to know it's functionality and build a cli command.
    
    Args: None

    Returns:
        Dictionary containing options of BrowserBruter
    """
    return await get_from_data_handler("browser_bruter_switches_and_arguments")

@mcp.tool(name="get_browser_bruter_screenshot", description="Fetch the screenshot of the currently opened web page in browser.")
async def browser_bruter_switches_and_arguments() -> dict:
    """ Fetch the screenshot of the currently opened web page in browser.
    
    Args: None

    Returns:
        Dictionary containing screenshot image of currently opened web page in browser bruter
    """
    return await get_from_data_handler("screenshot")

# MCP Prompt
@mcp.prompt(name="Build Browser Bruter Command", description="Builds the cli command to run the Browser Bruter")
async def build_browser_bruter_cli_command() -> str:
    return "call the dom_snapshot(), current_url() and browser_bruter_switches_and_arguments() tools and then analyze the available options in Browser Bruter, then using current url and current dom structure of the current web page, build up the command to run BrowserBruter to fuzz the current web page."

if __name__ == "__main__":
    mcp.run(transport="stdio")
