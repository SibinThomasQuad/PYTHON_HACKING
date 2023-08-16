import hashlib
import os
import re
import subprocess
from datetime import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def calculate_hash(filepath, algorithm='sha256'):
    try:
        hash_obj = hashlib.new(algorithm)
        with open(filepath, 'rb') as file:
            while chunk := file.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        return str(e)

def get_file_metadata(filepath):
    try:
        stat_info = os.stat(filepath)
        metadata = {
            'size_bytes': stat_info.st_size,
            'created': datetime.fromtimestamp(stat_info.st_ctime),
            'modified': datetime.fromtimestamp(stat_info.st_mtime),
            'accessed': datetime.fromtimestamp(stat_info.st_atime),
            'permissions': oct(stat_info.st_mode)[-3:],
            'owner_uid': stat_info.st_uid,
            'group_gid': stat_info.st_gid
        }
        return metadata
    except Exception as e:
        return str(e)

def carve_embedded_files(filepath):
    try:
        with open(filepath, 'rb') as file:
            data = file.read()
            embedded_files = re.findall(rb'\x89PNG\x0D\x0A\x1A\x0A', data)
            return len(embedded_files)
    except Exception as e:
        return str(e)

def search_for_keywords(filepath, keywords):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as file:
            content = file.read()
            matches = []
            for keyword in keywords:
                if keyword in content:
                    matches.append(keyword)
            return matches
    except Exception as e:
        return str(e)

def create_memory_dump(output_path):
    try:
        subprocess.run(['winpmem', '-o', output_path], capture_output=True, text=True, check=True)
        print(f"Memory dump created at: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating memory dump: {e.stderr}")

def run_volatility(plugin, memory_dump_path):
    try:
        result = subprocess.check_output(['volatility', '-f', memory_dump_path, plugin])
        return result.decode('utf-8')
    except Exception as e:
        return str(e)

def main():
    if not is_admin():
        print("This script requires administrative privileges. Restarting with elevated permissions...")
        run_as_admin()
        sys.exit()

    while True:
        print("\nDigital Forensics Toolkit")
        print("1. Calculate File Hash - Calculate hash value of a file.")
        print("2. Get File Metadata - Display metadata information about a file.")
        print("3. Carve Embedded Files - Find and count embedded files in a file.")
        print("4. Search for Keywords in a File - Search for keywords in a text file.")
        print("5. Create Memory Dump - Create a memory dump of the system (requires winpmem).")
        print("6. Run Volatility Plugin - Run a Volatility plugin on a memory dump.")
        print("7. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            filepath = input("Enter file path: ")
            hash_algorithm = input("Enter hash algorithm (default: sha256): ")
            hash_value = calculate_hash(filepath, hash_algorithm)
            print(f"Hash value: {hash_value}")
        elif choice == '2':
            filepath = input("Enter file path: ")
            metadata = get_file_metadata(filepath)
            print("File Metadata:")
            for key, value in metadata.items():
                print(f"{key}: {value}")
        elif choice == '3':
            filepath = input("Enter file path: ")
            embedded_file_count = carve_embedded_files(filepath)
            print(f"Found {embedded_file_count} embedded files.")
        elif choice == '4':
            filepath = input("Enter file path: ")
            keywords = input("Enter keywords (comma-separated): ").split(',')
            matches = search_for_keywords(filepath, keywords)
            if matches:
                print("Keywords found:", ', '.join(matches))
            else:
                print("No matches found.")
        elif choice == '5':
            output_path = input("Enter output path for memory dump: ")
            create_memory_dump(output_path)
        elif choice == '6':
            memory_dump_path = input("Enter memory dump file path: ")
            plugin = input("Enter Volatility plugin: ")
            result = run_volatility(plugin, memory_dump_path)
            print(result)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
