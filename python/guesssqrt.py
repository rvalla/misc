#Guessing square roots...

import random

def randomNumber():
	a = random.randint(1,100)
	return a

def askNumber():
	return int(input("-- Ingrese su propuesta de resultado: "))

def isCorrect(n, guess):
	if n == guess * guess:
		return True
	else:
		return False

def play(n):
	won = False
	a = askNumber()
	if isCorrect(n, a):
		print("-- ¡Faaaa! Fantástico... Es correcto...", end="\n")
		print("-- Paraparabaaaaam, pa pam, pa pam...", end="\n")
		print("-- ¡Sí! Es la música de feliz domingo...", end="\n")
		print("", end="\n")
		won = True
	else:
		print("-- Es incorrecto...", end="\n")
	if a == 0:
		exit()
	return won

def theMatch():
	n = randomNumber()
	print("-------------------------", end="\n")
	print("", end="\n")
	print("-- ¿Te animás a calcular una raíz cuadrada?", end="\n")
	print("-- El número es: " + str(n * n), end="\n")
	t = 0
	while t < 3:
		if play(n * n):
			break
		else:
			t += 1
			if t == 3:
				print("-- Era " + str(n), end="\n")
				print("", end="\n")

def runChallenge():
	count = 0
	while count < 100:
		theMatch()
		count += 1
	print("-- ¡Fue suficiente!", end="\n")

runChallenge()
print("Si querés jugá de nuevo...", end="\n")