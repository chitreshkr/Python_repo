my_set = {1,2,3,4,5,5,5}
your_set = {1,2,3,6}
my_set.add(2)
my_set.add(100)
print(my_set)
#print(my_set[0])
print(1 in my_set)
print(my_set.difference(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.issubset(your_set))
print(my_set.union(your_set))
print(my_set.issuperset(your_set))