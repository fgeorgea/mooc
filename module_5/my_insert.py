def	my_insert(lst, elem):
	i = 1
	cpy = lst.copy()
	if len(cpy) == 0 or type(elem) != int:
		return
	if elem < cpy[0]:
		cpy.insert(0, elem)
	while i < len(cpy):
		if elem > cpy[i - 1] and elem < cpy[i]:
			cpy.insert(i, elem)
		i += 1
	if elem > cpy[i - 1]:
		cpy.insert(i, elem)
	return cpy

#lst = [1, 5, 78]
#res = my_insert(lst, 80)
#print(res)
#print(lst)