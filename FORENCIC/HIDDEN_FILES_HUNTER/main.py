import os

def find_hidden_items(root_dir):
    hidden_items = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for item in dirnames + filenames:
            full_path = os.path.join(dirpath, item)
            if is_hidden(full_path):
                hidden_items.append(full_path)

    return hidden_items

def is_hidden(path):
    try:
        attrs = os.stat(path).st_file_attributes
        return attrs == (attrs | FILE_ATTRIBUTE_HIDDEN)
    except Exception:
        return False

FILE_ATTRIBUTE_HIDDEN = 0x2

def main():
    root_directory = input("Enter the root directory path: ")
    print("Scanning hidden items...")
    hidden_items = find_hidden_items(root_directory)

    if hidden_items:
        print("Hidden items found:")
        for item in hidden_items:
            print(item)
    else:
        print("No hidden items found.")

if __name__ == "__main__":
    main()
