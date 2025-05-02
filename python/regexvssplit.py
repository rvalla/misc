#Testing ways to evaluate strings...
import re
import time as tm
import random as rd

#Here I compare two ways to check if a hashtag is present
#in a string to decide which to use in another project

#First we create a big list of random sentences... 
standard_words = ["un", "la", "el", "día", "mañana", "tarde", "soleada", "nublada", "urgencia"
								"negativo", "afirmativo", "estadio", "teatro", "curva", "recta", "dilatación"]
hash_words = ["#importante", "#feriados", "#abordaje", "#actos", "#campamento", "#boletines"]

def create_string(w_count, w_set):
	s = ""
	for w in range(w_count):
		s += rd.choice(w_set)
		s += " "
	return s

def create_line():
	line = create_string(rd.randint(1,20), standard_words)
	line += create_string(rd.randint(1,5), hash_words)
	line += "\n"
	return line

def format_time(time):
	ms = ""
	minutes = time // 60
	seconds = time - minutes * 60
	seconds = round(seconds, 2)
	ms = "{:02d}".format(int(minutes))
	ms += ":"
	ms += "{:06.3f}".format(seconds)
	return ms

def get_working_time(start, end):
	time = end - start
	formatedTime = format_time(time)
	return formatedTime

#We can search a hashtag splitting our string...
def split_test(line, hashtag):
	tokens = line.split("#")
	is_hashtag = False
	for t in range(1,len(tokens)):
		if tokens[t].replace(" ","").replace("\n","") == hashtag:
			is_hashtag = True
			break
	return is_hashtag

#We can use regex match function...
def regex_match_test(line, hashtag):
	return bool(re.match(hashtag, line))

#Also we can use regex search function...
def regex_search_test(line, hashtag):
	return bool(re.search(hashtag, line))

#We create a file full of sentences...
def create_file(lines):
	with open("data/regexvssplit.txt", "w") as file:
		for l in range(lines):
			file.write(create_line())

#We now can run our test...
def run_test(*, new_file=False, lines=50000, hashtag="#importante"):
	print("Ready to start a new regex vs split test...", end="\n")
	if new_file:
		print("I am creating a new file full of sentences now...", end="\r")
		create_file(lines)
		print("New file full of senteces just created...        ", end="\n")
	split_tag = hashtag[1:]
	regex_tag = hashtag
	print("I will search for your hashtag <" + split_tag + "> in every line...")
	lines = open("data/regexvssplit.txt", "r").readlines()
	print("First I will split each line when a <#> character appears...", end="\n\n")
	matches = 0
	start_time = tm.time()
	for l in lines:
		if split_test(l, split_tag):
			matches += 1
	elapsed_time = get_working_time(start_time, tm.time())
	print("I finished the split test!", end="\n")
	print("I found " + str(matches) + " lines with your hashtag.", end="\n")
	print("I took me " + elapsed_time, end="\n\n")
	print("Second I will use the search function in regex module...", end="\n\n")
	matches = 0
	start_time = tm.time()
	for l in lines:
		if regex_search_test(l, regex_tag):
			matches += 1
	elapsed_time = get_working_time(start_time, tm.time())
	print("I finished the regex search test!", end="\n")
	print("I found " + str(matches) + " lines with your hashtag.", end="\n")
	print("I took me " + elapsed_time, end="\n\n")
	print("That's all!", end="\n")

run_test(new_file=True, lines=50000, hashtag="#feriados")
run_test(new_file=True, lines=1000, hashtag="#importante")
run_test()
