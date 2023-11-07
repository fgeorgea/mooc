
def	nouveaux_heros(src, dst):
	first_file = open(src)
	original_text = first_file.readlines()
	final_text = open(dst, "w")
	for line in original_text:
		line = line.replace("Paul", "Tom")
		line = line.replace("Pierre", "Paul")
		line = line.replace("Jacqueline", "Mathilde")
		final_text.write(line)
	first_file.close()
	final_text.close()

nouveaux_heros("test.txt", "final.txt")



string = "felix mange"

string = string.replace("felix", "gaspard")
print(string)