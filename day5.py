# PYTHON LOOPS
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)
  
# Average Height (without using len() or sum())
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)

total_height = 0
student_count = 0
for height in student_heights:
  total_height += height
  student_count += 1

average = total_height / student_count
# print(total_height, student_count, average)
print(average)

# Highest Score (without using max() - opposite of min())
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for score in student_scores:
  if score > high_score:
    high_score = score

print(f"The highest score in the class is: {high_score}")

# for loops and the range() function
total_sum = 0
for number in range(1, 101):
  total_sum += number
print(total_sum)

# Adding Even Numbers
even_total = 0
for number in range(1, 101):
  if number % 2 == 0:
    even_total += number
print(even_total)

# different solution:
total = 0
for number in range(0, 101, 2):
  total += number
print(total)

# FizzBuzz Job Interview Question
# if divisible by 3: Fizz
# if divisible by 5: Buzz
# if divisible by 3 and 15: FizzBuzz

for number in range(0, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

# Day 5 Project - Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for symbol in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
  
# for number in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

password = []

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
  password += random.choice(symbols)
  
for number in range(1, nr_numbers + 1):
  password += random.choice(numbers)

# print(password)
random.shuffle(password)
separator = ''
print(f"Your suggested password is: {separator.join(password)}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P