#OOP
class PlayerCharacter:
    #class object attribute
    membership = False
    def __init__(self,name,age):
        if (self.membership):
            self.name = name
            self.age = age
            pass

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Chitresh',26)
player2 = PlayerCharacter('Cindy',44)

print(player1.name,player1.age)
#print(player2.name,player2.age)
#print(player1.run())
#help(list)
print(player2.membership)