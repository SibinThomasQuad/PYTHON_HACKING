import pywifi

def get_wifi_history():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    profiles = iface.network_profiles()

    wifi_history = []

    for profile in profiles:
        wifi_info = {
            "ssid": profile.ssid,
            "bssid": profile.bssid,
            "auth": profile.auth,
            "cipher": profile.cipher,
        }
        wifi_history.append(wifi_info)

    return wifi_history

def main():
    wifi_history = get_wifi_history()

    if wifi_history:
        for idx, wifi_info in enumerate(wifi_history, start=1):
            print(f"Network {idx}:")
            print(f"SSID: {wifi_info['ssid']}")
            print(f"BSSID: {wifi_info['bssid']}")
            print(f"Authentication: {wifi_info['auth']}")
            print(f"Cipher: {wifi_info['cipher']}")
            print("=" * 40)
    else:
        print("No Wi-Fi history found.")

if __name__ == "__main__":
    main()
