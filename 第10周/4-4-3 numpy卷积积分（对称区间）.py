import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sgn

sample_freq = 4096  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔(deltaT)
T = 5  # 实际是半个周期
tao = 1  # 脉冲宽度
# 定义区间
t = np.linspace(-T, T, 2 * T * sample_freq)
#t = np.arange(-T,T+sample_interval,sample_interval)
# 定义e(t)和h(t)
e = np.heaviside(t + tao, 1) - np.heaviside(t - tao, 1)
h = np.heaviside(t + tao, 1) - np.heaviside(t - tao, 1)
# 时域卷积
t1 = datetime.datetime.now()
r = np.convolve(e, h, mode='same') * sample_interval
t2 = datetime.datetime.now()
print("时域卷积运算时间：", t2 - t1)

# 对比：FFT卷积
t1 = datetime.datetime.now()
r = np.fftconvolve(e, h, mode='same') * sample_interval
t2 = datetime.datetime.now()
print("利用FFT进行卷积的运算时间：", t2 - t1)

plt.rcParams['font.serif'] = ['SimSun']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
plt.figure()
plt.subplot(3, 1, 1)  # 画布位置1
plt.title("e(t)", loc='left')
plt.plot(t, e, c='r')
plt.grid()

plt.subplot(3, 1, 2)
plt.title("h(t)", loc='left')
plt.plot(t, h, c='g')
plt.grid()

plt.subplot(3, 1, 3)
plt.title("r(t)", loc='left')
plt.plot(t, r, c='purple')
plt.grid()

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
