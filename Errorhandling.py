while True:
    try:
        age = int(input("Enter your age:"))
        #x = 100/age
        print(f'Your age is {age}')
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please enter a number higher than zero')
    else:
        print('Thank you')
        break
