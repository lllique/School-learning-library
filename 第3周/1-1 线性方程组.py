import sympy as sp
x1,x2,x3 = sp.symbols('x1 x2 x3')
result = sp.solve([x1-2*x2+3*x3-1,
                   2*x1+3*x2+x3-2,
                   3*x1-x2-x3-4],
                  [x1, x2,x3])
print(result)
