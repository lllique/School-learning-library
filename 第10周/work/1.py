from sympy import *

n = symbols('n')

h = Heaviside(n) - Heaviside(n - 5)
x = (Heaviside(n) - Heaviside(n - 5)) * n

p1 = plot(h,(n,-10,10),title = 'h(n)',xlabel = 'n',line_color = 'blue',show = False)
p2 = plot(x,(n,-10,10),title = 'x(n)',xlabel = 'n',line_color = 'yellow',show = False)

n_ = symbols('n_')

h_ = h.subs(n,n_)
x_ = x.subs(n,n_)

fn = integrate(h_ * x_,(n_,-1 * oo,oo))
p3 = plot(fn,(n,-10,10),title = 'Fn(n)',xlabel = 't',line_color = 'black',show = False)
p = plotting.PlotGrid(3,1,p1,p2,p3)