import os
import re

# Function to search for files matching the regular expression in a directory
def search_files_by_regex(directory, extensions, regex_pattern):
    matching_files = []

    # Split the comma-separated extensions into a list
    allowed_extensions = [ext.strip() for ext in extensions.split(',')]

    # Compile the regular expression pattern
    regex = re.compile(regex_pattern)

    for root, _, files in os.walk(directory):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            if file_extension.lstrip('.').lower() in allowed_extensions:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file_content:
                        content = file_content.read()
                        if regex.search(content):
                            matching_files.append(file_path)
                except Exception as e:
                    print(f"Error processing file {file_path}: {str(e)}")

    return matching_files

# Input: Folder path, allowed extensions, and regular expression pattern
folder_path = input("Enter the folder path: ")
extensions = input("Enter the allowed extensions (comma-separated): ")
regex_pattern = input("Enter the regular expression pattern: ")

# Search for matching files
matching_files = search_files_by_regex(folder_path, extensions, regex_pattern)

# Display the matching files
if matching_files:
    print("Matching files found:")
    for file in matching_files:
        print(file)
else:
    print("No matching files found.")
