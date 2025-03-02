Port Scanner
This is a simple Python-based Port Scanner that allows you to check open ports on a target system or network. The tool scans a range of ports and provides feedback on whether they are open or closed, making it useful for network administrators, security researchers, or anyone interested in network security.

Features
Scans a specified range of ports on a given target IP.
Displays the status of each port (open/closed).
Written in Python for simplicity and ease of use.
Provides a clear output of the scan results.
Requirements
Python 3.x (For Linux and MacOS, use python3)
No external libraries required (uses the built-in socket library).
Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/amaelahmed/portscanner.git
cd portscanner
2. Create a Virtual Environment (Optional but recommended)
bash
Copy
Edit
python3 -m venv venv
3. Activate the Virtual Environment
On Linux and MacOS:
bash
Copy
Edit
source venv/bin/activate
On Windows:
bash
Copy
Edit
venv\Scripts\activate
4. Run the Port Scanner
After setting up the environment, run the port_scanner.py script:

bash
Copy
Edit
python port_scanner.py
You can change the IP address and port range in the script for your own use case.

Usage
The script will prompt you for the target IP address and the port range you want to scan.
The tool will check each port in the range and display whether it's open or closed.
Example Output
bash
Copy
Edit
Scanning target: 192.168.1.1
Port 80: Open
Port 443: Open
Port 22: Closed
...
License
This project is open-source and available under the MIT License.

