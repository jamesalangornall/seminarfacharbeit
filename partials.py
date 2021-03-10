import sympy as sp

x, y = sp.symbols("x y")

f= input("Funktion f(x,y)= ")

deriv = sp.diff(f, x)

print(deriv)

