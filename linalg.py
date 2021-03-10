import numpy as np
a = np.array([[1, 2], [3, 5]])
b = np.array([0, 0])
x = np.linalg.solve(a,b)
print(x)
