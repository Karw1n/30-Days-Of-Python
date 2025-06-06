# Day 7 Sets
# Exercise Level 1
# 1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

len_it_companies = len(it_companies)
print(len_it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
new_companies = {'LSEG', 'Tech Company', 'MI5'}
it_companies.update(new_companies)
print(it_companies)

# 4. Remove one of the companies from the set it_companies
print(f'Company removed = {it_companies.pop()}')
print(it_companies)

# 5. What is the difference between remove and discard
# Remove raises errors if the item is not in the set however discard does not
# it_companies.remove('Pear') # KeyError: 'Pear'
it_companies.discard('Pear') # No Error

# Exercise Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
C = A.union(B)
print(C)

# 2. Find A intersection B
print(A.intersection(B))

# 3. Is A subset of B
print(A.issubset(B)) # True

# 4. Are A and B disjoint sets
print(A.isdisjoint(B))

# 5. Join A with B and B with A
A.union(B)
B.union(A)

# 6. What is the symmetric difference bewteen A and B
# Now it would be nothing {} empty set
print(A)
print(B)
print(A.symmetric_difference(B)) # {27, 28}
# I had realise that as I had used union it created a new set, I should have used update()
A.update(B)
B.update(A)
print(A.symmetric_difference(B)) # set()

# 7. Delete the sets completly
del A, B, C

# Exercise Level 3.
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(f'List Length: {len(age)}\nSet Length: {len(age_set)}')

# 2. Explain the difference between the following data types: string, list, tuple and set
# String is a combination of characters, and can be indexed like a list
# List is an ordered set of elements, that are mutatuble and indexeable
# Tuple is an unmodifiable set of items, once created cannot be editied only deleted. Ordered and accessible
# Set is a list of unique elements. Unordered. 

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'

sentence_set = set(sentence.split()) # .split() is used to split a sentence and turn it into a list
print(sentence_set)