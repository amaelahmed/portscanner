import socket
from datetime import datetime

# Clear the screen
print("\n" + "-"*50)
print("Port Scanner")
print("-"*50)

# Get the target from the user
target = input("Enter the IP address or hostname to scan: ")

# Get the current time
start_time = datetime.now()

# Print the start time
print(f"Scanning target: {target}")
print(f"Scan started at: {start_time}")

# Define the range of ports to scan (1-1024 for this example)
for port in range(1, 1025):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout if connection takes too long

    # Try to connect to the target and port
    result = s.connect_ex((target, port))

    # Check if the port is open (result will be 0 if successful)
    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()

# Get the end time
end_time = datetime.now()
# Print the total time taken to complete the scan
print(f"Scan completed at: {end_time}")
print(f"Time taken: {end_time - start_time}")
