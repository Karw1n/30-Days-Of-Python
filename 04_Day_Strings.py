# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days	Topics	Exercises
# Day 1	5	    5
# Day 2	6	    20
# Day 3	5	    23
# Day 4	1	    35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"

# Old Style String Formatting
# Strings only
first_name = 'Alexander'
last_name = 'Balfour'
formated_string = 'I am %s %s!' %(first_name, last_name)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with radius %d is %.2f.' %(radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)

# New Style String Formatting (str.format)
formated_string = 'I am {} {}!'.format(first_name,last_name)
print(formated_string)

a = 4 
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} / {} = {:.2f}'.format(a, b, a/b))

# Strings and numbers
formated_string = 'The area of a circle with a radius {} is {:.2f}'.format(radius, area)
print(formated_string)

# String Interpolation
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Slicing Strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but NOT including 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) #hon
#Other ways
last_three = language[-3:-1] # Testing
print(last_three)
last_three = language[3:] # Up to the end
print(last_three)

# Reversing a String
gretting = 'Hello, World!'
print(gretting[::-1]) # !dlroW ,olleH
# Skipping Through a string
print(gretting[0::2])

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# Is Alpha
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False