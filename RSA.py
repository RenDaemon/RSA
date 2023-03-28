import math
import random

def generate_key(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    gcd = math.gcd(e, phi)
    while gcd != 1:
        e = random.randrange(1, phi)
        gcd = math.gcd(e, phi)

    # Compute the private key d
    d = pow(e, -1, phi)

    # Check if public and private keys are equal
    if e == d:
        print("Please input larger prime key")
        return None, None

    # Return the public and private keys
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

def main():
    choice = 0
    while True:
        print("Choose an option:")
        print("1. Generate Key")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        print()
        
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number.\n")
        pass

        if choice == 1:
            p = int(input("Enter a prime number (p): "))
            q = int(input("Enter another prime number (q): "))
            public_key, private_key = generate_key(p, q)
            print("Public Key:", public_key)
            print("Private Key:", private_key)
            print()

        elif choice == 2:
            plaintext = input("Enter plaintext: ")
            e, n = input("Enter public key (e, n): ").split(",")
            public_key = (int(e), int(n))
            ciphertext = encrypt(public_key, plaintext)
            print("Ciphertext:", ciphertext)
            print()

        elif choice == 3:
            ciphertext = input("Enter ciphertext: ").split(",")
            d, n = input("Enter private key (d, n): ").split(",")
            private_key = (int(d), int(n))
            plaintext = decrypt(private_key, [int(char) for char in ciphertext])
            print("Plaintext:", plaintext)
            print()

        elif choice == 4:
            print("Adios...")

        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == '__main__':
    main()
