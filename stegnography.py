from PIL import Image

def encode_image(image, message):
    """
    Encode a secret message into an image using the LSB method.
    """
    # Convert the image and message to binary format
    image_binary = image.convert("RGB").tobytes()
    message_binary = ''.join(format(ord(c), '08b') for c in message)
    message_length = len(message_binary)

    # Check if the message can fit into the image
    max_message_length = len(image_binary) // 8
    if message_length > max_message_length:
        raise ValueError(f"The secret message is too long to fit into the image. Maximum message length: {max_message_length}")

    # Add the message length to the beginning of the binary data
    message_length_binary = format(message_length, '016b')
    binary_data = message_length_binary + message_binary

    # Modify the least significant bit of each pixel in the image with the binary data
    new_image_data = []
    for i in range(len(binary_data)):
        pixel_binary = format(image_binary[i], '08b')
        new_pixel_binary = pixel_binary[:-1] + binary_data[i]
        new_pixel_value = int(new_pixel_binary, 2)
        new_image_data.append(new_pixel_value)

    # Create a new image with the modified pixel values
    new_image = Image.frombytes(image.mode, image.size, bytes(new_image_data))

    return new_image

def decode_image(image):
    """
    Decode a secret message from an image that was encoded using the LSB method.
    """
    # Convert the image to binary format
    image_binary = image.convert("RGB").tobytes()

    # Extract the message length from the binary data
    message_length_binary = ''.join(format(image_binary[i], '08b')[-1] for i in range(16))
    message_length = int(message_length_binary, 2)

    # Extract the binary data from the image
    binary_data = ''.join(format(image_binary[i], '08b')[-1] for i in range(16, 16 + (message_length * 8)))

    # Convert the binary data to ASCII characters
    message = ''
    for i in range(0, len(binary_data), 8):
        message += chr(int(binary_data[i:i+8], 2))

    return message

# Example usage
image = Image.open("c.png")
secret_message = "This is a secret message!"
encoded_image = encode_image(image, secret_message)
encoded_image.save("output_image.png")
decoded_message = decode_image(encoded_image)
print(decoded_message) # Output: "This is a secret message!"
