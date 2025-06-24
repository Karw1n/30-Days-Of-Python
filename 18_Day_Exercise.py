# Exercise Level 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph_list = list(paragraph.split())
#remove puncts
#print(paragraph_list)
paragraph_dict = {}
for i in range(len(paragraph_list)):
    if  paragraph_list[i] in paragraph_dict.keys():
        paragraph_dict[paragraph_list[i]] = paragraph_dict[paragraph_list[i]] + 1
    else:
        paragraph_dict[paragraph_list[i]] = 1
        
print(paragraph_dict) 