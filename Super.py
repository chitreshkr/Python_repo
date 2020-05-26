class User():
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power,email):
        super().__init__(email) #super to get the email from User
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')

    # pass


class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'attacking with the power of {self.arrow}')
        # pass


Wizard1 = Wizard('Merlin', 50,'merlin@gmail.com')
Archer1 = Archer('Abbie', 20)

#for char in [Wizard1,Archer1]:
#    char.attack()
#print(Wizard1.email)
print(dir(Wizard1))