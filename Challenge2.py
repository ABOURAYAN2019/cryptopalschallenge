def fixed_xor(hex_string1, hex_string2):
    # Convert the input hex strings to bytes
    bytes1 = bytes.fromhex(hex_string1)
    bytes2 = bytes.fromhex(hex_string2)

    # Perform the XOR operation
    result_bytes = bytes(x ^ y for x, y in zip(bytes1, bytes2))

    # Convert the result bytes to a hex string
    result_hex = result_bytes.hex()

    return result_hex


# Example usage:
hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"
result = fixed_xor(hex_string1, hex_string2)
print(result)
