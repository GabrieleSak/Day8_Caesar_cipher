alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, encrypt_shift):
    encrypted_text = []
    for i in range(0, len(text)):
        index = alphabet.index(plain_text[i])
        encrypted_text.append(alphabet[(index + encrypt_shift) % 26])
    print(f"The encoded text is {''.join(encrypted_text)}")


def decrypt(cipher_text, decrypt_shift):
    decrypted_text = []
    for i in range(0, len(cipher_text)):
        index = alphabet.index(cipher_text[i])
        decrypted_text.append(alphabet[(index - decrypt_shift) % 26])
    print(f"The decrypted text is {''.join(decrypted_text)}")


if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)



