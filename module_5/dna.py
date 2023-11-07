def	est_adn(str):
	i = 0
	size = len(str)
	if size == 0:
		return False
	while i < size:
		if str[i] != 'A' and str[i] != 'C' and str[i] != 'G' and str[i] != 'T':
			return False
		i += 1
	return True