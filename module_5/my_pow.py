def	my_pow(m, b):
	if type(m) != int or type(b) != float:
		return
	i = 0
	j = m
	powers = []
	while i < j:
		powers.append(b**i)
		i += 1
	return (powers)

#print(my_pow(20, 2.0))