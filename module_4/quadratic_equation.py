import math

def	rac_eq_2nd_deg(a, b, c):
	delta = (b ** 2) - (4 * a * c)
	if (delta < 0):
		return ()
	if (delta == 0):
		return ((-b) / 2 * a,)
	x1 = ((-b) - math.sqrt(delta)) / (2 * a)
	x2 = ((-b) + math.sqrt(delta)) / (2 * a)
	return (min(x1, x2), max(x1, x2))