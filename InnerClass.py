

class Student:
	def __init__(self,name,rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()
	def show(self):
		print(self.name,self.rollno)

	class Laptop:
		def __init__(self):
			self.brand = 'HP'
			self.cpu = 'i7'
			self.ram = '16GB'




s1 = Student('Chitresh',5)
s2 = Student('Ankit',2)

s1.show()
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))
