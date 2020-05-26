my_list = [1,2,3]
def check_odd(item):
    if item%2 !=0:
        return True

print(list(filter(check_odd,my_list)))
