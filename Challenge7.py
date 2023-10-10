from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

# Key and ciphertext
key = b'YELLOW SUBMARINE'
with open("challenge7.txt", "rb") as file:
    ciphertext_base64 = file.read()

# Decode Base64 and initialize the cipher
ciphertext = base64.b64decode(ciphertext_base64)
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
decryptor = cipher.decryptor()

# Decrypt the ciphertext and remove padding
plaintext_padded = decryptor.update(ciphertext) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
plaintext = unpadder.update(plaintext_padded) + unpadder.finalize()

print(plaintext.decode())
