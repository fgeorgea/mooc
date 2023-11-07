import math

def	distance_points(p1, p2):
	x = (p1[0] - p2[0]) ** 2
	y = (p1[1] - p2[1]) ** 2
	dist = math.sqrt(x + y)
	return (dist)

def	longueur(*points):
	lst_len = len(points)
	dist = 0
	i = 0
	while i < lst_len - 1:
		dist += distance_points(points[i], points[i + 1])
		i += 1
	return (dist)