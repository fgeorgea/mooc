def	acrostiche(file_name):
	res = ""
	file = open(file_name)
	lines = file.readlines()
	for line in lines:
		res = res + line[0]
	return res

print(acrostiche("test.txt"))