def add(X:"Macierz X", Y:"Macierz Y") -> "Funkcja dodania macierzy":
    for i in range(len(X)):  
        for j in range(len(X[0])):
            X[i][j] = X[i][j] + Y[i][j]
    return X;
"""
Funkcja dodania macierzy
"""


def addConst(X:"Macierz X", y:"stala liczba") -> "Funkcja dodania stalej do macierzy":
    return [[X[i][j] + Y[i][j]  for j in range (len(X[0]))] for i in range(len(X))]
"""
Funkcja dodania stalej do macierzy
"""


def multiplication(X:"Macierz X", Y:"Macierz Y") -> "Funkcja mnozenia macierzy":
    for i in range(len(X)):  
        for j in range(len(B[0])):
            for k in range(len(B)):
                X[i][j] = X[i][j] + y
    return X;
"""
Funkcja mnozenia macierzy
"""