from scapy.all import *
import time
import threading

# Define the log file
log_file = "http_traffic.log"

# Function to log HTTP traffic with timestamps
def log_http_traffic(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        try:
            payload = pkt.getlayer(Raw).load.decode('utf-8', errors='ignore')
        except UnicodeDecodeError as e:
            payload = f"Error decoding payload: {e}"

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as log:
            log.write("="*100+"\n")
            log.write(f"Timestamp: {timestamp}\n")
            log.write(f"URL: {payload.strip()}\n")

# Function to display the log file in another thread
def live_view_log():
    while True:
        try:
            with open(log_file, "a", encoding="utf-8") as log:
                print("\n=== HTTP Domain Traffic Logger ===\n")
                print(log.read())
            time.sleep(5)
        except FileNotFoundError:
            pass
        except KeyboardInterrupt:
            break

# Create a thread for live log viewing
log_view_thread = threading.Thread(target=live_view_log)
log_view_thread.daemon = True
log_view_thread.start()

# Start packet capture
try:
    print("HTTP Domain Traffic Logger")
    sniff(filter="tcp port 80 or tcp port 443", prn=log_http_traffic, store=0)
except KeyboardInterrupt:
    print("\nPacket capture stopped.")
