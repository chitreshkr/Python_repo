range(100)

#def make_list(num):
#    result = []
#    for i in range(num):
#        result.append(i*2)
#    return result


def generator_function():
    for i in range(10000):
        yield i

for item in generator_function():
    print(item)
#my_list = make_list(100)
#print(my_list)