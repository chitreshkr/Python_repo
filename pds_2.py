def generate_hailstone(num):
	count = 0

	seq = []

	hailstone = 0
	for a in range(1, 10):
		for b in range(1, 10):
			hailstone = 0
			count = 0
			seq = []
			temp = num
			while (temp != 1 and temp not in seq and hailstone != 1):
				count += 1
				if (count > 1000):
					hailstone = 1
					break

				seq.append(temp)
				if (temp % 2) == 0:
					temp = temp // 2
					if (temp % 2 != 0):
						for n in seq:
							if (n % 2 != 0 and temp > n and a % 2 == 0 and b % 2 == 0 and (
									((a // 2) % 2 == 0 and (b // 2) % 2 != 0) or (
									(b // 2) % 2 == 0 and (a // 2) % 2 != 0))):
								hailstone = 1
								break

				else:

					temp = (temp * a) + b
					if (temp % 2 != 0):
						hailstone = 1
						break

			seq.append(temp)
			if (hailstone == 0):
				print('At a = {}, b = {}, {} is hailstone with sequence {} \n'.format(a, b, value, seq))
			else:
				print('At a = {}, b = {}, {} does not converge \n'.format(a, b, value))
	return (seq)


value = input("Enter a number:")
value = int(value)

x = generate_hailstone(value)