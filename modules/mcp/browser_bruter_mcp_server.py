# /// script
# dependencies = [ "fastmcp", "httpx", "logging" ]
# ///

import httpx
import logging
import argparse
import json

from typing import Union, Any, List, Callable, Dict
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


## TO do add pagination utils code logic in separate file
# ---------- PaginationUtils (adapted from jadx_mcp_server.py) ----------
class PaginationUtils:
    """Utility class for handling pagination across different MCP tools."""

    DEFAULT_PAGE_SIZE = 100
    MAX_PAGE_SIZE = 10000
    MAX_OFFSET = 1000000

    @staticmethod
    def validate_pagination_params(offset: int, count: int) -> tuple[int, int]:
        offset = max(0, min(offset, PaginationUtils.MAX_OFFSET))
        count = max(0, min(count, PaginationUtils.MAX_PAGE_SIZE))
        return offset, count

    @staticmethod
    async def get_paginated_data(
        endpoint: str,
        offset: int = 0,
        count: int = 0,
        additional_params: dict = None,
        data_extractor: Callable[[Any], List[Any]] = None,
        item_transformer: Callable[[Any], Any] = None,
    ) -> Dict[str, Any]:
        """
        Generic pagination handler for BrowserBruter endpoints.
        - Calls the data handler endpoint (via get_from_data_handler) with offset/limit.
        - Normalizes the response into { "type": ..., "items": [...], "pagination": {...} }.
        - If the data handler returns a plain string (e.g. full DOM), it will chunk the string.
        """

        offset, count = PaginationUtils.validate_pagination_params(offset, count)

        params = {"offset": offset}
        if count > 0:
            params["limit"] = count
        if additional_params:
            params.update(additional_params)

        raw_response = await get_from_data_handler(endpoint, params)

        # If data handler returned an error dict, pass it back
        if isinstance(raw_response, dict):
            return raw_response
        
        # If data handler returned JSON but as a str, parse it
        if isinstance(raw_response, str):
            try:
                raw_response = json.loads(raw_response)
            except Exception:
                # Keep as string if not JSON
                pass

        # Try parse JSON first (common case where data handler already paginates)
        parsed = None
        if isinstance(raw_response, str):
            try:
                parsed = json.loads(raw_response)
            except Exception:
                parsed = None

        # If parsed JSON and contains "pagination" or "items" / "content", normalize it
        if isinstance(parsed, dict):
            # Let caller supply extractor, otherwise use common keys
            if data_extractor:
                items = data_extractor(parsed)
            else:
                # Prefer lists or single 'content' string (wrap it)
                items = parsed.get("items") or parsed.get("strings") or parsed.get("forms") or parsed.get("classes") \
                        or parsed.get("content") or []
                # If content is a string, wrap into list
                if isinstance(items, str):
                    items = [items]

            if item_transformer and items:
                items = [item_transformer(i) for i in items]

            # Build eventual pagination metadata from parsed if present
            pagination_info = parsed.get("pagination", {})
            result = {
                "type": parsed.get("type", "paginated-list"),
                "items": items,
                "pagination": {
                    "total": pagination_info.get("total", len(items)),
                    "offset": pagination_info.get("offset", offset),
                    "limit": pagination_info.get("limit", count),
                    "count": pagination_info.get("count", len(items)),
                    "has_more": pagination_info.get("has_more", False),
                },
            }
            # copy helper fields if available
            for k in ("next_offset", "prev_offset", "current_page", "total_pages", "page_size"):
                if k in pagination_info:
                    result["pagination"][k] = pagination_info[k]
            return result

        # Otherwise - raw_response is likely a plain string (e.g. DOM source)
        # We'll split it into chunks if requested
        if isinstance(raw_response, str):
            full_text = raw_response
            text_len = len(full_text)

            # if count == 0, return entire content as single page
            page_size = count if count > 0 else max(PaginationUtils.DEFAULT_PAGE_SIZE, text_len)
            # ensure page_size not larger than MAX_PAGE_SIZE
            page_size = min(page_size, PaginationUtils.MAX_PAGE_SIZE)

            # compute slice bounds
            start = offset
            end = min(offset + page_size, text_len)

            if start >= text_len:
                items = []
            else:
                items = [full_text[start:end]]

            has_more = end < text_len
            next_off = end if has_more else -1

            result = {
                "type": "dom-snapshot",
                "items": items,
                "pagination": {
                    "total": text_len,
                    "offset": offset,
                    "limit": page_size,
                    "count": len(items),
                    "has_more": has_more,
                },
            }
            if has_more:
                result["pagination"]["next_offset"] = next_off
            if offset > 0:
                prev_off = max(0, offset - page_size)
                result["pagination"]["prev_offset"] = prev_off

            # page math if page_size > 0
            if page_size > 0:
                current_page = (offset // page_size) + 1
                total_pages = (text_len + page_size - 1) // page_size
                result["pagination"]["current_page"] = current_page
                result["pagination"]["total_pages"] = total_pages
                result["pagination"]["page_size"] = page_size

            return result

        # Unknown type returned from handler, just wrap it
        return {"type": "unknown", "items": [raw_response], "pagination": {"total": 1, "offset": 0, "limit": 1, "count": 1, "has_more": False}}

    @staticmethod
    def create_page_based_tool(base_func: Callable) -> Callable:
        async def page_wrapper(page: int = 1, page_size: int = DEFAULT_PAGE_SIZE, **kwargs):
            page = max(1, page)
            page_size = max(1, min(page_size, PaginationUtils.MAX_PAGE_SIZE))
            offset = (page - 1) * page_size
            return await base_func(offset=offset, count=page_size, **kwargs)
        return page_wrapper

# ---------- End PaginationUtils ----------

async def get_from_data_handler(endpoint: str, params: dict = {}) -> Union[str, dict, list]:
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{MCP_DATA_HANDLER_BASE}/{endpoint}", params=params, timeout=120)
            resp.raise_for_status()
            return resp.text
    except httpx.HTTPStatusError as e:
        msg = f"HTTP error {e.response.status_code}: {e.response.text}"
        logger.error(msg)
        return msg  # Return as plain string!
    except httpx.RequestError as e:
        msg = f"Request failed: {str(e)}"
        logger.error(msg)
        return msg
    except Exception as e:
        msg = f"Unexpected error: {str(e)}"
        logger.error(msg)
        return msg
    
# MCP Tools
@mcp.tool(name="get_current_url", description="Fetch the current browser URL and page title.")
async def get_current_url() -> str:
    """ Fetch the current browser url and page title.
    
    Args: None

    Returns:
        Dictionary containing current url.
    """
    return await get_from_data_handler("current_url")

@mcp.tool(name="get_dom_snapshot", description="Get the current DOM snapshot (supports offset/limit pagination).")
async def get_dom_snapshot(offset: int = 0, count: int = 0) -> dict:
    """
    Fetch the current web page's source code (DOM snapshot).
    Args:
        offset: pagination offset
        count: count for paginated data
    Returns:
        Standardized dict: { "type": "dom-snapshot", "items": [...], "pagination": {...} }
    """
    return await PaginationUtils.get_paginated_data(
        endpoint="dom_snapshot",
        offset=offset,
        count=count,
        data_extractor=None  # default behavior: try to parse parsed JSON or treat as raw string
    )


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
    return await get_from_data_handler("analyze_specific_function", params={"function_name":function_name})

@mcp.tool(name="detect_validation_mechanisms", description="Detect client-side validation mechanisms that might interfere with fuzzing attempts.")
async def detect_validation_mechanisms() -> str:
    """Detect JavaScript validation, HTML5 patterns, required fields, and validation libraries.
    
    Returns:
        Dictionary containing validation mechanisms that need to be bypassed for effective fuzzing.
    """
    return await get_from_data_handler("detect_validation_mechanisms")

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
            mcp.run(transport="streamable-http",port=args.port)
        else:
            mcp.run(transport="streamable-http",port=8652)
    else:
        mcp.run(transport="stdio")
