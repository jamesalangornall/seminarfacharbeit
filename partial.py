from sympy import *

x= Symbol('x')

y= Symbol('y')

function= sin(x**2)+y**2

partialx = Derivative(function, x)
partialy = Derivative(function, y)
partialx.doit()
partialy.doit()
print(partialx.doit(),",",
      partialy.doit())

