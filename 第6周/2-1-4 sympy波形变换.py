from sympy import *
#定义函数和自变量
t = Symbol('t')
#原始信号
y = t*(Heaviside(t)-Heaviside(t-1))
#利用subs函数进行变量替换
y1 = y.subs(t,-1*t)
y2 = y.subs(t,t-1)
y3 = y.subs(t,0.5*t)
y4 = y.subs(t,-2*t+3)
y5 = y.subs(t-1,t)#结果不对,不支持反向变换，结果不太可控

p0=plot(y,(t,-1,4),title='f(t)',xlabel='t',show=False)
p1=plot(y1,(t,-4,4),title='f(-t)',xlabel='t',show=False)
p2=plot(y2,(t,-1,4),title='f(t-1)',xlabel='t',show=False)
p3=plot(y3,(t,-4,4),title='f(1/2t)',xlabel='t',show=False)
p4=plot(y4,(t,-1,4),title='f(-2t+3)',xlabel='t',show=False)
p5=plot(y5,(t,-1,4),title='f(-2t+3)->f(t)',xlabel='t',show=False)#结果不对
plotting.PlotGrid(3,2,p0,p1,p2,p3,p4,p5)





