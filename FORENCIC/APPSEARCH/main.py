import subprocess

def get_installed_apps():
    try:
        result = subprocess.run(["wmic", "product", "get", "name"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
        installed_apps = result.stdout.split('\n')
        return installed_apps
    except subprocess.CalledProcessError:
        print("Error fetching installed apps.")
        return []

def filter_apps_by_keywords(apps, keywords):
    filtered_apps = []

    for app in apps:
        app_name = app.strip()
        if any(keyword.lower() in app_name.lower() for keyword in keywords):
            filtered_apps.append(app_name)

    return filtered_apps

def main():
    keywords = ["virtualbox", "vmware", "tor", "onion"]
    installed_apps = get_installed_apps()
    filtered_apps = filter_apps_by_keywords(installed_apps, keywords)

    print("Installed apps matching keywords:")
    for app in filtered_apps:
        print(app)

if __name__ == "__main__":
    main()
