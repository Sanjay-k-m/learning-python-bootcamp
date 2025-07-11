from textwrap import shorten

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text,shift_amount):
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    encrypted_text = ""
    incriment_amount = 0
    for letter in original_text:
        original_index = alphabet.index(letter)
        encrypted_index = original_index + shift_amount
        if  encrypted_index >= 25:
            incriment_amount = encrypted_index - 25 -1
            encrypted_text += alphabet[incriment_amount]
        else:
            encrypted_text += alphabet[original_index + shift_amount]
    print(encrypted_text)

    #
    # print(encrypted_test,'LLLL')
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

if direction == "encode" :
    encrypt(text,shift)