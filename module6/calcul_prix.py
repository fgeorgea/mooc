def	calcul_prix(produits, catalogue):
	price = 0
	for product in produits:
		if product in catalogue:
			price += produits[product] * catalogue[product]
	return price