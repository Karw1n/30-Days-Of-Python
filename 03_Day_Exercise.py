# Day 3: Operators
# 1. Declare your age integer variable
age = 21
# 2. Declare your height as a float
height = 177.7
# 3. Declare a variable that stores a complex number
complex_number = 666j

# 4. Write a script that prompts the user to enter base and heigh of the triangle and calculate an area of this triangle.
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}.")

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Side a: "))
side_b = int(input("Side b: "))
side_c = int(input("Side c: "))
permieter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {permieter}.")

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)).
length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width 
permieter = 2 * (length + width)
print(f"The area of the rectangle is: {area}.\nThe perimeter of the rectangle is: {permieter}.")

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
circumference = round(2 * pi * radius, 2)
print(f"The area of the circle is: {area}cm^2.\nThe circumference of the circle is: {circumference}cm.")

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y = mx + b
# m = slope
m = 2
# b = y-intercept
b = -2
y_intercept = (0, b)

# x-intercept = y = 0 5
# 0 = 2x - 2, 2x = 2, x = 1
x_intercept = (-b / m, 0)

print(f"Slope: {m}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, x2, y1, y2 = 2, 6, 2, 10
m_2 = (y2-y1)/(x2-x1)
eucli_dist = (y2-y1)**2 + (x2-x1)**2
print(f"Slope: {m_2}")
print(f"Euclidean Distance: {eucli_dist}")

# 10. Compare the slopes in tasks 8 and 9.
print(f"The difference in slope 8 and 9 is {(m_2 - m)**2}")

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x = -3
y = x**2 + (6*x) + 9
a, b, c = 1, 6, 9
quad = (-b + (b**2 - (4 * a * c))**1/2)/2*a
print(f"y = {y}")
print(f"When y = 0, x = {quad}")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word1 = 'python'
word2 = 'dragon'
print(f"The length of python is: {len(word1)}")
print(f"The length of dragon is: {len(word2)}")
print(len(word1) != (len(word2)))

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in word1 and 'on' in word2)

# 14.I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# 15. There is no 'on' in both dragon and python
print(not ('on' in word1 and 'on' in word2))

# 16. Find the length of the text python and convert the value to float and convert it to string
word = 'python'
length = len(word)
print(f"Length variable type: {type(length)}")
length = float(length)
print(f"Length variable type: {type(length)}")
length = str(length)
print(f"Length variable type: {type(length)}")

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: "))
print(f"Is even: {number % 2 == 0}")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type('10') is type(10))

# 20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print(f"Your weekly earning is: {hours*rate}.")

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter a number of years: "))
print(f"You have lived for {years * 3153600} seconds.")

# 23. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
  print(i, 1, i, i**2, i**3)

