from cProfile import label
import socket
class Label:
    
    def label(self):
        label = '''
        █████████████████████████████████████████████████████
        █▄─▄▄─█─▄▄─█▄─▄▄▀█─▄─▄─███─▄▄▄─█─█─█▄▄▄░█─▄▄▄─█▄─█─▄█
        ██─▄▄▄█─██─██─▄─▄███─█████─███▀█─▄─██▄▄░█─███▀██─▄▀██
        ▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

        '''
        return label

class Scan:
    
    def check_port(self,ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        try:
            sock.connect((ip, port))
            print(f"Port {port} is open on {ip}")
        except socket.error:
            print(f"Port {port} is closed on {ip}")
        finally:
            sock.close()


def main():
    print(Label().label())
    ip = input("Enter IP or domain: ")
    port = int(input("Enter port number: "))
    Scan().check_port(ip, port)
try:
    main()
except:
    print("\nSomething went wrong please try again @@")
