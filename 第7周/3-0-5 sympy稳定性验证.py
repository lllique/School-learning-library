from sympy import *
t = symbols('t')
#假设出一个ht，看是否绝对可积
h = exp(-0.5*t)*Heaviside(t)
h = Heaviside(t)
h = DiracDelta(t)
h = log(t)
sum_x = integrate(h,(t,-oo,oo))
print("sum_x:",sum_x)
