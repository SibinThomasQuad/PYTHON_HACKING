import os
import hashlib
import datetime

# Function to calculate the MD5 checksum of a file
def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# Function to collect file information and write to a log file
def collect_file_info(root_directory, log_file):
    with open(log_file, 'w') as log:
        for drive in range(ord('A'), ord('Z')+1):
            drive = chr(drive) + ":\\"
            if os.path.exists(drive):
                for root, _, files in os.walk(drive):
                    for filename in files:
                        file_path = os.path.join(root, filename)
                        try:
                            # Calculate MD5 checksum
                            md5_checksum = calculate_md5(file_path)
                            
                            # Get file size
                            file_size = os.path.getsize(file_path)
                            
                            # Get file extension
                            file_extension = os.path.splitext(filename)[-1]
                            
                            # Get file creation and modification dates
                            created_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                            
                            # Write information to the log file
                            log.write(f"File: {file_path}\n")
                            log.write(f"MD5: {md5_checksum}\n")
                            log.write(f"Size: {file_size} bytes\n")
                            log.write(f"Extension: {file_extension}\n")
                            log.write(f"Created Date: {created_time}\n")
                            log.write(f"Modified Date: {modified_time}\n")
                            log.write("\n" + "-" * 80 + "\n")  # Separator line
                        except Exception as e:
                            log.write(f"Error processing {file_path}: {e}\n")

if __name__ == "__main__":
    log_file = "file_info_log.txt"  # The log file to write results to

    collect_file_info("/", log_file)  # "/" is used as the starting point for all drives
    print(f"File information has been logged to {log_file}.")
