alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_text = []
    for i in range(0, len(text)):
        index = alphabet.index(text[i])
        if index + shift > 25:
            encrypted_text.append(alphabet[index + shift - 26])
        else:
            encrypted_text.append(alphabet[index + shift])
    print(encrypted_text)


encrypt(text, shift)


