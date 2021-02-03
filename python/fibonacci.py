#Functions to obtain Fibonacci related numbers
def fibo(n):
	if n <= 1:
		return 1
	else:
		return (fibo(n-1) + fibo(n-2))

def fiboSucession(n):
	l = []
	for t in range(n):
		l.append(fibo(t))
	return l

def fiboSum(n):
	s = 0
	for t in range(n):
		s += fibo(t)
	return s
