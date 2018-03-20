#zad1
from math import sqrt 
class Zespolona:
  r = None
  i = None
  
  def __init__(self, re, im):
    self.r = re
    self.i = im
  def wypisz(self):
	  if self.r == 0 and self.i >= 0 :
		  print("%si" %(self.i))
	  elif self.r == 0 and self.i < 0 :
		  print ("%si" %(self.i))
	  elif self.r > 0 and self.i < 0:
		  print("%s+%si" %(self.r, self.i))
	  else:
		  print("%s+%si" %(self.r, self.i))

  def __add__(self, other):
	  return Zespolona(self.r + other.r, self.i + other.i)
		
  def __sub__(self, other):
	  return Zespolona(self.r - other.r, self.i - other.i)
		
  def __mul__(self, other):
	  return Zespolona(self.r * other.r - self.i *other.i, self.i * other.r + self.r * other.i)
		
  def __truediv__(self, other):
	  rz, ur, rz2, ur2 = self.r, self.i, other.r, other.i 
	  r = float(rz2**2 + ur2**2)
	  return Zespolona((rz*rz2+ur*ur2)/r, (ur*rz2 - rz*ur2)/r)

  def __abs__(self):
	  return sqrt(self.r**2 + self.i**2)
		
  def __setattr__(self,name,value): 
    return object.__setattr__(self, name, value) 

  def modul(self): 
    return sqrt(self.r**2 + self.i**2) 

  def __lt__(self,other): 
    return self.modul() < other.modul() 

  def __le__(self,other): 
    return self.modul() <= other.modul() 

  def __eq__(self,other): 
    return self.modul() == other.modul() 

  def __ne__(self,other): 
    return self.modul() != other.modul() 

  def __gt__(self,other): 
    return self.modul() > other.modul() 

  def __ge__(self,other): 
    return self.modul() >= other.modul() 
    
print(Zespolona(2,3).wypisz())
z1 = Zespolona(5,6)
z2 = Zespolona(3,4)
print((z1+z2).wypisz())
print((z1-z2).wypisz())
print((z1*z2).wypisz())
print((z1 /z2).wypisz())

#zad2
from math import sqrt 
from math import pow 

class Punkt2D(object):
	def __init__(self, x,y):
		self.x = x
		self.y = y
	def odl(self, other):
		return sqrt( pow(self.x - other.x,2) + pow(self.y - other.y,2))

class Punkt3D(Punkt2D):
	z = None
	def __init__(self, x, y,z):
		super(Punkt3D, self).__init__(x,y)
		self.z = z
	def odl(self, p3d):
		return sqrt( pow(self.z - p3d.z,2) + pow(super(Punkt3D, self).odl(p3d),2))


p1 = Punkt3D(1,8,6)
p2 = Punkt3D(1,2,3)

print(p1.odl(p2))

#zad3
class Kolo:
  __rozmiar = None
  __rodzaj = None
  def zamienKolo(self):
    print('kolo zostalo zamienione')
  def setChar(self, rozmiar, rodzaj):
    self.__rozmiar = rozmiar
    self.__rodzaj = rodzaj
  
class SkrzyniaBieg?w:
  __typ = None
  __il_biegow = None
  def ustawBieg(self):
    print('bieg ustawiony')
  def settChar(self, typ, il_biegow):
    self.__typ = typ
    self.__il_biegow = il_biegow
    
class Silnik:
  __pojemnosc = None
  __moc = None
  def odpal(self):
    print('silnik odpalony')
  def setttChar(self, pojemnosc, moc):
    self.__pojemnosc = pojemnosc
    self.__moc = moc

class Samochod(Kolo, Silnik, SkrzyniaBieg?w):
  __kolor = None
  __marka = None
  def odpal_silnik(self):
    super(Samochod, self).odpal()
  def ustaw_bieg(self):
    super(Samochod, self).ustawBieg()
  def zamien_kolo(self):
    super(Samochod, self).zamienKolo()
  def otworz_bagaznik(self):
    print('bagaznik zostal otwarty')
  def otworz_okno(self):
    print('okno zostalo otwarte')
  def hamuj(self):
    print('samochod zalamowal')
  
  
samochod = Samochod()
samochod.odpal_silnik()
samochod.ustaw_bieg()
samochod.zamien_kolo() 
