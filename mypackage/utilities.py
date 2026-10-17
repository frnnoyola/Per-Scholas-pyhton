import math

def greet(name):
	print('Hello ' + name + '!')

name = input('What is your name?')
greet(name)


def factorials(n):
	result = math.factorial(n)
	print(result)

number = int(input("Enter a number: "))
factorials(number)