import time
import pywifi
from pywifi import const

def get_wifi_strength():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming you have one Wi-Fi interface

    iface.scan()
    time.sleep(2)
    scan_results = iface.scan_results()

    print("Wi-Fi Networks and Signal Strengths:")
    for result in scan_results:
        ssid = result.ssid
        signal_strength = result.signal
        print(f"SSID: {ssid}, Signal Strength: {signal_strength} dBm")

if __name__ == "__main__":
    get_wifi_strength()
