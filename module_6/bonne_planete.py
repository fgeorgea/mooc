import math

diameter = int(input())

def	bonne_planete(diameter):
	surface = math.pi * diameter**2
	if surface >= 50000:
		return True
	return False

good_planet = bonne_planete(diameter)
if good_planet:
	print("Bonne planète")
else:
	print("Trop petite")