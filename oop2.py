#OOP
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name,age):
        if (self.membership):
            self.name = name                    #attributes
            self.age = age


    def shout(self):
        print(f'My name is {self.name}')


player1 = PlayerCharacter('Chitresh',26)
player2 = PlayerCharacter('Cindy',44)

#print(player1.name,player1.age)
#print(player2.name,player2.age)
print(player1.shout())
#help(list)
#print(player2.membership)