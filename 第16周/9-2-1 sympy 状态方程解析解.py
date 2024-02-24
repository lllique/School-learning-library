import sympy as sy
t,s = sy.symbols('t s')
A = sy.Matrix([[ 1, -2], [1, 4]])
x0 =sy.Matrix([3,2])
#求e^at
eat = sy.diag(sy.exp(sy.diag(t * A)))
eat = sy.simplify(eat)
print(sy.pretty(eat))
#求lambda(t)
求lambda=sy.simplify(eat*x0)
print(sy.pretty(求lambda))

#拉氏变换
Fs = sy.laplace_transform(eat,t,s,noconds=True)
print(sy.pretty(Fs))
Xs = sy.laplace_transform(求lambda,t,s,noconds=True)
print(sy.pretty(Xs))

