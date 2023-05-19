import socket

# MAC address of the Bluetooth device to connect to
target_address = '00:00:00:00:00:00'  # Replace with the MAC address of your device

# RFCOMM channel number (default is 1)
channel = 1

# Create a socket
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Connect to the Bluetooth device
sock.connect((target_address, channel))

# Now, you can send and receive data through the socket

# Close the socket
sock.close()
