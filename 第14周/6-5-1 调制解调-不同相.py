import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft

sample_freq = 4096  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
fm = 10 #信号频率
fc = 40  # 载波频率
# 直接计算FFT建议用linspace
# ----------------------

'''定义时间和频率轴'''
# 定义总区间
t = np.arange(0, 1, sample_interval)
# 定义频域长度区间
f = fftshift(fftfreq(len(t), sample_interval))
'''定义信号'''
sig = np.cos(2 * np.pi * fm * t)  # 采集的信号
# 调制载波
carrier = np.cos(2 * np.pi * fc * t)
'''调制过程'''
mod_sig = sig * carrier
'''解调过程'''
# 定义多种具有相位差的本地载波
carrier2_0 = np.cos(2 * np.pi * 40 * t + np.pi * 0.125)  # 解调载波1
carrier2_1 = np.cos(2 * np.pi * 40 * t + np.pi * 0.25)  # 解调载波1
carrier2_2 = np.cos(2 * np.pi * 40 * t + np.pi * 0.5)  # 解调载波2
carrier2_3 = np.cos(2 * np.pi * 40 * t + np.pi * 0.75)  # 解调载波3
carrier2_4 = np.cos(2 * np.pi * 40 * t + np.pi)  # 解调载波4
# 已调信号乘以本地载波,再作FFT
sig0_fft = fftshift(fft(mod_sig * carrier2_0))* sample_interval
sig1_fft = fftshift(fft(mod_sig * carrier2_1))* sample_interval
sig2_fft = fftshift(fft(mod_sig * carrier2_2))* sample_interval
sig3_fft = fftshift(fft(mod_sig * carrier2_3))* sample_interval
sig4_fft = fftshift(fft(mod_sig * carrier2_4))* sample_interval

'''在频域定义一个低通，并进行滤波'''
LPF_HW = 2 * np.heaviside(f + fm * 1.5 , 1) - 2 * np.heaviside(f - fm * 1.5, 1)
#反变换得到信号
RW0 = sig0_fft * LPF_HW
rt0 = ifft(ifftshift(sig0_fft * LPF_HW / sample_interval)).real
rt1 = ifft(ifftshift(sig1_fft * LPF_HW / sample_interval)).real
rt2 = ifft(ifftshift(sig2_fft * LPF_HW / sample_interval)).real
rt3 = ifft(ifftshift(sig3_fft * LPF_HW / sample_interval)).real
rt4 = ifft(ifftshift(sig4_fft * LPF_HW / sample_interval)).real

# -------------------绘图----------------------
# 字体大小
fontsize = 12
plt.figure()  # 新建绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = fontsize - 3  # 字体大小

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title("原信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, sig, "r--")

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.125\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt0)
plt.plot(t, sig, "r--")

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.25\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt1)
plt.plot(t, sig, "r--")

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.5\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt2)
plt.plot(t, sig, "r--")

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$0.75\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt3)
plt.plot(t, sig, "r--")

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(0, 0.5)
plt.title("解调信号（解调载波相位差为$\pi$）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt4)
plt.plot(t, sig, "r--")

plt.suptitle("解调载波具有相位差的影响")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# exit()
