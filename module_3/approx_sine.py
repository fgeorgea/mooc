x = float(input())

power = 3
sine = x
is_neg = True
while True:
	num = x ** power
	fact = 1
	for i in range(2, power+1):
		fact = fact * i
	power += 2
	if abs(num / fact) < (1 / (10 ** 6)):
		break
	if is_neg:
		sine -= num / fact
	else:
		sine += num / fact
	is_neg = not is_neg

print(sine)