import math, random, platform


random_number = random.randint(1,100)
square_root = math.floor(math.sqrt(random_number))

print('Random Number:', random_number)
print('Square Root (floored):', square_root)
print('Operating System:', platform.system())
print('Python Version:', platform.python_version())