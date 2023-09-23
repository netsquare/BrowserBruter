# BrowserBruter

BrowserBruter is a web automation tool for fuzzing web forms using Selenium and Python. It automates the process of sending payloads to input fields and capturing HTTP requests and responses to identify potential vulnerabilities.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Usage Demo](#usage-demo)
- [Customization & Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Automated web form fuzzing which utilizes Browser
- Supports both Firefox and Chrome browsers
- Payload-based testing for various input fields
- Multithreaded execution for efficient testing
- Detailed request and response capture
- Highly customizable
- Final report generation for analysis
- Robust handling of crashes so no testing record is lost

## Prerequisites

Before using BrowserBruter, make sure you have the following prerequisites installed:

- **Python 3.x**: The tool is written in Python, so you need Python 3.x installed.

- **Selenium**: Install the Selenium library to automate web interactions using Python.

- **Mozilla Firefox or Google Chrome**: Ensure that your web browser (Firefox or Chrome) is installed.

## Installation

1. Clone this repository:

   ```shell
   git clone https://github.com/netsquare/BrowserBruter.git
   cd BrowserBruter
   ```
2. Install the required Python packages using pip:

    ```shell
   pip install -r requirements.txt
    ```
3. Ensure that your web browser (Firefox or Chrome) is installed.

## Usage
### Basic Usage
   
Navigate to the BrowserBruter directory.

Run the script with Python:

```shell
python BrowserBruter.py [options]
```
Replace `[options]` with the appropriate command-line options, such as specifying the target URL, payloads file, elements to fuzz, browser choice, and more. Use the --help option to view available options and their descriptions.

BrowserBruter will automate the web form fuzzing process and generate individual reports for each thread.

Once all threads have finished, BrowserBruter will merge the reports into a final report for analysis. Final report can be found in `BrowserBruter_Reports` directory.

### For detailed demo of Usage see this demo

## Customization & Configuration

BrowserBruter offers several customization options to tailor your fuzzing sessions:

    --target: Specify the target URL for fuzzing.
    --payloads: Provide a file containing payloads to use for fuzzing.
    --elements: Specify the elements (input fields) to fuzz, separated by commas.
    --threads: Set the number of threads (browser instances) to use for fuzzing.
    --firefox or --chrome: Choose the browser for automation.
    --cookie: Add cookies to the browser session for authenticated testing.
    --headless: Run the browser in headless mode (no GUI).
    --silent: Disable console output for request/response details.
    --form: Specify the form number to target (if multiple forms exist).
    --csrf: Specify the CSRF token field to avoid overwriting it.
    --remove: Clear cookies and other data after each request.

BrowserBruter can be configured using command-line options, but you can also customize the tool further by modifying the source code directly. In the BrowserBruter.py script, you'll find global variables and functions that you can adjust to fit your testing needs.

## Contributing

Contributions to BrowserBruter are welcome! If you have any feature requests, bug reports, or suggestions, please open an issue on the GitHub repository.

To contribute code or improvements:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and test them.
4. Submit a pull request with a clear description of your contribution.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
