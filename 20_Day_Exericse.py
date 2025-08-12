import requests
import json

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/47960/pg47960-images.html'

# link = 'https://www.gutenberg.org/cache/epub/47960/pg47960-images.html'
# response = requests.get(link)
# print(response)
# print(response.status_code)
# print(response.text)
# # Link is outdated

# # 2.
url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
print(response)
print(response.status_code)
cats_dict = response.json()
##cats_dict = json.loads(cats)
cats_weight_freq = {}
for cat in cats_dict:
  weight = cat['weight']['metric']
  min_w, max_w = map(float, weight.split(' - '))
  avg_weight = int(round(((min_w+max_w)/2), 2))
  if avg_weight in cats_weight_freq:
    cats_weight_freq[avg_weight] = cats_weight_freq[avg_weight] + 1
  else:
    cats_weight_freq[avg_weight] = 1
print(cats_weight_freq)

cats_weight_freq_sorted = sorted(cats_weight_freq, key=cats_weight_freq.get, reverse=False)

min = cats_weight_freq_sorted[0]
max = cats_weight_freq_sorted[-1]

print(f'Min = {min} metric units, with {cats_weight_freq[min]} cats having this weight')
print(f'Max = {max} metric units, with {cats_weight_freq[max]} having this weight')

total_cats = sum(cats_weight_freq.values())

def calculate_mean(dict):
  total = sum(dict.values())
  initial_sum = 0
  for key in dict:
    initial_sum += key * dict[key]
  return initial_sum / total

print(f'Mean weight is: {calculate_mean(cats_weight_freq)}')

def calculate_median(dict):
  total = sum(dict.values())
  dict_sorted = sorted(dict, key=dict.get, reverse=False)
  mid = total // 2
  counter = 0
  current = dict[dict_sorted[0]]
  while current < mid:
    counter += 1
    current += dict[dict_sorted[counter]]
  return dict_sorted[counter]

print(f'Median is: {calculate_median(cats_weight_freq)}')