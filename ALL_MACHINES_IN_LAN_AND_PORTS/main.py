import socket
from concurrent.futures import ThreadPoolExecutor
def label():
    print('''
          
          
██████╗░░█████╗░██████╗░████████╗░░░░░░██╗░░██╗░░██╗██╗░░░██╗███╗░░██╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝░░░░░░╚██╗░██║░░██║██║░░░██║████╗░██║╚══██╔══╝
██████╔╝██║░░██║██████╔╝░░░██║░░░█████╗░╚██╗███████║██║░░░██║██╔██╗██║░░░██║░░░
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░╚════╝░██╔╝██╔══██║██║░░░██║██║╚████║░░░██║░░░
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░░░░░░░██╔╝░██║░░██║╚██████╔╝██║░╚███║░░░██║░░░
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚═╝░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░
          ''')
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+]  IP Address {ip}, Port {port} is open.")
        sock.close()
    except (socket.timeout, socket.error):
        pass  # Port is closed or not reachable

def scan_ip_range(base_ip, start_range, end_range, ports):
    with ThreadPoolExecutor() as executor:
        for last_octet in range(start_range, end_range + 1):
            ip = f"{base_ip}.{last_octet}"
            for port in ports:
                executor.submit(scan_port, ip, port)

if __name__ == "__main__":
    print(label())
    base_ip = "192.168.3"  # Change this to your LAN's base IP address
    start_range = 1
    end_range = 255
    ports_to_scan = [80, 443, 22, 21]  # Add more ports if needed

    scan_ip_range(base_ip, start_range, end_range, ports_to_scan)
