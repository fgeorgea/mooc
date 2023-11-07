import math

def	premier(n):
	if n == 2:
		return True
	if n < 2:
		return False
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i += 1
	return True

x = int(input())

i = 2
while i < x:
	if premier(i):
		print(i)
	i += 1