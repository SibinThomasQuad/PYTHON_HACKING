from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_key_pair():
    """Generate an RSA key pair."""
    key_pair = RSA.generate(2048)
    return key_pair


def encrypt_message(message, public_key):
    """Encrypt the message using the provided public key."""
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, private_key):
    """Decrypt the encrypted message using the provided private key."""
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message


# Example usage
message_to_send = "This is a confidential email message."

# Generate a key pair
key_pair = generate_key_pair()

# Extract the public and private keys from the key pair
public_key = key_pair.publickey()
private_key = key_pair

# Encrypt the message using the public key
encrypted_message = encrypt_message(message_to_send, public_key)

# Decrypt the message using the private key
decrypted_message = decrypt_message(encrypted_message, private_key)

print(f"Original message: {message_to_send}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")

