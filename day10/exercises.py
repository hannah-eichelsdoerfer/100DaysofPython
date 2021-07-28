# Functions with Outputs

def my_function():
  result = 3 * 2
  return result

def my_function():
  return 3 * 2

output = my_function() # output = 6
print(output)

# Transform words into Title Case
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inptuts"
  
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  # print(f"{formatted_f_name} {formatted_l_name}")
  return f"{formatted_f_name} {formatted_l_name}" 

formatted_name = format_name("hannah", "EICH")
print(formatted_name)

print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Days in Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  # if month > 12 or month < 1:
    # return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
    return 29
  # return month_days[month - 1]
  else:
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# Docstrings
# -> way for us to create little bits of documentation as we are coding along in our functions or other blocks of code
# -> by default included in python functions
# we can write such hints in the document ourself using """xxxx"""

def sample_function(x, y):
  """Multiplies the inputs with each other"""
  return x * y

