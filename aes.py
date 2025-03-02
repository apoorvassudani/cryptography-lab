from Crypto.Cipher import AES
import base64
import sys

def pad_key(key: str, length: int) -> bytes:
    return key.ljust(length, '0').encode('utf-8')[:length]

def pad_plaintext(plaintext: str) -> bytes:
    while len(plaintext) % 16 != 0:
        plaintext += ' '
    return plaintext.encode('utf-8')

def encrypt(plaintext: str, secret_key: bytes) -> str:
    cipher = AES.new(secret_key, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad_plaintext(plaintext))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt(ciphertext: str, secret_key: bytes) -> str:
    cipher = AES.new(secret_key, AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(ciphertext))
    return decrypted_bytes.decode('utf-8').strip()

if __name__ == "__main__":
    key_size = int(input("Enter key size (128, 192, 256): "))
    if key_size not in [128, 192, 256]:
        print("Invalid key size. Choose 128, 192, or 256.")
        sys.exit(1)
    
    key = input("Enter encryption key: ")
    secret_key = pad_key(key, key_size // 8)
    
    plaintext = input("Enter plaintext: ")
    encrypted_text = encrypt(plaintext, secret_key)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, secret_key)
    print("Decrypted Text:", decrypted_text)

# Input 1
'''
Enter key size (128, 192, 256): 128
Enter encryption key: mysecretkey
Enter plaintext: Hello, AES!
'''

# Input 2
'''
Enter key size (192, 256, or 128): 192
Enter encryption key: anotherkey
Enter plaintext: Python AES Encryption

'''
