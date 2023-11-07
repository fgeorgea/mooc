

def	find_intersection(str1, str2):
	result = ""
	i = 0
	while i < len(str1):
		if str1[i] == str2[0]:
			break
		i += 1
	j = 0
	while (j < len(str2) or j < len(str1)) and str1[i + j] == str2[j]:
		result = result + str2[j]
		j +=1 
	return result



def	intersection(str1, str2):
	intersections = []
	intersections.append(find_intersection(str1, str2))
	intersections.append(find_intersection(str2, str1))
	if len(intersections[0]) > len(intersections[1]):
		return (intersections[0])
	return intersections[1]


print(intersection("programme", "agrammaire"))