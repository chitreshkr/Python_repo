class Computer:
	def config(self):
		print("This is a i7 machine with 16GB RAM")


#a = '8'
#x = 9
com1 = Computer()
com2 = Computer()
#print(type(x))
#print(type(a))
#print(type(com1))
Computer.config(com1)
Computer.config(com2)

com1.config()