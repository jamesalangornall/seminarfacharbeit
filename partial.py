from sympy import *

x = Symbol('x')

y = Symbol('y')


#infunc = input ("Dreidimensionale Funktion eingeben als function = [...]: ")
#exec(infunc)
#print(function)

partialx = Derivative(function, x)
partialy = Derivative(function, y)
partialx.doit()
partialy.doit()

#partialxx = Derivative(partialx, x)
#partialxy = Derivative(partialx, y)
##Satz von Schwarz, daher kein partialyx
#partialyy = Derivative(partialy, y)
#partialxx.doit()
#partialxy.doit()
#partialyy.doit()

print(partialx.doit(), ",", partialy.doit())
