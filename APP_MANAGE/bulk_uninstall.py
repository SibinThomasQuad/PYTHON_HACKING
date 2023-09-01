import subprocess

def list_installed_apps():
    try:
        # Run PowerShell command to list installed applications
        cmd = "Get-WmiObject -Class Win32_Product | Select-Object -Property Name"
        result = subprocess.run(["powershell.exe", "-Command", cmd], stdout=subprocess.PIPE, shell=True, text=True, check=True)
        app_list = result.stdout.strip().split('\n')
        
        return app_list
    except subprocess.CalledProcessError as e:
        print(f"Failed to list installed apps: {str(e)}")
        return []

def uninstall_app(app_name):
    try:
        # Run PowerShell command to uninstall the selected application
        cmd = f"Get-WmiObject -Class Win32_Product | Where-Object {{ $_.Name -eq '{app_name}' }} | ForEach-Object {{ $_.Uninstall() }}"
        subprocess.run(["powershell.exe", "-Command", cmd], shell=True, check=True)
        print(f"Successfully uninstalled: {app_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to uninstall {app_name}: {str(e)}")

def main():
    app_list = list_installed_apps()

    if not app_list:
        print("No installed applications found.")
        return

    print("Installed Applications:")
    for idx, app_name in enumerate(app_list, start=1):
        print(f"{idx}. {app_name}")

    try:
        choice = int(input("Enter the number of the application to uninstall (0 to exit): "))
        if 0 < choice <= len(app_list):
            selected_app = app_list[choice - 1]
            uninstall_app(selected_app)
        elif choice == 0:
            print("Exiting...")
        else:
            print("Invalid choice. Please select a valid application number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
