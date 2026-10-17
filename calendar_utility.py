import calendar, datetime

year = int(input("Enter a year: "))
month = int(input("Enter a month number (1-12): "))

print('\nCalendar:')
print(calendar.month(year, month))

today = datetime.datetime.now()

print("Today's date:", today.date())

if today.year == year and today.month == month:
	print (f'Today is {today.strftime('%B')} {today.day}, {today.year}')
else:
	print("Today's date is not in the month and year you selected.")
