import matplotlib.pylab as plt  # 绘制图形
import numpy as np

'''
结论：
matplotlib画折线图的方式和x轴数据的排列顺序有关
'''

x = [1,2,3,4,5,-5,-4,-3,-2,-1]
y = [1,2,3,4,5, 6, 7, 8, 9, 10]
#调整横坐标顺序，相应（根据实际情况）调整y轴顺序
x1 = [-5,-4,-3,-2,-1,1,2,3,4,5]
y1 = [6, 7, 8, 9, 10,1,2,3,4,5 ]
plt.figure()#新建绘图
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题
plt.grid()  # 显示网格
plt.plot(x,y)
#plt.plot(x1,y1)
plt.show()