import numpy as np
import matplotlib.pylab as plt  # 绘制图形

x = np.arange(-10.0, 10.0, 0.1)  # 采样点：取-10.0到10.0，间隔为0.1

#定义哈维赛德函数
y1 = np.array(x > 0).astype(int)  # np.array(x > 0)输出True 和False,然后.astype(int)将他们转换为1和0
y2 = np.piecewise(x,[x<0,x>=0],[0,1]).astype(int)  # x:对x进行判断   [x<0,x>=0]判断条件   [0,1]输出值
y3 = np.heaviside(x,1/2)  # 0的时候取值1/2
y4 = np.hstack([np.zeros(100) ,np.ones(100)])  #拼接 100个0 和 100个1
y5 = np.append(np.zeros(100),np.ones(100))
print("y=",y5)

#定义门函数
gate = np.array(np.logical_and(x <= 1 , x >= -1) ).astype(int)  # 生成阶跃函数
gate1 = np.array(x >= -1).astype(int) - np.array(x > 1).astype(int)
gate2 = np.piecewise(x,[x<-1,x>1,np.logical_and(x>=-1, x <= 1)],[0,0,1]).astype(int)  # 生成阶跃函数
gate3 = np.piecewise(x, [x < -1, x >= -1, x > 1], [0, 1, 0])
gate4 = np.piecewise(x, [x >= -1, x > 1], [1, 0, 0])  #默认值
gate5 = np.heaviside(x+1,1) - np.heaviside(x-1,1)
print("gate=",gate)

#运算对齐问题
y5 = np.hstack([np.zeros(100) ,np.ones(101)])
y6 = y4 + gate4
print("对齐运算:",y6)

#分段函数
gate6 = np.piecewise(x, [x >= 0, x >= 1, x >= 2, x >= 3], [lambda x: x, 1, lambda x: 3 - x, 0, 0])  #需要lambda表达式方法定义分段函数
#gate = np.piecewise(x, [x >= 0, x >= 1, x >= 2, x >= 3], [x, 1, 3 - x, 0, 0])

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
gate7 = np.array([cut(i) for i in x])


plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题

plt.figure()#新建绘图
plt.subplot(211) #子图1
plt.grid() #显示网格
plt.plot(x, y1)

plt.subplot(212) #子图2
plt.grid() #显示网格
plt.plot(x, gate)

plt.show()  # 显示
