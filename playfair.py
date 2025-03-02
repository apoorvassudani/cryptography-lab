def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    key_set = set()
    matrix = []
    
    for char in key:
        if char.isalpha() and char not in key_set:
            key_set.add(char)
            matrix.append(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_set:
            matrix.append(char)
            
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]



def find_position(matrix, char):
    char = char.upper()
    if char == 'J':
        char = 'I'
    
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None



def encrypt_playfair(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace("J", "I").replace(" ", "")
    
    # Handle duplicate letters by inserting 'X'
    i = 0
    processed_text = ""
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += text[i] + "X"
            i += 1
        elif i + 1 < len(text):
            processed_text += text[i] + text[i + 1]
            i += 2
        else:
            processed_text += text[i] + "X"
            i += 1
    
    text = processed_text
    
    encrypted_text = ""
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            encrypted_text += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            encrypted_text += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:
            encrypted_text += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return encrypted_text



def decrypt_playfair(text, key):
    matrix = generate_playfair_matrix(key)
    decrypted_text = ""
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            decrypted_text += matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            decrypted_text += matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
        else:
            # For rectangle case, we still swap columns as in encryption
            decrypted_text += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return decrypted_text



if __name__ == "__main__":
    text = input("Enter text: ").strip()
    key = input("Enter key: ").strip()
    cipher_text = encrypt_playfair(text, key)
    print("Encrypted:", cipher_text)
    print("Decrypted:", decrypt_playfair(cipher_text, key))

 
