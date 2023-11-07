nbr = int(input())

for i in range(nbr):
	print(" " * (nbr - 1 - i), end="")
	cycle = i + 1
	for j in range(i):
		print(cycle % 10, end="")
		cycle += 1
	print(cycle % 10, end="")
	cycle -= 1
	for x in range(i):
		print(cycle % 10, end="")
		cycle -= 1
	print()