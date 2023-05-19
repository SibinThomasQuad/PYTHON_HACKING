import wmi

# Connect to the Windows Management Instrumentation (WMI) service
wmi_service = wmi.WMI()

# Query for Bluetooth devices
bt_devices = wmi_service.query("SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%Bluetooth%'")

# Print the details of each Bluetooth device
for device in bt_devices:
    print("Device Name:", device.Name)
    print("Device Description:", device.Description)
    print("Device ID:", device.DeviceID)

    # Extract the MAC address from the Device ID
    mac_address = device.DeviceID.split("_")[-1]
    print("MAC Address:", mac_address)
    
    print("----")
