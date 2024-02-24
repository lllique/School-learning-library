from sympy import *

t = Symbol('t')
r = symbols('r', cls=Function)
'''
#sympy并不能直接求出冲激响应:
1,激励信号中给出冲激信号或其导数后，初值并非手动分析得到的0+值，而且响应中也无法体现出冲激项）
2，这里本质上是求解齐次方程，并且手算0+值，带入求全解，此时只能得到h(t)在0+时刻之后的解
3，最佳方式是结合齐次解法，分步求解，此时如果响应中由冲激项也可以体现出来
'''
# 例2（a=2）  #iv = [2]
diffeq = Eq(r(t).diff(t) + 2 * r(t), DiracDelta(t))  # ics ={r(0): -2}
# 需要手动分析0+值，这里利用冲激函数匹配法分析，该值为2
h = dsolve(diffeq, r(t), ics={r(0): 2})
print(h)
print("----------------")
# 例3，结合齐次解法
# 1，先假定右边只有一个冲激项，此时响应中必然不含冲激项，解齐次方程：
diffeq = Eq(r(t).diff(t) + 2 * r(t), 0)
# 2，根据齐次解法，次高阶导数项的初值为1
h_cap = dsolve(diffeq, r(t), ics={r(0): 1})
print(h_cap)
# 3,由于原式不带u(t)，这里要乘一下u(t),才能获得正确的导数
h = (h_cap.rhs * Heaviside(t)).diff(t)
# 3,根据线性关系，对h_cap的右边进行求导，可以得到真实的冲激响应
# 如果结果没有充分化简，可以尝试使用simplify等方法化简
print(simplify(h))
print("----------------")
# 例5
# 1，先假定右边只有一个冲激项，此时响应中必然不含冲激项，解齐次方程：
diffeq = Eq(r(t).diff(t, 2) + 4 * r(t).diff(t) + 3 * r(t), 0)
# 2，根据齐次解法，次高阶导数项的初值为1
h_cap = dsolve(diffeq, r(t), ics={r(0): 0, r(t).diff(t).subs(t, 0): 1})
print(h_cap)
# 3,由于原式不带u(t)，这里要乘一下u(t),才能获得正确的导数
hh = h_cap.rhs * Heaviside(t)
h = hh.diff(t) + 2 * hh
# 3,根据线性关系，对h_cap的右边进行求导，可以得到真实的冲激响应
print(simplify(h))
