import sympy as sy

z = sy.symbols('z')
A = sy.Matrix([[0, 1], [-6, 5]])
F = sy.det(z*sy.eye(2)-A)
r=sy.solve(F)
print(sy.pretty(F))
print(r)

