import numpy as np

def get_key_matrix(key):
    key_matrix = np.zeros((3, 3), dtype=int)
    k = 0
    for i in range(3):
        for j in range(3):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1
    return key_matrix

def encrypt(key_matrix, message_vector):
    cipher_matrix = np.dot(key_matrix, message_vector) % 26
    return cipher_matrix

def hill_cipher(message, key):
    key_matrix = get_key_matrix(key)
    message_vector = np.array([[ord(char) % 65] for char in message], dtype=int)
    cipher_matrix = encrypt(key_matrix, message_vector)
    cipher_text = ''.join(chr(num + 65) for num in cipher_matrix.flatten())
    print("Ciphertext:", cipher_text)

if __name__ == "__main__":
    message = input().strip()
    key = input().strip()
    hill_cipher(message, key)

# Input 1
'''
ACT
GYBNQKURP

Output: POH
'''

# Input 2
'''
HEL
GYBNQKURP

Output: DRX
'''
