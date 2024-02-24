import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sgn

sample_freq = 4096  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔(deltaT)
T = 2  # 实际是半个周期
tao = 1  # 脉冲宽度
# 定义区间
t = np.linspace(0, T, T * sample_freq)
# 定义e(t)和h(t)
e = np.heaviside(t, 1) - np.heaviside(t - tao, 1)
h = np.heaviside(t, 1) - np.heaviside(t - tao, 1)
# 时域卷积
#裁切之后，实际只剩下从时间从1到3的数据
r1 = np.convolve(e, h, mode='same') * sample_interval
#此时卷积范围应该是0到4，但实际有效数据是从0到2，从2到4是全零的
r2 = np.convolve(e, h, mode='full') * sample_interval
r2 = r2[:len(t)]#把后面的零裁切掉

plt.rcParams['font.serif'] = ['SimSun']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
plt.figure()
plt.subplot(2, 2, 1)  # 画布位置1
plt.title("e(t)", loc='left')
plt.plot(t, e, c='r')
plt.grid()

plt.subplot(2, 2, 2)
plt.title("h(t)", loc='left')
plt.plot(t, h, c='g')
plt.grid()

plt.subplot(2,2, 3)
plt.title("r(t)-same mode", loc='left')
plt.plot(t, r1, c='purple')
plt.grid()

plt.subplot(2, 2, 4)
plt.title("r(t)-full mode", loc='left')
plt.plot(t, r2, c='purple')
plt.grid()
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
