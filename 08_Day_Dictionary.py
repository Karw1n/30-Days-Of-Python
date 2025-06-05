# Removing Key and Values from a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.pop('key1')) # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
print(dct)
del dct['key2'] # removes key2 item
print(dct)

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

dict_1 = {'key1':'value1', 'key2':'value2'}
dict_2 = {'key3':'value3', 'key4':'value4'}
dict_1.update(dict_2)
