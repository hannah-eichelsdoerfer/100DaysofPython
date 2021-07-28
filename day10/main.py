# Day 10 Project - Calculator
from os import system, name
def clear():
  # for windows
  if name == 'nt':
      _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
      _ = system('clear')
      
from art import logo
print(logo)

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

calculating = True

while calculating:
  nr1 = float(input("Whats the first number? "))
  operator = input("+ - * / \nPick an operator: ")
  while operator not in ["+", "-", "*", "/"]:
    operator = input("Please choose a valid operator (+ - * /): ")
  nr2 = float(input("Whats the second number? "))
  result = 0
  if operator == "+":
    result = add(nr1, nr2)
  elif operator == "-":
    result = subtract(nr1, nr2)
  elif operator == "*":
    result = multiply(nr1, nr2)
  elif operator == "/":
    result = divide(nr1, nr2)
  
  print(f"{nr1} {operator} {nr2} = {result}")
  again = input("Go again? yes/no ")
  
  if again == "no":
    calculating = False

# Solution using dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# for symbol in operations:
#   num1 = int(input("Whats the first number? "))
#   operation_symbol = input("+ - * / \nPick an operator: ")
#   num2 = int(input("Whats the second number? "))
#   print(symbol)
#   calculation_function= operations[operation_symbol]
#   answer = calculation_function(num1, num2)
  
#   print(f"{num1} {operator} {num2} = {answer}")

# def calculator():
#   print(logo)

#   num1 = float(input("What's the first number?: "))
#   for symbol in operations:
#     print(symbol)
#   should_continue = True
 
#   while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = answer
#     else:
#       should_continue = False
#       clear()
#       calculator()

# calculator()

