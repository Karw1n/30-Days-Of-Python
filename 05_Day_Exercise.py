# exercise 1
# 1. Declare an empty list
empty_list = list()
empty_list = []

# 2. Declare a list with more than 5 items
fruits = ['apple', 'orange', 'pear', 'kiwi', 'passionfruit', 'banana', 'lemon']

# 3. Find the length of your list
print(len(fruits)) # 6

# 4. Get the first item, the middle item and the last item of the list
print(f"First Item: {fruits[0]}\nMiddle Item: {fruits[int(len(fruits)/2)]}\nLast Item: {fruits[-1]}")

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Alex', 22, 177, 'To be married', 'No House']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 

# 7. Print the list using print()
print(mixed_data_types)
print(companies)

# 8. Print the number of companies in the list
print(len(companies))

# 9. Print the first, middle and last company
print(f"First Item: {companies[0]}\nMiddle Item: {companies[int(len(fruits)/2)]}\nLast Item: {companies[-1]}")

# 10. Print the list after modifying one of the companies
companies[3] = 'Pear'
print(companies)

# 11. Add an IT company to it_companies
it_companies = companies.copy()
it_companies.append('FIS')

# 12. Insert an IT company into the middles of the companies list
it_companies.insert(int((len(it_companies)-1) / 2), 'Computer Company')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;'
print("#; ".join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print('Five Guys' in it_companies)
print('Pear' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies from the list
print(it_companies[3:])

# 19. Slice out the last 3 companies from the list
print(it_companies[:-3])

# 20. Slice out the middle IT company or companies from the list
print(it_companies[:int(len(it_companies)/2)
  ] + it_companies[int(len(it_companies)/2 + 1):])

# 21. Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(int((len(it_companies) - 1) /2))
print(it_companies)

# 23. Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies from the list
for i in range(0, len(it_companies)):
  it_companies.pop()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the two lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
position_to_insert = full_stack.index('Redux')
full_stack.insert(position_to_insert + 1,'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# Exercise 2
# 1. The following is a list of 10 student ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Find the median age
median_age = 0
if len(ages) % 2 == 0:
  median_age = (ages[int((len(ages)-1)/2)] + ages[int((len(ages))/2)]) / 2
else:
  median_age = ages[int((len(ages)-1)/2)]
print(median_age)  

# Find the average age
average_age = sum(ages) / len(ages)
print(average_age)

# Find the range of the ages
age_range = ages[-1] - ages[0]
print(f'Age range: {age_range}')

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_age - average_age))
print(abs(max_age -average_age))

# 1. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
middle_country = 0
if len(ages) % 2 == 0:
  middle_country = (countries[int((len(countries)-1)/2)], countries[int(((len(countries) - 1)/2) + 1)])
else:
  middle_country = countries[int((len(countries)-1)/2)]
print(middle_country) 

# 2 Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = []
second_half = []
if (len(countries) % 2 == 0):
  first_half = countries[:int(len(countries)/2)]
  second_half = countries[int(len(countries)/2):]
else:
  first_half = countries[:int(len(countries)/2)]
  second_half = countries[int(len(countries)/2) + 1:]


# 3 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

country1, country2, country3, country4, country5, country6, country7, *rest = countries

print(country1)