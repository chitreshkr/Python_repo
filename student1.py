class Student:
	school = 'UTD'
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
	def avg(self):
		return (self.m1+self.m2+self.m3)/3
	def get_m1(self):
		return self.m1
	@classmethod
	def info(cls):
		return cls.school



s1 = Student(31,64,57)
s2 = Student(87,84,46)

print(s1.avg())
print(s2.avg())
print(s1.m1)
print(Student.info())