# Day 16 Python Datetime
from datetime import datetime, date

# Getting datetime Information
now = datetime.now()
print(now)                      # 2025-06-13 15:59:26.339713
day = now.day                   # 13
month = now.month               # 6
year = now.year                 # 2025
hour = now.hour                 # 15
minute = now.minute             # 59
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)  # timestamp 1749826766.339713
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 13/6/2025, 15:59

# Formatting Date Output Using strftime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

# Using date from datetime
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2025-06-13
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2025
print("Current month:", today.month) # 6
print("Current day:", today.day)     # 13

