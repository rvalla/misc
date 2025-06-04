#Boolean evaluation of integers and strings...
import time as tm
import random as rd

def create_lists(loop_size):
	i_list = []
	s_list = []
	for n in range(loop_size):
		number = rd.randint(0,1000)
		i_list.append(number)
		s_list.append(str(number))
	return i_list, s_list

def formatTime(time):
	ms = ""
	minutes = time // 60
	seconds = time - minutes * 60
	seconds = round(seconds, 2)
	ms = "{:02d}".format(int(minutes))
	ms += ":"
	ms += "{:05.2f}".format(seconds)
	return ms

def getWorkingTime(start, end):
	time = end - start
	formatedTime = formatTime(time)
	return formatedTime

def testing(loops_count, loop_size):
	i_list, s_list = create_lists(loop_size)
	start_time = tm.time()
	working_time = None
	checks = 0
	for l in range(loops_count):
		number = rd.randint(0,1000)
		for n in i_list:
			if (n == number):
				checks += 1
	working_time = tm.time()
	print("-- Comparamos números enteros... ", end="\n")
	print("-- Realicé " + str(loops_count) + " búsquedas de un número al azar...", end="\n")
	print("-- Conté: " + str(checks) + " apariciones...", end="\n")
	print("-- Me tomó: ", end=" ")
	print(getWorkingTime(start_time, working_time), end="\n\n")
	start_time = tm.time()
	checks = 0
	for l in range(loops_count):
		number = str(rd.randint(0,1000))
		for n in s_list:
			if (n == number):
				checks += 1
	working_time = tm.time()
	print("-- Comparamos números enteros como cadenas de caracteres... ", end="\n")
	print("-- Realicé " + str(loops_count) + " búsquedas de un número al azar...", end="\n")
	print("-- Conté: " + str(checks) + " apariciones...", end="\n")
	print("-- Me tomó: ", end=" ")
	print(getWorkingTime(start_time, working_time), end="\n\n")
	start_time = tm.time()
	checks = 0
	for l in range(loops_count):
		number = rd.randint(0,1000)
		for n in s_list:
			if (int(n) == number):
				checks += 1
	working_time = tm.time()
	print("-- Comparamos números enteros después de transformar una cadenas de caractere... ", end="\n")
	print("-- Realicé " + str(loops_count) + " búsquedas de un número al azar...", end="\n")
	print("-- Conté: " + str(checks) + " apariciones...", end="\n")
	print("-- Me tomó: ", end=" ")
	print(getWorkingTime(start_time, working_time), end="\n\n")
