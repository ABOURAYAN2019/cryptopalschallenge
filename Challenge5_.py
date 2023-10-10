def repeating_key_xor(text, key):
    encrypted = b""
    for i in range(len(text)):
        encrypted_byte = text[i] ^ key[i % len(key)]
        encrypted += bytes([encrypted_byte])
    return encrypted


plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
plaintext_bytes = plaintext.encode()
key_bytes = key.encode()

encrypted_bytes = repeating_key_xor(plaintext_bytes, key_bytes)
hex_result = encrypted_bytes.hex()

print(hex_result)
