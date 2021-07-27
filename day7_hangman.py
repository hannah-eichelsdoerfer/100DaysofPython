import random

# Day 7 Project - Hangman

# generate a random word -> fill letters with blanks
# ask user to guess a letter
# if letter is in the word show them at correct spot
# else start drawing hangman
# this will be repeated till hanged or word guessed (while loop?)

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
display = []

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}.')

for _ in chosen_word:
    display += "_"
print(" ".join(display))

alive = True
end_of_game = False
hanged = 0

while not end_of_game:
  guess = input("Guess a letter: \n").lower()
  for number in range(word_lenght):
    letter = chosen_word[number]
    if letter == guess:
      display[number] = guess
  
  if guess not in chosen_word:
    hanged += 1
    print(stages[hanged])
    if hanged == 6:
      end_of_game = True
      print("You lost 💀💀💀")
  
  print(" ".join(display))
  
  if "_" not in display:
    end_of_game = True
    print(f"Congratulations, you figured out the secret word {chosen_word} 🤓🤓🤓")
