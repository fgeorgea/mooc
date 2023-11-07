def	init_mat(row, column):
	matrice = []
	for i in range(row):
		submatrice = []
		for j in range(column):
			submatrice.append(0)
		matrice.append(submatrice)
	return matrice

values = init_mat(3, 2)
print(values)