# Day 2: 30 Days of python programming
# Variables in Python

# Exercise 1
name = 'Alex'
last_name = 'Balfour'
full_name = 'Alex Balfour'
country = 'UK & Thailand'
city = 'London & Bangkok'
age = 22
year = 2025
is_married = False
is_true = True
is_light_on = True
weather, temperature, vibe = 'Cloudy', 'Humid', 'Tired'

# Exercise 2
# 1.
print('Name Type: ', type(name))
print('Last Name Type: ', type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(weather))
print(type(temperature))
print(type(vibe))

# 2 + 3. Using the len() built-in function, find the length of your first name. Compare the length of your first name and your last name
print(len(name), " | ", len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4

# 5. Add num_one and num_two and assign the value to a variable total
total =  num_one + num_two

# 6. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# 7. Multiply num_two and num_one and assign the value to a variable product
product = num_one  * num_two

# 8. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# 9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

# 10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two

# 11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# 12. The radius of a circle is 30 meters.
radius = 30
pi = 3.14
# i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * (radius**2)

# ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = pi * (radius*2)

# iii. Take radius as user input and calculate the area.
user_radius =  int(input("Input a radius:"))
user_area = pi * (user_radius**2)

# 13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
name = input("Enter Your First Name:")
last_name = input("Enter Your Last Name:")
country = input("Enter The Country You Are From:")
age = int(input("Enter Your Age:"))
print("Hello", name, " ", last_name, " from ", country, " age: ", age)
# Python auto does the spacing for you!

# 14.
help # shift enter
# Input 'keywords'