import os, datetime

if os.path.exists('diary.txt'):
	print('diary.txt exists.')
else:
	print('diary.txt does not exist.Creating file...')
	with open('diary.txt', 'w') as file:
		pass
	
entry = input('Enter your diary entry: ')

timestamp = datetime.datetime.now()

with open('diary.txt', 'a') as file:
	file.write(f'{timestamp} - {entry}\n')

with open('diary.txt', 'r') as file:
	content = file.read()

print('\nDiary Entries:')
print(content)