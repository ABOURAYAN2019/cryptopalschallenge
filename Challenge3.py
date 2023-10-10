def single_byte_xor_cipher(hex_string):
    # Convert the input hex string to bytes
    bytes_data = bytes.fromhex(hex_string)

    # Define a list of possible keys (all ASCII characters)
    possible_keys = range(256)

    # Initialize variables to store the best score and corresponding plaintext
    best_score = 0
    best_plaintext = ''

    # Loop through all possible keys
    for key in possible_keys:
        # XOR the bytes with the current key
        plaintext_bytes = bytes(x ^ key for x in bytes_data)

        # Calculate a score based on character frequency (you can use a dictionary)
        # For simplicity, we'll just count the number of printable ASCII characters
        score = sum(1 for byte in plaintext_bytes if 32 <= byte <= 126)

        # If the current score is better than the best score, update the best score and plaintext
        if score > best_score:
            best_score = score
            best_plaintext = plaintext_bytes.decode('utf-8', errors='ignore')

    return best_plaintext


# Example usage:
hex_encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
decrypted_message = single_byte_xor_cipher(hex_encoded_string)
print(decrypted_message)
