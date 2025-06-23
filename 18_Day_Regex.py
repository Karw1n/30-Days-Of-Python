import re

# Match
# Syntax
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match) # <re.Match object; span=(0, 15), match='I love to teach'>
modified_txt = 'I love to teach python and I love to teach javaScript'
print(re.match('I love to teach', modified_txt, re.I)) # Returns first match

# Span returns the starting and ending position of the match
span = match.span()
print(span) # (0, 15)

start, end = span # 0, 15
print(txt[start:end]) # I love to teach

no_match = re.match('I like to teach', txt, re.I)
print(no_match) # None

# Search Syntax
# re.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match) # <re.Match object; span=(100, 105), match='first'>
# We can do the same span operations

# Searching for All Matches Using findall
matches = re.findall('language', txt, re.I)
print(matches) # ['language', 'language']
print(re.findall('I love to teach', modified_txt, re.I))
# ['I love to teach', 'I love to teach']

# How about 'Python'?
matches = re.findall('python', txt, re.I)
print(matches) # ['Python', 'python']
# re.I includes both lowercase and uppercase letters.
# If the re.I flag is not included we must write it in directly.
matches = re.findall('Python|python', txt)
print(matches)# ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches) # ['Python', 'python']

# Replacing a Substring
match_replaced = re.sub('Python|python', 'Javascript', txt, re.I)
print(match_replaced)
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)

# Text cleaning example
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?

# Splitting Text Using RegEx Split
print(re.split('\n', matches))

# Writing RegEx Patterns
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)

new_pattern = re.sub(regex_pattern, 'Pear', txt)
print(new_pattern)

# Square Bracket
regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern,txt)
print(matches) # ['Apple', 'banana', 'apple', 'banana']

# Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!

# Period (.)
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Zero or more times(*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Zero or one time(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

# Cart ^
# Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Negation (when in brackets)
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']