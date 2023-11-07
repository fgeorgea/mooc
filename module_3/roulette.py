guess_nbr = int(input())
real_nbr = int(input())

if guess_nbr >= 0 and guess_nbr <= 12 and guess_nbr == real_nbr:
	print("120")
elif (guess_nbr == 13) and ((real_nbr % 2) == 0):
	print("20")
elif (guess_nbr == 14) and ((real_nbr % 2) != 0):
	print("20")
elif guess_nbr == 15 and real_nbr != 0:
	if real_nbr == 12 or ((real_nbr % 2) != 0 and real_nbr != 11):
		print("20")
	else:
		print("0")
elif guess_nbr == 16 and real_nbr != 0:
	if real_nbr == 11 or ((real_nbr % 2) == 0 and real_nbr != 12):
		print("20")
	else:
		print("0")
else:
	print("0")