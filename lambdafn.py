from functools import reduce

#lambda parameter : func(param)
my_list = [1,2,3]
print(list(map(lambda item:item*2,my_list)))

my_list1 = [5,4,3]

print(list(map(lambda item : item**2 , my_list1)))

a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort(key= lambda x : x[1])
print(a)
#lambda item : for i in list[i,1] return sorted(item)

my_list2 = [char for char in 'hello']
my_list3 = [num for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num%2==0]

print(my_list2)
print(my_list3)
print(my_list4)