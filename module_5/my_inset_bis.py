def	my_insert(lst, elem):
	i = 1
	if len(lst) == 0:
		return
	assert type(elem) == int
	if elem < lst[0]:
		lst.insert(0, elem)
	while i < len(lst):
		if elem > lst[i - 1] and elem < lst[i]:
			lst.insert(i, elem)
		i += 1
	if elem > lst[i - 1]:
		lst.insert(i, elem)

lst = [1, 5, 78]
res = my_insert(lst, 1)
print(res)
#print(lst)