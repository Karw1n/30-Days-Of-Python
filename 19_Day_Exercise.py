import re
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
        
# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

obama_speech = 'file_handling_data\obama_speech.txt'
michelle_obama_speech = 'file_handling_data\michelle_obama_speech.txt'
donald_speech = 'file_handling_data\donald_speect.txt'
melina_trump_speech = 'file_handling_data\melina_trump_speech.txt'

# Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech

def find_most_common_words(filename, number):
  words = {}
  with open(filename) as f:
    for line in f:
      for word in line.split():
        if word in words.keys() and word.isalpha():
          words[word] = words[word] + 1
        else:
          words[word] = 1
  top_words = sorted(words, key=words.get, reverse=True)[:number]
  tup_list = []
  for word in top_words:
    tup_list.append((word, words[word]))
    
  return tup_list

print(find_most_common_words(obama_speech, 10))
print(find_most_common_words(michelle_obama_speech, 10))
print(find_most_common_words(donald_speech, 10))
print(find_most_common_words(melina_trump_speech, 10))

# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def find_most_common_words_mod(filename, number):
  words = {}
  with open(filename) as f:
    for line in f:
      for word in line.strip().split():
        if word in words.keys() and word.isalpha() and word not in stop_words:
          words[word] = words[word] + 1
        else:
          words[word] = 1
  top_words = sorted(words, key=words.get, reverse=True)[:number]
  return top_words

def check_text_similarity(file1, file2):
  similar = 0
  file1_top_words = find_most_common_words_mod(file1, 10)
  file2_top_words = find_most_common_words_mod(file2, 10)
  
  for word in file1_top_words:
    if word in file2_top_words:
      similar += 1
      
  if similar < 0:
    return 'Not Similar'
  else:
    return f'Similarity of score: {similar}/10'
  
print(check_text_similarity(michelle_obama_speech, melina_trump_speech))

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
   
romeo_juliet_file = 'file_handling_data/romeo_and_juliet.txt'
print(find_most_common_words_mod(romeo_juliet_file, 10))

# 9. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
hacker_news_file = 'file_handling_data\hacker_news.csv'

def count_word(filename, words):
  with open(filename) as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      contains = False
      for item in row:
        if any(word in item for word in words):
          contains = True
          break
      if contains:
        line_count += 1
  return line_count
    
print(count_word(hacker_news_file, ['python', 'Python']))
print(count_word(hacker_news_file, ['JavaScript', 'javascript', 'Javascript c']))

def count_word_mod(filename, words):
  with open(filename) as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      contains = False
      for item in row:
        if any(word in item for word in words) and not 'JavaScript':
          contains = True
          break
      if contains:
        line_count += 1
  return line_count

print(count_word(hacker_news_file, ['Java']))
    