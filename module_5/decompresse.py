def	decompresse(list):
	res = []
	for elem in list:
		for i in range(elem[0]):
			res.append(elem[1])
	return res

test = [(1, "He"), (2, "l"), (1, "o")]
res = decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
print(res)
