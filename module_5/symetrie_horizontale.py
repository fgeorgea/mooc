def	symetrie_horizontale(matrice):
	i = 0
	tmp = []
	length = len(matrice)
	while (i < length / 2):
		tmp = matrice[i]
		matrice[i] = matrice[length - i - 1]
		matrice[length - i - 1] = tmp
		i += 1
	return matrice

values = symetrie_horizontale([[2, 7, 6], [9, 5, 1], [4, 3, 8]])

print(values)