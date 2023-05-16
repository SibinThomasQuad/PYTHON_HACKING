MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}


def encode_morse_code(message):
    encoded_message = ''
    for char in message:
        if char.upper() in MORSE_CODE_DICT:
            encoded_message += MORSE_CODE_DICT[char.upper()] + ' '
    return encoded_message.strip()


def decode_morse_code(code):
    inverted_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    decoded_message = ''
    for word in code.split(' / '):
        for char in word.split():
            if char in inverted_dict:
                decoded_message += inverted_dict[char]
        decoded_message += ' '
    return decoded_message.strip()


# Example usage
message_to_encode = "Hello, World!"
encoded_message = encode_morse_code(message_to_encode)
print(f"Encoded message: {encoded_message}")

code_to_decode = ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
decoded_message = decode_morse_code(code_to_decode)
print(f"Decoded message: {decoded_message}")
