import matplotlib.pylab as plt  # 绘制图形
from sympy import *
#定义函数和自变量
a = 2
t = Symbol('t')
y = symbols('y', cls=Function)
#冲激信号（#冲激函数无法直接画图显示）
print(DiracDelta(0))#输出DiracDelta(0)
print(DiracDelta(1))#输出0
print(DiracDelta(t))#输出DiracDelta(t)
print(DiracDelta(2*t))#输出DiracDelta(2*t)
#常见函数波形
y0 =Heaviside(t)#阶跃函数
print(Heaviside(0))#阶跃函数)
#另一种定义阶跃函数的方法,利用时sympy的Piecewise方法
#参数是多个（值，条件）
y0 =Piecewise((1,t>0),(0,t<0),(1/2,t==0))

y1 = sign(t)#符号函数sign(t)
y2 = 5*exp(-a*t)*cos(10*t)*Heaviside(t)
#plot(y2,(t,-1,4),title='e指数振荡函数',xlabel='t')
y3 = sin(t)/t
y4 = t*(Heaviside(t)-Heaviside(t-1))
y5 = sinc(t) #注意sympy里的sinc实际就是Sa，numpy里的sinc是正确的
y6 = 0.5**t*Heaviside(t)
#另一种定义分段函数的方法,利用时sympy的Piecewise方法
#参数是多个（值，条件）,支持and or等条件，可以存在少量间断点
#y4 =Piecewise((t,And(t>0,t<1)),(0,Or(t<0,t>1)))

#如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
#显示函数图像，实际调用的是sympy的plot函数
# 但底层是调用matplotlib，所以上面的plt开头的参数是有用的
p0=plot(y0,(t,-1,4),title='阶跃函数',xlabel='t',show=False)
p1=plot(y1,(t,-4,4),title='符号函数',xlabel='t',show=False)
p2=plot(y2,(t,-1,4),title='e指数振荡函数',xlabel='t',show=False)
p3=plot(y3,(t,-4,4),title='Sa函数',xlabel='t',show=False)
p4=plot(y4,(t,-1,4),title='分段函数',xlabel='t',show=False)
p5=plot(y5,(t,-4,4),title='（假）sinc函数',xlabel='t',show=False)
#冲激函数无法显示
#p5=plot(DiracDelta(t),(t,-4,4),title='冲激函数',xlabel='t',show=False)
#将所有图形组合显示（三行二列）
plotting.PlotGrid(3,2,p0,p1,p2,p3,p4,p5)
#也可利用xlim=(-1,5)限定横轴范围，默认显示范围是-10到+10

