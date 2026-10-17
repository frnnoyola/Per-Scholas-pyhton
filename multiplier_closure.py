def make_multiplier(factor):
	def multiply(number):
		return number * factor

	return multiply

times3 = make_multiplier(3)
times10 = make_multiplier(10)

print(times3(7))

print(times10(7))