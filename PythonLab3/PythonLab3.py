from math import *

#def funkcja(imie, nazwisko="Nowak"):
#    print("Witaj",imie,nazwisko)


#funkcja("Adam","Adamiak")
#funkcja("Janusz")

#def fun(a,b=1,c=1):
#    suma = a+b+c
#    iloczyn = a*b*c
#    return (suma,iloczyn)

#w1,w2 = fun(5,6,7)
#print(w1,w2)
#w1,w2 = fun(99)
#print(w1,w2)
#w1,w2 = fun(a=99,b=65,c=8)
#w1,w2 = fun(a=9,c=7)
#w1,w2 = fun(3,c=7)

## Na to uważać
#def fun2(a=[]):
#    a.append(1)
#    print(a)
#fun2()
#fun2()
#print(a)

#f = lambda x:x**2-5
#print(f(5))


#Zad 1
def czas(sek):
    godz = int(sek/3600)
    sek -= godz*3600
    min = int(sek/60)
    sek -= min*60
    return str(godz)+" godzin, "+str(min)+" minut, "+str(sek)+" sekund."

print(czas(1900))


#Zad 2
def funkcja2(x,n=10,k=2):
    return log((x**x+5),n)*(k+1)*x

print(funkcja2(x=2,k=7))


#Zad 3
f3 = lambda x : sin(x+1)+cos(pow(x,4))

list_f3 = [f3(x) for x in range(-5,2,1)]
print(list_f3)


#
#def f(*args):
#    print(args)
#    for i in args:
#        print(i,"^2= ",i**2, sep="")
#f(5,6,7,-3,8.77)

#def f2(typ, **kwargs):
#    print(typ)
#    print(kwargs)
#    print(type(kwargs))
#    print(kwargs["a"])
#    if typ == 'trojkat':
#        print(kwargs['a']*kwargs['h']*0.5)
#    elif typ == 'kwadrat':
#        print(kwargs['a']**2)
#f2("trojkat",a=7,h=4)

#def rozpakuj(a,b,c,d):
#    print(a,b,c,d)
#
#l = [1,2,3,4]
#rozpakuj(*l)
#s = {'a':7,'b':9,'c':4,'d':6}
#rozpakuj(**s)
#

#Zad 4
def funkcja4(*args):
    suma = 0
    for i in args:
        suma += i
    return suma

print(funkcja4(1,2,3,4,5,6,7,8,9))


#Zad 5
def funkcja5(typ, **kwargs):
    if typ == "kula":
        print((4/3) * pi * pow(kwargs['r'],3))
    elif typ == "prostopadloscian":
        print(kwargs['a']*kwargs['b']*kwargs['h'])
    elif typ == "walec":
        print(pi * pow(kwargs['r'],2) * kwargs['h'])
    elif typ == "stozek":
        print((1/3) * pi * pow(kwargs['r'],2) * kwargs['h'])
    else:
        print("Brak wskazanego typu")


#Zad 6
def rozpakuj(a,b,c,d):
    return (a,b,c,d)

l = [1,2,3,4]
a,b,c,d = rozpakuj(*l)
print(a,b,c,d)

a,b,c,d = [*l]
print(a,b,c,d)


#Zad 7
def silnia(n):
    wynik = 1
    for i in range(2,n):
        wynik = wynik*i
    return n*wynik

print(silnia(5))

def silnia_rek(n):
    if n < 2:
        return 1
    return n*silnia_rek(n-1)

print(silnia_rek(5))


#Zad 8
def tribonacci(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

print(tribonacci(10))