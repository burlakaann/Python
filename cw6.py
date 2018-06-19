#!/usr/bin/env
from math import sqrt
def sqrtt(x):
	try:
		result = sqrt(x)
	except (ValueError, ArithmeticError ,TypeError) as ex:
		print("wyjatek")
		print (ex)
	else:
		print ("brak wyjatku")
		return result
	finally:		
		print ("koniec funkcji")
print(sqrtt(-1))