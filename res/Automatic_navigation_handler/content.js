// content.js
/*
##################################################################
"""
Name  : content.js
Date  : 04/08/2024
Author: Jafar Pathan (jafar.pathan2503@outlook.com)
Copyright: Net-Square Solutions PVT LTD.
"""
##################################################################

*/

/*
##################################################################
"""
Name          -> content.js
Functionality -> Record navigation and save it in element
Algorithm     ->
    1. TO DO
Parameters    -> 
Return        -> 
"""
##################################################################
*/

(function() {
    'use strict';

    // Function to create the header
    function createHeader() {
        const header = document.createElement('BrowserBruterNavigation');
        header.id = 'BrowserBruterNavigationHeader';
        header.style.position = 'fixed';
        header.style.top = '0';
        header.style.left = '0';
        header.style.width = '100%';
        header.style.height = '50px';
        header.style.backgroundColor = 'black';
        header.style.color = 'white';
        header.style.display = 'flex';
        header.style.alignItems = 'center';
        header.style.padding = '0 20px';
        header.style.zIndex = 1000;
        header.innerHTML = '<span>[+]-----[+] BrowserBruter Navigation Recorder [+]-----[+]  </span>';

        document.body.appendChild(header);

        // Shift the body down
        document.body.style.marginTop = '50px';
    }

    // Function to create a button
    function createButton(id, text, onClickHandler) {
        const button = document.createElement('button');
        button.id = id;
        button.innerText = text;
        button.style.backgroundColor = 'white';
        button.style.color = 'black';
        button.style.marginLeft = id === 'stopTrackingButton' ? '20px' : '0';
        button.onclick = onClickHandler;
        return button;
    }

    // Function to get the XPath of an element
    function getXPathForElement(element) {
        function getPath(el) {
        if (el.nodeType === Node.ELEMENT_NODE) {
            let path = [];
            while (el && el.nodeType === Node.ELEMENT_NODE) {
                let index = 1;
                let sibling = el.previousSibling;
                while (sibling) {
                    if (sibling.nodeType === Node.ELEMENT_NODE && sibling.tagName === el.tagName) {
                        index++;
                    }
                    sibling = sibling.previousSibling;
                }
                path.unshift(el.tagName.toLowerCase() + (index > 1 ? `[${index}]` : ''));
                el = el.parentNode;
            }
            return '/' + path.join('/');
        }
        return null;
    }

    return getPath(element);
    }

    // Retrieve navigation details from localStorage
    let navigationDetails = JSON.parse(localStorage.getItem('navigationDetails')) || [];

    // Variable to keep track of whether tracking is active
    let isTracking = false;

    // Function to save navigation details to localStorage
    function saveNavigationDetails() {
        localStorage.setItem('navigationDetails', JSON.stringify(navigationDetails));
    }

    // Function to log element information on click
    function logClick(event) {
        if (!isTracking) return;
        const targetElement = event.target;
        const eid = targetElement.id;
        const ename = targetElement.name;
        const eclassName = targetElement.className;
        const elementXPath = getXPathForElement(targetElement);

        navigationDetails.push({
            type: 'click',
            id: eid,
            name: ename,
            className: eclassName,
            xPath: elementXPath
        });
        document.getElementById('latest_event').innerHTML="";
        document.getElementById('latest_event').style.color = "white";
        document.getElementById('latest_event').innerHTML="Latest Event: Event Type = 'click', Event Element = '" + eid + "', '" + ename + "', '" + eclassName + "', '" + elementXPath + "'";
        saveNavigationDetails();
        console.log(JSON.stringify(navigationDetails, null, 2));

    }

    // Function to log element information on keypress
    function logKeyPress(event) {
        if (!isTracking) return;
        const targetElement = event.target;
        const eid = targetElement.id;
        const ename = targetElement.name;
        const eclassName = targetElement.className;
        const elementXPath = getXPathForElement(targetElement);
        const pressedKey = event.key;

        navigationDetails.push({
            type: 'key',
            id: eid,
            name: ename,
            className: eclassName,
            key: pressedKey,
            xPath: elementXPath
        });
        document.getElementById('latest_event').innerHTML="";
        document.getElementById('latest_event').style.color = "red";
        document.getElementById('latest_event').innerHTML="Latest Event: Event Type = 'key', Pressed Key = '" + pressedKey + "', Event Element = '" + eid + "', '" + ename + "', '" + eclassName + "', '" + elementXPath + "'";
        saveNavigationDetails();
        console.log(JSON.stringify(navigationDetails, null, 2));
    }

    // Function to send navigation details back to Python
    function sendNavigationDetailsToPython() {
        const navigationDetailsJSON = JSON.stringify(navigationDetails, null, 2);
        const resultInput = document.createElement('input');
        resultInput.type = 'hidden';
        resultInput.id = 'navigationDetails';
        resultInput.value = navigationDetailsJSON;
        document.body.appendChild(resultInput);
    }

    // Start tracking
    function startTracking() {
        isTracking = true;
        const start_button = document.getElementById("BrowserBruterStartTrackingButton");
        const stop_button = document.getElementById("BrowserBruterStopTrackingButton");
        start_button.style.visibility = "hidden";
        stop_button.style.visibility = "visible";
        document.getElementById('start_notification').innerHTML="  [+]-----[+] Started Recording Navigation [+]-----[+]  ";
        console.log('Navigation tracking started.');
    }

    // Stop tracking
    function stopTracking() {
        isTracking = false;
        sendNavigationDetailsToPython();
        const stop_button = document.getElementById("BrowserBruterStopTrackingButton");
        const start_button = document.getElementById("BrowserBruterStartTrackingButton");
        start_button.style.visibility = "visible";
        stop_button.style.visibility = "hidden";
        document.getElementById('start_notification').innerHTML="  [+]-----[+] Stopped Recording Navigation [+]-----[+]  ";
        
        console.log('Navigation tracking stopped.');
        console.log('Final navigation details:', JSON.stringify(navigationDetails, null, 2));
    }

    // Create and append the header and buttons
    createHeader();
    const startButton = createButton('BrowserBruterStartTrackingButton', 'Add This Page To Navigation', startTracking);
    const stopButton = createButton('BrowserBruterStopTrackingButton', 'Stop Tracking', stopTracking);
    stopButton.style.visibility = "hidden";
    document.getElementById('BrowserBruterNavigationHeader').appendChild(startButton);
    document.getElementById('BrowserBruterNavigationHeader').appendChild(stopButton);
    const start_notification = document.createElement("p");
    start_notification.id = 'start_notification';
    document.getElementById('BrowserBruterNavigationHeader').appendChild(start_notification);
    const latest_event = document.createElement("p");
    latest_event.id = "latest_event";
    document.getElementById('BrowserBruterNavigationHeader').appendChild(latest_event);

    // Attach event listeners
    document.addEventListener('click', logClick);
    document.addEventListener('keydown', logKeyPress);

    // Log the current state of navigation details on load
    console.log('Current navigation details:', JSON.stringify(navigationDetails, null, 2));
})();
