# Day 9 Conditionals Exercise
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input('Enter your age: '))

if age >= 18:
  print("You are old enough to drive")
else:
  print(f"You need to wait {18-age} years to drive")
  
# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 22
your_age = int(input("Enter your age: "))
if your_age == my_age:
  print("You are the same age as me")
elif abs(your_age - my_age) == 1:
  if (your_age - my_age) > 0:
    print("You are a year older than me")
  else:
    print("You are a year younger than me")
elif your_age > my_age:
  print(f"Your are {your_age - my_age} years older than me")
else:
  print(f'You are {my_age - your_age} years younger than me')
  
# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

a = int(input('Enter a: '))
b = int(input('Enter b: '))

if a > b:
  print(f'{a} is greater than {b}')
elif a < b:
  print(f'{a} is less than {b}')
else:
  print(f'{a} is equal to {b}')
  
# Exercise 2
# 1. Write a code which gives grade to students according to theirs scores:
score = int(input('Input Score [0-100]: '))
if score <= 100 and score >= 0:
  if score >= 80:
    print('Grade A')
  elif score >= 70:
    print('Grade B')
  elif score >= 60:
    print('Grade C')
  else:
    print('F')
    
# # 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

season = input('Season (correct spelling please):')
season.lower()
if season == 'september' or season == 'october' or season == 'november':
  print(f'{season.capitalize()}:Autumn')
elif season in ('december', 'januray', 'february'):
  print(f'{season.capitalize()}:Winter')
elif season in ('march', 'april', 'may'):
  print(f'{season.capitalize()}:Spring')
else:
  print(f'{season.capitalize()}:Summer')  

# # 3. The following list contains some fruits:
# # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input('Enter fruit: ')
if new_fruit in fruits:
  print('That fruit already exists in the list')
else:
  fruits.append(new_fruit)
  print('Fruit added')
print(fruits)

# Exercise 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
  print((person.get('skills'))[int(len(person.get('skills'))/2)])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
  print('Python' in person['skills'])
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
  if len(person.get('skills')) == 2 and 'JavaScript' in person.get('skills') and 'React' in person.get('skills'):
    print('He is a front end developer')
  elif 'Node' in person.get('skills') and 'MongoDB' in person.get('skills'):
    if 'React' in person.get('skills') and ('Python') in person.get('skills'):
      print('He is a backend and full stack developer')
    elif 'React' in person.get('skills'):
      print('He is a full stack developer')
    elif 'Python' in person.get('skills'):
      print('He is a backend developer')
  else:
    print('Unknown Title')

#  * If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person.get('is_married') and person.get('country') == 'Finland':
  print(f'{person["first_name"]} {person["last_name"]} lives in {person['country']}. He is married.')
