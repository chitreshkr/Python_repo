class Computer:
	def __init__(self):
		self.name = "Chitresh"
		self.age = 27

	def update(self):
		self.age = 30

	def compare(self,other):
		if self.age == other.age:
			return True
		else:
			return False
c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
	print("They are same")
else:
	print("They are different")

print(c1.name)
print(c2.name)
