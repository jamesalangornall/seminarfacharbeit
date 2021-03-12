
from sympy import *
import LocalExtrema as le

x = Symbol("x")
y = Symbol("y")

infunc = input("Dreidimensionale Funktion eingeben als function = (Funktion): ")
exec(infunc)

result = le.findLocalExtrema(function)

print(result)

