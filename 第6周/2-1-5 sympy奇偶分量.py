from sympy import *
#定义函数和自变量
t = Symbol('t')
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
#先不进行show，交给plotgrid显示
p1 = plot(y,(t,-5,5),title='f(t)',xlabel='t',ylabel='y(t)',show=False)
p2 = plot(yflip,(t,-5,5),title='f(-t)',xlabel='t',ylabel='yflip(t)',show=False)
p3 = plot(y_odd,(t,-5,5),title='f_odd',xlabel='t',ylabel='y_odd(t)',show=False)
p4 = plot(y_even,(t,-5,5),title='f_even',xlabel='t',ylabel='y_even(t)',show=False)
p5 = plot(y_odd,(t,-5,5),show=False)
p6 = plot(y_even,(t,-5,5),title='f_odd+f_even',xlabel='t',ylabel='y_odd(t)',show=False)
p6.extend(p5) #把p5图加到P6上
#下面是p6的另一种叠加显示方法
p7 = plot(y_even,y_odd,(t,-5,5),title='f_odd+f_even',xlabel='t',ylabel='y_odd(t)',show=False)
plotting.PlotGrid(3,2,p1,p2,p3,p4,p6,p7)

