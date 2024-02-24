from sympy import *

#问题1：特征根
x= symbols('x')
R,L,C = symbols('R L C')
#可以带入不同的参数值
#L=1;C=1;R=0;
L=1;C=1;R=0.2;
#L=1;C=1;R=2;
#L=1;C=1;R=3;
rts = roots(x ** 2 +R / L * x  + 1/L /C,x)
print(pretty(rts))

#问题2 得到响应，（利用齐次解法）并画图(必须给出RLC)
t = symbols('t')
r = symbols('r', cls=Function)
diffeq = Eq(r(t).diff(t, 2) + R / L * r(t).diff(t) + 1/L /C * r(t), 0)
respone = dsolve(diffeq, r(t), ics={r(0): 0, r(t).diff(t).subs(t, 0): 1})
h  = respone.rhs*Heaviside(t)/L/C
print(respone)
plot(h,(t,0,30))#绘图，修改R值，可以观察四种阻尼效果






