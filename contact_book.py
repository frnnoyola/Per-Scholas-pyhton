contactbook = {"Jack": "9178888888", "Dan": "7182222222", "John": "7183333333" }

def  viewcon():
	print(contactbook)

def searcon():
	search = input('Enter a name to search: ')

	for name in contactbook:
		if search.lower() in name.lower():
			print(name, contactbook[name])

def Exi():
	print('Goodbye')
	raise SystemExit

def morecon():
    key = input("Enter a name: ")
    value = input("Enter a number: ")

    if key in contactbook:
        print("This contact name exists already, try again.")

    elif len(value) > 10:
        print("Not a valid number, try again.")

    else:
        contactbook[key] = value
        print("Contact added.")


def delcon():
	search2 = input('Enter a name to delete: ')
	for name in list(contactbook):
		if search2.lower() in name.lower():
			del contactbook[name]
			print('Contact deleted.')
			return
	print("contact not found")

choice = 0
while choice != 5:
    try:
        choice = int(input(
            "Contact Book Menu:\n"
            "1. Add Contact\n"
            "2. View All Contacts\n"
            "3. Search Contact\n"
            "4. Delete Contact\n"
            "5. Exit\n"
            "Enter your choice (1-5): "
        ))

        if choice == 1:
            morecon()

        elif choice == 2:
            viewcon()

        elif choice == 3:
            searcon()

        elif choice == 4:
            delcon()

        elif choice == 5:
            print("Goodbye")

        else:
            print("Invalid option. Try again.")

    except ValueError:
        print("Please enter a number from 1 to 5.")




#I started this By creating the dictionary that is going to be called to.,
#then I started creating the functions for the contact list, starting with the most simple which was printing the contact list for the user.
#searching in the contact list gave me some trouble because it was difficult for the function to distinguish when I was searching for the contacts
#until I used ".lower" to make the entries lowercase as well to make it simple to search for the contact.
#my favorite part of this was making the actual menu because it gave me understanding of how menus can work in program or games.
#I put all the functions in a while loop so that the menu loops again until the user hits "5" which would exit the program.
#