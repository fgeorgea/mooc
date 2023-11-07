def	substitue(message, abreviation):
	words = message.split(" ")
	i = 0
	while i < len(words):
		if words[i] in abreviation:
			words[i] = abreviation[words[i]]
		i += 1
	string = " ".join(words)
	return string