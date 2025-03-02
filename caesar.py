def encrypt(text, s):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

def decrypt(text, s):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

if __name__ == "__main__":
    text = input("Enter text: ").strip()
    s = int(input("Enter shift: "))
    cipher_text = encrypt(text, s)
    print("Text:", text)
    print("Shift:", s)
    print("Cipher:", cipher_text)
    print("Decrypted:", decrypt(cipher_text, s))
 
# Input 1
'''
Text: HELLO
Shift: 3
Cipher: KHOOR

'''

# Input 2
'''
Text: attack
Shift: 5
Cipher: fyyfhp

'''
