##################################################################
"""
Name  : fill_form.py 
Date  : 13/03/2023
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

##################################################################
# Importing Custom Modules
##################################################################
from modules.input_validation.remove_attributes import remove_attributes_and_get_focus
from modules.element_interaction.get_element import get_element
from modules.global_config_arguments.global_variables import global_variable

##################################################################
# Importing Python Libraries
##################################################################
from time import sleep # used to pause the script
from selenium.webdriver.common.by import By # used to found elements by various methods
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidElementStateException

##################################################################
"""
Name          -> fill_the_form
Functionality -> Function to perform fill the elements of the form which are not being fuzzed.
Algorithm     ->
    1. handle --delay-before
    2. get the fields to be filled from user and store them into list of fields
    3. for each field to be filled do following
        a. find the field
        b. if that field is marked to remove the class, remove it's class
        c. if field is <select> then 
            1. if there are two options then select second one
            2. else select first one
        d. get the field type
        e. if the field is checkbox then select the first options
        f. else check what type of field it is and fill its default value or user supplied values --fill-values
            1. if there is InvalidElementStateException then replicate that element by creating new element with same attributes and replace original field with it's replica
        g. if element is not interactable then throw the error
Parameters    -> driver(webdriver.Chrome)
Return        -> 
"""
################################################################## 

def fill_the_form(driver):
    if global_variable.args.delay_before:  # Algorithm step: 1 delay in case of --delay-before
        sleep(global_variable.args.delay_before) # sleep to cause delay
    input_fields = global_variable.args.fill.split(',') # Algorithm step: 2 get the elements to be filled
    # fill the form
    for input_field in input_fields: # Algorithm step: 3 for each field do following
        try:
            field = get_element(driver,input_field,False) # Algorithm step: 3.a get the element to filled 
            if input_field in global_variable.remove_class_elements: # Algorithm step: 3.b remove class attribute if required
                driver.execute_script("arguments[0].removeAttribute('class');",field) # remove class
                driver.execute_script("arguments[0].setAttribute('name',arguments[1]);",field,input_field) # change the name of the element as its class
            # Fill other fields with valid inputs
            # Adding support to handle <select> tags
            if field.tag_name == "select": # Algorithm step: 3.c
                # Select the second option
                options = field.find_elements(By.TAG_NAME, "option")
                # Algorithm step: 3.c.1if there are two options in <select>, choose the second one as the first option can be empty, for example, <option value="">choose country</option><option value="india">india</option>
                if len(options) == 1: # Algorithm step: 3.c.1
                    remove_attributes_and_get_focus(driver, options[0])
                    # Set payload to the first option
                    options[0].click()
                else: # Algorithm step: 3.c.2 else choose the second option
                    remove_attributes_and_get_focus(driver,options[1])
                    options[1].click()
            else:
                # Algorithm step: 3.d get the field type, Taking field value appropriate to its type
                fieldType = field.get_attribute("type")
                # Algorithm step: 3.e fill the checkbox and radio type
                if fieldType == "checkbox" or fieldType == "radio":
                    driver.execute_script("arguments[0].checked = true;", field) # Select the option
                else: # Algorithm step: 3.f check the field type and fill appropriate values according to the type for field
                    # Filling the predefined values
                    if field.tag_name == "textarea": # fill value for text area
                        fieldValue = global_variable.attribute_values.get("textarea","defaultValue") # Get the default value set for text area
                        field.clear() # clear the field
                        driver.execute_script("arguments[0].value = arguments[1];", field, fieldValue) # fill the value
                        field.send_keys(fieldValue) # Also send key strokes
                    else:
                        try:
                            fieldValue = global_variable.attribute_values.get(fieldType, "defaultValue") # Whatever type of the field is get it's value
                            driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", field, fieldValue) # fill the value
                            driver.execute_script("arguments[0].setAttribute('type','text');", field) # mark the field as text
                            field.clear() # clear the field
                            field.send_keys(fieldValue) # send keystrokes of value
                        except InvalidElementStateException: # Algorithm step: 3.f.1 in case of this error replicate and replace the element
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
                                              """,field,fieldValue)
        except ElementNotInteractableException: # Algorithm step: 3.g if element is not interactable then throw the error
            print(f"\n\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]\nERROR: {global_variable.RESET}Specified Element is not interactable -> {input_field}\nFollowings are the possible reason:\n 1. Either tool is running too fast, make it slow using --delay-* options\n 2. May be the {input_field} requires some action like clicking on button to make it interactable, in such case, provide a javascript using --javascript option to execute javascript.\n Skipping filling this {input_field}\n{global_variable.RED}[+]--------------------------------------------------------------------------------------------------------------------------[+]{global_variable.RESET}")
