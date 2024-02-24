import matplotlib.pylab as plt  # 绘制图形
from sympy import *
#定义函数和自变量
t = Symbol('t',real=True)
#注意sympy用大写I表示虚数
y = exp((-0.5+3*pi*I)*t)
#把e指数显示为实部+虚部的形式
print(y.as_real_imag()) #(exp(-0.5*t)*cos(10*t), exp(-0.5*t)*sin(10*t))
#分别显示y的实部和虚部
print(re(y),im(y))
print(pretty(re(y)),pretty(im(y))) #注意pretty对显示方式的影响
#y的模值和相位(弧度)
print(Abs(y),arg(y))

#如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
#先不进行show，交给plotgrid显示
p1 = plot(re(y),(t,0,10),title='实部',xlabel='t',ylabel='y(t)',show=False)
p2 = plot(im(y),(t,0,10),title='虚部',xlabel='t',ylabel='yflip(t)',show=False)
p3 = plot(Abs(y),(t,0,10),title='模值',xlabel='t',ylabel='y_odd(t)',show=False)
p4 = plot(arg(y),(t,0,10),title='相位',xlabel='t',ylabel='y_even(t)',show=False)
plotting.PlotGrid(2,2,p1,p2,p3,p4)

