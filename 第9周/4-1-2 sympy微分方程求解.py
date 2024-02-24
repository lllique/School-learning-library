from sympy import *

'''定义微分方程'''
# 定义自变量和函数，对于单输入单输出系统，只需要定义t和y
t = symbols('t')
e, r = symbols('e r', cls=Function)
# 激励信号
e = 6 * sin(2 * t)
# 建立微分方程，格式为一个Eq（等式）
diffeq = Eq(r(t).diff(t, 2) + 7 * r(t).diff(t) + 6 * r(t), e) #diff(t,2)对t求两次导,二阶导数
print('------方式1--------')
# 求通解（包括特解），调用dsolve函数,返回一个Eq对象
# 求解出r(t)表达式
respone = dsolve(diffeq, r(t), ics={r(0): 1, r(t).diff(t).subs(t, 0): 0}) #r(t).diff(t).subs(t, 0): 0 => r倒数(0) = 0
# 两种显示方式
print(respone)  # 常规方式，如果形式复杂，可以尝试调用simplify进行化简
print(pretty(respone))  # 易读方式
print('------方式2--------')
# 如果不给出初始值，则求出来的全解具有待定系数
respone = dsolve(diffeq, r(t))
print(respone)
# 之后可以通过手动方式求待定系数
x1, x2 = symbols('x1 x2')
result = solve([x1 + x2 - 21 / 50 - 1, -x1 - 6 * x2 + 3 / 25], [x1, x2]) #x1 + x2 - 21 / 50 - 1,是指x1 + x2 - 21 / 50 - 1 = 0作为一个方程
print("待定系数：", result)



