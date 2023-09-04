import winreg
import psutil

def list_installed_apps():
    # Open the Windows Registry key where the installed applications are stored
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    installed_apps = []

    try:
        i = 0
        while True:
            # Enumerate subkeys (each subkey represents an installed program)
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)

            # Read the DisplayName and DisplayVersion values
            try:
                app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                app_version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                installed_apps.append((app_name, app_version))
            except FileNotFoundError:
                pass  # Some subkeys may not have DisplayName or DisplayVersion values

            i += 1

    except OSError:
        pass  # End of registry keys reached

    winreg.CloseKey(key)

    return installed_apps

def list_running_apps():
    running_apps = []

    for process in psutil.process_iter(attrs=["name"]):
        try:
            process_name = process.info["name"]
            running_apps.append(process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return running_apps

def list_running_services():
    running_services = []
    for service in psutil.win_service_iter():
        running_services.append((service.name(), service.display_name()))

    return running_services

def list_startup_apps():
    startup_apps = []
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")

    try:
        i = 0
        while True:
            try:
                entry_name, entry_data, _ = winreg.EnumValue(key, i)
                startup_apps.append((entry_name, entry_data))
            except OSError:
                break

            i += 1

    except OSError:
        pass  # End of registry keys reached

    winreg.CloseKey(key)

    return startup_apps

def list_internet_apps():
    internet_apps = set()
    
    for conn in psutil.net_connections(kind='inet'):
        try:
            pid = conn.pid
            process = psutil.Process(pid)
            app_name = process.name()
            internet_apps.add(app_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return internet_apps

def display_section_title(title):
    print(f"\n=== {title} ===")

def main():
    print("Welcome to App Hunter")
    while True:
        print("="*90)
        print("\nOptions:")
        print("1. List Installed Apps")
        print("2. List Running Apps")
        print("3. List Running Services")
        print("4. List Auto-Starting Apps in Startup")
        print("5. List Internet-Using Applications")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_section_title("Installed Applications")
            installed_apps = list_installed_apps()
            if installed_apps:
                for idx, (app_name, app_version) in enumerate(installed_apps, start=1):
                    print(f"{idx}. {app_name} (Version: {app_version})")
            else:
                print("No installed applications found.")

        elif choice == "2":
            display_section_title("Running Applications")
            running_apps = list_running_apps()
            if running_apps:
                for idx, app_name in enumerate(running_apps, start=1):
                    print(f"{idx}. {app_name}")
            else:
                print("No running applications found.")

        elif choice == "3":
            display_section_title("Running Services")
            running_services = list_running_services()
            if running_services:
                for idx, (service_name, display_name) in enumerate(running_services, start=1):
                    print(f"{idx}. {service_name} (Display Name: {display_name})")
            else:
                print("No running services found.")

        elif choice == "4":
            display_section_title("Auto-Starting Applications in Startup")
            startup_apps = list_startup_apps()
            if startup_apps:
                for idx, (entry_name, entry_data) in enumerate(startup_apps, start=1):
                    print(f"{idx}. {entry_name} (Command: {entry_data})")
            else:
                print("No auto-starting applications found in the startup.")

        elif choice == "5":
            display_section_title("Internet-Using Applications")
            internet_apps = list_internet_apps()
            if internet_apps:
                for idx, app_name in enumerate(internet_apps, start=1):
                    print(f"{idx}. {app_name}")
            else:
                print("No internet-using applications found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
