import sympy as sy
t,s = sy.symbols('t s')
'''
#laplace_transform实际是单边拉氏变换
#加入noconds=True条件，返回值是一个F(s)的表达式，
# 如果不加该条件，返回值是一个tuple，包含表达式、收敛轴、辅助收敛条件(auxiliary convergence conditions)
#simplify: if True, it simplifies the final result. The default setting is
'''
#冲激函数
yt  = sy.DiracDelta(t)
Ys = sy.laplace_transform(yt,t,s)
print(Ys)
#冲激偶，无法正确的出结果
#(LaplaceTransform(DiracDelta(t, 1), t, s), -oo, True)
yt  = sy.DiracDelta(t).diff(t)
Ys = sy.laplace_transform(yt,t,s)
print(Ys)
#阶跃函数
yt = sy.Heaviside(t)
Ys = sy.laplace_transform(yt,t,s)
print(Ys)
#两个e指数函数，例如某个微分方程的齐次解
yt = sy.exp(-2*t)*sy.Heaviside(t) +  sy.exp(-3*t)*sy.Heaviside(t)
Ys = sy.laplace_transform(yt,t,s)
print(sy.pretty(Ys))
#t的平方
yt = t**2 * sy.Heaviside(t)
Ys = sy.laplace_transform(yt,t,s,noconds=True,simplify=True)
print(Ys)
#理论上不存在s变换
yt= sy.exp(t**2) * sy.Heaviside(t)
Ys = sy.laplace_transform(yt,t,s)
print(Ys) # (oo*exp(-s**2/4), -oo, True)

