def	transcription_clavier(src):
	str = src
	i = 0
	strlen = len(str)
	while i < strlen:
		if str[i] == '%':
			str = str[:i] + 'M' + str[i + 1:]
		i += 1
	return (str)