# # Data Types 👇
# two_digit_number = input("Type a two digit number: ")

# sum = int(two_digit_number[0]) + int(two_digit_number[1])
# print(sum)


# # BMI Calculator 👇
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

# bmi = int(weight) / (float(height) * float(height))
# print(int(bmi))

# # Your Life in Weeks 👇
# age = input("What is your current age?\n")
# yearsleft = 90 - int(age)
# print(f"You have {yearsleft * 365} days, {yearsleft * 52} weeks, and {yearsleft * 12} months left.")

# Tip Calculator 👇
print("Welcome to the tip calculator 💲")
people = int(input("How many people are splitting the bill?\n"))
bill = float(input("How much was the total bill?\n"))
tip = int(input("How much percent would you like to tip?\n"))
tipamount = bill * tip/100
totalbill = bill + tipamount
amountperperson = totalbill/people

total_formatted = "{:.2f}".format(totalbill)
amountperson_formatted = "{:.2f}".format(amountperperson)

print(f"The total bill with tip is €{total_formatted} - each person should pay €{amountperson_formatted}")