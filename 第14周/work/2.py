import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from numpy.fft import fftshift,fftfreq,fft

a = 1000
sample_freq = 8000
sample_interval = 1 / sample_freq
length = 1 #时长

t = np.arange(0,length,sample_interval)
lpf = ([0, a], [1, a])
t , ht = signal.impulse(lpf,T=t)

f = fftshift(fftfreq(len(t),sample_interval))


num = {
    '1': [697, 1209],
    '2': [697, 1336],
    '3': [697, 1477],
    'A': [697, 1633],
    '4': [770, 1209],
    '5': [770, 1336],
    '6': [770, 1477],
    'B': [770, 1633],
    '7': [852, 1209],
    '8': [852, 1336],
    '9': [852, 1477],
    'C': [852, 1633],
    '*': [941, 1209],
    '0': [941, 1336],
    '#': [941, 1477],
    'D': [941, 1633],
}

def getvwavebynum(numstr):
    sin1 = np.sin(2 * np.pi * num[numstr][0] * t)
    sin2 = np.sin(2 * np.pi * num[numstr][1] * t)
    DTMFsin = 10 * sin1 + 10 * sin2
    return DTMFsin

sig = getvwavebynum('4')
r_sig = np.convolve(sig,ht,mode='same') * sample_interval


# system = ([0,a],[1,a])
# t,ht = signal.impulse(system,T = t)

# 频轴
f = fftshift(fftfreq(len(t), sample_interval))

fw = fftshift(fft(sig))
fw_amp = np.abs(fw) * sample_interval
r_fw = fftshift(fft(r_sig))
r_fw_amp = np.abs(r_fw) * sample_interval



plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 40 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.plot(t, sig)

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-sample_freq / 4, sample_freq / 4)
plt.plot(f, fw_amp)

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 5 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.plot(t, ht)

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-sample_freq / 4, sample_freq / 4)
plt.plot(f, r_fw_amp)

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 40 / a)  # 显示区间为5倍时间常数，理论上已经衰减到最大值的1%以内
plt.plot(t, r_sig)  # 注意截短

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-sample_freq / 4, sample_freq / 4)
plt.plot(f, r_fw)

plt.tight_layout()
plt.show()