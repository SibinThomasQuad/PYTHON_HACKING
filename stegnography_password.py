from PIL import Image
import binascii

def to_bits(n, pad):
    return bin(n)[2:].zfill(pad)

def to_bytes(bits):
    return int(bits, 2).to_bytes(len(bits) // 8, byteorder='big')

def hide_message(image_path, message, password):
    image = Image.open(image_path)
    pixels = image.load()

    message_bits = ''.join(to_bits(ord(c), 8) for c in message)
    message_bits += '0' * (len(message_bits) % 3)  # Pad message bits to multiple of 3

    password_bits = ''.join(to_bits(ord(c), 8) for c in password)

    for i in range(len(message_bits) // 3):
        x, y = i // image.size[1], i % image.size[1]
        r, g, b = pixels[x, y]
        password_bit = int(password_bits[i % len(password_bits)])
        new_r = r & ~1 | (int(message_bits[i * 3]) ^ password_bit)
        new_g = g & ~1 | (int(message_bits[i * 3 + 1]) ^ password_bit)
        new_b = b & ~3 | (int(message_bits[i * 3 + 2]) ^ password_bit)
        pixels[x, y] = (new_r, new_g, new_b)

    image.save(image_path[:-4] + '_hidden.png')

def reveal_message(image_path, password):
    image = Image.open(image_path)
    pixels = image.load()

    password_bits = ''.join(to_bits(ord(c), 8) for c in password)

    message_bits = ''
    for i in range(image.size[0] * image.size[1] // 3):
        x, y = i // image.size[1], i % image.size[1]
        r, g, b = pixels[x, y]
        password_bit = int(password_bits[i % len(password_bits)])
        message_bits += str(r & 1 ^ password_bit)
        message_bits += str(g & 1 ^ password_bit)
        message_bits += str(b & 3 ^ password_bit)

    message_bytes = to_bytes(message_bits[:-16])
    message = message_bytes.decode('utf-8')
    return message

# Example usage
image_path = 'image.png'
message = 'This is a secret message!'
password = 'password123'

hide_message(image_path, message, password)

hidden_image_path = image_path[:-4] + '_hidden.png'
revealed_message = reveal_message(hidden_image_path, password)

print(revealed_message)  # Should output: "This is a secret message!"
