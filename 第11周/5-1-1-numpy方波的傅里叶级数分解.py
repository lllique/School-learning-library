import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

# 定义方波
T1 = 2
w1 = 2 * np.pi / T1
tao = 0.6 * T1
n1 = np.arange(1, 6)  # 计算哪些谐波分量
t = np.arange(-2 * T1, 2 * T1, 0.01)  # 时间轴

# 定义一个周期方波
Gate = 0.5 * signal.square(w1 * (t + tao/2), duty=tao/T1) + 0.5  # 周期方波，duty为占空比
# 偶函数 从0到1的方波

# 直流分量幅度
c0 = tao / T1 * np.ones(len(t))


# 计算任意谐波分量的幅度
def harmonic(n, t):
    return 2 / (n * np.pi) * np.sin(n * w1 * tao/2) * np.cos(n * w1 * t)


plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 依次画图
plt.subplot(321)
plt.grid()
plt.plot(t, c0)
plt.plot(t, Gate, 'r--')
plt.title("直流分量")

for i in n1:
    plt.subplot(3, 2, i + 1)
    plt.grid()
    plt.plot(t, harmonic(i, t))
    plt.plot(t, Gate, 'r--')
    plt.title("%d次谐波" % i)

plt.tight_layout()
plt.show()
