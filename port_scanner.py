import socket
import threading
from datetime import datetime

# Function to scan a single port
def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Reduced timeout for faster scanning
            if s.connect_ex((target, port)) == 0:
                print(f"Port {port} is OPEN")
    except:
        pass  # Ignore errors

# Function to scan multiple ports using threading
def port_scanner(target, start_port, end_port):
    print("\n" + "-" * 50)
    print(f"Scanning target: {target}")
    print(f"Scan started at: {datetime.now()}")
    print("-" * 50)

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print total scan time
    print(f"Scan completed at: {datetime.now()}")

# Get target input from user
target = input("Enter the IP address or hostname to scan: ")
port_scanner(target, 1, 1024)  # Scan ports from 1 to 1024
