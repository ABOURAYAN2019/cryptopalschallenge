def pkcs7_padding(text, block_size):
    # Calculate the number of bytes needed to pad
    padding_length = block_size - (len(text) % block_size)
    # Create the padding bytes
    padding = bytes([padding_length] * padding_length)
    # Append the padding to the input text
    padded_text = text + padding
    return padded_text

# Example usage:
plaintext = "YELLOW SUBMARINE"
block_size = 20
padded_text = pkcs7_padding(plaintext.encode(), block_size)
print(padded_text.decode())
