import matplotlib.pylab as plt  # 绘制图形
from sympy import *
#定义函数和自变量
t = Symbol('t')
y = symbols('y', cls=Function)
#原函数。注意sympy用大写I表示虚数
y = exp((-0.5+10*I)*t)
#分别显示y的实部和虚部
#print(y.as_real_imag())
#显示y的实函数部分和虚函数部分
print(pretty(re(y)))  #pretty()将其改为可读性更好的方法
print(pretty(im(y)))
#y的模值和相位(弧度)
print(Abs(y))
print(arg(y))
#如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
#先不进行show，交给plotgrid显示
p1 = plot(re(y),(t,0,10),title='实部',xlabel='t',ylabel='y(t)',show=False)
p2 = plot(im(y),(t,0,10),title='虚部',xlabel='t',ylabel='yflip(t)',show=False)
p3 = plot(Abs(y),(t,0,10),title='模值',xlabel='t',ylabel='y_odd(t)',show=False)
p4 = plot(atan(im(y)/re(y)),(t,0,10),title='相位',xlabel='t',ylabel='y_even(t)',show=False)
#PlotGrid实际还没有提供正式接口，所以调用方式是实例化该类，在做显示
#参数2，2表示两行两列显示，后面是图形列表
p = plotting.PlotGrid(2,2,p1,p2,p3,p4)

