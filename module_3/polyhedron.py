import math

name = input()
length = float(input())

if name == 'T':
	print((math.sqrt(2) / 12) * (length ** 3))
elif name == 'C':
	print(length ** 3)
elif name == 'O':
	print((math.sqrt(2) / 3) * (length ** 3))
elif name == 'D':
	print(((15 + 7 * math.sqrt(5)) / 4) * length ** 3)
elif name == 'I':
	print(((5 * (3 + math.sqrt(5))) / 12) * length ** 3)
else:
	print("Polyèdre non connu")