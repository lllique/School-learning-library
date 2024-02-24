from sympy import *


# 定义函数和自变量
t, tao = symbols('t tao')
# 定义输入信号，酌情选择
x = Heaviside(t) - Heaviside(t - 1)
h = Heaviside(t) - Heaviside(t-1)

#4.4节的例6
f = 2  # 模拟角频率,如果设置为200，会出现精度问题，且运算极慢
a = f * 2 * pi
x = sin(2 * pi * f * t) * Heaviside(t)
h = a*exp(-a * t) * Heaviside(t)
''''''
# 替换自变量为tao和t-tao
xtao = x.subs(t, tao)
htao = h.subs(t, t - tao)
'''
integrate参数为 integrate（函数、（自变量、下限、上限））
1，oo表示无穷大，
2，表达式可能即便简化后也很复杂（但不影响画图），有时候调整积分限会简化输出结果
但需要注意积分限必须大于理论上结果区间
3，有些复杂表达式，可能无法算出结果
'''
# 算卷积
#yconv = integrate(xtao*htao,(tao,-1*oo,oo)) #上下限为正负无穷
#上下限“足够大”
yconv = integrate(xtao * htao, (tao, 0, 10 * pi))
print(simplify(yconv))  # 显示卷积结果的解析式

p1 = plot(x, (t, -1, 5), title='x(t)', xlabel='t', line_color='blue', show=False)
p2 = plot(h, (t, -1, 5), title='h(t)', xlabel='t', line_color='green', show=False)

p11 = plot(x, (t, -1, 5), show=False)
p3 = plot(yconv, (t, -1, 5), title='r(t)', xlabel='t', line_color='orange', show=False)
p3.extend(p11)
p = plotting.PlotGrid(3, 1, p1, p2, p3)

