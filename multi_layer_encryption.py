from cryptography.fernet import Fernet
import os

# Encrypt a file using AES encryption
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print("File encrypted successfully.")

# Decrypt a file using AES decryption
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("File decrypted successfully.")

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt and decrypt the file multiple times using different keys
def multilayer_encrypt_decrypt(file_path, num_layers):
    # Encrypt the file
    key = generate_key()

    for i in range(num_layers):
        encrypt_file(file_path, key)
        key = generate_key()

    print("Multilayer encryption completed.")

    # Decrypt the encrypted file
    key = generate_key()

    for i in range(num_layers):
        decrypt_file(file_path + '.enc', key)
        key = generate_key()

    print("Multilayer decryption completed.")

# Example usage
file_path = 'path/to/file.txt'
num_layers = 3

multilayer_encrypt_decrypt(file_path, num_layers)
