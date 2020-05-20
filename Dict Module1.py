user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}
user2 = dict(name = 'JohnJohn')
user3 = user.copy()
print(user.get('age',25))
print(user2)
print('basket' in user.keys())
print('hello' in user.values())
print(user.items())
print(user.popitem())
print(user.clear())
print(user3.items())