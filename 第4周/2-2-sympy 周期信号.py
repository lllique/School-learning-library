import sympy as sy

# 定义函数和自变量
a = 2
t = sy.Symbol('t')
y = sy.symbols('y', cls=sy.Function)

#t,tao , w1= symbols('t tao w1',positive=True,real=True)
#n = symbols('n',integer=True,real=True,positive=True)

y1 = sy.sin(5 * t)
y2 = sy.sin(100 * t)
y3 = sy.sin(2 * sy.pi * t)
#sy.plot(y1, (t, -10, 10))
#latex
p0 = sy.plot(y1, (t, -10, 10), title='sin5t', xlabel='t', show=False)
p1 = sy.plot(y2, (t, -10, 10), title='sin10t', xlabel='t', show=False)
p2 = sy.plot(y3, (t, -10, 10), title=r'$sin2\pi t$', xlabel='t', show=False)
p3 = sy.plot(y1 + y2, (t, -20, 20), title='sin5t+sin10t', xlabel='t', show=False)
p4 = sy.plot(y1 * y2, (t, -2, 2), title=r'sin5t+$sin2\pi t$', xlabel='t', show=False)
p5 = sy.plot(y2 + y3, (t, -20, 20), title=r'sin10t+$sin2\pi t$', xlabel='t', show=False)

sy.plotting.PlotGrid(3, 2, p0, p1, p2, p3, p4, p5)
