def	f(elem):
	if type(elem) == int:
		return True
	return False

def	my_filter(lst, f):
	res = []
	for elem in lst:
		if f(elem):
			res.append(elem)
	return res


print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0))