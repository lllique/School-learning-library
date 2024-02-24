import numpy as np
import matplotlib.pylab as plt  # 绘制图形


t1 = np.arange(-10.0, 10.0, 0.1)
t2 = np.linspace(-10, 10, 200)
print(len(t1), len(t2))
print(t1[199],t2[199])
print(t1)
print(t2)
y1 = np.sinc(t1/np.pi)
y2 = np.exp(-0.5*t1)*np.sin(2*np.pi*t1)

np.seterr(divide='ignore', invalid='ignore')#numpy忽略除以零的警告
#定义离散信号
#注意区间问题
n = np.arange(-10.0, 10.0, 1) #一共20个点，最后是开区间  实际上是一个数组
n1 = np.linspace(-10.0, 10.0, 20)#一共20个点，最后是闭区间

'''定义sa函数的方法'''
z1 =np.sinc(n/np.pi)
z2 = np.sin(n)/n # invalid value encountered in divide
z3 = np.where(n == 0, 1, np.sin(n)/n) #如果n == 0为True,那么函数值是1.否则为np.sin(n)/n


z1 = np.array([1,2,3,3,2,1,2,3,4,3,2,4,3,2,1,2,3,2,1,2,0])#有限长序列 20个点
z2 = np.heaviside(n,1)#阶跃
z3 = np.power(0.5,n)
z4  = np.sin(np.pi/4*n)

plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题

plt.figure()#新建绘图
plt.subplot(211) #子图1
plt.grid() #显示网格
plt.plot(t1, y1)  #折线图

plt.subplot(212) #子图2
plt.grid() #显示网格
plt.stem(n, z1)   #茎叶图

plt.tight_layout() #紧凑布局，防止标题重叠
plt.show()  # 显示
