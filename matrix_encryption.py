import numpy as np

def encrypt(plaintext, key):
    plaintext = np.array(list(plaintext))  # Convert plaintext to numpy array
    key = np.array(key)  # Convert key to numpy array
    key_len = len(key)
    plaintext_len = len(plaintext)
    encrypted = np.zeros(plaintext_len, dtype=int)
    
    for i in range(plaintext_len):
        encrypted[i] = ord(plaintext[i]) ^ key[i % key_len]  # XOR encryption
    
    return encrypted.tolist()

def decrypt(encrypted, key):
    encrypted = np.array(encrypted)  # Convert encrypted message to numpy array
    key = np.array(key)  # Convert key to numpy array
    key_len = len(key)
    encrypted_len = len(encrypted)
    decrypted = np.zeros(encrypted_len, dtype=int)
    
    for i in range(encrypted_len):
        decrypted[i] = encrypted[i] ^ key[i % key_len]  # XOR decryption
    
    decrypted = np.char.mod('%c', decrypted)  # Convert integers to characters
    return ''.join(decrypted)

# Example usage
plaintext = "the candle of matrix"
key = [6, 10, 7, 1,3,63]  # Random key
encrypted_message = encrypt(plaintext, key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
