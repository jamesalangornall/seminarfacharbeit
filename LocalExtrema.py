from sympy import *

x = Symbol('x') #specifying x and y as real
y = Symbol('y') #doesn't work as a solution to solve()-problem

class Extremum:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

def findLocalExtrema(f):
    partialx = Derivative(f, x)
    partialy = Derivative(f, y)
    xgradz = Eq((partialx.doit()), 0)
    ygradz = Eq((partialy.doit()), 0)
    coords = solve((xgradz, ygradz),(x,y), dict=True)
    #gives out x, y plus their values as a list of dictionaries
    #solve only solves symbolically, tends to spit out complex numbers or leave out variables (Bug)
    #solveset doesn't yet work for nonlinear equations of multible variables
    print(coords)
    partialxx = Derivative(partialx, x)
    partialxy = Derivative(partialx, y) #Satz v. Schwarz
    partialyy = Derivative(partialy, y)

    listex = list()

    for extremum in coords:

        xx_ab = partialxx.doit().subs(x, extremum[x]).subs(y, extremum[y])
        xy_ab = partialxy.doit().subs(x, extremum[x]).subs(y, extremum[y])
        yy_ab = partialyy.doit().subs(x, extremum[x]).subs(y, extremum[y])
        D = xx_ab * yy_ab - xy_ab * xy_ab
        if D > 0 and xx_ab > 0:
            type = "min"
        elif D > 0 and xx_ab < 0:
            type = "max"
        elif D < 0:
            type = "saddle"
        else:
            type = "nosol"
        listex.append(Extremum(extremum[x], extremum[y], type))



    return listex


