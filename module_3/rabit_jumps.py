current_pos = 0
jump = int(input())
nut_pos = int(input())
	
while True:
    current_pos = (current_pos + jump) % 100
    if current_pos == 0 or current_pos == nut_pos:
        break
    print(current_pos)

	    
if current_pos == 0:
    print(0)
    print("Pas trouvée")
else:
    print("Cible atteinte")