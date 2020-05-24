class User():
    def sign_in(self):
        print('logged in')
        

class Wizard(User):
    def __init__(self,name,power):
        self.name= name
        self.power = power
    def attack(self):
        print(f'attacking with the power of {self.power}')

    #pass

class Archer(User):
    def __init__(self,name,arrow):
        self.name= name
        self.arrow = arrow
    def attack(self):
        print(f'attacking with the power of {self.arrow}')
        #pass

Wizard1 = Wizard('Merlin',50)
Archer1 = Archer('Abbie',20)
print(Wizard1.sign_in())
print(Wizard1.attack())
print(Archer1.attack())