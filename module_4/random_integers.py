import random

def	alea_dice(s):
	random.seed(s)
	x = random.randint(1, 6)
	y = random.randint(1, 6)
	z = random.randint(1, 6)
	if x + y + z == 7:
		return True
	return False

#print(alea_dice((1)))