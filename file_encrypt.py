from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a new encryption key and saves it to a file.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the encryption key from the key file.
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(filename, key):
    """
    Encrypts the specified file using the given encryption key.
    """
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
        encrypted_data = fernet.encrypt(data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    """
    Decrypts the specified file using the given encryption key.
    """
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# Example usage:
# Generate a new key:
# generate_key()

# Load the key:
key = load_key()

# Encrypt a file:
# encrypt_file("example.txt", key)

# Decrypt a file:
# decrypt_file("example.txt", key)
