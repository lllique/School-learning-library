import sympy as sy

t = sy.symbols('t')

y1 = sy.sin(10 * t)+sy.sin(sy.pi * t)
y2 = sy.Heaviside(t)

sy.plot(y1,(t,-10,10))
sy.plot(y2,(t,-5,5))