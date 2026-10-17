def validate_age(age):

	if age > 120:
		raise ValueError("Age cannot be greater than 120")
	elif age < 0:
		raise ValueError("Age cannot be less than 0")

try:
	age = int(input("Please enter an age from 0 -120: "))
	validate_age(age)
	print("Age accepted.")

except ValueError as error:
	print(error)

	

