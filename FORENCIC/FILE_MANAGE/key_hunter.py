import os
import re

def identify_secure_keys_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        file_content = file.read()
        
        # Regular expressions to identify secure keys
        secure_key_patterns = [
            # SSH keys (RSA, DSA, ECDSA, Ed25519)
            r'-----BEGIN (?:RSA|DSA|EC|OpenSSH) PRIVATE KEY-----',
            r'ssh-(?:rsa|dsa|ecdsa|ed25519) [A-Za-z0-9+/=]+',
            
            # BitLocker recovery keys
            r'BitLocker Recovery Key',
            
            # SSL/TLS private keys (PEM format)
            r'-----BEGIN (?:RSA|DSA|EC|PRIVATE|ENCRYPTED) KEY-----',
            
            # Git tokens (GitHub, GitLab, etc.)
            r'github\.com[/:]?[a-zA-Z0-9\-]+/[a-zA-Z0-9\-]+\.git(?:[\w\.:/-]+)?',
            r'gitlab\.com[/:]?[a-zA-Z0-9\-]+/[a-zA-Z0-9\-]+\.git(?:[\w\.:/-]+)?',
        ]

        for pattern in secure_key_patterns:
            if re.search(pattern, file_content):
                return True

    return False

def identify_secure_keys_in_directory(directory):
    secure_key_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if identify_secure_keys_in_file(file_path):
                secure_key_files.append(file_path)
    
    return secure_key_files

if __name__ == "__main__":
    directory_to_scan = input("Enter the directory path to scan for secure keys: ")
    secure_key_files = identify_secure_keys_in_directory(directory_to_scan)

    if secure_key_files:
        print("Secure keys found in the following files:")
        for file_path in secure_key_files:
            print(file_path)
    else:
        print("No secure keys found in the specified directory.")
