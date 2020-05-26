class Superlist(list):
    def __len__(self):
        return 1000
    pass
superlist1 = Superlist();
print(len(superlist1))
superlist1.append(5)
print(superlist1[0])
print(issubclass(Superlist,list))
print(issubclass(list,superlist1))
