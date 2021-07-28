# Day 8 Project - Ceasars Cipher
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(cipher_direction, original_text, shift_amount):
  transformed_text = ""
  for char in original_text:
    if char in alphabet:
      current_index = alphabet.index(char)
      if cipher_direction == "encode" and current_index + shift < 26:
        new_index = current_index + shift 
      else:
        new_index = current_index - shift
      
      
      transformed_text += alphabet[new_index]
    else:
      transformed_text += char
    # if cipher_direction == "decode":
    #    shift_amount *= 1
    # new_index = current_index + shift_amount
  print(f"The {direction}d text is {transformed_text}")
  
program_running = True

while program_running:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # shift = shift % 26
  
  ceasar(cipher_direction=direction, original_text=text, shift_amount=shift)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    program_running = False
    print("Goodbye 👋")
