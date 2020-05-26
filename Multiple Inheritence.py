class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')

    # pass


class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def check_arrows(self):
        print(f'attacking with the power of {self.arrow}')
        # pass
        def run(self):
            print('Ran really fast')
class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,arrow):
        Archer.__init__(self,name,arrow)
        Wizard.__init__(self,name,power)
    #pass

hb1 = HybridBorg('Bergie',50,100)
#print(hb1.attack())
print(hb1.check_arrows())
print(hb1.attack())
#Wizard1 = Wizard('Merlin', 50)
#Archer1 = Archer('Abbie', 20)
#print(Wizard1.sign_in())
#print(Wizard1.attack())
#print(Archer1.attack())