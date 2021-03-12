import LocalExtrema as le
from sympy import *

x = Symbol("x")
y = Symbol("y")

infunc = input("Dreidimensionale Funktion eingeben als function = (Funktion): ")
exec(infunc)

result = le.findLocalExtrema()

print(result)

