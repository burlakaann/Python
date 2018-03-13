#zad1

a = input('podaj imie') 
a1 = input('podaj nazwisko')
b = input('podaj wiek') 

def pelnoletni(w): 
if(w > 17): 
return 'pelnoletni' 
else: 
return 'niepelnoletni' 

print('Czesc ',a, ' ', a1,' jestes ', pelnoletni(int (b)))

#zad2
def maximum(a ,b , c ): 
	if(a1 > b1): 
		if(a1 > c1): 
			print(a1) 
		else: 
			print(c1) 
	else: 
		if(b1 > c1): 
			print(b1) 
		else: 
			print(c1) 

print('podaj trzy liczby') 

a1= input() 
b1 = input() 
c1 = input() 

maximum(int(a1), int(b1), int(c1))

#zad3
for i in range(26): 
	print(chr(i+65),chr(i+97)) 


#zad4
from math import floor 

liczba = input('podaj co ile wyswietlac') 
n = floor(26 / int(liczba)) 
for i in range(n): 
	print(chr(i*int(liczba)+65),chr(i*int(liczba)+97)) 

#zad5

l = int(input('ile liczb?')) 
print(l) 
tab = [] 
for i in range(l): 
	tab.append(int(input())) 
tab.sort() 

print('podaj pszedzial\n') 
q1 = int(input('od elementu - ')) 
q2 = int(input('do elementu - ')) 

print(tab[q1:q2+1]) 

 