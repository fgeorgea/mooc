def	store_email(liste_mails):
	dic = {}
	for mail in liste_mails:
		tmp = mail.split("@")
		if tmp[1] not in dic:
			dic[tmp[1]] = []
		dic[tmp[1]].append(tmp[0])
		dic[tmp[1]].sort()
	return dic