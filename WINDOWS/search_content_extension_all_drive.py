import os

# Function to search for files with a specific keyword and extension
def search_files(keyword, extension):
    results = []
    
    # Iterate through all drives on Windows (A-Z)
    for drive in range(ord('A'), ord('Z')+1):
        drive = chr(drive) + ":\\"
        if os.path.exists(drive):
            for root, _, files in os.walk(drive):
                for filename in files:
                    if filename.lower().endswith(extension.lower()):
                        file_path = os.path.join(root, filename)
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                                content = file.read()
                                if keyword.lower() in content.lower():
                                    results.append(file_path)
                        except Exception as e:
                            pass  # Ignore unreadable files

    return results

# Get user input for keyword and extension
keyword = input("Enter the keyword to search for: ")
extension = input("Enter the file extension (e.g., .txt, .docx): ")

# Search for files
found_files = search_files(keyword, extension)

# Display the results with full paths
if found_files:
    print(f"Files containing '{keyword}' with '{extension}' extension:")
    for file in found_files:
        print(file)
else:
    print(f"No files found containing '{keyword}' with '{extension}' extension.")
