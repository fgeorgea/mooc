import math

def valid_params(param):
	if type(param) != int or param < 0:
		return False
	return True

def	is_prime(nb):
	i = 2
	if nb == 2:
		return True
	if nb == 1:
		return False
	while i <= math.sqrt(nb):
		if nb % i == 0:
			return False
		i += 1
	return True

def	prime_numbers(count):
	if not valid_params(count):
		return
	numbers = []
	nb = 2
	while len(numbers) < count:
		if is_prime(nb):
			numbers.append(nb)
		nb += 1
	return numbers