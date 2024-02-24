import sympy as sy

z = sy.symbols('z')
#ABCD一定要定义为二维形式（双层中括号）
A = sy.Matrix([[1 / 2, 0], [1 / 4, 2]])
B = sy.Matrix([[1], [1]])
C = sy.Matrix([[2, 0]])
D = sy.Matrix([[0]])

F = (z*sy.eye(A.shape[0])-A).inv()
H = C*F*B+D
H = sy.simplify(H)
print('H=',sy.pretty(H))


