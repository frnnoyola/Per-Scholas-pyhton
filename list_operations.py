mylist = [1, 3, 8, 6, 5]

print(mylist)

## uses the built in sorted() function
print(sorted(mylist))

#uses .sort() method
mylist.sort()

#appending to the list
mylist.append(10)
print(mylist)

#removing from the list
mylist.remove(3)
print(mylist)



#uses the reverse method to reverse list
print(list(reversed(mylist)))