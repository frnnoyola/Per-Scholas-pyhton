lablist = [1, 2, 3, 4, 5, 6, 7]

cont = ""

def add_number():
    try:
        number = int(input("Please select a number: "))
        lablist.append(number)
        print(lablist)

    except ValueError:
        print("Invalid input. Please enter a whole number.")


def remove_number():
    try:
        index = int(input("Enter the index you want to remove: "))
        lablist.pop(index)
        print(lablist)

    except ValueError:
        print("Invalid input. Please enter a whole number for the index.")

    except IndexError:
        print("Invalid index. That position does not exist in the list.")


def display_list():
	print(lablist)


while cont != "d" :
	cont = input(
		"a. Add a number:\n"
		"b. Remove a number:\n"
		"c. Display list:\n"
		"d. Quit:\n"
		"Enter your choice..."
		)
	if cont == "a":
		add_number()
	elif cont == "b":
		remove_number()
	elif cont == "c":
		display_list()
	elif cont == "d":
		print("Goodbye")
	else:
		print("Invalid option try again" )