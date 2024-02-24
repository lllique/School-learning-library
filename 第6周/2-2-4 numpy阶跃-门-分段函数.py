import numpy as np
import matplotlib.pylab as plt  # 绘制图形

'''定义阶跃信号的多种方法'''
t = np.arange(-10.0, 10.0, 0.1)  # 采样点：取-10.0到10.0，间隔为0.1
y1 = np.array(t > 0).astype(int)
y2 = np.piecewise(t, [t < 0, t >= 0], [0, 1]).astype(int)
y3 = np.heaviside(t, 1 / 2)
#下面两种方法注意匹配样本点个数，否则无法和x结合画图
y4 = np.hstack([np.zeros(100) ,np.ones(100)])
y5 = np.append(np.zeros(100),np.ones(100))
print("y=",y1)

'''定义门函数的多种方法'''
gate1 = np.array(np.logical_and(t <= 1, t >= -1)).astype(int)
gate2 = np.array(t >= -1).astype(int) - np.array(t > 1).astype(int)
gate3 = np.piecewise(t, [t < -1, t > 1, np.logical_and(t >= -1, t <= 1)], [0, 0, 1]).astype(int)  # 生成阶跃函数
gate4 = np.piecewise(t, [t < -1, t >= -1, t > 1], [0, 1, 0])
gate5 = np.piecewise(t, [t >= -1, t > 1], [1, 0, 0])
gate6 = np.heaviside(t + 1, 1) - np.heaviside(t - 1, 1)
print("gate=",gate1)

'''定义分段函数，方法1'''
p1 = np.piecewise(t, [t >= 0, t >= 1, t >= 2, t >= 3],
                     [lambda t: t, 1, lambda t: 3 - t, 0, 0])
'''定义分段函数，方法2'''
def cut(x):
    if 0 > x >= -1:
        y = abs(x)
    elif -1 > x >= -2:
        y = 1
    elif -2 > x >= -3:
        y = 3 - abs(x)
    else:
        y = 0
    return y
p2 = np.array([cut(i) for i in t])


plt.figure()#新建绘图
plt.grid() #显示网格
plt.plot(t, y1) #如果是连续信号，则绘制折线图
#plt.stem(t, y5) #如果是离散信号，则绘制茎叶图
plt.show()  # 显示
