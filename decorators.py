def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
    return wrap_func
@my_decorator
def hello():
    print('Hello')
@my_decorator
def bye():
    print('See ya alll')

hello()
bye()