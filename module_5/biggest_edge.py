def	plus_grand_bord(src):
	max_size = len(src) - 1
	while max_size >= 1:
		tmp1 = src[:max_size]
		tmp2 = src[len(src) - max_size:]
		if src[:max_size] == src[len(src) - max_size:]:
			return src[:max_size]
		max_size -= 1
	return ""