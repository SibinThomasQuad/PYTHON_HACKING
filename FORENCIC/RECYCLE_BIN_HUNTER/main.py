import ctypes
import os
import shutil

def list_files_in_recycle_bin():
    files = []

    # Enumerate items in the Recycle Bin
    recycle_bin_path = os.path.expanduser("~") + "\\AppData\\Local\\Microsoft\\Windows\\Explorer"
    for filename in os.listdir(recycle_bin_path):
        full_path = os.path.join(recycle_bin_path, filename)
        if os.path.isfile(full_path):
            files.append(full_path)

    return files

def restore_file_from_recycle_bin(file_path, restore_folder):
    # Convert file path to Unicode
    file_path = file_path.encode('utf-16-le')

    # SHFileOperation parameters
    flags = 0x0001  # FO_RENAME (move)
    from_file = file_path + b'\x00'
    to_file = os.path.join(restore_folder, os.path.basename(file_path)) + b'\x00'
    params = ctypes.c_wchar_p(to_file)
    params.value += '\0\0'  # Double-null terminated

    # Call SHFileOperation to restore the file
    shell32 = ctypes.windll.shell32
    result = shell32.SHFileOperationW(ctypes.byref(params), flags)
    
    return result == 0

def main():
    files = list_files_in_recycle_bin()

    if not files:
        print("No files found in the Recycle Bin.")
        return

    print("Files in the Recycle Bin:")
    for index, file_path in enumerate(files, start=1):
        print(f"{index}. {file_path}")

    try:
        selection = int(input("Select a file by number: "))
        if 1 <= selection <= len(files):
            selected_file = files[selection - 1]
            restore_folder = input("Enter the restore destination folder: ")

            if not os.path.exists(restore_folder):
                os.makedirs(restore_folder)

            success = restore_file_from_recycle_bin(selected_file, restore_folder)

            if success:
                print("File restored successfully.")
            else:
                print("Failed to restore the file.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
