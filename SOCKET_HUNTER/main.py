import psutil
import socket
import threading

def label():
    title_text = '''

█████████████████████████████████████████████████████
█─▄▄▄▄█─▄▄─█─▄▄▄─█▄▄▄░█─▄─▄─█▀▀▀▀▀██─█─█▄─██─▄█▄─▄─▀█
█▄▄▄▄─█─██─█─███▀██▄▄░███─██████████─▄─██─██─███─▄─▀█
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▄▀▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀


'''
    return title_text

def get_outgoing_connections():
    connections = psutil.net_connections(kind='inet')
    outgoing_connections = []
    
    for conn in connections:
        if conn.status == 'ESTABLISHED' and conn.raddr:
            outgoing_connections.append((conn.laddr.ip, conn.laddr.port, conn.raddr.ip, conn.raddr.port))
    
    return outgoing_connections

class LiveConnectionMonitor:
    def __init__(self):
        self.connections = {}
        self.lock = threading.Lock()
        
    def start(self):
        while True:
            outgoing_connections = get_outgoing_connections()
            
            with self.lock:
                for conn in outgoing_connections:
                    if conn not in self.connections:
                        self.connections[conn] = self.connect_and_monitor(conn)
            
            active_connections = list(self.connections.keys())
            for conn in active_connections:
                if conn not in outgoing_connections:
                    with self.lock:
                        self.connections.pop(conn)
            
    def connect_and_monitor(self, conn_info):
        local_ip, local_port, remote_ip, remote_port = conn_info
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(2)  # Adjust the timeout as needed
        
        try:
            client_socket.connect((remote_ip, remote_port))
            print(f"[+][---] Connected to {remote_ip}:{remote_port}")
        except Exception as e:
            print(f"Error connecting to {remote_ip}:{remote_port}: {e}")
            return None
        
        connection_thread = threading.Thread(target=self.monitor_connection, args=(conn_info, client_socket))
        connection_thread.start()
        
        return client_socket
    
    def monitor_connection(self, conn_info, client_socket):
        local_ip, local_port, remote_ip, remote_port = conn_info
        
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"[+][<--] Connection {local_ip}:{local_port} -> {remote_ip}:{remote_port} - Received: {data.decode()}")
            except:
                break
        
        print(f"[+][-->] Connection {local_ip}:{local_port} -> {remote_ip}:{remote_port} - Closed")
        client_socket.close()

if __name__ == "__main__":
    print(label())
    monitor = LiveConnectionMonitor()
    monitor_thread = threading.Thread(target=monitor.start)
    monitor_thread.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Shutting down...")
