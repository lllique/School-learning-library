import matplotlib.pylab as plt  # 绘制图形
from sympy import *
#定义函数和自变量
a = 2
t,f,w = symbols('t f w')
y = symbols('y', cls=Function)
#原始信号
y = t*(Heaviside(t+1)-Heaviside(t-1))
#压缩扩展
y1 = y.subs(t,2*t+3)
y2 = y.subs(t,-0.5*t)
#F变换
FW = fourier_transform(y,t,f)
FW1 = fourier_transform(y1,t,f)
FW2 = fourier_transform(y2,t,f)
#注意，该方法的频域变量是频率，不是角频率
#如果要转化为角频率，则执行变量转换，f = w/2pi：
FW = FW.subs(f,w/(2*pi))
FW1 = FW1.subs(f,w/(2*pi))
FW2 = FW2.subs(f,w/(2*pi))

#如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
#显示函数图像，实际调用的是sympy的plot函数
# 但底层是调用matplotlib，所以上面的plt开头的参数是有用的
p0=plot(y,(t,-4,4),title='f(t)',ylabel='',show=False)
p1 = plot(abs(FW),(w,-20,20),title='f(t)幅度谱',ylabel='',show=False)
p2 = plot(arg(FW),(w,-20,20),title='f(t)相位谱',ylabel='',show=False)
p10 =plot(y1,(t,-4,4),title='f(2t+3)',ylabel='t',show=False)
p11 = plot(abs(FW1),(w,-20,20),title='f(2t+3)幅度谱',ylabel='',show=False)
p12 = plot(arg(FW1),(w,-20,20),title='f(2t+3)相位谱',ylabel='',show=False)
p20 =plot(y2,(t,-4,4),title='f(-0.5t)',ylabel='t',show=False)
p21 = plot(abs(FW2),(w,-20,20),title='f(-0.5t)幅度谱',ylabel='',show=False)
p22 = plot(arg(FW2),(w,-20,20),title='f(-0.5t)相位谱',ylabel='',show=False)

#将所有图形组合显示（三行二列）
plotting.PlotGrid(3,3,p0,p1,p2,p10,p11,p12,p20,p21,p22)
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




