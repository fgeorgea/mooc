def	print_mat(matrice):
	if len(matrice) == 0:
		print()
	for row in matrice:
		for elem in row:
			print(elem, end=" ")
		print()

print_mat([['H','E','L','L','O'],['W','O','R','L','D']])