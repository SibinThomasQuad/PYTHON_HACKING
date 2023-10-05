import base64

def xor_encrypt_decrypt(data, key):
    # Initialize an empty list to store the result
    result = []

    # Repeat the key to match the length of the data
    key = key * (len(data) // len(key)) + key[:len(data) % len(key)]

    # Perform the XOR operation on each character in the data with the corresponding character in the key
    for i in range(len(data)):
        result.append(chr(ord(data[i]) ^ ord(key[i])))

    # Join the result list into a string
    encrypted_text = ''.join(result)

    # Encode the encrypted text in base64 format
    encrypted_base64 = base64.b64encode(encrypted_text.encode()).decode()
    
    return encrypted_base64

def xor_decrypt(encrypted_base64, key):
    # Decode the base64-encoded text
    encrypted_text = base64.b64decode(encrypted_base64.encode()).decode()

    # Initialize an empty list to store the result
    result = []

    # Repeat the key to match the length of the encrypted text
    key = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]

    # Perform the XOR operation on each character in the encrypted text with the corresponding character in the key
    for i in range(len(encrypted_text)):
        result.append(chr(ord(encrypted_text[i]) ^ ord(key[i])))

    # Join the result list into a string
    decrypted_text = ''.join(result)
    
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the encryption key: ")

    # Encrypt the plaintext
    encrypted_base64 = xor_encrypt_decrypt(plaintext, key)
    print("Encrypted text (base64):", encrypted_base64)

    # Decrypt the ciphertext
    decrypted_text = xor_decrypt(encrypted_base64, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
