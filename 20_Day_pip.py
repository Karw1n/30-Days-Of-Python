import numpy
import webbrowser # web browser module to open websites
import requests

# Switch interpreter If not working

lst = [1, 2, 3, 4, 5]
np_array = numpy.array(lst)
print(np_array)

np_array = np_array * 2
print(np_array)
np_array += 3
print(np_array)


# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# # opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)
    
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page