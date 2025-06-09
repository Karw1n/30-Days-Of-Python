import random as r
import string
# Day 12 - Modules Exercises
# Exercises Level 1
# 1. Write a function which generates a six digit/character random_user_id
def random_user_id():
  id = ""
  character_pool = string.ascii_letters + str(string.digits) 
  for i in range(6):
    id = id + str(character_pool[r.randint(0, len(character_pool))])
  return id

print(random_user_id())  
  
# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# def user_id_gen_by_user():
#   num_char = int(input('Select number of characters: '))
#   num_ids = int(input('Select number of ids to generate: '))
#   character_pool = string.ascii_letters + str(string.digits) 
#   print(character_pool)
#   for i in range(num_ids):
#     id = ""
#     for i in range(num_char):
#       id = id + str(character_pool[randint(0, len(character_pool) - 1)])
#     print(id)
    
# user_id_gen_by_user()

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
  red = r.randint(0, 255)
  blue = r.randint(0, 255)
  green = r.randint(0, 255)
  return (f'rgb({red},{blue},{green})')

print(rgb_color_gen())

# Exercise Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def generate_hexadecimal_color():
  hexa_pool = '123456789abcdef'
  hexa = "#"
  for i in range(6):
    hexa = hexa + hexa_pool[r.randint(0, len(hexa_pool) - 1)]
  return hexa

def list_of_hexa_colors(num):
  hex_list = []
  for i in range(num):
    hex_list.append(generate_hexadecimal_color())
  return hex_list

print(list_of_hexa_colors(5))

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
  rgb_list = []
  for i in range(num):
    rgb_list.append(rgb_color_gen())
  return rgb_list

print(list_of_rgb_colors(5))
  
# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type : str, amount):
  if color_type.lower() == 'hexa':
    return list_of_hexa_colors(amount)
  elif color_type.lower() == 'rgb':
    return list_of_rgb_colors(amount)
  else:
    return 'Invalid Input'
  
# print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
# print(generate_colors('hexa', 1)) # ['#b334ef']
# print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
# print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']
    
# Exercise Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst : list):
  r.shuffle(lst)

temp = [1, 2, 3, 4, 5, 6, 7, 8]  
print(temp)
shuffle_list(temp)
print(temp)

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def randomness():
  arr = []
  while len(arr) < 7:
    to_add = r.randint(0, 9)
    if to_add not in arr:
      arr.append(to_add)
  return arr

print(randomness())