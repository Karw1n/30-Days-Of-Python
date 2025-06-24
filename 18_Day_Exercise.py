import re
# Exercise Level 1
# 1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# paragraph_list = list(paragraph.split())
#remove puncts
paragraph_list = re.split(r'[.\s]+', paragraph)
#print(paragraph_list)
paragraph_dict = {}
for i in range(len(paragraph_list)):
    if  paragraph_list[i] in paragraph_dict.keys():
        paragraph_dict[paragraph_list[i]] = paragraph_dict[paragraph_list[i]] + 1
    else:
        paragraph_dict[paragraph_list[i]] = 1
        
print(paragraph_dict) 
most_common = sorted(paragraph_dict, key=paragraph_dict.get, reverse=True)[:1]

print(f'Most Common = {most_common[0]}\nCount = {paragraph_dict[most_common[0]]}')

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

points_txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
points_list = re.findall(r'[-]?\d+', points_txt) # ['-12', '-4', '-3', '-1', '0', '4', '8']
points_list = [int(point) for point in points_list]
sorted_points = points_list
sorted_points.sort()
print(sorted_points)
distance = sorted_points[0] - sorted_points[-1]
print(distance)

# Exercise Level 2
# 1. Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(variable):
    regex = r'^[a-z]+[a-z|_]+'
    pattern = re.findall(regex, variable, re.I)
    if pattern:
        return pattern[0] == variable
    return False
        
print(is_valid_variable('first_name_pls')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True)

# Exercise Level 3
# 1. Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_txt = re.sub(r'[%$@&;#?!]', '', sentence)

def most_frequent_words(txt):
    txt_dict = {}
    txt_list = re.split(r'[.\s]+', txt)
    for i in range(len(txt_list)):
        if txt_list[i] in txt_dict.keys():
            txt_dict[txt_list[i]] = txt_dict[txt_list[i]] + 1
        else:
            txt_dict[txt_list[i]] = 1
    most_frequent = sorted(txt_dict, key=txt_dict.get, reverse=True)[:3]
    result = []
    for word in most_frequent:
        result.append((word, txt_dict[word]))
    return result

print(most_frequent_words(clean_txt))    
    