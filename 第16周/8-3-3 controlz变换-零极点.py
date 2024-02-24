import numpy as np
import control as ct
import matplotlib.pylab as plt  # 绘制图形

b = [1, 0.5, 0, 0]
a = [1, -1.25, 0.75, -0.125]

# 构造一个分式,True参数构造离散系统
sys = ct.tf(b, a, True)

plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
ct.bode_plot(sys, dB=True, Hz=True, grid=True)
plt.show()

zp = ct.pzmap(sys, plot=True, title="零极点图", grid=True)
plt.show()

print(zp)  # 显示零极点结果
