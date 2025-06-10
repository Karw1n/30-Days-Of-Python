# List Comprehension with if expressions
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
print([i for i in range(len(numbers)) if i % 2 == 0 and i > 0])

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [number for row in list_of_lists for number in row]
print(flatten_list)

# Lambda Functions
def add_two_nums(a, b):
  return a + b
print(add_two_nums(2, 3)) # 5
# Converting the function above to lambda
add_two_nums_test = lambda a, b: a + b
print(add_two_nums_test(2, 3)) # 5

# Self invoking lambda function
print((lambda a, b: a + b)(5, 5))

# Lambda Function Inside Another Function
def power(x):
  return lambda n : x ** n

cube = power(2)(3) # function power needs 2 arguments to run, in sep ()
print(cube)