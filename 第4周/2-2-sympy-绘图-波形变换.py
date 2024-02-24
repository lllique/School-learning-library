from sympy import *
import matplotlib.pylab as plt  # 绘制图形
#1.定义函数和自变量
a = 2
t = Symbol('t')
y = symbols('y', cls=Function)
#原始信号
y = t*(Heaviside(t)-Heaviside(t-1))
#利用subs函数进行变量替换
y1 = y.subs(t,-1*t)
y2 = y.subs(t,t-1)
y3 = y.subs(t,0.5*t)
y4 = y.subs(t,-2*t+3)
# 最基本的绘图方法
#plot(y)
#plot(y,(t,-1,4))
#中文支持，如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
#plot(y,(t,-1,4),title='原函数')
#exit()

#显示函数图像，实际调用的是sympy的plot函数
# 但底层是调用matplotlib，所以上面的plt开头的参数是有用的
p0=plot(y,(t,-1,4),title='f(t)',xlabel='t',show=False)
p1=plot(y1,(t,-4,4),title='f(-t)',xlabel='t',show=False)
p2=plot(y2,(t,-1,4),title='f(t-1)',xlabel='t',show=False)
p3=plot(y3,(t,-4,4),title='f(2t)',xlabel='t',show=False)
p4=plot(y4,(t,-1,4),title='f(-2t+3)',xlabel='t',show=False)
p4.extend(p3)
#将所有图形组合显示（三行二列）
plotting.PlotGrid(2,2,p0,p1,p2,p4)


#plotting.PlotGrid(3,2,p0,p1,p2,p3,p4,p5)

#也可利用xlim=(-1,5)限定横轴范围，默认显示范围是-10到+10
'''
title : str
xlabel : str
ylabel : str
legend : bool
xscale : {'linear', 'log'}
yscale : {'linear', 'log'}
axis : bool
axis_center : tuple of two floats or {'center', 'auto'}
xlim : tuple of two floats
ylim : tuple of two floats
aspect_ratio : tuple of two floats or {'auto'}
autoscale : bool
margin : float in [0, 1]
backend : {'default', 'matplotlib', 'text'} or a subclass of BaseBackend
size : optional tuple of two floats, (width, height); default: None
The per data series options and aesthetics are: There are none in the base series. See below for options for subclasses.
Some data series support additional aesthetics or options:
ListSeries, LineOver1DRangeSeries, Parametric2DLineSeries, Parametric3DLineSeries support the following:
Aesthetics:
line_color : function which returns a float.
options:
label : str
steps : bool
integers_only : bool
SurfaceOver2DRangeSeries, ParametricSurfaceSeries support the following:
aesthetics:
surface_color : function which returns a float.
'''




