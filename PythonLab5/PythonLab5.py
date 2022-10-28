#Słownik
slownik = {'klucz1':12, 'klucz2':32}
slownik['klucz1']
del slownik['klucz1']
slownik['klucz3'] = 44
slownik.keys()
slownik.values()
slownik.items()

'klucz1' in slownik
'klucz3' not in slownik

##Zbiór
#l = [2,55,6,7,7,4,4]
#zbior = set(l)
#print(zbior)

#A = {1,2,3}
#B = {2,4,6}

#print(A&B)
#print(A|B)
#print(A-B)
#print(A^B)

#binary = str(bin(ord('s')))+str(bin(ord('a')))+str(bin(ord('m')))
#c2ft
#print(binary)
#print(bin(ord('t')))
#dA==

#Zad 1
tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
tekst = tekst.lower()
tekst = tekst.replace('.','')
tekst = tekst.replace(',','')
tekst1 = tekst.split()
tekst2 = set(tekst1)

print("Ilość słów: przed -",len(tekst1)," po -",len(tekst2))


#Zad 2
A = {1,2,3,4,5}
B = {2,4,5}

A.issubset(B)
B.issubset(A)

print(A&B)
print(A|B)
print(A^B)
print((A|B)^B) #A.symmetric_difference(B) ?


#Zad 3
il_kartezjanski = []

for i in A:
	for j in B:
		il_kartezjanski.append([i,j])

print(il_kartezjanski)


#Zad 4
slownik_liczb = {0:'zero', 1:'jeden', 2:'dwa', 3:'trzy', 4:'cztery', 5:'pięć', 6:'sześć', 7:'siedem', 8:'osiem', 9:'dziewięć', 10:'dziesięć', 11:'jedenaście', 12:'dwanaście', 13:'trzynaście', 14:'czternaście', 15:'piętnaście', 16:'szesnaście', 17:'osiemnaście', 18:'dziewiętnaście', 20:'dwadzieścia', 30:'trzydzieści', 40:'czterdzieści', 50:'pięćdziesiąt', 60:'sześćdziesiąt', 70:'siedemdziesiąt', 80:'osiemdziesiąt', 90:'dziewięćdziesiąt'}

x = int(input("Podaj liczbę: "))

if x >= 0 and x < 21:
	print(slownik_liczb[x])
elif x >= 21 and x < 100:
	x = str(x)
	z1 = int(x[0] + '0')
	z2 = int(x[1])
	print(slownik_liczb[z1],slownik_liczb[z2])


#Zad 5 TODO



