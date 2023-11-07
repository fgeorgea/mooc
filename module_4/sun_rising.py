def	soleil_leve(rise, set, current):
	if rise == set and rise == 12:
		return False
	if rise == set and rise == 0:
		return True
	if current == rise:
		return True
	if current == set:
		return False
	if rise > set and (current < set or current > rise):
		return True
	elif set > rise and current < set and current > rise:
		return True
	else:
		return False