import matplotlib.pylab as plt
import sympy as sy

t = sy.Symbol('t')
x1 = sy.symbols('x1',cls=sy.Function)

#定义原函数
x1 = sy.sin(2 * sy.pi * t) * (sy.Heaviside(t - 1) - sy.Heaviside(t - 2))
#定义翻转函数
x1_flip = x1.subs(t,-t)
#推导出 偶分量 和 奇分量
x1_odd = 0.5 * (x1 - x1_flip) #奇分量
x1_even = 0.5 * (x1 + x1_flip) #偶分量

#显示中文的必要条件
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

p1 = sy.plot(x1,(t,-5,5),title='原函数',xlabel='t',ylabel='x1(t)',show=False)
p1_flip = sy.plot(x1_flip,(t,-5,5),title='翻转函数',xlabel='t',ylabel='x_flip(t)',show=False)
p1_odd = sy.plot(x1_odd,(t,-5,5),title='奇分量',xlabel='t',ylabel='x1_odd(t)',show=False)
p1_even = sy.plot(x1_even,(t,-5,5),title='偶分量',xlabel='t',ylabel='x1_even(t)',show=False)

sy.plotting.PlotGrid(2,2,p1,p1_flip,p1_odd,p1_even)