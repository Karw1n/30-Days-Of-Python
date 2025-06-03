# Exercise Level 1
# 1. Create an empty tuple
empty_tuple = tuple()

# 2. Create a tuple containing names of your sisters and brothers
brothers = ('James', 'Rob', 'Ben', 'Tom')
sisters = ('Josie', 'Will', 'Adam')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
print(f'You have {len(siblings)} siblings')

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings) + ['Max', 'Thanya']
family_members = tuple(family_members)
print(family_members)

# Exercise Level 2
# 1. Unpack siblings and parents from family_members
sibling1, sibling2, sibling3, sibling4, *rest = family_members
print(sibling1, sibling2, sibling3, sibling4)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Pear', 'Apple', 'Orange')
vegetables = ('Sweetcorn', 'Leek', 'Lettuce')
animal = ('Dog', 'Cat', 'Monkey')

food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
food_stuff_lt = food_stuff_lt[:int(len(food_stuff_lt)/2)] + food_stuff_lt[int((len(food_stuff_lt)/2)) + 1:]
print(food_stuff_lt)

# 5. Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt = food_stuff_lt[3:-3]
print(food_stuff_lt)

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) # False
print('Iceland' in nordic_countries) # True