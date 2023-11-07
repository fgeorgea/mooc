def	liste_des_mots(file_name):
	file = open(file_name)
	text = file.readlines()
	array = []
	subarray = []
	for line in text:
		line = line.replace(",", " ")
		line = line.replace("\n", " ")
		line = line.replace("\t", " ")
		line = line.replace("-", " ")
		line = line.replace("'", " ")
		line = line.replace("\"", " ")
		line = line.replace("?", " ")
		line = line.replace("!", " ")
		line = line.replace(";", " ")
		line = line.replace(":", " ")
		line = line.replace(".", " ")
		line = line.replace(",", " ")
		line = line.replace("*", " ")
		line = line.replace("=", " ")
		line = line.replace("(", " ")
		line = line.replace(")", " ")
		line = line.replace("0", " ")
		line = line.replace("1", " ")
		line = line.replace("2", " ")
		line = line.replace("3", " ")
		line = line.replace("4", " ")
		line = line.replace("5", " ")
		line = line.replace("6", " ")
		line = line.replace("7", " ")
		line = line.replace("8", " ")
		line = line.replace("9", " ")
		subarray = line.split(" ")
		for elem in subarray:
			array.append(elem)
	new = []
	for line in array:
		if line.lower() not in new and len(line) > 0:
			new.append(line.lower())
		else:
			print(line)
	new.sort()
	file.close()
	return new



array = liste_des_mots("test.txt")
print(array)