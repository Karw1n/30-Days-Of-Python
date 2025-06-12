import functools
# Higher Order Functions
# Function as a Parameter
def sum_numbers(nums):
  return sum(nums)

def higher_order_function(f, lst):
  summation = f(lst)
  return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)

# Function as a Return Value
def square(x):
  return x **2
def cube(x):
  return x **3
def absolute(x):
  if x >= 0:
    return x
  else:
    return -(x)
  
def higher_order_function(type):
  if type == 'square':
    return square
  elif type == 'cube':
    return cube
  elif type == 'absolute':
    return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3)) 

# Python Decorators
# Normal function
def greeting():
  return 'Welcome to Python'
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper
g = uppercase_decorator(greeting)
print(g())

## Let us implement the example above with a decorator
'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper
@uppercase_decorator
def modified_greeting():
  return 'Welcome to Python'
print(modified_greeting())

# Adding Multiple Decorators
def add_sprinkles(func):
  def wrapper(flavour):
    print('*You add spinkles!*')
    func(flavour)
  return wrapper
def add_fudge(func):
  def wrapper(*args, **kwargs): # Any of arguements or keyword arguemnts
    print('*You add fudge!')
    func(*args, **kwargs)
  return wrapper
    
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
  print(f'Here is you {flavour} ice cream')
  
get_ice_cream('vanilla')

# Reduce Function
words = ['Alex', 'is', 'trying!']
def join_words(x, y):
  return x + " " +y

print(functools.reduce(join_words, words))