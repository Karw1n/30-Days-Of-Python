import os
import json
import csv
# Day 19 File Handling

# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words

def line_and_word_counter(person, file):
  try:
    line_count = 0
    word_count = 0
    with open(file) as f:
      for line in f:
        line_count += 1
        word_count += len(line.split())
    print(f'{person}\nLine Count: {line_count}\nWord Count: {word_count}')

  except FileNotFoundError:
    print('File Not Found!')

# a: ombama_speech
obama_speech = '30-Days-Of-Python/file_handling_data/obama_speech.txt'
line_and_word_counter('Obama', obama_speech)
  
# b: michelle_obama_speech
michelle_obama_speech = '30-Days-Of-Python/file_handling_data/michelle_obama_speech.txt'
line_and_word_counter('Michelle Obama', michelle_obama_speech)

# c: donald_speech
donald_speech = '30-Days-Of-Python/file_handling_data/donald_speect.txt'
line_and_word_counter('Donald Trump', donald_speech)
# d: melina_trump_speech
melina_trump_speech = '30-Days-Of-Python/file_handling_data/melina_trump_speech.txt'
line_and_word_counter('Melina Trump', melina_trump_speech)

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def get_unique_langauges(data):
  unique_languages = set()
  for country in data:
    for language in country.get('languages'):
      unique_languages.add(language)
  return unique_languages


def most_spoken_langauges(filename, number):
  with open(filename, encoding='utf-8') as f:
    data = json.load(f)
    unique_languages = get_unique_langauges(data)
    
    languages_spoken = dict.fromkeys(unique_languages, 0)
    
    for country in data:
      for language in country.get('languages'):
        languages_spoken[language] = languages_spoken[language] + 1
      
    top_n = sorted(languages_spoken, key=languages_spoken.get, reverse=True)[:number]
    return [(language, languages_spoken[language]) for language in top_n]
    

country_file_location = 'file_handling_data/countries_data.json'
print(most_spoken_langauges(country_file_location, 10))
print(most_spoken_langauges(country_file_location, 3))

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(filename, number):
  with open(filename, encoding='utf-8') as f:
    data = json.load(f)
    top_n_pop = sorted(data, key=lambda x: x['population'], reverse=True)[:number]
    return [(country['name'], country['population']) for country in top_n_pop]    

print(most_populated_countries(country_file_location, 10))
print(most_populated_countries(country_file_location, 3))

# Exercises: Level 2
# 4. Extract all incoming email adresses as a list from the email_exchange_big.txt file.
emails = []

with open('file_handling_data/email_exchanges_big.txt') as f:
  for line in f:
    if line.startswith("From "):
      parts = line.split()
      if len(parts) > 1:
        emails.append(parts[1]) 
        
