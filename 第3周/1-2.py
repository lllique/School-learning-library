from sympy import *
import matplotlib.pylab as plt  # 绘制图形
t = Symbol('t')
y2 = 5*exp(-2*t)*cos(10*t)*Heaviside(t)
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定非衬线（中文）字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
plot(y2,(t,-1,4),title='e指数振荡函数',xlabel='t')
