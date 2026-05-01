alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

#A single function that would do both encoding and decoding
def ceaser(text, shift, encode_or_decode):
    display = ""
    if direction == "decode":
                shift *= -1
    for letter in text:
        if letter not in alphabet:
            display += letter
        else:
            letter_index = alphabet.index(letter)
            

            shift_index = letter_index + shift

            shift_index %= len(alphabet) #allowing a cycle shifting in our code

            display += alphabet[shift_index]
    print(f" Your {encode_or_decode}d message : {display}")

# def encrypt(text, shift):
#     display = ""
#     for letter in text:
#         if letter == " ":
#             display += " "
#         else:
#             letter_index = alphabet.index(letter)
#             shift_index = letter_index + shift
            
#             shift_index %= len(alphabet) #allowing a cycle shifting in our code

#             display += alphabet[shift_index]
#     print(f" Your encrypted message : {display}")

# def decrypt( text , shift ):
#     display = ""
#     for letter in text:
#         if letter == " ":
#             display += " "
#         else:
#             letter_index = alphabet.index(letter)
#             shift_index = letter_index - shift
            
#             shift_index %= len(alphabet) #allowing a cycle shifting in our code

#             display += alphabet[shift_index]
#     print(f" Your encrypted message : {display}")

should_continue = True

while should_continue == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)
    restart = input("Do you wnat to restart again?").lower()

    if restart == "no":
        should_continue = False
        print("Good bye")
