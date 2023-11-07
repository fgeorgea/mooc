def	print_sum(list, power):
	i = 0
	length = len(list)
	print(" ", end="")
	while i < length:
		print(list[length - i - 1], "^", power, sep="", end="")
		if i < length - 1:
			print(" + ", end="")
		i += 1

def est_armstrong(number):
	power = 0
	tmp = number
	list = []
	while True:
		list.append(tmp % 10)
		tmp = tmp // 10
		if tmp == 0:
			break
	power = len(list)
	sum = 0
	for elem in list:
		sum += elem ** power
	if sum == number:
		print(number, "=", end="")
	else:
		print(number, "!=", end="")
	print_sum(list, power)
	print()