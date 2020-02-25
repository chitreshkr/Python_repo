'''Recall in class that we discussed the hailstone numbers
 wherexn= 3xn−1+1 if xn−1 is odd and xn = xn − 1/2 if xn−1 is even.
 The hailstone numbers converge to a sort of holding pattern 4→2→1→4→2→1→4→2→1.
 We call this kind of pattern a convergence because it repeats.Write a program to
  test generalized hailstone numbers where xn = axn−1 + b if
  xn−1 is odd and xn =xn−1/2 if xn−1 is even where
  a and b are positive integers. For each of thea,bpairs less than or equal to 10,
   findwhether or not the sequence seems to converge.
    Once you can do that, tell me how many different holding patterns
    the sequence converges to. For instance, when a= 3 and b = 5
    then 1→8→4→2→1 this is holding pattern. However,
     if we start with a different number, say5 we get a different holding pattern5→20→10→5.
'''

a = int(input('Enter a number '))
b = int(input('Enter a number '))


def run():
    global hailstone
    try:
        if (a + b) <= 10:
            hailstone = {1: 0}
            for i in range(2, 10):
                x = i
                mylist = []
                count = 0
                while x not in hailstone:
                    mylist += [x]
                    count += 1
                    x = x // 2 if x % 2 == 0 else a * x + b
                for item in mylist:
                    hailstone[item] = count + hailstone[x]
                    count -= 1
        else:
            print('a and b are greater than 10')
        print(hailstone)
    except:
        print("Something else went wrong")


run()
