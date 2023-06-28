from scapy.all import ARP, Ether, srp
import socket
import platform

def banner():
    banner = '''
    
███╗░░██╗██████╗░████████╗░░░░░░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
████╗░██║╚════██╗╚══██╔══╝░░░░░░██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
██╔██╗██║░█████╔╝░░░██║░░░█████╗██║░░░░░██║░░██║██║░░██║█████═╝░
██║╚████║░╚═══██╗░░░██║░░░╚════╝██║░░░░░██║░░██║██║░░██║██╔═██╗░
██║░╚███║██████╔╝░░░██║░░░░░░░░░███████╗╚█████╔╝╚█████╔╝██║░╚██╗
╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░░░░░░░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝
    
    '''
    return banner
def scan_lan(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    
    result = srp(packet, timeout=3, verbose=0)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def get_username(ip):
    try:
        username = socket.gethostbyaddr(ip)[0]
        return username
    except socket.herror:
        return 'Unknown'

def get_operating_system():
    return platform.system()


def main():
    print("Enter IP Range (Eg : 192.168.2.0/24)")
    ip_range = input(">")
    print("-"*50)
    print("Scaning Started ..")
    print("-"*50)
    devices = scan_lan(ip_range)

    for device in devices:
        username = get_username(device['ip'])
        os = get_operating_system()
        print("IP: ", device['ip'])
        print("MAC: ", device['mac'])
        print("Username: ", username)
        print("Operating System: ", os)
        print("-"*50)
try:
    print(banner())
    main()
    print("[+] Scaning completed")
except:
    print("[***] EXITED")
    input("Press any key to quit the app > ")
