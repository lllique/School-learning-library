import sympy as sp
t = sp.Symbol('t')
y2 = 5 * sp.exp(-2 * t) * sp.cos(10 * t) * sp.Heaviside(t)
sp.plot(y2, (t, -1, 4))
