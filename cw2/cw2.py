#zad1
napis = 'ala ma kota'
ls = [(slowo, len(slowo)) for slowo in napis.split()]
print (ls)

#zad2
n = int(input('podaj ilosc elementow'))
def fibonacci(n):
	fib1, fib2 = 0, 1
	for i in range(n):
		fib1, fib2 = fib2, fib1 + fib2
	yield fib1

fib = [x for x in fibonacci(n)]
print(fib)

#zad3
def f1(n):
	if n % 2 == 0:
		return True
	return False

def f2(f, n):
	lista = []
	for i in n:
		if(f(i)):
			lista.append(i)
	return lista

lst = []
for i in range(20):
	lst.append(i)

print(f2(f1, lst))

#zad4
from math import sqrt

from math import pow

import random 


krotka = () 

lista = [] 

res = [] 

point = (random.randint(0, 11),random.randint(0, 11)) 


print(point) 


for i in range(10): 
  
	krotka = (random.randint(0, 11),random.randint(0, 11)) 
  
	lista.append(krotka)


for i in range(9): 
  
	krotka = (round(sqrt( pow(lista[i][0] - point[0],2) + pow(lista[i][1] - point[1],2)),3),lista[i])
	print(krotka)
	res.append(krotka) 


res = sorted(res, key=lambda elem: elem[0]) 


print(res) 

#zad5
from fnmatch import fnmatch 

from os import listdir 


sciezka = input('Podaj sciezke ') 


sciezka = sciezka[:-1] 


rozsz = input('Podaj rozszerzenie') 


rozsz = '*.' + rozsz 


pliki = listdir(sciezka) 


def f( lista, rozsz ): 
  
	for i in lista: 
    
		if fnmatch(i, rozsz): 
      
			yield i 


lista = [x for x in f(pliki, rozsz)] 


print(pliki) 