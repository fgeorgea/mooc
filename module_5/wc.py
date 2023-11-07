def	count_words(string):
	length = len(string)
	i = 0
	wc = 0
	while i < length:
		while i < length and not string[i].isalnum():
			i += 1
		if i < length and string[i].isalnum():
			wc += 1
		while i < length and string[i].isalnum():
			i += 1
	return wc


def	wc(file_name):
	file = open(file_name)
	nbr_words = 0
	nbr_char = 0
	nbr_lines = 0
	lines = file.readlines()
	nbr_lines = len(lines)
	for line in lines:
		line = line.replace("\n", " ")
		nbr_char += len(line)
	for line in lines:
		nbr_words += count_words(line)
	file.close()
	return nbr_char, nbr_words, nbr_lines


values = wc("test.txt")
print(values)