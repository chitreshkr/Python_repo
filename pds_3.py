def findRepeatingPattern(l1):
	firstElementAgain = [i for i, x in enumerate(l1) if x == l1[0]]
	if ([i for i, x in enumerate(l1)
	     if x == l1[-1]] != [0]):
		ind = [i for i, x in enumerate(l1) if x == l1[-1]]
		convergingPattern = ind[-1] - ind[-2]
	#print(convergingPattern)
	elif (firstElementAgain == [0]):

# The series does not converge to the first number

# Hence check for 1

indicesFor1 = [i for i, x in enumerate(l1) if x == 1]

convergingPattern = indicesFor1[-1] - indicesFor1[-2]

# print(convergingPattern)


else:

convergingPattern = firstElementAgain[-1] - firstElementAgain[-2]

# print(convergingPattern)


return convergingPattern

for i in range(1, 11, 1):

print("i : ", i)

for j in range(1, 11, 1):

print("j : ", j)

for x in range(1, 100):

print("x : ", x)

flag = False

hailstone = [x]

temp = x

for k in range(0, 50):

if x % 2 == 0:

x = int(x / 2)

else:

x = int(i * x + j)

hailstone.append(x)

if (hailstone[-1] in hailstone[:-1]):

flag = True

if (flag):

numberofPatterns = findRepeatingPattern(hailstone)

print(hailstone)

# print(seq_len(hailstone))

print("Number of converging patterns for {0} and {1} is {2}".format(i, j, numberofPatterns))

else:

print("No converging pattern found for {0}, {1}, {2}".format(i, j, temp))

print()