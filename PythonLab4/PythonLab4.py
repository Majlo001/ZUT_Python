import collections as c
import random

#osoba = c.namedtuple('osoba',['imie','nazwisko','wiek'])
#osoba1 = osoba(imie='Jan',nazwisko='Kowalski',wiek=38)
#print(osoba1.imie)


#Zad 1
def analizujProstokat(wsp1, wsp2):
    a1 = abs(wsp1[0] - wsp2[0])
    a2 = abs(wsp1[1] - wsp2[1])
    obw = 2*a1 + 2*a2 
    pp = a1*a2
    print("Obwód:", obw, ", pole powierzchni", pp)

analizujProstokat([12,23], [44,27])


#Zad 2
prostokat = c.namedtuple('prostokat',['wsp1','wsp2'])
prostokat1 = prostokat(wsp1=[12,23], wsp2=[44,27])


def analizujProstokat(prostokat):
    a1 = abs(prostokat.wsp1[0] - prostokat.wsp2[0])
    a2 = abs(prostokat.wsp1[1] - prostokat.wsp2[1])
    obw = 2*a1 + 2*a2 
    pp = a1*a2
    print("Obwód:", obw, ", pole powierzchni", pp)

analizujProstokat(prostokat1)

#Zad 3
lista = list(range(1,1001, 2))
#print(lista)


#Zad 4
lista2 = [i for i in range(1,11)]
print(lista2)
lista3 = lista2.copy()
lista3[0] = 99

print("Lista 2:", lista2)
print("Lista 3:", lista3)


#Zad 5
lista5_1 = [random.randint(1,999) for i in range(0,20)]
lista5_2 = [random.random() for i in range(0,20)]

lista5_1 += lista5_2

print(random.sample(lista5_1,3))

#Zad 6
def Levenshtein(slowo1, slowo2):
    x = 0
    lnegth = 0
    
    x += abs(len(slowo1) - len(slowo2))

    if len(slowo1) > len(slowo2):
        lenght = len(slowo2)
    else:
        lenght = len(slowo1)

    for i in range(0, lenght):
        if (slowo1[i] != slowo2[i]):
            x += 1

    return x

print("Odległość między słowami:",Levenshtein('kot', 'kocioł'))