def factorial(n):
	factorial = 1
	i = 1
	while i <= n:
		factorial *= i
		i += 1
	return factorial

def	get_term(n, x):
	num = ((-1) ** n) * factorial(2 * n)
	denom = (2 ** (2 * n)) * (factorial(n) ** 2) * (2 * n + 1)
	mult = x ** (2 * n + 1)
	return ((num / denom) * mult)

def	arcsinh(x):
	n = 0
	arcsinh = 0
	while n <= 300:
		arcsinh += get_term(n, x)
		n += 1
	return arcsinh
