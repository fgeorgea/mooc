nbr_elem = 0
sum = 0

while True:
    nbr = int(input())
    if nbr == -1:
        break
    sum += nbr
    nbr_elem += 1
    
print(sum / nbr_elem)