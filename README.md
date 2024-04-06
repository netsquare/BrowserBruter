# The Browser-Bruter

![banner](https://raw.githubusercontent.com/netsquare/BrowserBruter/main/res/img/banner.png)

**The Browser-Bruter** is first ever browser based automated web pentesting tool for fuzzing **web forms** by controlling the browser it self. It automates the process of sending **payloads** to input fields of browser and sends them too server. It completely **bypasses** the need of breaking the **encryption** in order to fuzz and insert payloads in BurpSuite scanner and intruder. After fuzzing it generates a **comprehensive report** including all the data and result of the pentest along with HTTP traffic, this report can be viewed by **The Report-Explorer** tool which comes with The Browser-Bruter.

**Handcrafted in India 🇮🇳**

#### Please refer to this for Proof of Concept of our claims - https://net-square.com/browserbruter/WhyWeNeedBrowserBruter/

#### Please refer official documentation for installation and usage, It is highly recommended. You can find the official documentation - https://net-square.com/browserbruter/

## Table of Contents

- [The Browser-Bruter](#the-browser-bruter)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Quick Installation](#installation)
  - [Working Flow Overview](#working-flow-overview)
  - [Features](#features) 
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)

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

## Working Flow Overview

![image](https://net-square.com/browserbruter/img/work-flow-sniper.svg)

## Features 

- [Bypass Encryption](https://net-square.com/browserbruter/WhyWeNeedBrowserBruter/)
- [Multiple Attack Modes](https://net-square.com/browserbruter/UsageManual/attack.html)
    1. Sniper
    2. Battering Ram
    3. PitchFork
    4. Cluster Bomb
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

You can reach to **Jafar Pathan** at **[LinkedIn](https://linkedin.com/in/jafar-pathan/)** and **[GitHub](https://github.com/zinja-coder)**

You can reach to **Ravi Kumar Paghdal** at **[LinkedIn](https://www.linkedin.com/in/raviramesh/)** and **[GitHub](https://github.com/RavikumarPaghdal-NS)**

## License 

This project is licensed under the GNU General Public License v3.0

