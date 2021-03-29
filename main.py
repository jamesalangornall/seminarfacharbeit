
from sympy import *
import LocalExtrema as le

f = input("Dreidimensionale Funktion eingeben: f(x,y)= ")

result = (le.findLocalExtrema(f))

for r in result:
    if r.type == "min":
        print("Lokales Minimum bei: " + str(r.x) + ", " + str(r.y))
    elif r.type == "max":
        print("Lokales Maximum bei: " + str(r.x) + ", " + str(r.y))
    elif r.type == "saddle":
        print("Sattelpunkt bei: " + str(r.x) + ", " + str(r.y))
    elif r.type == "nosol":
        print("Keine Lösung bei: " + str(r.x) + ", " + str(r.y))


