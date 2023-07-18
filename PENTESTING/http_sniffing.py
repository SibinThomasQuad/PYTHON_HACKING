from scapy.all import *

# Define a function to handle each captured packet
def handle_packet(packet):
    # Check if the packet is an HTTP packet
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet[TCP].dport == 80:
        # Print the packet details
        print(packet.show())

# Start sniffing packets on the default network interface, with a filter for HTTP traffic
sniff(filter='tcp port 80', prn=handle_packet)
