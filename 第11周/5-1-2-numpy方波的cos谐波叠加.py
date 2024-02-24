import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

# 定义方波
T1 = 1
w1 = 2 * np.pi / T1
tao = 0.5
# 范围
t = np.arange(-2 * T1, 2 * T1, 0.01)
n = np.arange(0, 12)
# 定义一个周期方波
Gate = 0.5 * signal.square(w1 * (t + tao/2), duty=tao/T1) + 0.5  # 周期方波，duty为占空比

#叠加谐波的函数
def harmonic(n, t):
    c0 = tao / T1 * np.ones(len(t)) #直流分量
    sum_f_cn = c0  # 直流分量
    # 利用for循环，在ft基础上依次叠加方波，叠加个数由n决定，注意开闭区间问题
    for i in range(1, n + 1):
        Cn = 2 * tao/ T1 * np.sinc(i  * tao / T1)
        sum_f_cn = sum_f_cn + Cn * np.cos(i * w1 * t)
    return sum_f_cn

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

for i in range(1, 7):
    plt.subplot(3, 2, i)
    plt.grid()  # 显示网格
    plt.title("直流+%d个谐波" % (i * 2), loc='left')
    plt.plot(t, Gate, 'r--')  # 对照组方波
    plt.plot(t, harmonic(i * 2, t))  # 谐波叠加情况
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
