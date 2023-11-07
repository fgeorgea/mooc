import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
attempts = 0

for i in range(6):
	nbr = int(input())
	if nbr == secret:
		print("Gagné en ", i + 1, " essai(s) !", sep="")
		break
	elif (attempts + 1) == 6:
		print("Perdu ! Le secret était ", secret, sep="")
		break
	elif nbr > secret:
		print("Trop grand")
	elif nbr < secret:
		print("Trop petit")
	attempts += 1