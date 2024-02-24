import matplotlib.pylab as plt  # 绘制图形
import sympy as sy
#定义函数和自变量
a = 2
t = sy.Symbol('t')
# 其他定义定义变量的方法参考
# t,tao, w1= symbols('t tao w1',positive=True,real=True)
# n = symbols('n',integer=True,real=True,positive=True)
# y = sy.symbols('y', cls=sy.Function)

'''定义一些信号'''
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
#参数是多个（值，条件）,支持and or等条件，可以存在少量间断点
y4 =sy.Piecewise((t,sy.And(t>0,t<1)),(0,sy.Or(t<0,t>1)))
#冲激函数（无法画图）
y5 = sy.DiracDelta(t)

'''带入数值进行计算'''
#可以执行
print(sy.DiracDelta(1))
print(sy.Heaviside(1))
print(sy.sinc(1))#sinc(1)
#会报错
#print(y5(1)) #TypeError: 'DiracDelta' object is not callable
#print(y0(1))#采用两种方式定义阶跃函数都无法带入数值
#TypeError: 'Piecewise' object is not callable
#TypeError: 'Heaviside' object is not callable
#print(y3(1)) #TypeError: 'sinc' object is not callable

'''把定义的表达式改为能够带入数值进行计算的式子'''
f5 = sy.lambdify(t, y5)
f4 = sy.lambdify(t, y4)
f3 = sy.lambdify(t, y3)
#print(f5(1)) #NameError: name 'DiracDelta' is not defined
print(f4(1))#注意，原定义在1这个位置无定义，所以输出为nan，即为空值，但不报错
print(f3(1))