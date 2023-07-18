import socket

# Define a function to scan for open ports on a target host
def scan_for_open_ports(host, start_port, end_port):
    # Iterate over the range of port numbers to scan
    for port in range(start_port, end_port + 1):
        # Create a new socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout value of 1 second
        sock.settimeout(1)
        try:
            # Attempt to connect to the target host on the specified port
            result = sock.connect_ex((host, port))
            # Check if the connection was successful (result is 0)
            if result == 0:
                print('Port', port, 'is open')
            # Close the socket connection
            sock.close()
        except socket.error:
            # Handle any errors that occur while attempting to connect
            print('Could not connect to port', port)

# Test the function with a sample host and port range
scan_for_open_ports('128.106.56.244', 1, 1024)
