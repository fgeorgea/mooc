def	distance_mots(str1, str2):
	i = 0
	length = 0
	if len(str1) != len(str2):
		if len(str1) > len(str2):
			return len(str1)
		else:
			return len(str2)
	while i < len(str1):
		if str1[i] != str2[i]:
			length += 1
		i += 1
	return length

def	correcteur(str, lst):
	i = 1
	index = 0
	length = distance_mots(str, lst[0])
	while i < len(lst):
		if distance_mots(str, lst[i]) < length:
			index = i
			length = distance_mots(str, lst[i])
		i += 1
	return lst[index]


res = correcteur('reyter', ['angle', 'armoire', 'banc', 'bureau', 'carreau', 'chaise', 'dossier', 'escalier', 'lavabo', 'lecture', 'marche', 'matelas', 'maternelle', 'meuble', 'mousse', 'peluche', 'placard', 'plafond', 'portemanteau', 'poubelle', 'radiateur', 'rampe', 'rideau', 'robinet', 'savon', 'serrure', 'serviette', 'sieste', 'silence', 'sommeil', 'sonnette', 'sortie', 'table', 'tableau', 'tabouret', 'tapis', 'tiroir', 'toilette', 'aller', 'amener', 'apporter', 'appuyer', 'attendre', 'dormir', 'emmener', 'endormir', 'ennuyer', 'entrer', 'fermer', 'frapper', 'installer', 'lever', 'ouvrir', 'presser', 'rentrer', 'reposer', 'rester', 'sonner', 'tricher', 'venir', 'bonjour', 'crayon', 'stylo', 'pointe', 'mine', 'dessin', 'coloriage', 'rayure', 'peinture', 'pinceau', 'couleur', 'craie', 'papier', 'feuille', 'carnet', 'carton', 'ciseaux', 'découpage', 'pliage', 'pli', 'colle', 'affaire', 'caisse', 'trousse', 'cartable', 'jouet', 'jeu', 'pion', 'domino', 'puzzle', 'cube', 'perle', 'chose', 'forme', 'rond', 'tampon', 'livre', 'histoire', 'image', 'album', 'dictionnaire', 'magazine', 'catalogue', 'page', 'enveloppe', 'carte', 'affiche', 'alphabet', 'appareil', 'cassette', 'chanson', 'chiffre', 'contraire', 'doigt', 'film', 'instrument', 'intrus', 'lettre', 'main', 'micro', 'musique', 'nom', 'nombre', 'orchestre', 'ordinateur', 'photo', 'pouce', 'question', 'radio', 'sens', 'tambour', 'trompette', 'voix', 'xylophone']) 
print(res)