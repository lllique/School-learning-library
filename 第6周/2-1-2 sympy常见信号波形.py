import matplotlib.pylab as plt  # 绘制图形
import sympy as sy
#定义函数和自变量
a = 2
t = sy.Symbol('t')
# 其他定义定义变量的方法参考
# t,tao, w1= symbols('t tao w1',positive=True,real=True)
# n = symbols('n',integer=True,real=True,positive=True)
# y = sy.symbols('y', cls=sy.Function)
print("------------")
'''冲激信号（冲激函数无法直接画图显示）'''
print(sy.DiracDelta(0))#输出DiracDelta(0)
print(sy.DiracDelta(1))#输出0
print(sy.DiracDelta(t))#输出DiracDelta(t)
print(sy.DiracDelta(2*t))#输出DiracDelta(2*t)
print("------------")
'''阶跃函数'''
print(sy.Heaviside(-1))#-1
print(sy.Heaviside(0))#1/2
print(sy.Heaviside(1))#1
print(sy.Heaviside(t))#Heaviside(t)
print(sy.Heaviside(2*t))#Heaviside(2*t)

'''常见信号画图'''
print("------常见信号画图------")
#阶跃信号
y0 =sy.Heaviside(t)
#另一种定义阶跃函数的方法,利用时sympy的Piecewise方法
#参数是多个（值，条件）
y0 =sy.Piecewise((1,t>0),(0,t<0),(1,t==0))

#符号函数
y1 = sy.sign(t)
#衰减震荡
y2 = 5*sy.exp(-a*t)*sy.cos(10*t)*sy.Heaviside(t)
#Sa函数
y3 = sy.sin(t)/t
#注意sympy里的sinc实际就是Sa，numpy里的sinc是正确的
y3 = sy.sinc(t)
#分段斜边函数
y4 = t*(sy.Heaviside(t)-sy.Heaviside(t-1))
#另一种定义分段函数的方法,利用时sympy的Piecewise方法
#参数是多个（值，条件）,支持and or等条件，可以存在间断点
y4 =sy.Piecewise((t,sy.And(t>0,t<1)),(0,sy.Or(t<0,t>1)))
#或者简化一下
y4 =sy.Piecewise((t,sy.And(t>0,t<1)),(0,True))
#冲激函数（无法画图）
y5 = sy.DiracDelta(t)

'''单独画图参考'''
#plot(y2,(t,-1,4),title='e指数振荡函数',xlabel='t')

'''网格化绘图'''
#如果需要显示中文，则需要加入下面两行
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
p0=sy.plot(y0,(t,-1,4),title='阶跃函数',xlabel='t',show=False)
p1=sy.plot(y1,(t,-4,4),title='符号函数',xlabel='t',show=False)
p2=sy.plot(y2,(t,-1,4),title='衰减指数振荡函数',xlabel='t',show=False)
p3=sy.plot(y3,(t,-10,10),title='Sa函数',xlabel='t',show=False)
p4=sy.plot(y4,(t,-1,4),title='分段函数',xlabel='t',show=False)
p5=sy.plot(y5,(t,-10,10),title='冲激函数',xlabel='t',show=False)
sy.plotting.PlotGrid(3,2,p0,p1,p2,p3,p4,p5)#将所有图形组合显示（三行二列）

#plot实际调用的是sympy的plot函数
# 但底层是调用matplotlib，所以上面的plt开头的参数是有用的
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
