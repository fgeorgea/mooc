def	sort_dic(dic):
	list = []
	for elem in dic:
		list.append(elem)
	list.sort()
	dict = {}
	for elem in list:
		dict[elem] = dic[elem]
	return dict

def	compteur_lettres(text):
	i = 0
	dic = {}
	text = text.lower()
	while i < len(text):
		if text[i].isalpha() and (not text[i] in dic):
			dic[text[i]] = 1
		elif text[i] in dic:
			dic[text[i]] += 1
		i += 1
	letter = ord('a')
	while letter <= ord('z'):
		if not chr(letter) in dic:
			dic[chr(letter)] = 0
		letter += 1
	return sort_dic(dic)

res = compteur_lettres('aab')
print(res)
