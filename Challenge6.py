import base64
import itertools
import sys

# Function to compute the edit distance (Hamming distance) between two strings
def hamming_distance(str1, str2):
    return sum(bin(byte1 ^ byte2).count('1') for byte1, byte2 in zip(str1, str2))

# Function to find the likely key size
def find_key_size(ciphertext, max_keysize=40):
    normalized_distances = []
    for keysize in range(2, max_keysize + 1):
        blocks = [ciphertext[i:i + keysize] for i in range(0, len(ciphertext), keysize)]
        pairs = itertools.combinations(blocks, 2)
        distances = [hamming_distance(pair[0], pair[1]) / keysize for pair in pairs]
        normalized_distance = sum(distances) / len(distances)
        normalized_distances.append((keysize, normalized_distance))
    
    # Sort by normalized distance and return the key size with the smallest distance
    return min(normalized_distances, key=lambda x: x[1])[0]

# Function to break repeating-key XOR encryption
def break_repeating_key_xor(ciphertext, key_size):
    blocks = [ciphertext[i:i + key_size] for i in range(0, len(ciphertext), key_size)]
    transposed_blocks = [bytes(b[i] for b in blocks if len(b) > i) for i in range(key_size)]
    
    key = b""
    for block in transposed_blocks:
        _, best_key, _ = single_byte_xor_decrypt(block)
        key += bytes([best_key])
    
    return key

# Function to decrypt with a single-byte XOR key
def single_byte_xor_decrypt(ciphertext):
    best_score = sys.float_info.max
    best_key = None
    best_plaintext = None
    
    for key in range(256):
        plaintext = bytes([byte ^ key for byte in ciphertext])
        score = calculate_score(plaintext)
        if score < best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext
    
    return best_score, best_key, best_plaintext

# Function to calculate a score for plaintext (lower is better)
def calculate_score(text):
    # This is a simple scoring function that favors text with more printable ASCII characters
    score = sum(1 for byte in text if 32 <= byte <= 126)
    return score

if __name__ == "__main__":
    with open("challenge6.txt", "rb") as file:
        ciphertext_base64 = file.read()
    
    ciphertext = base64.b64decode(ciphertext_base64)
    
    # Find the likely key size
    likely_key_size = find_key_size(ciphertext)
    
    # Break the repeating-key XOR encryption
    key = break_repeating_key_xor(ciphertext, likely_key_size)
    
    # Decrypt the ciphertext
    decrypted_text = repeating_key_xor(ciphertext, key)
    
    print(decrypted_text.decode())
