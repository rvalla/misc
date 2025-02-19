#Testing ways to check valid email addresses
import time as tm

def testPeriod(domain):
	dotFound = False
	for char in domain[::-1]:
		if char == ".":
			dotFound = True
			break
	return dotFound

def testDomain(mail):
	address = mail.split("@")
	looksGood = False
	if len(address) == 2:
		looksGood = testPeriod(address[1])
	return looksGood

def checkLoop(mail):
	hasPeriod = False
	hasA = False
	for char in mail[::-1]:
		if char == "@":
			hasA = True
		elif char == ".":
			hasPeriod = True
	if hasPeriod and hasA:
		return True
	else:
		return False

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

def testing(loopsCount, loopsSize, mail):
	startTime = tm.time()
	workingTime = None
	checks = 0
	for l in range(loopsCount):
		for ll in range(loopsSize):
			if (testDomain(mail)):
				checks += 1
	workingTime = tm.time()
	print("-- Probamos con split... ", end="\n")
	print("-- Revisé la misma dirección " + str(loopsCount * loopsSize) + " veces...", end="\n")
	print("-- Conté: " + str(checks) + " direcciones válidas...", end="\n")
	print("-- Me tomó: ", end=" ")
	print(getWorkingTime(startTime, workingTime), end="\n")
	startTime = tm.time()
	checks = 0
	for l in range(loopsCount):
		for ll in range(loopsSize):
			if (checkLoop(mail)):
				checks += 1
	workingTime = tm.time()
	print("-- Probamos recorriendo la dirección... ", end="\n")
	print("-- Revisé la misma dirección " + str(loopsCount * loopsSize) + " veces...", end="\n")
	print("-- Conté: " + str(checks) + " direcciones válidas...", end="\n")
	print("-- Me tomó: ", end=" ")
	print(getWorkingTime(startTime, workingTime), end="\n")
