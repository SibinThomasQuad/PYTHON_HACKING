import hashlib

def identify_hash_type(input_hash):
    hash_length = len(input_hash)

    if hash_length == 32:
        return "MD5"
    elif hash_length == 40:
        return "SHA-1"
    elif hash_length == 64:
        return "SHA-256"
    elif hash_length == 56:
        return "SHA-224"
    elif hash_length == 128:
        return "SHA-512"
    elif hash_length == 96:
        return "SHA-384"
    elif hash_length == 60:
        return "SHA-3-224"
    elif hash_length == 64:
        return "SHA-3-256"
    elif hash_length == 96:
        return "SHA-3-384"
    elif hash_length == 128:
        return "SHA-3-512"
    elif hash_length == 60:
        return "BLAKE2-224"
    elif hash_length == 64:
        return "BLAKE2-256"
    elif hash_length == 128:
        return "BLAKE2-512"
    elif hash_length == 40:
        return "RIPEMD-160"
    elif hash_length == 128:
        return "Whirlpool"
    elif hash_length == 32:
        return "CRC32"
    elif hash_length == 64:
        return "HMAC"
    elif hash_length == 60:
        return "bcrypt"
    elif hash_length == 86:
        return "scrypt"
    else:
        return "Unknown"

# Example usage:
input_hash = "5eb63bbbe01eeed093cb22bb8f5acdc3"  # Replace with your hash
hash_type = identify_hash_type(input_hash)

if hash_type != "Unknown":
    print(f"The hash type is {hash_type}.")
else:
    print("Unknown hash type.")
