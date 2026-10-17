even_sum = 0

for i in range (1, 51):
    if i % 2 == 0:
        even_sum += i

print('the sum of even numbers from 1 to 50 is:' ,even_sum)





##this is the while loop version of the above code

even_sum2 = 0
number = 1

while number <= 50:
    if number % 2 == 0:
        even_sum2 += number
    number += 1
print(' the sum of even numbers from 1 to 50 is:' , even_sum2)