import numpy as np
from matplotlib import patches
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

'''一个重根系统'''
b = [1, 0.5, 0, 0]
a = [1, -1.25, 0.75, -0.125]

dsys = signal.dlti(b, a)
# 零极点
p = dsys.poles
z = dsys.zeros  # [-0.5  0.   0. ]

'''获得非重复的元素，以及元素的个数'''
z, cz = np.unique(z, return_counts=True)  # [-0.5  0. ] [1 2]
p, cp = np.unique(p, return_counts=True)

# 手动画图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.title('零极点')
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
# 零点
for i in range(len(z)):
    plt.scatter(z[i].real, z[i].imag, marker='o', c='none', edgecolors='b')
    if cz[i] > 1:
        plt.text(z[i].real + 0.02, z[i].imag + 0.02, cz[i])
# 极点
for i in range(len(p)):
    plt.scatter(p[i].real, p[i].imag, marker='x', c='b')
    if cp[i] > 1:
        plt.text(p[i].real + 0.02, z[i].imag + 0.02, cp[i])

# 画个单位圆
ax1 = plt.subplot()
unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')
ax1.add_patch(unit_circle)
ax1.axis('scaled')  # 保持坐标系统正圆

plt.tight_layout()
plt.show()
