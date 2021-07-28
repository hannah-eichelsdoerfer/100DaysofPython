# Dictionaries and Nesting
# Dictionaries are similar to Ruby Hashes or JavaScript objects?
# Dictionary is another Data Structure

programming_dictionary = {
  "Loop": "The action of doing something over and over again."
}

programming_dictionary["Bug"] = "Coding error in a computer program"

empty_dictionary = {} # to empty dictionariy: programming_dictionary = empty_dictionary

programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary)

# Loop through a dictionairy
for key in programming_dictionary:
  print(f"{key} - {programming_dictionary[key]}")

# Grading Program Exercise
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_grades = {}

# student = key

# for student in student_scores:
#   score = student_scores[student]
#   grade = 0
#   if score > 90:
#     grade = "Outstanding"
#   elif score > 80:
#     grade = "Exceeds Expectations"
#   elif score > 70:
#     grade = "Acceptable"
#   else:
#     grade = "Fail"
#   student_grades[f"{student}"] = grade

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

# Nested Dictionaries - Travel Log
# nesting list and nesting dictionary in a dictionary
travel_log = {
  "Germany": ["Berlin", "Munch", "Hamburg"],
  "Portugal": {"cities_visited": ["Lagos", "Porto", "Lisbon"], "total_visits": 12},
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
}

# Nesting dictionary in a list
travel_log2 = [
  {
    "country": "Portugal",
    "cities_visited": ["Lagos", "Porto", "Lisbon"], 
    "total_visits": 12
  },
  {
    "country": "Spain",
    "cities_visited": ["Palma", "Barcelona", "Madrid"], 
    "total_visits": 2
  },
]

# Exercise
def add_new_country(name, visits, cities):
  new_country = {}
  new_country["country"] = name
  new_country["cities_visited"] = visits
  new_country["cities_visited"] = cities
  travel_log2.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log2)

