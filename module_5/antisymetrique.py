def	antisymetrique(matrice):
	for i in range(len(matrice)):
		for j in range(len(matrice[i])):
			if matrice[i][j] != matrice[j][i] * -1:
				return False
	return True