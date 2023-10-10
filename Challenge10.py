from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii


def encrypt_aes_ecb(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt_aes_cbc(key, plaintext, iv):
    block_size = AES.block_size
    ciphertext = b""
    previous_block = iv

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        block = pad(block, block_size)  # Pad the current block if needed
        xored_block = xor_bytes(block, previous_block)
        encrypted_block = encrypt_aes_ecb(key, xored_block)
        ciphertext += encrypted_block
        # Update the previous block for the next iteration
        previous_block = encrypted_block

    return ciphertext


# Example usage:
key = b"YELLOW SUBMARINE"
iv = bytes([0] * AES.block_size)
plaintext = b"This is a secret message."
ciphertext = encrypt_aes_cbc(key, plaintext, iv)
print(binascii.hexlify(ciphertext).decode())
