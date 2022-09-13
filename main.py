import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

start_program = True

while start_program:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(start_text, shift_amount, cipher_direction):
        end_text = []
        if cipher_direction == "decode":
            shift_amount *= -1
        for i in range(0, len(start_text)):
            if start_text[i] in alphabet:
                index = alphabet.index(start_text[i])
                end_text.append(alphabet[(index + shift_amount) % 26])
            else:
                end_text.append(start_text[i])
        print(f"The {cipher_direction}d text is {''.join(end_text)}")


    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart != "yes":
        start_program = False

