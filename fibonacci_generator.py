def gen_fibonacci(n):
 	a = 0
 	b = 1

 	for i in range(n):
		
 		print(a)
 		a, b = b, a + b

gen_fibonacci(10)
