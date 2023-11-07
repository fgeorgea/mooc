def	duree(start, end):
	hours = end[0] - start[0]
	if start[1] > end[1]:
		hours -= 1
	if hours <= 0:
		hours += 24
	minutes = end[1] - start[1]
	if minutes < 0:
		minutes += 60
	return hours, minutes