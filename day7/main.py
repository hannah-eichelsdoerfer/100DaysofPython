import random
from hangman_words import word_list
from hangman_ascii_art import logo, stages

from os import system, name
def clear():
  # for windows
  if name == 'nt':
      _ = system('cls')

  # for mac and linux(here, os.name is 'posix')
  else:
      _ = system('clear')
        
# Day 7 Project - Hangman

# generate a random word -> fill letters with blanks
# ask user to guess a letter
# if letter is in the word show them at correct spot
# else start drawing hangman
# this will be repeated till hanged or word guessed (while loop?)

clear()
print(logo)

display = []
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

for _ in chosen_word:
    display += "_"
print(" ".join(display))

alive = True
end_of_game = False
hanged = 0

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  clear()
  
  if guess in display:
    print("You've already guessed this letter correctly!")
  
  for number in range(word_lenght):
    letter = chosen_word[number]
    if letter == guess:
      print(f"Correct, the letter {guess} is in the secret word!")
      display[number] = guess
  
  if guess not in chosen_word:
    hanged += 1
    print(f"Sorry, the letter {guess} is not in the secret word, the hanging continues...")
    if hanged == 6:
      print(f"You lost 💀💀💀 - the secret word was {chosen_word}")
      end_of_game = True
  
  print(" ".join(display))
  print(stages[hanged])
  
  if "_" not in display:
    end_of_game = True
    print(f"Congratulations, you figured out the secret word {chosen_word} 🤓🤓🤓")
