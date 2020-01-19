#print(2**3)
def raise_to_power(a,b):
    result = 1
    for index in range(b):
        result = result*a
    return result
print(raise_to_power(24,3))