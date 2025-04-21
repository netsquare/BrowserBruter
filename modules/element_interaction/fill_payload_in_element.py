##################################################################
"""
Name  : fill_payload_in_element.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.input_validation.remove_attributes import remove_attributes_and_get_focus
from modules.global_config_arguments.global_variables import global_variable

##################################################################
# Importing Python Libraries
##################################################################
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By # used to found elements by various methods
import sys

##################################################################
"""
Name          -> fill_payload_in_element
Functionality -> Function to fill the payload in selected input field
Algorithm     ->
    1. handle the element if it <select> if yes then handle accordingly
        a. Get the options available in <select> element
        b. Call the remove_attribute_and_get_focus
        c. set the payload as option of <select> element
    2. else If element is <textarea> then 
        a. clear the text area
        b. fill the payload
    3. else convert the element into text field and then
        a. set the payload as its value
        b. clear the element
        c. fill the payload again by sending key strokes of payloads
        d. if there is InvalidElementStateException then
            1. Create a new <input> element
            2. Copy the attributes of the element being fuzzed into this newly created element
            3. set the payload into this new element
            4. Replace the original element being fuzzed with newly created element
        e. if there is WebDriverException then handle it
    4. If there is ElementNotInteractableException then handle it
Parameters    -> driver(webdriver.Chrome), element_being_fuzzed(element), payload(string)
Return        -> 
"""
##################################################################                                 

def fill_payload_in_element(driver,element_being_fuzzed,payload):
    try:
        #if "++" in element:
        #    element, temp = element.split("++")
        #if element_being_fuzzed.tag_name == "ng-select":
            #if "++" in element:
            #    element, temp = element.split("++")
        #    if element in global_variable.elements_properties:
        #        ng_select_property = global_variable.elements_properties.get(element)
        #    else:    
                #global_variable.pause_keyboard_thread = True
                #global_variable.pause_event.set()
                ##sys.stdin = StringIO('\n')
                #ng_select_property = input(f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} The <ng-select> element is detected! the {element_being_fuzzed} is <ng-select> element, kindly provide property which will hold the value of <ng-select> when form is submitted (For more information refer to this guide), This property is usually a ngModel attribute, You can also find it by debugging the application.\nProperty: {global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}\n Enter Property: ")
                #f"\n\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nINFO:{global_variable.RESET} Do you want to retry one more time? - Y/N\n{global_variable.YELLOW}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
                #global_variable.pause_event.clear()
                #global_variable.puase_keyboard_thread = False
                #global_variable.elements_properties[element] = ng_select_property
        #        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR:{global_variable.RESET} The <ng-select> element is detected! the {element_being_fuzzed} is <ng-select> element, kindly provide property which will hold the value of <ng-select> when form is submitted (For more information refer to this guide), This property is usually a ngModel attribute, You can also find it by debugging the application.\n Kindly pass the property along with element as follows -> {element}::property \n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
        #        sys.exit(0)
            # JavaScript to replace the element
            #try:
            #    driver.execute_script("""
            #        ngComponent = ng.getContext(arguments[0]);
            #        ngComponent[arguments[1]] = arguments[2];
            #    """,element_being_fuzzed,ng_select_property,payload)
            #    #print("fuzzed the property")
                #
            #except Exception as e:
            #    print(e)
        #if element in global_variable.elements_properties:
        #    element_property = global_variable.elements_properties.get(element)
            # Split the property if it's in the obj.obj2.property format
        #    property_parts = element_property.split(".")
        #    property_access = "[" + "][".join([f"'{part}'" for part in property_parts]) + "]"
            
            # JavaScript to replace the element
        #    try:
        #        js_script = f"""
        #            ngComponent = ng.getContext(arguments[0]);
        #            ngComponent{property_access} = arguments[1];
        #            """
        #        driver.execute_script(js_script, element_being_fuzzed, payload)
                # JavaScript to check for property in ngComponent and its descendants
                #driver.execute_script("""
                #    let ngComponent = ng.getContext(arguments[0]);
                #    let property = arguments[1];
                #    let payload = arguments[2];
                    
               #     if (ngComponent.hasOwnProperty(property)) {
               ##         ngComponent[property] = payload;
                #    } else {
                #        let updated = false;
                #        for (let child in ngComponent) {
                #            if (ngComponent[child] && typeof ngComponent[child] === "object" && ngComponent[child].hasOwnProperty(property)) {
                #                ngComponent[child][property] = payload;
                #                updated = true;
                #                break;
                #            }
                #        }
                #    }
                #""", element_being_fuzzed, element_property, payload)
                #driver.execute_script("""
                #    ngComponent = ng.getContext(arguments[0]);
                #    ngComponent[arguments[1]] = arguments[2];
                #""",element_being_fuzzed,element_property,payload)
                #print("fuzzed the property")
                #
        #    except Exception as e:
        #        print(e)
        # Algorithm step: 1 Check if the element that is being fuzzed is <select> or not, if it is <select>, then set payload to its first <option> tag and mark it as the selected option
        if element_being_fuzzed.tag_name in ["select","mat-select"]: 
            # Algorithm step: 1.a  get the options available in select element
            options = element_being_fuzzed.find_elements(By.TAG_NAME, "option")
            if options:
                remove_attributes_and_get_focus(driver, options[0]) # Algorithm step: 1.b
                # Set payload to the first option
                driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", options[1], payload) # Algorithm step: 1.c
                options[0].click() # Select the option with payload by clicking on it
        else:
            if element_being_fuzzed.tag_name == "textarea": # Algorithm step: 2 fuzz <textarea>
                element_being_fuzzed.clear() # Algorithm step: 2.a clear the text area
                driver.execute_script("arguments[0].value = arguments[1];", element_being_fuzzed, payload) # Algorithm step: 2.b fill the payload in textarea
                element_being_fuzzed.send_keys(payload) # Algorithm step: 2.c send keystrokes
            else:
                # Setting the payload
                driver.execute_script("arguments[0].setAttribute('type','text');", element_being_fuzzed) # Algorithm step: 3
                driver.execute_script("arguments[0].setAttribute('value',arguments[1]);", element_being_fuzzed, payload) # Algorithm step: 3.a set the payload as its value
                #driver.execute_script("arguments[0].setAttribute('valueAsNumber',arguments[1]);", element_being_fuzzed, payload) # Algorithm step: 3.a set the payload as its value
                #driver.execute_script("arguments[0].setAttribute('checked',arguments[1]);", element_being_fuzzed, payload) # Algorithm step: 3.a set the payload as its value
                try:
                    element_being_fuzzed.clear() # Algorithm step: 3..b clear the element field
                    element_being_fuzzed.send_keys(payload) # Algorithm step: 3.c send keyboard strokes
                except InvalidElementStateException: # Algorithm step: 3.d 1-4
                    driver.execute_script("""
                                                // Create a new <input> element
                                                var inputElement = document.createElement('input');

                                                // Copy attributes
                                                for (var i = 0; i < arguments[0].attributes.length; i++) {
                                                    var attr = arguments[0].attributes[i];
                                                    inputElement.setAttribute(attr.name, attr.value);
                                                }
                                                // set the values
                                                inputElement.value = arguments[1];

                                                // Replace element with <input> in the DOM
                                                arguments[0].parentNode.replaceChild(inputElement, arguments[0]);
                                              """,element_being_fuzzed,payload)
                except WebDriverException as e: # Algorithm step: 3.e
                    if "ChromeDriver only supports characters in the BMP" in str(e): # if this error is only due to bmp (bmp means if payload contains emoji,etc) error then skip 
                        pass
                    else:
                        raise
        
    except ElementNotInteractableException: # Algorithm step: 4 handle the exception
        print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Specified Element is not interactable -> {element_being_fuzzed}\nFollowings are the possible reason:\n 1. Either tool is running too fast, make it slow using --delay-* options\n 2. May be the {element_being_fuzzed} requires some action like clicking on button to make it interactable, in such case, provide a javascript using --javascript option to execute javascript.\n Skipping filling this {element_being_fuzzed}\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
