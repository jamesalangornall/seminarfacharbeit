from sympy import *

x = Symbol("x")
y = Symbol("y")

def findLocalExtrema(function):
    partialx = Derivative(function, x)
    partialy = Derivative(function, y)
    partialx.doit()
    partialy.doit()
    #gradient = (partialx.doit(), partialy.doit())
    xgradz = Eq((partialx.doit()), 0)
    ygradz = Eq((partialy.doit()), 0)
    coords = solve((xgradz, ygradz),(x,y))

    return coords
