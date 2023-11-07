import math

EPSILON = 1 * (1/(10**9))
x = float(input())

def get_fraction(pos, x):
	i = pos
	numerator = x ** (2 * i + 1)
	denominator = 2 * 1 + 1
	return numerator / denominator

def get_ci(pos):
	i = pos
	ci = 1
	while i >= 1:
		ci *= ((2 * i) - 1) / (2 * 1)
		i -= 1
	return (ci)

def approx_arccos(x):
	i = 1
	arccos = (math.pi / 2) - x
	while i <= 1000 and (get_ci(i) * get_fraction(i, x)) < EPSILON:
		arccos -= get_ci(i) * get_fraction(i, x)
		i += 1
	return arccos

arccos = approx_arccos(x)
print(arccos)