def encrypt(text, rails):
    # Create the rail fence pattern
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for moving down, -1 for moving up
    
    # Place characters in the rail fence pattern
    for char in text:
        fence[rail].append(char)
        rail += direction
        
        # Change direction when we reach the top or bottom rail
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    # Read off the characters from the fence
    result = ''.join([''.join(rail) for rail in fence])
    return result



def decrypt(cipher_text, rails):
    # Calculate the length of each rail
    fence_len = len(cipher_text)
    fence = [[''] * fence_len for _ in range(rails)]
    
    # Mark the rail fence pattern with placeholder '*'
    rail = 0
    direction = 1
    for i in range(fence_len):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    # Fill in the fence with the cipher text
    index = 0
    for i in range(rails):
        for j in range(fence_len):
            if fence[i][j] == '*' and index < len(cipher_text):
                fence[i][j] = cipher_text[index]
                index += 1
    
    # Read off the fence in zigzag pattern
    result = ''
    rail = 0
    direction = 1
    for i in range(fence_len):
        result += fence[rail][i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    return result



# Example usage
if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    rails = int(input("Enter number of rails: "))
    
    encrypted = encrypt(text, rails)
    print(f"Encrypted: {encrypted}")
    
    decrypted = decrypt(encrypted, rails)
    print(f"Decrypted: {decrypted}")
