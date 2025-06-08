# Day 11 - Function Exercises
# Exercises Level 1
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum
def add_two_numbers(x, y):
  print(x + y)

add = lambda x,y : x + y
print(add(5, 2)) # Messing with lambda
print(add_two_numbers(5, 2)) # Same result

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circle(radius):
  return 3.14 * radius * radius

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*numbers):
  sum = 0
  for number in numbers:
    if type(number) == int or type(number) == float:
      sum += number
    else:
      print(f'{number} is not a number')
  return sum

print(add_all_nums(1, 2, 3, 4, 'hi', 5))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(cel):
  return (cel * (9/5)) + 32

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def season_check(month):
  month.lower()
  if month == 'september' or month == 'october' or month == 'november':
    return ('Autum')
  elif month in ('december', 'januray', 'february'):
    return 'Winter'
  elif month in ('march', 'april', 'may'):
    return 'Spring'
  else:
    return 'Summer'  
  
# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
  positive = (- b + ((b*b) - (4 * a * c))**1/2)/(2*a)
  negative = (- b - ((b*b) - (4 * a * c))**1/2)/(2*a)
  return (positive, negative)

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
  for item in lst:
    print(item)
    
# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
  reversed_list = []
  for i in range(len(lst)):
    reversed_list.append(lst[-(i+1)])
  return reversed_list 
numbers = [1, 2, 3, 4, 5, 6]
print(reverse_list(numbers))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst : list[str]):
  for i in range(len(lst)):
    lst[i] = lst[i].capitalize()
  

abc = ['a', 'bb', 'ccc']
capitalize_list_items(abc)
print(abc)

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_items(lst : list, item):
  lst.append(item)
  return lst

lst = abc
print(add_items(lst, 'DDDD'))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst : list, item):
  lst.remove(item)
  return(lst)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(x):
  sum = 0
  for i in range(1, x + 1):
    sum += i
  return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(x):
  sum = 0
  for i in range(1, x + 1):
    if i % 2 != 0:
      sum += i
  return sum

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(x):
  sum = 0
  for i in range(1, x + 1):
    if i % 2 == 0:
      sum += i
  return sum

# Exercise Level 2
# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(x):
  even = 0
  odd = 0
  for i in range(0, x + 1):
    if i % 2 == 0:
      even += 1
    else:
      odd += 1
  print(f'The number of odds are {odd}.\nThe number of evens are {even}')  

evens_and_odds(100)

# 2. Call your function is_empty, it takes a parameter and it checks if it is empty or not
empty_list = []

def is_empty(x):
  if x:
    return False
  else:
    return True

print(is_empty(empty_list))
print(is_empty(""))
print(is_empty(2))

# 3. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst : list[int]):
  sum = 0
  for x in lst:
    sum += x
  return (sum/len(lst))

def calculate_median(lst : list):
  lst.sort()
  return lst[len(lst)/2]

def calculate_mode(lst : list):
  freq_dict = {}
  for i in range(len(lst)):
    if lst[i] in freq_dict.keys():
      freq_dict[lst[i]] = freq_dict[lst[i]] + 1
    else:
      freq_dict[lst[i]] = 1
  return(sorted(freq_dict, key=freq_dict.get, reverse=True)[:1])

print(calculate_mode([2, 2, 3, 1, 1, 2, 4, 5, 6]))

def calculate_range(lst : list[int]):
  lst.sort()
  return lst[-1] - lst[0]

def calculate_variance(lst : list):
  mean = calculate_mean(lst)
  sum_of_squared = 0 
  for num in lst:
    sum_of_squared += 1(num-mean)**2
  
  return sum_of_squared / len(lst)

def calculate_std(lst):
  return calculate_variance(lst)**1/2
    