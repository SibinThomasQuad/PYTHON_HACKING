from cryptography.fernet import Fernet

def encrypt_message(password, message):
    # Generate a key from the password using Fernet
    key = Fernet.generate_key()

    # Use the key to create a Fernet instance
    fernet = Fernet(key)

    # Encode the message to bytes and encrypt it with the Fernet instance
    encrypted_message = fernet.encrypt(message.encode())

    # Return the key and encrypted message as bytes
    return key, encrypted_message

def decrypt_message(password, key, encrypted_message):
    # Use the password to create a Fernet instance
    fernet = Fernet(key)

    # Decrypt the message using the Fernet instance
    decrypted_message = fernet.decrypt(encrypted_message)

    # Decode the decrypted message to a string and return it
    return decrypted_message.decode()

# Example usage
password = "my_password"
message = "Hello, world!"

# Encrypt the message with the password
key, encrypted_message = encrypt_message(password, message)

# Print the key and encrypted message
print("Key:", key)
print("Encrypted message:", encrypted_message)

# Decrypt the message with the password and key
decrypted_message = decrypt_message(password, key, encrypted_message)

# Print the decrypted message
print("Decrypted message:", decrypted_message)
