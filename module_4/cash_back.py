def	rendre_monnaie(price, twenty, ten, five, two, one):
	given_money = (twenty * 20) + (ten * 10) + (five * 5) + (two * 2) + one
	difference = given_money - price
	if difference < 0:
		return None, None, None, None, None
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	while difference - 20 >= 0:
		difference -= 20
		a += 1
	while difference - 10 >= 0:
		difference -= 10
		b += 1
	while difference - 5 >= 0:
		difference -= 5
		c += 1
	while difference - 2 >= 0:
		difference -= 2
		d += 1
	while difference - 1 >= 0:
		difference -= 1
		e += 1
	return a, b, c, d, e