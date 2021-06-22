# Data Types
two_digit_number = input("Type a two digit number: ")

sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum)


# BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / (float(height) * float(height))
print(int(bmi))