import subprocess
import pyperclip
import platform
import os
import hashlib

def extract_registry_information(registry_key, output_file):
    try:
        # Use the 'reg query' command to extract registry information
        command = f'reg query {registry_key} /s > {output_file}'
        subprocess.run(command, shell=True, check=True)
        print(f"Registry information extracted and saved to {output_file}")
    except subprocess.CalledProcessError:
        print("Error occurred while extracting registry information.")

def extract_clipboard_contents(output_file):
    clipboard_text = pyperclip.paste()
    with open(output_file, 'w') as f:
        f.write(clipboard_text)
    print(f"Clipboard contents extracted and saved to {output_file}")

def extract_system_information(output_file):
    system_info = f"System Information:\n\n"
    system_info += f"OS: {platform.system()} {platform.release()}\n"
    system_info += f"Processor: {platform.processor()}\n"
    system_info += f"Memory: {platform.memory()} bytes\n"
    system_info += f"Disk Information:\n"

    try:
        disk_info = subprocess.check_output("wmic diskdrive get caption,size", shell=True).decode("utf-8")
        system_info += disk_info
    except subprocess.CalledProcessError:
        system_info += "Error retrieving disk information.\n"

    with open(output_file, 'w') as f:
        f.write(system_info)
    print(f"System information extracted and saved to {output_file}")

def extract_running_processes(output_file):
    try:
        process_info = subprocess.check_output("tasklist", shell=True).decode("utf-8")
        with open(output_file, 'w') as f:
            f.write(process_info)
        print(f"Running process list extracted and saved to {output_file}")
    except subprocess.CalledProcessError:
        print("Error retrieving running process list.")

def extract_running_services(output_file):
    try:
        services_info = subprocess.check_output("net start", shell=True).decode("utf-8")
        with open(output_file, 'w') as f:
            f.write(services_info)
        print(f"Running services list extracted and saved to {output_file}")
    except subprocess.CalledProcessError:
        print("Error retrieving running services list.")

def search_files_by_extension(extension, drive_letter, output_file):
    try:
        search_command = f'where /r {drive_letter}: *.{extension}'
        file_paths = subprocess.check_output(search_command, shell=True, text=True).splitlines()
        with open(output_file, 'w') as f:
            for path in file_paths:
                f.write(path + '\n')
        print(f"File paths with extension .{extension} extracted and saved to {output_file}")
    except subprocess.CalledProcessError:
        print("Error occurred while searching for files.")

def search_files_by_md5_hash(md5_hash, drive_letter, output_file):
    try:
        search_command = f'certutil -hashfile "{drive_letter}:\\*" MD5'
        hash_output = subprocess.check_output(search_command, shell=True, text=True)
        hash_lines = hash_output.splitlines()
        
        matching_files = []
        for line in hash_lines:
            if md5_hash in line:
                file_path = line.split(None, 1)[1]
                matching_files.append(file_path)
        
        with open(output_file, 'w') as f:
            for path in matching_files:
                f.write(path + '\n')
        
        print(f"File paths with MD5 hash {md5_hash} extracted and saved to {output_file}")
    except subprocess.CalledProcessError:
        print("Error occurred while searching for files by MD5 hash.")

def calculate_md5_hash(file_path):
    try:
        with open(file_path, 'rb') as f:
            md5_hash = hashlib.md5(f.read()).hexdigest()
            print(f"MD5 hash value of {file_path}: {md5_hash}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

def extract_cmd_history(output_file):
    try:
        history_command = 'doskey /history'
        cmd_history = subprocess.check_output(history_command, shell=True, text=True)
        with open(output_file, 'w') as f:
            f.write(cmd_history)
        print(f"Command history extracted and saved to {output_file}")
    except subprocess.CalledProcessError:
        print("Error retrieving command history.")

def main():
    print("Data Extraction Tool")
    print("--------------------")

    while True:
        print("Choose an option:")
        print("1. Extract Registry Information")
        print("2. Extract Clipboard Contents")
        print("3. Extract System Information")
        print("4. Extract Running Process List")
        print("5. Extract Running Services List")
        print("6. Search Files by Extension")
        print("7. Extract Command History")
        print("8. Search Files by MD5 Hash")
        print("9. Calculate MD5 Hash")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            registry_key = input("Enter the registry key (e.g., HKLM): ")
            output_file = input("Enter the output file name: ")
            extract_registry_information(registry_key, output_file)
        elif choice == '2':
            output_file = input("Enter the output file name: ")
            extract_clipboard_contents(output_file)
        elif choice == '3':
            output_file = input("Enter the output file name: ")
            extract_system_information(output_file)
        elif choice == '4':
            output_file = input("Enter the output file name: ")
            extract_running_processes(output_file)
        elif choice == '5':
            output_file = input("Enter the output file name: ")
            extract_running_services(output_file)
        elif choice == '6':
            extension = input("Enter the file extension (without dot): ")
            drive_letter = input("Enter the drive letter (e.g., C): ")
            output_file = input("Enter the output file name: ")
            search_files_by_extension(extension, drive_letter, output_file)
        elif choice == '7':
            output_file = input("Enter the output file name: ")
            extract_cmd_history(output_file)
        elif choice == '8':
            md5_hash = input("Enter the MD5 hash value: ")
            drive_letter = input("Enter the drive letter (e.g., C): ")
            output_file = input("Enter the output file name: ")
            search_files_by_md5_hash(md5_hash, drive_letter, output_file)
        elif choice == '9':
            file_path = input("Enter the file path: ")
            calculate_md5_hash(file_path)
        elif choice == '10':
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please select 1-10.")

if __name__ == "__main__":
    main()
