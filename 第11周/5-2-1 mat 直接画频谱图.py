import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftshift

# 公共参数
E = 1
tao = 1
sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
t = np.arange(-10 * tao, 10 * tao, sample_interval)
# 定义时域信号：门函数
ft = E * np.heaviside(t + tao / 2, 1) - E * np.heaviside(t - tao / 2, 1)
# 定义时域信号：指数函数
ft = tao * np.exp(-tao * t) * np.heaviside(t, 1)
'''
fft
1，由于时间轴为对称区间，所以先对其进行fftshift，再做fft，
2. 注意要用fftshift之前的ft画图
'''
ft_shift = fftshift(ft)
# 显示中文
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(311)
plt.grid()  # 显示网格
plt.title("时域信号")
plt.xlabel('time(s)', loc='right')
plt.plot(t, ft)

plt.subplot(312)
plt.grid()  # 显示网格
plt.xlim(-3 / tao, 3 / tao)
plt.title("幅度谱（演示）")
plt.magnitude_spectrum(ft_shift, Fs=sample_freq, sides='twosided')
'''
可选参数：
scale ='dB',分贝坐标
sides = 'onesided'在概念上有点问题，幅度没有乘以2，只是画一半谱线
'''

# 双边谱
plt.subplot(313)
plt.grid()  # 显示网格
plt.xlim(-3 / tao, 3 / tao)
plt.title("相位谱")
plt.angle_spectrum(ft_shift, Fs=sample_freq, sides='twosided')
plt.tight_layout()
plt.show()

'''
https://matplotlib.org/2.0.2/api/pyplot_api.html

angle_spectrum
Plots the angles of the corresponding frequencies.
phase_spectrum (解卷绕后的结果)
Plots the phase (unwrapped angle) of the corresponding frequencies.
'''
