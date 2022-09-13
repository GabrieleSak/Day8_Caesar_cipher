alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == "encode":
        encrypted_text = []
        for i in range(0, len(start_text)):
            index = alphabet.index(start_text[i])
            encrypted_text.append(alphabet[(index + shift_amount) % 26])
        print(f"The encoded text is {''.join(encrypted_text)}")
    elif cipher_direction == "decode":
        decrypted_text = []
        for i in range(0, len(start_text)):
            index = alphabet.index(start_text[i])
            decrypted_text.append(alphabet[(index - shift_amount) % 26])
        print(f"The decrypted text is {''.join(decrypted_text)}")
    else:
        print("Wrong choice")


caesar(text, shift, direction)
