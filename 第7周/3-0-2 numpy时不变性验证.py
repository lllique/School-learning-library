import numpy as np
import matplotlib.pylab as plt  # 绘制图形
from scipy.ndimage import shift

#原始区间
tao = -5
n = np.arange(0, 20, 1)
n_ds = np.arange(0, 10, 1)#画图用
#原始信号
x = np.sin(np.pi * n / 16)
print("原始序列：",x)
# 先经过系统，进行平移
y_1 = x[::2]#系统
y_1 = shift(y_1, tao * 1)#时移
# 先进行平移，在经过系统
x2 = shift(x, tao * 1)
y_2 = x2[::2]#系统
#支持中文
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题

plt.figure()#新建绘图
plt.subplot(211) #子图1
plt.title("现经过系统再时移", loc='left')
plt.grid() #显示网格
plt.stem(n_ds, y_1)

plt.subplot(212) #子图2
plt.grid() #显示网格
plt.title("先时移再经过系统", loc='left')
plt.stem(n_ds, y_2)

plt.tight_layout()
plt.show()  # 显示