import matplotlib.pylab as plt  # 绘制图形
from sympy import *
#定义函数和自变量
t = Symbol('t')
y = symbols('y', cls=Function)
#原函数
y = 5*exp(-t+2)*(Heaviside(t-2)-Heaviside(t-3))
#定义翻转函数，subs方法把t换成-t
yflip = y.subs(t,-t)
print(yflip)
#定义奇偶分量
y_odd = 0.5*(y-yflip)
print(y_odd)
y_even = 0.5*(y+yflip)
print(y_even)
#如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
#先不进行show，交给plotgrid显示
p1 = plot(y,(t,-5,5),title='原函数',xlabel='t',ylabel='y(t)',show=False)
p2 = plot(yflip,(t,-5,5),title='翻转',xlabel='t',ylabel='yflip(t)',show=False)
p3 = plot(y_odd,(t,-5,5),title='奇分量',xlabel='t',ylabel='y_odd(t)',show=False)
p4 = plot(y_even,(t,-5,5),title='偶分量',xlabel='t',ylabel='y_even(t)',show=False)
#PlotGrid实际还没有提供正式接口，所以调用方式是实例化该类，在做显示
#参数2，2表示两行两列显示，后面是图形列表
p = plotting.PlotGrid(2,2,p1,p2,p3,p4)
p.show()
