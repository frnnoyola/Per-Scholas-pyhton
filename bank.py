class BankAccount:
	def __init__(self, account_number, owner, balance,):
		self.account_number = account_number
		self.owner = owner
		self.balance = balance
		
	def deposit(self, amount):
		self.balance += amount

	def show_balance(self):
		print(self.balance)

	def withdraw(self, amount):
		if amount > self.balance:
			raise ValueError("Cannot withdraw, insufficient funds")
		else:
			self.balance -= amount
			print(self.balance)



class SavingsAccount(BankAccount):
	def __init__(self, account_number, owner, balance, interest_rate):
		super().__init__(account_number, owner, balance)
		self.interest_rate = interest_rate

	def apply_interest(self):
		interest = self.balance * (self.interest_rate / 100)
		self.balance += interest

	def __str__(self):
		return f"{self.owner} - Balance: {self.balance} - Interest Rate: {self.interest_rate}%"	
		
		

account1 = BankAccount(100100, "John Doe", 0)



account1.deposit(1000)

account1.show_balance()


account1.withdraw(500)

account1.show_balance()
try:
	account1.withdraw(600)
except ValueError as error:
	print(error)


savings1 = SavingsAccount(100100, "John Doe", 1000, 5)

savings1.apply_interest()

print(savings1)

savings1.deposit(500)
print(savings1)

savings1.withdraw(200)
print(savings1)

