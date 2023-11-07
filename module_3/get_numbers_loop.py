case = int(input())
sum = 0
nbr = 0

if case >= 0:
	for x in range(case):
		nbr = int(input())
		sum += nbr
else:
	while True:
		nbr = input()
		if nbr == 'F':
			break
		else:
			nbr = int(nbr)
			sum += nbr

print(sum)