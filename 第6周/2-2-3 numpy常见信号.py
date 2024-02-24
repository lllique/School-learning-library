import numpy as np
import matplotlib.pylab as plt  # 绘制图形

'''
这里定义的是离散信号
如果要定义连续的时间轴，只需要加大抽样间隔或减少采样点
例如：
t1 = np.arange(-10.0, 10.0, 0.01)
t2 = np.linspace(10, 15, 2000)
'''
t = np.linspace(-10.0, 10.0, 20)#一共20个点，最后是闭区间
t = np.arange(-10.0, 10.0, 1) #一共20个点，最后是开区间

#定义常见信号
np.seterr(divide='ignore', invalid='ignore')#numpy忽略除以零的警告
#sinc函数
y1 =np.sinc(t/np.pi)
#Sa函数
y2 = np.sin(t)/t # invalid value encountered in divide
y2 = np.where(t == 0, 1, np.sin(t)/t)
#阶跃信号
y3 = np.heaviside(t,1)#阶跃
#正弦信号
y4  = np.sin(np.pi/4*t)
y4  = np.cos(np.pi/4*t)
#指数信号(连续的指数信号较少用，离散的指数信号用的较多)
a = 0.5 #改变a的数值和正负号，观察图像结果
z3 = np.power(a,t)
#自定义序列
y5 = np.array([1,2,3,3,2,1,2,3,4,3,2,4,3,2,1,2,3,2,1,2])
'''绘图，注意选择所需的信号替换语句中的信号'''
plt.figure()#新建绘图
plt.grid() #显示网格
#plt.plot(t, y1) #如果是连续信号，则绘制折线图
plt.stem(t, y5) #如果是离散信号，则绘制茎叶图
plt.show() # 显示
