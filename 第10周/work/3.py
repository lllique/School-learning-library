from sympy import *

t = symbols('t')
e,r = symbols('e r',cls=Function)

e = Function("heaviside")
diffeq = Eq(r(t).diff(t,2) + 3*r(t).diff(t) + 2*r(t),e(t).diff(t) + 3 * e(t))
respone = dsolve(diffeq,r(t),ics={r(0):1,r(t).diff(t).subs(t,0):2})
print(respone)