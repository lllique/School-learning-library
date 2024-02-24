import numpy as np
import matplotlib.pylab as plt  # 绘制图形

'''注意：如果区间不是对称的，例如在（1，10）之间，则需要手动创建新坐标轴'''
x = np.linspace(-10.0, 10.0, 200)  # 采样点：取-10.0到10.0，间隔为0.1
y = np.piecewise(x, [x >= 1, x >= 2, x >= 3], [ 1, lambda x: 3 - x, 0, 0])
#翻转方法1
#y2 =  y1[::-1]
#翻转方法2，要求numpy版本在1.12版以上
y_flip =  np.flip(y)
#计算奇偶分量
y_even = 0.5 * (y + y_flip)
y_odd = 0.5 * (y - y_flip)

plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题


plt.figure()#新建绘图
plt.subplot(221) #子图1
plt.grid() #显示网格
plt.title("f(t)")
plt.plot(x, y)

plt.subplot(222) #子图2
plt.grid() #显示网格
plt.title("f(-t)")
plt.plot(x, y_flip)

plt.subplot(223) #子图2
plt.grid() #显示网格
plt.title("f_even")
plt.plot(x, y_even)

plt.subplot(224) #子图2
plt.grid() #显示网格
plt.title("f_odd")
plt.plot(x, y_odd)

plt.tight_layout() #如果不加这一句，可能导致标题和图重叠
plt.show()  # 显示
