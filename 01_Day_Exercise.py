# Exercise: Level 1
"""1. Check the python version you are using
# Typing 'python' into the python shell
# Answer:  'Python 3.12.10'
"""
# Triple """ can be used for multiple line comments.

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
"""addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)"""

print(3+4) # = 7
print(3-4) # = -1
print(3*4) # = 12
print(3%4) # = 3
print(3/4) # = 0.75
print(3**4) # = 81
print(3//4) # = 0
# To do in the shell simply remove the print() statement

# 3.Write strings on the python interactive shell. The strings are the following:
"""Your name
Your family name
Your country
I am enjoying 30 days of python"""

print('Alex')
print('Balfour')
print('United Kingdom And Thailand')
print('I am enjoying 30 days of Python!')
# To do in the shell simply remove the print() statement

# 4. Check the data types of the following data.
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j)) # Complex
print(type(['Asabeneh', 'Python', 'Finland'])) # List
print(type('Alexander')) 
print(type('Balfour'))
print(type('United Kingdom And Thailand'))

# Exercise: Level 2
# This exercise was during the questions above in a python file which I had done. So I kind of skipped a step.

# Exercise: Level 3
# 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

# Integer
print(type(21))

# Float
print(type(7.77))

# Complex
print(type(5 + 5)) # = 'int' I was testing my definition of a complex
# print(type(5 + 5x)) I tried with the value x but it didn't work
x = 5
print(type(5 + 5 * (x))) # = 'int'
print(type(4-4j)) # So complex is a data structure or object that refers to a complex number (an imaginary number).
print(4-4j) # = (4-4j)

# String 
print(type("Hello World"))

# Boolean
print(type(True))
print(type(False))

# List
print(type([1, 2, 3, 4, 3]))

# Tuple
print(type((1, 2, 3, 4, 3)))

# Set
print(type({1 , 2, 3, 3}))
print({1, 2, 3, 3}) # = {1, 2, 3} Removes duplicates

# Dictionary
print(type({'a':1, 'b':2, 100:'One Hundred'}))

# 2. Find an Euclidian distance between (2, 3) and (10, 8)
# (2 - 10)**2 + (3 - 8)**2
print((2 - 10)**2 + (3 - 8)**2) # = 89