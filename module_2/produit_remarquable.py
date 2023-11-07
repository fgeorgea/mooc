def print_diff(str1, str2):
	strlen = len(str1)
	i = 0
	res = ""
	while i < strlen:
		if str1[i] != str2[i] and "^" not in res:
			res = res + "^"
		else:
			res = res + "-" 
		i += 1
	print(res, "|", res)
	



def	diff(lst1, lst2):
	lstlen = len(lst1)
	if lstlen <= 0:
		return None
	strlen = len(lst1[0])
	for i in range(lstlen):
		print(lst1[i], "|", lst2[i])
		print_diff(lst1[i], lst2[i])

lst1 = ['abcd', 'abcd', 'abcd', 'abcd']
lst2 = ['abcd', 'abdd', 'xxxx', 'akcd']

diff(lst1, lst2)