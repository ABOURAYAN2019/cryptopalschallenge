def detect_ecb(ciphertexts):
    for ciphertext in ciphertexts:
        blocks = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]
        if len(blocks) != len(set(blocks)):
            return ciphertext
    return None


with open("challenge8.txt", "r") as file:
    ciphertexts = [line.strip() for line in file]

ecb_ciphertext = detect_ecb(ciphertexts)

if ecb_ciphertext is not None:
    print(f"ECB-encrypted ciphertext found:\n{ecb_ciphertext}")
else:
    print("No ECB-encrypted ciphertexts detected.")
