def caesar_cipher(text, shift, decrypt=False):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            
            if decrypt:
                shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            
            if not is_upper:
                shifted_char = shifted_char.lower()
            
            result += shifted_char
        else:
            result += char

    return result

def main():
    action = input("Do you want to encrypt or decrypt (e/d)? ").strip().lower()
    
    if action == 'e':
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value (integer): "))
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted text:", encrypted_text)
    elif action == 'd':
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value (integer): "))
        decrypted_text = caesar_cipher(text, shift, decrypt=True)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
