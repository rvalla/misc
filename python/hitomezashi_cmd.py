#Deciding if a symbol is a vowel...
def is_vowel(symbol):
	offset = 1
	if symbol in ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]:
		offset = 0
	return offset
	
#Calculating where are the stiches...
def hitomezashi_matrices(word_a, word_b):
	
	#We check our sizes...
	grid_a = len(word_a)
	grid_b = len(word_b)

	#Here we have two matrices to save the color of cells and two matrices to control future average calculation...
	row_matrix = [[0 for i in range(grid_a)] for i in range(grid_b)]
	col_matrix = [[0 for i in range(grid_a)] for i in range(grid_b)]
	
	#We use the first word to decide vertical pattern...
	for i in range(grid_a):
		is_v = is_vowel(word_a[i])
		for r in range(grid_b//2):
			row_matrix[2*r+is_v][i] = 1

	#We use the second word to decide horizontal pattern...
	for i in range(grid_b):
		is_v = is_vowel(word_b[i])
		for c in range(grid_a//2):
			col_matrix[i][2*c+is_v] = 1

	return row_matrix, col_matrix

def write_hitomezashi(row_matrix, col_matrix, x, y):
	print("", end="\n\n")
	for r in range(len(row_matrix)):
		row = ""
		for c in range(len(col_matrix[0])):
			if col_matrix[r][c] == 1:
				row += x
			else:
				row += " "
			if row_matrix[r][c] == 1:
				row += y
			else:
				row += " "
		print(row, end="\n")
	print("", end="\n\n")

while True:
	print("Hello, let's create a Hitomezashi pattern...", end="\n")
	print("I will need two words...", end="\n")

	#We get our words...
	line = input()
	if not line == "exit":
		words = line.split(" ")
		#try:
		row_matrix, col_matrix = hitomezashi_matrices(words[0], words[1])
		write_hitomezashi(row_matrix, col_matrix, "|", "_")
		#except:
		#	print("I need two words separated by one space...", end="\n")
	else:
		break
