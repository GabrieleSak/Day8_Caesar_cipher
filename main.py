alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = []
    if cipher_direction == "decode":
        shift_amount *= -1
    for i in range(0, len(start_text)):
        index = alphabet.index(start_text[i])
        end_text.append(alphabet[(index + shift_amount) % 26])
    print(f"The {cipher_direction}d text is {''.join(end_text)}")

caesar(text, shift, direction)
