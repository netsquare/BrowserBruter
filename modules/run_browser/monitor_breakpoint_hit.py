##################################################################
"""
Name  : get_and_initialize_driver.py 
Date  : 1/01/2025
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.error_handling.error_handling import handle_unknown_exception
from modules.global_config_arguments.global_variables import global_variable

##################################################################
# Importing Python Modules
##################################################################
import json
import websocket
import requests
import threading


def monitor_breakpoint_hit(driver, on_hit_code):
    """Monitor for breakpoint hit using WebSocket and execute custom code."""
    try:
        # Fetch WebSocket URL
        #port = 9222
        port = int(driver.port)
        response = requests.get(f"http://127.0.0.1:{port}/json").json()
        ws_url = response[0]["webSocketDebuggerUrl"]
        # For DEBUG purpose #print(f"Connecting to WebSocket: {ws_url}")

        # Function to handle WebSocket connection
        def on_open(ws):
            #print("WebSocket opened")
            # Enable Debugger domain
            ws.send(json.dumps({"id": 1, "method": "Debugger.enable"}))

        # Function to handle incoming WebSocket messages
        def on_message(ws, message):
            data = json.loads(message)
            if data.get("method") == "Debugger.paused":
                # Extract call frames from the event
                call_frames = data["params"]["callFrames"]
                #for frame in call_frames:
                    #print(f"Function Name: {frame['functionName']}")
                    #print(f"Call Frame ID: {frame['callFrameId']}")
                    #print(f"Location: {frame['location']}")
                # Example: Use the first call frame
                first_call_frame_id = call_frames[0]["callFrameId"]
                #print(f"First Call Frame ID: {first_call_frame_id}")
                #print(f"Breakpoint hit: {data}")
                # Execute custom code when breakpoint is hit
                try:
                    #print(on_hit_code)
                    exec(on_hit_code, globals(), {'driver': driver, 'ws': ws, 'call_frame_id': first_call_frame_id})
                except Exception as e:
                    handle_unknown_exception(e)
                    #traceback.print_exc(e)
#                from time import sleep
                # Send JavaScript code to execute via Runtime.evaluate
                #js_code = """
                #    ngComponent['testForm']['value']['projectId'] = '%s';
                #    ngComponent['testForm']['value']['revalTestId'] = '%s';
                #    console.log('done');
                #""" % (global_variable.current_payload, global_variable.current_payload)

                

                #eval_msg = {"id": 2, "method": "Runtime.evaluate", "params": {"expression": "ngComponent['testForm']['value']['projectId'] = '(select*from(select(sleep(20)))a)';ngComponent['testForm']['value']['revalTestId'] = '(select*from(select(sleep(20)))a)';console.log('done');"}}
                #json.dump(eval_msg)
               # eval_msg = {
               #     "id": 2,
               #     "method": "Runtime.evaluate",
               #     "params": {
               #     "expression": js_code
               # }
            #}
                #sleep(10)
                #print(json.dumps(eval_msg))
                #response = ws.send(json.dumps(eval_msg))#json.dumps(eval_msg))  # Send evaluate command to execute JS code
                #print(response)
                #print('JavaScript code executed via WebSocket')
                #time.sleep(10)
                #response = ws.send(json.dumps(eval_msg))
                #print(response)
                #print('attempt 2')

                #{"id": 3,"method": "Runtime.evaluate","params": {"expression": "formData['projectId'] = '123';formData['revalTestId'] = '123';console.log('done');"}}

                # Resume script execution
                ws.send(json.dumps({"id": 2, "method": "Debugger.resume"}))
                #driver.execute_cdp_cmd("Debugger.resume", {})
                #print('done')
            #else:
                #ws.send(json.dumps({"id": 3, "method": "Debugger.stepOver"}))
        # WebSocket event handlers
        def on_error(ws, error):
            #print(f"WebSocket error: {error}")
            pass

        def on_close(ws, close_status_code, close_msg):
            #print("WebSocket closed")
            pass

        # Initialize and run WebSocket client in a background thread
        ws = websocket.WebSocketApp(
            ws_url,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )
        ws_thread = threading.Thread(target=ws.run_forever, daemon=True)
        ws_thread.start()

    except Exception as e:
        handle_unknown_exception(e)
        #print("Error occurred while monitoring breakpoints:")
        #print(e)
