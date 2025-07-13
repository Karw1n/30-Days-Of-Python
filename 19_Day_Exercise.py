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

