import os
import json
import csv

f = open('30-Days-Of-Python/files/reading_file_example.txt')
# Has to be forward slash!
txt = f.read()
print(type(txt)) # <class 'str'>
print(txt)
# This is an example to show how to open a file and read.
# This is the second line of the text.
f.close()

f = open('30-Days-Of-Python/files/reading_file_example.txt')
txt_10 = f.read(10)
print(type(txt_10)) # <class 'str'>
print(txt_10) # This is an
f.close()

f = open('30-Days-Of-Python/files/reading_file_example.txt')
lines = f.readlines()
print(type(lines)) # <class 'list'>
print(lines) # ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
f.close()

# Alternate method same result
f = open('30-Days-Of-Python/files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines)) # <class 'list'>
print(lines) # ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
f.close()

# Another alternative where file is closed by itself
with open('30-Days-Of-Python/files/reading_file_example.txt') as f:
  lines = f.read().splitlines()
  print(type(lines)) # <class 'list'>
  print(lines) # ['This is an example to show how to open a file and read.', 'This is the second line of the text.']
  
# Append
# txt_file = '30-Days-Of-Python/files/reading_file_example.txt'
# with open(txt_file, 'a') as the_file:
#   the_file.write('\nThis text has been appended.')
  
# with open(txt_file) as reading:
#   lines = reading.read()
#   print(lines)
  
# Writing to a new file
with open('30-Days-Of-Python/files/writing_file_example.txt', 'w') as writing:
  writing.write('This text will be written in a newly created file')
  
with open('30-Days-Of-Python/files/writing_file_example.txt') as f:
  print(f.read())
  
try: 
	os.remove('.file/examples.txt')
except FileNotFoundError:
	print('The file does not exist')
 

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct['name'])

# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(person_json)

# Saving json to a file
# with open('30-Days-Of-Python/files/json_example.json', 'w', encoding='utf-8') as f:
#     json.dump(person, f, ensure_ascii=False, indent=4)

csv_file = '30-Days-Of-Python/files/csv_example.csv'
with open(csv_file) as f:
  csv_reader = csv.reader(f, delimiter=',') # w ise, reader method to read csv
  line_count = 0
  for row in csv_reader:
    if line_count == 0:
      print(f'Column names are :{", ".join(row)}')
      line_count += 1
    else:
      print(
        f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.' 
      )
      line_count += 1
  print(f'Number of lines: {line_count}.')