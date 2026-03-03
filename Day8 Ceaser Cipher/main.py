from ceaser_art import ceaser_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ceaser_art()

should_continue = True

def ceaser(direction, text, shift):
    global should_continue
    if direction == "encode":
        encrypted_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position + shift) % 26
                encrypted_text += alphabet[new_position]
        print(f"Here is the encoded result: {encrypted_text}")
    elif direction == "decode":
        decrypted_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position - shift) % 26
                decrypted_text += alphabet[new_position]
        print(f"Here is the {direction}d result: {decrypted_text}")

while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(direction, text, shift)

    again = input("Would you like to play again? y/n\n").lower()
    if again == "n":
        should_continue = False

