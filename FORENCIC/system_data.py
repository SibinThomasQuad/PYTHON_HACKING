import os
import hashlib
import datetime
import pytz
import re
import stat
import pwd
import grp
import shutil
import sqlite3
import winreg

def get_file_size(filepath):
    return os.path.getsize(filepath)

def get_file_extension(filepath):
    _, ext = os.path.splitext(filepath)
    return ext

def is_file_hidden(filepath):
    attrs = os.stat(filepath).st_file_attributes
    return attrs & stat.FILE_ATTRIBUTE_HIDDEN

def calculate_md5(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        md5_hash = hashlib.md5(content).hexdigest()
    return md5_hash

def calculate_sha1(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        sha1_hash = hashlib.sha1(content).hexdigest()
    return sha1_hash

def get_file_creation_time(filepath):
    timestamp = os.path.getctime(filepath)
    return datetime.datetime.fromtimestamp(timestamp)

def get_file_modified_time(filepath):
    timestamp = os.path.getmtime(filepath)
    return datetime.datetime.fromtimestamp(timestamp)

def get_file_accessed_time(filepath):
    timestamp = os.path.getatime(filepath)
    return datetime.datetime.fromtimestamp(timestamp)

def get_file_permissions(filepath):
    mode = os.stat(filepath).st_mode
    permissions = stat.filemode(mode)
    return permissions

def get_file_owner(filepath):
    return pwd.getpwuid(os.stat(filepath).st_uid).pw_name

def get_file_group(filepath):
    return grp.getgrgid(os.stat(filepath).st_gid).gr_name

def search_regex_in_file(filepath, regex_pattern):
    matches = []
    with open(filepath, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if re.search(regex_pattern, line):
                matches.append((line_number, line.rstrip()))
    return matches

def extract_email_addresses(filepath):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return search_regex_in_file(filepath, email_pattern)

def create_disk_image(source_path, destination_path):
    shutil.copyfile(source_path, destination_path)

def create_memory_dump(output_file_path):
    # Implement memory dump creation using external tools or libraries
    pass

def parse_log_file(filepath):
    logs = []
    with open(filepath, 'r') as file:
        for line in file:
            # Implement parsing logic specific to the log format
            parsed_log = parse_line(line)
            logs.append(parsed_log)
    return logs

def analyze_log_entries(logs):
    # Perform analysis on the parsed log entries
    pass

def extract_browser_history():
    browser_db_paths = {
        "Chrome": r"C:\Users\{username}\AppData\Local\Google\Chrome\User Data\Default\History",
        "Firefox": r"C:\Users\{username}\AppData\Roaming\Mozilla\Firefox\Profiles\{profile}\places.sqlite"
        # Add more browsers and their database paths as needed
    }

    for browser, db_path in browser_db_paths.items():
        expanded_path = os.path.expandvars(db_path)
        if os.path.exists(expanded_path):
            if browser == "Chrome":
                extract_chrome_history(expanded_path)
            elif browser == "Firefox":
                extract_firefox_history(expanded_path)
            # Add more browser-specific history extraction functions as needed
        else:
            print(f"{browser} history database not found.")

def extract_chrome_history(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT url, title, last_visit_time FROM urls")
    rows = c.fetchall()

    print("Chrome History:")
    for row in rows:
        url = row[0]
        title = row[1]
        visit_time = datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=row[2])
        print(f"URL: {url}\nTitle: {title}\nVisit Time: {visit_time}\n")

    conn.close()

def extract_firefox_history(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT url, title, last_visit_date FROM moz_places")
    rows = c.fetchall()

    print("Firefox History:")
    for row in rows:
        url = row[0]
        title = row[1]
        visit_time = datetime.datetime.fromtimestamp(row[2] / 1000000)
        print(f"URL: {url}\nTitle: {title}\nVisit Time: {visit_time}\n")

    conn.close()

def list_users():
    users = pwd.getpwall()
    print("List of Users:")
    for user in users:
        print(f"Username: {user.pw_name}")
        print(f"User ID: {user.pw_uid}")
        print(f"Home Directory: {user.pw_dir}")
        print()

def list_installed_apps():
    app_paths = []
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as key:
        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            with winreg.OpenKey(key, subkey_name) as subkey:
                try:
                    app_path = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    app_paths.append(app_path)
                except OSError:
                    pass

    print("Installed Apps:")
    for app_path in app_paths:
        print(app_path)

def list_running_apps():
    # Implement listing of running apps based on the platform (e.g., Windows-specific APIs, task manager, etc.)
    pass

def search_file_by_md5(root_path, md5_hash):
    found_files = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if calculate_md5(file_path) == md5_hash:
                found_files.append(file_path)
    return found_files

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_option():
    clear_screen()
    print("Digital Forensic Functions")
    print("--------------------------")
    print("1. Get File Size")
    print("2. Get File Extension")
    print("3. Check if File is Hidden")
    print("4. Calculate MD5 Hash")
    print("5. Calculate SHA-1 Hash")
    print("6. Get File Creation Time")
    print("7. Get File Modified Time")
    print("8. Get File Accessed Time")
    print("9. Get File Permissions")
    print("10. Get File Owner")
    print("11. Get File Group")
    print("12. Search Regex in File")
    print("13. Extract Email Addresses from File")
    print("14. Create Disk Image")
    print("15. Create Memory Dump")
    print("16. Parse Log File")
    print("17. Analyze Log Entries")
    print("18. Extract Browser History")
    print("19. List Users")
    print("20. List Installed Apps")
    print("21. List Running Apps")
    print("22. Search File by MD5 Hash")
    print("23. Exit")
    print()

    choice = input("Enter your choice (1-23): ")
    return choice

def process_choice(choice):
    if choice == "1":
        filepath = input("Enter the file path: ")
        print("File Size:", get_file_size(filepath))
    elif choice == "2":
        filepath = input("Enter the file path: ")
        print("File Extension:", get_file_extension(filepath))
    elif choice == "3":
        filepath = input("Enter the file path: ")
        print("Is File Hidden:", is_file_hidden(filepath))
    elif choice == "4":
        filepath = input("Enter the file path: ")
        print("MD5 Hash:", calculate_md5(filepath))
    elif choice == "5":
        filepath = input("Enter the file path: ")
        print("SHA-1 Hash:", calculate_sha1(filepath))
    elif choice == "6":
        filepath = input("Enter the file path: ")
        print("File Creation Time:", get_file_creation_time(filepath))
    elif choice == "7":
        filepath = input("Enter the file path: ")
        print("File Modified Time:", get_file_modified_time(filepath))
    elif choice == "8":
        filepath = input("Enter the file path: ")
        print("File Accessed Time:", get_file_accessed_time(filepath))
    elif choice == "9":
        filepath = input("Enter the file path: ")
        print("File Permissions:", get_file_permissions(filepath))
    elif choice == "10":
        filepath = input("Enter the file path: ")
        print("File Owner:", get_file_owner(filepath))
    elif choice == "11":
        filepath = input("Enter the file path: ")
        print("File Group:", get_file_group(filepath))
    elif choice == "12":
        filepath = input("Enter the file path: ")
        pattern = input("Enter the regex pattern: ")
        print("Matches:")
        matches = search_regex_in_file(filepath, pattern)
        for line_number, line in matches:
            print(f"Line {line_number}: {line}")
    elif choice == "13":
        filepath = input("Enter the file path: ")
        print("Email Addresses:")
        emails = extract_email_addresses(filepath)
        for line_number, email in emails:
            print(f"Line {line_number}: {email}")
    elif choice == "14":
        source_path = input("Enter the source file path: ")
        destination_path = input("Enter the destination file path: ")
        create_disk_image(source_path, destination_path)
        print("Disk image created successfully.")
    elif choice == "15":
        output_file_path = input("Enter the output file path: ")
        create_memory_dump(output_file_path)
        print("Memory dump created successfully.")
    elif choice == "16":
        filepath = input("Enter the log file path: ")
        logs = parse_log_file(filepath)
        analyze_log_entries(logs)
        print("Log file parsed and analyzed.")
    elif choice == "17":
        print("Log analysis functionality not implemented yet.")
    elif choice == "18":
        extract_browser_history()
    elif choice == "19":
        list_users()
    elif choice == "20":
        list_installed_apps()
    elif choice == "21":
        list_running_apps()
    elif choice == "22":
        root_path = input("Enter the root directory path: ")
        md5_hash = input("Enter the MD5 hash: ")
        found_files = search_file_by_md5(root_path, md5_hash)
        if found_files:
            print("Files with the given MD5 hash:")
            for file_path in found_files:
                print(file_path)
        else:
            print("No files found with the given MD5 hash.")
    elif choice == "23":
        print("Exiting...")
        return True
    else:
        print("Invalid choice. Please try again.")

    input("Press Enter to continue...")
    return False

def main():
    exit_program = False
    while not exit_program:
        choice = prompt_option()
        exit_program = process_choice(choice)

if __name__ == "__main__":
    main()
