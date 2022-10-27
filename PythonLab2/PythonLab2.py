#import math as m
from math import *

#lista = ['wi',2,True,7.8,[-1,2]]


#print(lista)
#print(len(lista))
#print(lista[2])
#print(lista[-1])
#print(lista[1:4])
#print(lista[0:5:2])
#print(lista[::2])
#lista.append(-7.1)
#lista.insert(3,-1)
#del lista[2]
#print(lista)


#krotka = (False,3,7.8)
#print(krotka)
#a,b,c = krotka
#print(a,b,c)
#lista2 = list(krotka)
#print(lista2)


zad1 = [0,-2,1,7,3,4]
print(zad1)
print(zad1[::-1])


x = float(input("Podaj x: "))
y = float(input("Podaj y: "))
zad2 = e+log10((x*x)+1)*((x-1)/(cos(pow(y,3)-1)+6))
print(zad2)

# 2.8183362733213935
# -1.3367487551407415

liczba = int(input("Podaj liczbę: "))
if liczba%3==0:
    print("Podzielne przez 3")
elif liczba%3==1:
    print("Reszta 1")
else:
    print("Reszta 2")


#n = 2
#m = 8
#while n<=m:
#    print(n)
#    n += 2

#n = 2
#for i in range(n, m+1, 2):
#    print(i)


# Zad 3
print("\nZad 3")
x = float(input("Podaj wartość x: "))
y = float(input("Podaj wartość y: "))
c = int(input("Podaj wartość c: "))

if c == 1:
    print(x+y)
elif c == 2:
    print(x-y)
elif c == 3:
    print(x*y)
else:
    print(x/y)

# Zad 5
print("\nZad 5")
n = int(input("Podaj wysokość trójkąta: "))
for i in range(n):
    print("X"*(i+1))

# Zad 6
print("\nZad 6")
list6 = [[i for i in range(1,8,3)] for x in range(3)]
print(list6)

# Zad 7
n = int(input("Zad 8 | Podaj liczbę: "))
for i in range(2,n):
    isPrime = False
    if (n % i) == 0:



# Zad 8
n = int(input("Zad 8 | Podaj liczbę: "))
count = 0
for i in range(n+1):
    if str(i)[-1] == '3':
        count += i
        print(count)
    if i >= 14 and str(i)[-2:-1] == '14':
        count += i
        print(count)
print(count)