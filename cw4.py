#zad1 
napis = """k1:w1 
k2:w2""" 
print napis 
slownik1 = {} 
for x in napis.split('\n'): 
	z_p = x.split(':') 
	slownik1[z_p[0]] = z_p[1] 
print slownik1 

#zad2 
import sys 
nap = "" 
with open(sys.argv[1], "r") as f: 
	nap = f.read() 
slownik2 = {} 
for i in nap.split('\n'): 
	z_p1 = i.split(':') 
	slownik2[z_p1[0]] = z_p1[1] 
print slownik2


#zad3
import sys
slownik = {}
with open(sys.argv[1], "r") as f:
	for x in f:
		for el in x.split():
			if(el in slownik):
				slownik[el]+=1
			else:
				slownik[el] = 1
			
print slownik