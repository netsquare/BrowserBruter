# The Browser-Bruter

![banner](https://raw.githubusercontent.com/netsquare/BrowserBruter/main/res/img/banner.png)

**The Browser-Bruter** is first ever browser based automated web pentesting tool for fuzzing **web forms** by controlling the browser it self. It automates the process of sending **payloads** to input fields of browser and sends them too server. It completely **bypasses** the need of breaking the **encryption** in order to fuzz and insert payloads in BurpSuite scanner and intruder. After fuzzing it generates a **comprehensive report** including all the data and result of the pentest along with HTTP traffic, this report can be viewed by **The Report-Explorer** tool which comes with The Browser-Bruter.

**Handcrafted in India 🇮🇳**

![pse2](https://github.com/netsquare/BrowserBruter/assets/65374935/380dbfa0-ffc3-4327-8e60-ac00a8a6f914)

### Please refer to this for Proof of Concept of our claims - https://net-square.com/browserbruter/WhyWeNeedBrowserBruter/

## Proof Of Concept

HTTP Manipulation ineffective due to **Encryption**

**https://net-square.com/browserbruter/img/need-1.mp4**

Trying to find SQLInjection using **SQLMAP**

**https://net-square.com/browserbruter/img/sqlmap.mp4**

Trying to find SQLInjection using **BurpSuite**

**https://net-square.com/browserbruter/img/burp-scan.mp4**

BruteForcing login page using **FFUF**

**https://net-square.com/browserbruter/img/ffuf-1-video.mp4**

Finding SQL Injection which can not be found in other tools using **The Browser Bruter**

**https://net-square.com/browserbruter/img/sql-injection.mp4**

BruteForcing Login page using **The Browser Bruter**

**https://net-square.com/browserbruter/img/brute-force-login-1.mp4**

### Please refer official documentation for installation and to learn how to use, It is highly recommended. You can find the official documentation - https://net-square.com/browserbruter/

- [Download now!](https://github.com/netsquare/BrowserBruter/releases/)
- [Jump to Installation](https://net-square.com/browserbruter/SetupInstallation/)
- [Jump to How to use](https://net-square.com/browserbruter/UsageManual/)
- [Click here to know Why we created The BrowserBruter](https://net-square.com/browserbruter/WhyWeNeedBrowserBruter/)

## Table of Contents

- [The Browser-Bruter](#the-browser-bruter)
  - [Table of Contents](#table-of-contents)
  - [What It Does?](#what-it-does?)
  - [Prerequisites](#prerequisites)
  - [Quick Installation](#installation)
  - [Test Lab for BrowserBruter](#test-lab-for-browserbruter)
  - [Working Flow Overview](#working-flow-overview)
  - [Features](#features) 
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)
 
## What it does?

The biggest advantage of using browser bruter for fuzzing the web application is that all of the fuzzing will take place at browser level, so all of the attack will be as they have been manually done by the user by typing payloads in the input fields of the web application on browser.

This approach -

- Allows Pentester to fuzz the web application forms when the HTTP body (or part of the body) is encrypted making HTTP proxy tools like ZAP and BurpSuite or SQLMap unable to insert payloads in such traffic. Learn more here.

- Creates a way to bypass captchas by allowing the pentester to manually perform the required human interactions and then proceed to payload insertions.

- Can fuzz front-end when there is no HTTP traffic, for example when Input is utilized on the client side, i.e. when you want to brute force OTP input which is validated on the client side, so there is no HTTP Traffic.

- Removes the burden of session management, auth handling and other micro management like CSRF handling while using HTTP proxy tools.

![console](https://raw.githubusercontent.com/netsquare/BrowserBruter/main/res/img/image-23.png)
![console](https://raw.githubusercontent.com/netsquare/BrowserBruter/main/res/img/image-24.png)

## Prerequisites

- Linux
- Python3

## Quick Installation

Requires following python packages:
-  selenium
-  selenium-wire
-  webdriver_manager
-  ttkthemes
-  pytimedinput
-  colorama
-  beautifulsoup4
-  undetected-chromedriver
-  requests
-  pandas
-  tqdm

Tested on latest version (as of March 2024) of each package.

1. Download and install Python3
2. Download the [latest release from releases](https://github.com/netsquare/BrowserBruter/releases/).
3. Unzip the archive.
4. Run `pip3 install -r requirements.txt`
5. Done

**Refer documentation for detailed installation guide.** - https://net-square.com/browserbruter/SetupInstallation/

## Test Lab for BrowserBruter

The Lab shown in documentation can be setup using docker as follows- 

1. Download and run the docker image - `sudo docker run --rm -p 80:80 hpandro/vims`
2. Start the MySQL service using following - 
   1. First copy the container id using `sudo docker container ls -a`
   2. Then start the service using `sudo docker exec -it [containerid] service mysql start`
Navigate to `http://localhost/` to test site.

## Working Flow Overview

![image](https://net-square.com/browserbruter/img/work-flow-sniper.svg)

## Features 

- [Bypass Encryption](https://net-square.com/browserbruter/WhyWeNeedBrowserBruter/)
- [Multiple Attack Modes](https://net-square.com/browserbruter/UsageManual/attack.html)
    [1. Sniper](https://net-square.com/browserbruter/UsageManual/attack.html#1-sniper-attack)
    [2. Battering Ram](https://net-square.com/browserbruter/UsageManual/attack.html#2-battering-ram-attack)
    [3. PitchFork](https://net-square.com/browserbruter/UsageManual/attack.html#3-pitchfork-attack)
    [4. Cluster Bomb](https://net-square.com/browserbruter/UsageManual/attack.html#4-clusterbomb-attack)
- [Guaranteed Report Generation even in crash](https://net-square.com/browserbruter/UsageManual/output.html)
- [Advance In-Built Report Exploration Tool - The Report Explorer](https://net-square.com/browserbruter/ReportExplorer/)
- [BurpSuite Support](https://net-square.com/browserbruter/UsageManual/browser.html#routing-http-traffic-through-proxy-burp-zap-using---proxy-option)
- [Customize the Final Report](https://net-square.com/browserbruter/UsageManual/report.html)
- [Customize the Attack Scope](https://net-square.com/browserbruter/UsageManual/report.html#extending-the-scope-using---scope-option)
- [Completely or Partially Automate Browsers as per need using Interactive mode](https://net-square.com/browserbruter/UsageManual/fuzzing.html#the-interactive-mode-using---interactive-switch)
- [Extremely Stealthy](https://net-square.com/browserbruter/UsageManual/browser.html#tackling-bot-detection-using---anti-bot-and---no-anti-bot-options)
- [Session Handling](https://net-square.com/browserbruter/UsageManual/session.html)
- [Bypass Captchas](https://net-square.com/browserbruter/UsageManual/fuzzing.html#the-interactive-mode-using---interactive-switch)
- [Bypass Input Validation](https://net-square.com/browserbruter/UsageManual/javascript.html#altering-removing--replacing-input-validation-code-using---replace-code---replace-file---auto-remove-javascript)
- [Log Tracking](https://net-square.com/browserbruter/UsageManual/debug.html#the-debug-options)
- [Error Handling](https://net-square.com/browserbruter/UsageManual/debug.html#the-debug-options)
- [Can be As fast as you want!](https://net-square.com/browserbruter/UsageManual/fuzzing.html#unleashing-the---threads)
- [Take Full Control of the Browser](https://net-square.com/browserbruter/UsageManual/browser.html)
- [Take Full Control of fuzzing](https://net-square.com/browserbruter/UsageManual/fuzzing.html)
- [Get insights of the attack](https://net-square.com/browserbruter/UsageManual/debug.html#getting-http-traffic-on-runtime-using---verbose)
- [Pause - Resume the attack in middle](https://net-square.com/browserbruter/UsageManual/basic.html#pause---resume-attack-in-the-middle-by-pressing-enter)
- [Extendable Beyond the Core Capabilities](https://net-square.com/browserbruter/UsageManual/javascript.html#the-art-of-browser-automation-using-javascript-----javascript--javascript-after-and---javascript-file-options)
- [Continue The Previously Crashed Attack](https://net-square.com/browserbruter/UsageManual/output.html#resuming-previous-attack)
- [Can Fuzz various types of input elements](https://net-square.com/browserbruter/UsageManual/elements.html)
- [Modify web pages on fly](https://net-square.com/browserbruter/UsageManual/javascript.html#altering-removing--replacing-input-validation-code-using---replace-code---replace-file---auto-remove-javascript)

## Contributing

BrowserBruter is an open-source project, and we welcome contributions from the community. If you would like to contribute to BrowserBruter, you can do so in several ways:

- **GitHub Repository:** The source code for BrowserBruter is hosted on GitHub. You can contribute by forking the repository, making your changes, and submitting a pull request. Contributions can include bug fixes, new features, documentation improvements, or any other enhancements.

- **Reporting Issues:** If you encounter a bug or issue while using BrowserBruter, please report it on the GitHub issue tracker. Include as much detail as possible, such as steps to reproduce the issue and your environment details.

- **Feature Requests:** If you have a feature request or idea for improving BrowserBruter, you can submit it on the GitHub issue tracker. We welcome feedback and suggestions from the community.

- **Documentation:** Improving the documentation is another valuable way to contribute. If you find any errors or gaps in the documentation, you can submit a pull request to update it.

- **Spread the Word:** You can also contribute by spreading the word about BrowserBruter. Share it with your friends, colleagues, or on social media to help grow the user community.

Thank you for considering contributing to BrowserBruter. Your support is greatly appreciated!

## Contact 

  - **[Jafar Pathan](https://zinja-coder.github.io/)** at **[LinkedIn](https://linkedin.com/in/jafar-pathan/)**, **[X (Twitter)](https://twitter.com/zinja_coder)** and **[GitHub](https://github.com/zinja-coder)**

  - **Ravi Kumar Paghdal** at **[LinkedIn](https://www.linkedin.com/in/raviramesh/)**, **[X (Twitter)](https://twitter.com/_RaviRamesh)** and **[GitHub](https://github.com/RavikumarPaghdal-NS)**

  - **Jatan Raval** at **[LinkedIn](https://www.linkedin.com/in/jatanraval/)**, **[X (twitter)](https://twitter.com/JatanKRaval)** and **[GitHub](https://github.com/jatankraval)**

  - **Saumil Shah** at **[LinkedIn](https://www.linkedin.com/in/saumilshah/)**, **[X (twitter)](https://twitter.com/therealsaumil)** and **[Github](https://github.com/therealsaumil/emux)**

## License 

This project is licensed under the MPL license

## Legal Warning

This BrowserBruter (‘Software’)  is protected under the Indian Copyright Act and is the exclusively property  owned by Net Square Solutions Private Limited (‘Net Square’). The use of this Software (including but not limited to) reproduction, distribution, copying, republication, modification, transmission, sale or offer for sale, alteration in any form (including but not limited to electronic or otherwise) is strictly prohibited without the prior written consent from Net Square. Permission to grant license to use the Software shall be at the sole discretion of Net Square.
