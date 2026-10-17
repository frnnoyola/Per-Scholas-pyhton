#greeting user

name = input("enter your name: ")
def greet_user(name):
    print("hello! " + name + " welcome!")
    if name == None:
        print("Hello!, Welcome!")

greet_user(name)


##adding two numbers

a=float(input(" enter your first number: "))
b=float(input(" enter your second number: "))
def add_numbers(a, b):
    sum = a+ b
    print("the addition of these two numbers is:" + str(sum))

add_numbers(a, b)

#is even or odd

def is_even(num):
    if num % 2 == 0:
        print(str(num) + " is an even number")
    else:
        print(str(num) + " is an odd number")

num = int(input("enter a number please: "))

is_even(num)
