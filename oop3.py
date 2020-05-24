#OOP
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name,age):
        if (self.membership):
            self.name = name                    #attributes
            self.age = age


    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter('Chitresh',26)
player2 = PlayerCharacter('Cindy',44)

player1.speak()
'hello'.upper()