

class A:
	def feature1():
		print('Feature 1 is working')
	def feature2():
		print('Feature 2 is working')
class B(A):
	def feature3():
		print('Feature 1 is working')
	def feature4():
		print('Feature 2 is working')

a1 = A
b1 = B

a1.feature1()
a1.feature2()
b1.feature1()
