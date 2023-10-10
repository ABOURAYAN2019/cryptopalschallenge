def single_char_xor(input_string, char):
    result = ""
    for char_in_hex in input_string:
        char_in_int = int(char_in_hex, 16)
        xor_result = char_in_int ^ char
        result += chr(xor_result)
    return result

def find_single_char_xor_string(hex_string):
    max_score = 0
    best_candidate = None
    for char in range(256):
        candidate = single_char_xor(hex_string, char)
        score = sum([1 for c in candidate if c.isalpha() or c.isspace()])
        if score > max_score:
            max_score = score
            best_candidate = candidate
    return best_candidate, max_score

# Read the file
with open("file.txt", "r") as file:
    hex_strings = file.read().splitlines()

best_string = None
max_score = 0

for hex_string in hex_strings:
    candidate, score = find_single_char_xor_string(hex_string)
    if score > max_score:
        max_score = score
        best_string = candidate

print("Decrypted String:", best_string)
