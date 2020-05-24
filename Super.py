class User():
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print('logged in')
class Wizard(User):
    def __init__(self, name, power,email):
        User.__init__(self,email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')

Wizard1 = Wizard('Merlin', 50,'merlin@gmail.com')

print(Wizard1.email)