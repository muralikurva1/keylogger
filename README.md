# Keylogger Project

## Overview

This project is a Python-based keylogger that records keystrokes and logs them to a file. It also captures the title of the active window and timestamps the keypresses. The application is designed to run in the background and log user input for educational purposes only.

**Note:** Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission before deploying or using this tool.

## Features

- **Keystroke Logging:** Records every key pressed and saves it to `keylogger.log`.
- **Active Window Detection:** Logs the title of the active window along with each keystroke.
- **Timestamping:** Adds a timestamp for each recorded keypress to track when it occurred.
- **Stop Mechanism:** Stops logging when `Ctrl + Alt + Esc` is pressed.

## Installation

### Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)

### Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/muralikurva1/keylogger.git
cd keylogger

### Install Dependencies
Install the required Python packages listed in requirements.txt:
pip install -r requirements.txt

Usage
To run the keylogger, execute the keylogger.py script:
python keylogger.py
