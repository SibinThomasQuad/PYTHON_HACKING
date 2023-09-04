import os
import datetime
import hashlib
import ctypes
import win32security

# ANSI escape codes for text color
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def calculate_hash(file_path, hash_algorithm):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as file:
        while True:
            data = file.read(8192)
            if not data:
                break
            hash_object.update(data)
    return hash_object.hexdigest()

def get_file_owner_and_permissions(file_path):
    file_owner = None
    file_permissions = None

    try:
        file_owner_sid, _, _ = win32security.GetFileSecurity(
            file_path, win32security.OWNER_SECURITY_INFORMATION
        )
        file_owner_name, _, _ = win32security.LookupAccountSid(None, file_owner_sid)
        file_owner = file_owner_name
    except Exception as e:
        pass

    try:
        file_permissions = oct(os.stat(file_path).st_mode)[-3:]
    except Exception as e:
        pass

    return file_owner, file_permissions

def search_files_by_date_range(directory, start_date, end_date):
    try:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD' format.")
        return

    found_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            stat_info = os.stat(file_path)
            file_creation_date = datetime.datetime.fromtimestamp(stat_info.st_ctime)
            file_modification_date = datetime.datetime.fromtimestamp(stat_info.st_mtime)

            if start_date <= file_creation_date <= end_date or start_date <= file_modification_date <= end_date:
                md5_hash = calculate_hash(file_path, "md5")
                sha1_hash = calculate_hash(file_path, "sha1")
                file_extension = os.path.splitext(file_path)[1]
                file_owner, file_permissions = get_file_owner_and_permissions(file_path)
                file_size = stat_info.st_size  # Get file size in bytes
                found_files.append((file_path, file_extension, file_owner, file_permissions, file_size, file_creation_date, file_modification_date, md5_hash, sha1_hash))

    return found_files

def main():
    print("File Search by Date Range")
    directory = input("Enter the directory path: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    found_files = search_files_by_date_range(directory, start_date, end_date)

    if found_files:
        print(f"Files modified or created between {start_date} and {end_date}:")
        for file_info in found_files:
            file_path, file_extension, file_owner, file_permissions, file_size, created_date, modified_date, md5_hash, sha1_hash = file_info
            print(f"File: {file_path}")
            print(f"File Extension: {file_extension}")
            print(f"File Owner: {file_owner}")
            print(f"File Permissions: {file_permissions}")
            print(f"File Size (bytes): {file_size}")
            print(f"{GREEN}Created Date: {created_date}{RESET}")  # Green color for created date
            print(f"{RED}Modified Date: {modified_date}{RESET}")  # Red color for modified date
            print(f"MD5 Hash: {md5_hash}")
            print(f"SHA-1 Hash: {sha1_hash}")
            print("-" * 80)
    else:
        print("No files found within the specified date range.")

if __name__ == "__main__":
    main()
