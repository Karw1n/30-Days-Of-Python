# Day 15 Python Type Errors
# This is a mix of the notes and challenge.
# For each error I will test the error, record the error message and correct the issue. Due to an extension I have on vscode I have very useful syntax highlighting that helps me identify problems/errors before they arise

# 1. Syntax Error
# Original: print 'hello world'
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print('hello world')

# 2. Name Error
# Original print(age)
# NameError: name 'age' is not defined
age = 22 
print(age)

# 3. Index Error
numbers = [1, 2, 3, 4, 5]
# Original: print(numbers[5])
# IndexError: list index out of range
print(numbers[4])

# 4. Module Not Found Error
# Original: import maths
# ModuleNotFoundError: No module named 'maths'
import math # My extension suggest that module level should be at the top of the file as good practise

# 5. Attribute Error
# Original: print(math.PI)
#AttributeError: module 'math' has no attribute 'PI'
print(math.pi)

# 6. Key Error
users = {'name' : 'Alex', 'age' : age, 'country' : 'Thailand'}
# Original: print(users['county'])
#KeyError: 'county'
print(users['country'])

# 7. Type Error
# Original: print(4 + '3')
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(4 + int('3'))
print(str(4) + '3')

# Import Error
# Original: from math import power
# ImportError: cannot import name 'power' from 'math' (unknown location)
from math import pow
print(pow(2,3))

# Value Error
# Original: print(int('12a'))
#ValueError: invalid literal for int() with base 10: '12a'
print(int('12'))

# Zero Division Error
# Original: print(1/0)
# ZeroDivisionError: division by zero
# Solution, don't divide by zero.