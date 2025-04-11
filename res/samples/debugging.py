from time import sleep
import json
# Send JavaScript code to execute via Runtime.evaluate
#js_code = """
#ngComponent['testForm']['value']['projectId'] = %s;
#ngComponent['testForm']['value']['revalTestId'] = %s;
#console.log('done');
#""" % (global_variable.current_payload, global_variable.current_payload)

sleep(1)


global_variable.current_payload = global_variable.current_payload.replace("'", "\\'")

js_code = f"t['projectName'] = '{global_variable.current_payload}'; t['projectDesc] = '{global_variable.current_payload}'; t['projectShortName] = '{global_variable.current_payload}';"

eval_msg = {"id": 2, "method": "Runtime.evaluate", "params": {"expression": js_code}}
#sleep(10)
#print(json.dumps(eval_msg))
#response = ws.send(json.dumps(eval_msg))  # Send evaluate command to execute JS code
#print(response)
#print('JavaScript code executed via WebSocket')
#sleep(10)
#print(f"str{response}")
response = ws.send(json.dumps(eval_msg))
#print(response)
#print('attempt 2')
#print('done')
sleep(1)

#{"id": 3,"method": "Runtime.evaluate","params": {"expression": "formData['projectId'] = '123';formData['revalTestId'] = '123';console.log('done');"}}
