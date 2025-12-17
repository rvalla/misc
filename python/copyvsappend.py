#Testing ways to copy short lists...
import time as tm
import random as rd

#Here I compare two ways to copy sublists in nested lists...

def with_copy_method(the_list):
	return the_list.copy()

def with_append_method(the_list):
	new_list = []
	for e in the_list:
		new_list.append(e)
	return new_list

def random_sublist(the_list):
	return rd.choice(the_list)

def new_random_nested_list():
	the_list = []
	links = rd.randint(10, 20)
	for l in range(links):
		sublist = []
		elements = rd.randint(1,5)
		for e in range(elements):
			sublist.append(rd.randint(0,11))
		the_list.append(sublist)
	return the_list

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


#We now can run our test...
def run_test(*, times=1000, loop_size=1000):
	print("Ready to start a new copy vs append test...", end="\n")
	print("I will run the test " + str(times) + " times, with " + str(loop_size) + " iterations each...", end="\n")
	nested_list = new_random_nested_list()
	print("First I will use the copy() method to create new sublists...", end="\n\n")
	start_time = tm.time()
	for t in range(times):
		for i in range(loop_size):
			test = []
			for l in nested_list:
				test.append(with_copy_method(random_sublist(nested_list)))
	elapsed_time = get_working_time(start_time, tm.time())
	print("I finished the copy test!", end="\n")
	print("I took me " + elapsed_time, end="\n\n")
	print("Second I will use the classic loop calling append() for each element......", end="\n\n")
	start_time = tm.time()
	for t in range(times):
		for i in range(loop_size):
			test = []
			for l in nested_list:
				test.append(with_append_method(random_sublist(nested_list)))
	elapsed_time = get_working_time(start_time, tm.time())
	print("I finished the append test!", end="\n")
	print("I took me " + elapsed_time, end="\n\n")
	print("That's all!", end="\n")

run_test()
