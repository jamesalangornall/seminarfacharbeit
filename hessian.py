import sympy as sym
x, y = sym.symbols("x y")
f = sym.cos(x*10)**2 + sym.sin(y*10)**2
gradient = sym.derive_by_array(f, (x, y))
hessian = sym.Matrix(2, 2, sym.derive_by_array(gradient, (x, y)))
stationary_points = sym.solve(gradient, (x, y))

for p in stationary_points:
    value = f.subs({x: p[0], y: p[1]})
    hess = hessian.subs({x: p[0], y: p[1]})
    eigenvals = hess.eigenvals()
    if all(ev > 0 for ev in eigenvals):
        print("Local minimum at {} with value {}".format(p, value))
    elif all(ev < 0 for ev in eigenvals):
        print("Local maximum at {} with value {}".format(p, value))
    elif any(ev > 0 for ev in eigenvals) and any(ev < 0 for ev in eigenvals):
        print("Saddle point at {} with value {}".format(p, value))
    else:
        print("Could not classify the stationary point at {} with value {}".format(p, value))
