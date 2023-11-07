def anagrammes(str1, str2):
	if len(str1) != len(str2):
		return False
	i = 0
	size = len(str1)
	while i < size:
		j = 0
		while j < len(str2):
			if str1[i] == str2[j]:
				str2 = str2[:j] + str2[j+1:]
			j += 1
		i += 1
	if len(str2) == 0:
		return True
	return False

res = anagrammes('bonjour', 'bonjour')

print(res)