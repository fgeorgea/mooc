def	top_3_candidats(moyennes):
	candidats = {}
	for moyenne in moyennes:
		candidats[moyennes[moyenne]] = moyenne
	res = []
	for i in range(3):
		tmp = max(candidats)
		res.append(candidats[tmp])
		del candidats[tmp]
	return res[0], res[1], res[2]