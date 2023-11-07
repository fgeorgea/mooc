import math

def	even(nbr):
	even = set()
	i = 0
	while i <= nbr:
		if i % 2 == 0:
			even.add(i)
		i += 1
	return even

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

def	prime_numbers(nbr):
	i = 2
	prime = set()
	while i <= nbr:
		if is_prime(i):
			prime.add(i)
		i += 1
	return prime

def	prime_odd_numbers(numbers):
	max_nbr = max(numbers)
	even_nbrs = even(max_nbr)
	prime_nbrs = prime_numbers(max_nbr)
	odd = set()
	prime = set()
	for number in numbers:
		if not number in even_nbrs:
			odd.add(number)
		if number in prime_nbrs:
			prime.add(number)
	return prime, odd

res = prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18])
print(res)