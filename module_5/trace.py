def	trace(matrice):
	sum = 0
	i = 0
	length = len(matrice)
	while i < length:
		sum += matrice[i][i]
		i += 1
	return sum
