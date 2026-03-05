from math import sqrt
from scipy.integrate import quad

def fact(n):
	if n < 0:
		raise ValueError('Must be positive !')
	for i in range(1, n):
		n *= i
	return n

def roots(a, b, c):
	try:
		sq_delta = sqrt(b**2 - 4*a*c)
		sol_pos = (-b + sq_delta)/(2*a)
		sol_neg = (-b - sq_delta)/(2*a)
		return (sol_neg, sol_pos)
	except:
		print("Il n'y a pas de racine !")

def integrate(function, lower, upper):
	def fun(x):
		return eval(function,{"x":x})
	return quad(fun, lower, upper)[0]

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))