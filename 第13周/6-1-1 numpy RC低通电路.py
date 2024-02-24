from numpy.fft import fftfreq, fftshift, fft
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

'''
时域分析时，a = 1/RC，即1/a为时间常数，当t=(3~5)
频域分析时，a = 1/RC，即为低通滤波器的截止（角）频率（半功率点）,截至频率则为a/2pi
'''
a = 1000  # a = 1/RC
sample_freq = 8000
sample_interval = 1 / sample_freq
t = np.arange(0, 100 / a, sample_interval)  # 相当于20倍时间常数的长度
# 这是一个低通电路
lpf = ([0, a], [1, a])
# 求冲激响应，并自动确定一个适合的时间轴t
t, ht = signal.impulse(lpf, T=t)
# 如果直接定义ht
# ht = a * np.exp(-a*t)
'''求HW的方法
ht的傅里叶变换就是HW
验证：可以直接定义正确的系统函数，并对比幅度相位谱
# Hw = a / (1j*2*np.pi*f + a) 
'''
f = fftshift(fftfreq(len(t), sample_interval))  # fft的双边频域坐标
Hw = fftshift(fft(ht)) * sample_interval
Hw_amp = np.abs(Hw)
Hw_ang = np.angle(Hw)

# 绘图
fig = plt.figure()
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(311)
plt.grid()  # 显示网格
plt.xlim(0, 5 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)

plt.subplot(312)
plt.grid()  # 显示网格
plt.xlim(-a / 2, a / 2)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(j\omega)|$', loc='left')
plt.plot(f, Hw_amp)
# 在半功率点绘制一条虚线(Hw最大值 除以根号2) * np.ones，np.ones的长度和频轴f相同
plt.plot(f, np.max(Hw_amp) / np.sqrt(2) * np.ones(len(f)), ls='--', c='red')
# 在-1/rc画一条竖线
plt.axvline(x=a / 2 / np.pi, ls='--', c='r')

plt.subplot(313)
plt.grid()  # 显示网格
plt.xlim(-a / 2, a / 2)  # 显示范围够用即可，截止频率为a/2pi（Hz），范围显著超出截止频率即可
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$\phi(j\omega)$', loc='left')
plt.plot(f, Hw_ang)
# 理论上相位偏转-pi/4
plt.plot(f, -np.pi / 4 * np.ones(len(f)), ls='--', c='red')
# 在半功率点画竖线
plt.axvline(x=a / 2 / np.pi, ls='--', c='r')
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)
plt.ylim(-1.6,1.6)#如果y坐标设置的过多，还可以用ylim再卡一下范围

plt.tight_layout()
plt.show()

'''-------进一步查看滤波特性（响应能力）-------'''
# 定义一个信号
et = np.sin(0.5 * a * t) + np.sin(10 * a * t)
rt = np.convolve(et, ht, mode='same') * sample_interval  # 注意，这样会导致信号两端都被截断，但不影响显示（影响初相位）

# 激励信号频谱
Ew = fftshift(fft(et))
Ew_amp = np.abs(Ew) * sample_interval
# 响应信号频谱
Rw = fftshift(fft(rt))
Rw_amp = np.abs(Rw) * sample_interval

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 40 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$e(t)$', loc='left')
plt.plot(t, et)

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-sample_freq / 4, sample_freq / 4)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|E(j\omega)|$', loc='left')
plt.plot(f, Ew_amp)

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 5 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-sample_freq / 4, sample_freq / 4)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(j\omega)|$', loc='left')
plt.plot(f, Hw_amp)
# 在-1/rc画一条竖线
plt.axvline(x=a / 2 / np.pi, ls='--', c='r')
plt.axvline(x=-a / 2 / np.pi, ls='--', c='r')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 40 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$r(t)$', loc='left')
plt.plot(t, rt)  # 注意截短

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-sample_freq / 4, sample_freq / 4)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|R(j\omega)|$', loc='left')
plt.plot(f, Rw_amp)

plt.tight_layout()
plt.show()
