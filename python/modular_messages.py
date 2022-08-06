import random as rd
import json as js

input = open("data/modules_input_ex.csv").readlines()[1:]
input_links = js.load(open("data/modules_links_ex.json"))
output = open("data/modules_output_ex.csv", "w")
links = [] #Here we store de possible message fragments (a 3d matrix)...
links_count = 4
levels = 3
conectors = [", ", ". ", " aunque ", ".\n"] #The size of this lists is links_count!
capital = [False, False, True, False]

for i in range(links_count): #Let's build the matrix...
	l = []
	for j in range(levels):
		l.append([])
	links.append(l)

for m in input_links:
	links[m["category"]][m["level"]].append(m["text"])

for i in input:
	text = i.split(";")
	output.write(text[0] + " " + text[1] + ";")
	message = text[0].split(" ")[0] + " "
	for j in range(links_count):
		if capital[j]:
			link = rd.choice(links[j][int(text[j+2])]).capitalize()
		else:
			link = rd.choice(links[j][int(text[j+2])])
		message += link
		message += conectors[j]
	output.write(message)

output.close()
