from collections import *


#
c = Counter("informatyka")
print(c)

c = deque("zut")
print(c)
c.append("t")
c.appendleft("!")
c.pop()
c.popleft()

s = defaultdict(lambda: 7)
print(s['k'])
print(s)

def fun():
    return(1,2,3)

s1 = defaultdict(fun)
print(s1['a'])
print(s1)

o = OrderedDict({'a':1,'b':2,'c':3})
print(o)
o.move_to_end('b')
print(o)



#Zad 1
tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \
incididunt ut labore et dolore magna aliqua. Dolor sed viverra ipsum nunc aliquet bibendum \
enim. In massa tempor nec feugiat. Nunc aliquet bibendum enim facilisis gravida. Nisl nunc \
mi ipsum faucibus vitae aliquet nec ullamcorper. Amet luctus venenatis lectus magna fringilla. \
Volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in. Egestas egestas \
fringilla phasellus faucibus scelerisque eleifend. Sagittis orci a scelerisque purus semper \
eget duis. Nulla pharetra diam sit amet nisl suscipit. Sed adipiscing diam donec adipiscing \
tristique risus nec feugiat in. Fusce ut placerat orci nulla. Pharetra vel turpis nunc eget \
lorem dolor. Tristique senectus et netus et malesuada."
tekst = tekst.lower()
tekst = tekst.replace('.','')
tekst = tekst.replace(',','')
tekst = tekst.replace('/','')

c = Counter(tekst.split())
#print(c)


#Zad 2
tabela = [
    ['sunny', 85, 85, False, 'no'],
    ['sunny', 80, 90, True, 'no'],
    ['overcast', 83, 86, False, 'yes'],
    ['rainy', 70, 96, False, 'yes'],
    ['rainy', 68, 80, False, 'yes'],
    ['rainy', 65, 70, True, 'no'],
    ['overcast', 64, 65, True, 'yes'],
    ['sunny', 72, 95, False, 'no'],
    ['sunny', 69, 70, False, 'yes'],
    ['rainy', 75, 80, False, 'yes'],
    ['sunny', 75, 70, True, 'yes'],
    ['overcast', 72, 90, True, 'yes'],
    ['overcast', 81, 75, False, 'yes'],
    ['rainy', 71, 91, True, 'no'],
]

for i in range(5):
    c2 = Counter()
    tmp_list = []
    for tab in tabela:
        tmp_list.append(tab[i])
    c2.update(tmp_list)
    
    print(c2)
    for x in c2:
        print(str(x)," - ",str(c2[x]/len(c2)))

print("\n")
#Zad 3

od = OrderedDict()


print("\n")
#Zad 4
d = defaultdict(lambda: 5)

for i in range(5):
    x = input("Podaj wartość klucza: ")
    print(d[x])
    d[x] = d[x] + 1


print("\n")
#Zad 5

def palindrom(tekst):
    d2 = deque(tekst)

    while len(d2) > 1:
        if d2.pop() != d2.popleft():
            return False
    return True

print(palindrom("aleksy"))
print(palindrom("kajak"))
print(palindrom("anakokana"))


