def	symetrise_amis(d):
	friends = {}
	for friend in d:
		if friend not in friends:
			friends[friend] = set()
		for little_friend in d[friend]:
			if little_friend not in friends:
				friends[little_friend] = set()
			friends[little_friend].add(friend)
			friends[friend].add(little_friend)
	for friend in friends:
		d[friend] = friends[friend]





d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d)
print(d)