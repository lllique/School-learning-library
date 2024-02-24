import matplotlib.pylab as plt  # 绘制图形
import numpy as np

# 定义周期
T = 1
w1 = 2 * np.pi / T

# 范围
t = np.arange(-5 * T, 5 * T, 0.01)
#todo 可以修改谐波个数，查看叠加效果
n = np.arange(1, 50) #谐波个数

# 记录各次谐波的叠加情况
f = np.ones_like(t) / T #相当于直流分量
harms = []  # 记录各次谐波

# 画幅度频谱图
plt.grid()  # 显示网格
plt.xlim(-1.5,1.5)
for i in n:
    f_harm = 2 * np.cos(i*w1*t) / T
    plt.plot(t, abs(f_harm),linewidth = 0.2)
    f = f+ f_harm
#画出叠加之后的图
plt.plot(t, abs(f))
plt.show()
