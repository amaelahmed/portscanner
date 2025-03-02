# Port Scanner

This is a simple Python-based Port Scanner that allows you to check open ports on a target system or network. The tool scans a range of ports and provides feedback on whether they are open or closed, making it useful for network administrators, security researchers, or anyone interested in network security.

## Features

- Scans a specified range of ports on a given target IP.
- Displays the status of each port (open/closed).
- Written in Python for simplicity and ease of use.
- Provides a clear output of the scan results.

## Requirements

- Python 3.x (For Linux and MacOS, use `python3`).
- No external libraries required (uses the built-in `socket` library).

## Installation

### 1. Clone the Repository
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/amaelahmed/portscanner.git
cd portscanner
python3 -m venv venv
source venv/bin/activate
on windows:
venv\Scripts\activate
python port_scanner.py

After setting up the environment, run the port_scanner.py script:

`
python port_scanner.py
````
You can change the IP address and port range in the script for your use case.

Usage
When you run the script, it will prompt you for the target IP address and the port range you want to scan. The tool will check each port in the range and display whether it's open or closed.

````
Example Output:

Scanning target: 192.168.1.1
Port 80: Open
Port 443: Open
Port 22: Closed
...
License
This project is open-source and available under the MIT License.



