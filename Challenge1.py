import base64

# Input hexadecimal string
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Convert hexadecimal to bytes
bytes_data = bytes.fromhex(hex_string)

# Encode bytes to base64
base64_data = base64.b64encode(bytes_data).decode('utf-8')

print(base64_data)
