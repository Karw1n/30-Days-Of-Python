# Day 13 Exercise List Comprehension
# 1. Filter only negative and zer in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([number for number in numbers if number <= 0]) # [-4, -3, -2, -1, 0]

# 2.Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([number for lst in list_of_lists for sub_list in lst for number in sub_list]) # Think of it as a series of indented for loops
# for list in list_of_lists:
#   for sub_list in list:
#     for numb in sub_list:

# 3.  Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
print([(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)])

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
#  [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# for country in countries:
#   for element in country:
#     print([element[0].upper(), element[0][:3], element[1].upper()])

print([[element[0].upper(), element[0][:3], element[1].upper()] for country in countries for element in country])

# 5. Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
# for country in countries:
#   for element in country:
#     print(element)
#     {'country' : element[0], 'city' : element[1]}

print([{'country' : element[0], 'city' : element[1]} for country in countries for element in country])

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
print([name[0] + " " + name[1] for lst in names for name in lst])

# 7.Write a lambda function which can solve a slope or y-intercept of linear functions.
slope_solve = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
print(slope_solve(5, 10, 10, 5))
