
def	print_list(lst):
	i = 0
	lstlen = len(lst)
	while i < lstlen:
		print(lst[i], end="")
		if i < lstlen - 1:
			print(" + ", end="")
		i += 1

def	superdigit(str):
	digits = []
	for char in str:
		if char.isdigit():
			digits.append(int(char))
	if len(digits) == 0:
		print("Pas de chiffres !")
		return
	for digit in digits:
		print(digit, end="")
	tmp = 0
	while sum(digits) >= 10:
		print(" = ", end="")
		tmp = sum(digits)
		print_list(digits)
		digits = []
		while tmp / 10 > 0:
			digits.append(tmp % 10)
			tmp = tmp // 10
		digits.reverse()
	print(" = ", end="")
	print_list(digits)
	print(" =", sum(digits))

superdigit("akjsdfasjdfasdf")