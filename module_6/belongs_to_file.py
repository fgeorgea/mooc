def	belongs_to_file(word, file_name):
	file = open(file_name)
	list = file.readlines()
	i = 0
	while i < len(list):
		list[i] = list[i].replace('\n', '')
		print(list[i].replace('\n', ''))
		i += 1
	file.close()
	if word in list:
		return True
	return False

res = belongs_to_file("felix", "text.txt")
print(res)