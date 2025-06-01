# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
joined_words = ' '.join(words)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding', 'For', 'All')

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = 'Coding For All'
company = company.capitalize()
company = company.title()
company = company.swapcase()
print(company)

# 9. Cut(slice) out the first word of Coding For All string.
company = 'Coding For All'
print(company[:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding') != -1)
print(company.find('Coding'))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace('Coding', 'Python').replace('Python', 'Everyone'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
first_word = company[0:6]
second_word = company[7:10]
third_word = company[11:]

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# 15. What is the character at index 0 in the string Coding For All.
print(f'The character at index 0 of :\'{company}\' is: {company[0]}')

# 16. What is the last index of the string Coding For All
print(company.rfind(company[-1:]))

# 17. What character is at index 10 in "Coding For All" string.
print(company[10]) # Space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
pfe = 'Python For Everyone'
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = "Coding For All"

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(pfe.find('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(cfa.find('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(cfa.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

first_time = ('You cannot end a sentence with because because because is a conjunction')
first_because = first_time.index('because')


# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_because =  first_time.rindex('because')

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'[:first_because] + 'You cannot end a sentence with because because because is a conjunction'[last_because+len('because')+1:])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(first_because)

# 28. Does ''Coding For All' start with a substring Coding?
print(cfa.startswith('Coding')) # True

# 29. Does 'Coding For All' end with a substring coding?
print(cfa.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython # False
# thirty_days_of_python # True

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print("#".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
print(f'{'Name':<10}{'Age':<5}{'Country':<10}{'City':<10}')
print(f'{'Alexander':<10}{'21':<5}{'Thailand':<10}{'Bangkok':<10}')

# 35. Use the string formatting method to display the following:
print('''radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.''')

# 36. Make the following using string formatting methods:
print(f"{8} + {6} = {8+6}")
print(f"{8} - {6} = {8-6}")
print(f"{8} * {6} = {8*6}")
print(f"{8} / {6} = {8/6:.2f}")
print(f"{8} % {6} = {8%6}")
print(f"{8} // {6} = {8//6}")
print(f"{8} ** {6} = {8**6}")