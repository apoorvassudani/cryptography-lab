import math
import random



def gcd(a, b):
    """
    Compute the greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a



def is_prime(n):
    """
    Simple primality test
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True



def mod_inverse(e, phi):
    """
    Compute the modular multiplicative inverse of e modulo phi
    """
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x
    
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % phi



def generate_keys(p, q):
    """
    Generate public and private key based on p and q
    """
    # Validate inputs
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both p and q must be prime numbers")
    if p == q:
        raise ValueError("p and q cannot be the same")



    # Step 1: Calculate n = p*q
    n = p * q
    
    # Step 2: Calculate Euler's totient function φ(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)
    
    # Step 3: Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = 65537  # Common choice for e, as it's a prime with few 1's in binary
    if e >= phi:
        # Find another suitable e if 65537 is too large
        e = 3
        while e < phi:
            if gcd(e, phi) == 1:
                break
            e += 2
    
    # Step 4: Calculate d, the modular multiplicative inverse of e (mod φ(n))
    d = mod_inverse(e, phi)
    
    # Public key: (e, n)
    # Private key: (d, n)
    return ((e, n), (d, n))



def encrypt(message, public_key):
    """
    Encrypt a message using the public key
    """
    e, n = public_key
    
    # Check if the message is a number
    if isinstance(message, int):
        if message >= n:
            raise ValueError("Message must be less than n")
        return pow(message, e, n)
    
    # If the message is a string, convert to integers and encrypt
    encrypted_blocks = []
    for char in message:
        m = ord(char)
        encrypted_blocks.append(pow(m, e, n))
    
    return encrypted_blocks



def decrypt(encrypted_message, private_key):
    """
    Decrypt a message using the private key
    """
    d, n = private_key
    
    # If the encrypted message is a single number
    if isinstance(encrypted_message, int):
        return pow(encrypted_message, d, n)
    
    # If the encrypted message is a list of numbers
    decrypted_message = ""
    for c in encrypted_message:
        m = pow(c, d, n)
        decrypted_message += chr(m)
    
    return decrypted_message



if __name__ == "__main__":
    # Get prime numbers p and q from user
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter a different prime number (q): "))
    
    # Generate public and private keys
    try:
        public_key, private_key = generate_keys(p, q)
        print(f"Public Key (e, n): {public_key}")
        print(f"Private Key (d, n): {private_key}")



        # Get message from user
        message = input("Enter a message to encrypt: ")
        
        # Encrypt the message
        encrypted_message = encrypt(message, public_key)
        print(f"Encrypted message: {encrypted_message}")
        
        # Decrypt the message
        decrypted_message = decrypt(encrypted_message, private_key)
        print(f"Decrypted message: {decrypted_message}")
        
    except ValueError as e:
        print(f"Error: {e}")
        
