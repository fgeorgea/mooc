def	facto(n):
	res = 1
	for i in range (n):
		res *= i + 1
	return res

def	catalan(n):
	num = facto(2 * n)
	denom = facto(n + 1) * facto(n)
	return (num // denom)