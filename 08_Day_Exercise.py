# Day 8 Dictionary
# 1. Create an empty dictionary called dog
dog = dict() # dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Ottoya'
dog['color'] = 'Brown'
dog['breed'] = 'Dachshund'
dog['legs'] = 4
dog['age'] = 1
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
  'first_name'  : 'John',
  'last_name'   : 'Doe',
  'gender'      : 'Unknown',
  'age'         : '404',
  'skills' : ['Hacking', 'Cooking', 'Handyman', 'Cleaning', 'Childcare'],
  'marital_statues'   : 'Married',
  'country'     : 'United Kingdom',
  'address'     : 'Unknown'
}

# 4. Get the length of the student dictionary
print(len(student)) # 8

# 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills'))) # list

# 6. Modifiy the skills values by adding one or two skills
student['skills'] = student['skills'] + ['Building', 'Driving']
print(student.get('skills'))

# 7. Get the dictionary keys as a list
print(list(student.keys())) # dict_keys(['first_name', 'last_name', 'gender', 'age', 'skills', 'marital_statues', 'country', 'address'])

# 8. Get the dctionary values as a list
print(list(student.values()))

# 9. Change the dictionary to a list of tuples using items() method
student_tup = tuple(student.items())
print(student_tup)

# 10. Delete on of the items in the dictionary
print(student.popitem())

# 11. Delete one of the dictionaries
del student