def	valeurs(dic):
	list = []
	for elem in dic:
		list.append(elem)
	list.sort()
	lst = []
	for elem in list:
		lst.append(dic[elem])
	return lst