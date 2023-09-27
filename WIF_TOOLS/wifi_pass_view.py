import subprocess
print("="*100)
print("--WIFI PASSVIEWER--")
print("="*100)
# Run the "netsh wlan show profiles" command to get the list of saved Wi-Fi profiles
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)

# Check if the command was successful
if command_output.returncode == 0:
    # Extract the profile names from the command output
    profile_names = [line.split(":")[1].strip() for line in command_output.stdout.split("\n") if "All User Profile" in line]

    # Loop through the profile names and retrieve the passwords
    for profile_name in profile_names:
        # Run the "netsh wlan show profile name=<profile_name> key=clear" command for each profile
        password_output = subprocess.run(["netsh", "wlan", "show", "profile", "name=" + profile_name, "key=clear"],
                                         capture_output=True, text=True)
        
        # Check if the command was successful
        if password_output.returncode == 0:
            # Extract the password from the command output
            password_lines = [line for line in password_output.stdout.split("\n") if "Key Content" in line]
            if password_lines:
                password = password_lines[0].split(":")[1].strip()
                print(f"Wi-Fi Profile: {profile_name}")
                print(f"Wi-Fi Password: {password}")
            else:
                print(f"No password found for Wi-Fi Profile: {profile_name}")
        else:
            print(f"Error retrieving password for Wi-Fi Profile: {profile_name}")
        print("="*100)
else:
    print("Error retrieving Wi-Fi profiles.")

