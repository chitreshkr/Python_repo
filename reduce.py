my_list = [1,2,3]
from _functools import reduce
def accumulator(acc,item1,item2):
    print(acc,item1,item2)
    return acc + item1 + item2

print(reduce(accumulator,my_list,0))
print(my_list)