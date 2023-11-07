def	find_char_pos(lst, pos, elem):
	i = 0
	while i < pos:
		if lst[i] == elem:
			return True
		i += 1
	return False

def	dupliques(lst):
	i = 0
	lstsize = len(lst)
	while i < lstsize:
		if find_char_pos(lst, i, lst[i]):
			return True
		i += 1
	return False

#res = dupliques('abcda')
#print(res)