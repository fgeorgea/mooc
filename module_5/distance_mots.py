def	distance_mots(str1, str2):
	i = 0
	length = 0
	while i < len(str1):
		if str1[i] != str2[i]:
			length += 1
		i += 1
	return length