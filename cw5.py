#encoding: utf8 
#1
import sys 
nap = "" 
width = input()
with open(sys.argv[1], "r") as f: 
	nap = f.read() 
for i in nap.split():
	print i[:width]
	print i[width:]

#for index in range(0,len(nap), width):
	#print (nap[index:index+width].center(width))
#2
nap = "" 
width = input()
with open(sys.argv[1], "r") as f: 
	nap = f.read() 

print(nap.strip().center(width)) 


