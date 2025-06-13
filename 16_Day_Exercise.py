# Day 16 Exercise Python DateTime
from datetime import datetime, date

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
right_now = now.timestamp

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(f'{month}/{day}/{year}, {now.hour}:{now.minute}:{now.second}')
print(now.strftime('%m/%d/%Y, %H:%M:%S'))

# 3. Today is 5 December, 2019. Change this time string to time.
today = '5 December, 2019'
print('Today as string = ', today)
today_object = datetime.strptime(today, "%d %B, %Y")
print("Today as object = ", today_object)

# 4. Calculate the time difference between now and new year.
today = date(year=2025, month=6, day=13)
new_year = date(year=2026, month=1, day=1)
time_till_new_year = new_year - today
print('Time left for new year: ', time_till_new_year)

# 5. Calculate the time difference between 1 January 1970 and now.
print(now.timestamp())

# 6. Think, what can you use the datetime module for? Examples:
'''
- Using it to record transactions and when a sale was made
- Scheduling tasks and deadlines
- For threads detremining when a process is being carried out
'''