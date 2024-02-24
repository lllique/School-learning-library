import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift, fft

# 公共参数
E = 1
tao = 1
a = 2
sample_freq = 4096  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
# 时间轴
t = np.arange(-10 * tao, 10 * tao, sample_interval)
# 定义时域信号：门函数
ft = E * np.heaviside(t + tao / 2, 1) - E * np.heaviside(t - tao / 2, 1)
# 定义时域信号：指数函数
# ft = np.exp(-a * t) * np.heaviside(t, 1)

# 频轴
f = fftshift(fftfreq(len(t), sample_interval))
# 角频率轴
omega = f * 2 * np.pi
# 频谱
Fw = fftshift(fft(ft))  # 双边幅度谱,范围为正负sample_freq/2
# 模值为：np.abs(Fw * deltaT)
Fw_amp = np.abs(Fw * sample_interval)

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格

plt.subplot(311)
plt.grid()  # 显示网格
plt.title("原信号")
plt.xlim(-3 * tao, 3 * tao)
plt.xlabel('time(s)', loc='right')
plt.plot(t, ft)

plt.subplot(312)
plt.grid()  # 显示网格
plt.xlim(-3 * np.pi / tao, 3 * np.pi / tao)
plt.title("幅度谱$(f)$")
plt.xlabel('$frequency(Hz)$', loc='right')
# 利用magnitude_spectrum，直接用ft画图
plt.plot(f, Fw_amp)

plt.subplot(313)
plt.grid()  # 显示网格
plt.xlim(-3 * np.pi / tao, 3 * np.pi / tao)
plt.title(r"幅度谱$(\omega)$")
plt.xlabel(r'$Angular frequency(Rad/s)$', loc='right')
# 利用magnitude_spectrum，直接用ft画图
plt.plot(omega, Fw_amp)

plt.tight_layout()
plt.show()
