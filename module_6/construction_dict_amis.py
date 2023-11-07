def	construction_dict_amis(amis):
	friends = {}
	for ami in amis:
		if ami[0] not in friends:
			friends[ami[0]] = set()
			friends[ami[0]].add(ami[1])
		if ami[0] in friends:
			friends[ami[0]].add(ami[1])
	for ami in amis:
		if ami[1] not in friends:
			friends[ami[1]] = set()
	return friends