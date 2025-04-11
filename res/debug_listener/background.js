//// background.js

/*
Name  : background.js
Date  : 04/08/2024
Author: Jafar Pathan 
Copyright: Net-Square Solutions PVT LTD.
*/

chrome.debugger.attach({ tabId: 1 }, "1.3", function () {
    chrome.debugger.sendCommand({ tabId: 1 }, "Debugger.enable", {}, function () {
        chrome.debugger.onEvent.addListener(function (debuggee, method, params) {
            if (method === "Debugger.paused") {
                console.log("BREAKPOINT_HIT");  // Custom message when breakpoint is hit
            }
        });
    });
});
