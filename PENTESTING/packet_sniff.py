from scapy.all import *

# Define a function to handle each captured packet
def handle_packet(packet):
    # Print the packet details
    print(packet.summary())

# Start sniffing packets on the default network interface
sniff(prn=handle_packet)
