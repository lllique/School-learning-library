from sympy import *
import matplotlib.pylab as plt  # 绘制图形

# 定义函数和自变量
t = symbols('t')
tao = 2 * pi
# 定义信号
x = sin(pi * t / 16)
# 先经过系统，进行平移
y_1 = x.subs(t, 2 * t)
y_1 = y_1.subs(t, t - tao)
# 先进行平移，在经过系统
x2 = x.subs(t, t - tao)
y_2 = x2.subs(t, 2 * t)

# 如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块
p1 = plot(y_1, (t, -20, 20), title='先经过系统再时移', xlabel='t', line_color='blue', show=False)
p2 = plot(y_2, (t, -20, 20), title='先时移再经过系统', xlabel='t', line_color='green', show=False)
p = plotting.PlotGrid(2, 1, p1, p2)
