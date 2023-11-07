import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2


s = int(input())
random.seed(s)

def	bat(player_1, player_2):
	if (player_1 == PIERRE and player_2 == CISEAUX) or (player_1 == FEUILLE and player_2 == PIERRE) or (player_1 == CISEAUX and player_2 == FEUILLE):
		return 0
	elif (player_1 == player_2):
		return 1
	return 2

score = 0
for i in range(5):
	pc_choice = random.randint(0, 2)
	player_choice = int(input())
	win = bat(player_choice, pc_choice)
	if pc_choice == 0:
		print("Pierre", end="")
	elif pc_choice == 1:
		print("Feuille", end="")
	else:
		print("Ciseaux", end="")
	if win == 0:
		score += 1
		print(" est battu par ", end="")
	elif win == 1:
		print(" annule ", end="")
	if win == 2:
		score -= 1
		print(" bat ", end="")
	if player_choice == 0:
		print("Pierre", end="")
	elif player_choice == 1:
		print("Feuille", end="")
	else:
		print("Ciseaux", end="")
	print(" :", score)

if (score > 0):
	print("Gagné")
elif (score == 0):
	print("Nul")
else:
	print("Perdu")