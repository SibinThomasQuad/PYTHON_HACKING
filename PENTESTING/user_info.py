import socket
import uuid
import getpass

def get_location():
    """
    Gets the IP address of the current machine.
    """
    return socket.gethostbyname(socket.gethostname())

def get_mac():
    """
    Gets the MAC address of the current machine.
    """
    return ':'.join([uuid.UUID(int=uuid.getnode()).hex[-12+i:][:2] for i in range(0,12,2)])

def get_username():
    """
    Gets the username of the current user.
    """
    return getpass.getuser()

# Example usage:
ip_address = get_location()
mac_address = get_mac()
username = get_username()

print("IP Address:", ip_address)
print("MAC Address:", mac_address)
print("Username:", username)
