# syntax
lst = list()
empty_list = list() # empty list no items
print(len(empty_list)) # 0 
lst = list((1, 2, 3, 4))
print(lst)
fruits = list(('apple', 'pear', 'orange'))
print(fruits)

lst = []
empty_list = []
print(len(empty_list)) # 0
lst = [1, 2, 3, 4]
print(lst) # [1, 2 ,3, 4]
fruits = ['apple', 'pear', 'orange']
print(fruits)
print(len(fruits))

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

lst = ['item1', 'item2']
lst.remove('item1')
print(lst) # ['item2']