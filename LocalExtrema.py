from sympy import *

x = Symbol('x')
y = Symbol("y")

class Extremum:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

def findLocalExtrema(f):
    partialx = Derivative(f, x)
    partialy = Derivative(f, y)
    xgradz = Eq((partialx.doit()), 0)
    ygradz = Eq((partialy.doit()), 0) #Nullsetzen des Gradienten
    coords = solve((xgradz, ygradz),(x,y), dict=True, set=True)
    #Bestimmung der Koordinaten der lokalen Extrema
    print(coords)
    partialxx = Derivative(partialx, x)
    partialxy = Derivative(partialx, y) #Satz v. Schwarz
    partialyy = Derivative(partialy, y)

    listex = list()

    for extremum in coords: #Einsetzen der Koordinaten a und b

        xx_ab = partialxx.doit().subs(x, extremum[x]).subs(y, extremum[y])
        xy_ab = partialxy.doit().subs(x, extremum[x]).subs(y, extremum[y])
        yy_ab = partialyy.doit().subs(x, extremum[x]).subs(y, extremum[y])
        D = xx_ab * yy_ab - xy_ab * xy_ab #Hesse-Determinante
        if D > 0 and xx_ab > 0:
            type = "min"
        elif D > 0 and xx_ab < 0:
            type = "max"
        elif D < 0:
            type = "saddle"
        elif D == 0:
            type = "nosol"
        listex.append(Extremum(extremum[x], extremum[y], type))



    return listex


