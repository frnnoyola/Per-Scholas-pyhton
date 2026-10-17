sentence = input("Please write a sentecne")
modified = sentence.replace(" ", "-")

count = 0
for letter in sentence:
	if letter.lower() in "aeious":
		count += 1


print(sentence)
print("This is all uppercase:",sentence.upper)
print("Here it is in reverse:", sentence[::-1])
print("Number of vowels:", count)
print("Here is the spaces replaced with hyphens:", modified)