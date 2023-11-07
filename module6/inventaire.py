def	inventaire(offres, objects):
	names = set()
	for object in objects:
		if object in offres:
			names.add(offres[object])
	return names



offres = {"lit":"oscar", "bague":"felix", "orange":"isabelle"}
objects = ["lit", "orange"]

res = inventaire(offres, objects)
print(res)

