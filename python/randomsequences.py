import random as rd

#Rolling a dice
def diceroll(f):
	return rd.randint(1,f)

#A sequence of dice rolls
def dicerolls(n, f):
	l = []
	for r in range(n):
		l.append(diceroll(f))
	return l