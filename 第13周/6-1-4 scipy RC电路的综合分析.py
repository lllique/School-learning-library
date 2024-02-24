from math import sqrt

from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

'''
时域分析时，a = 1/RC，即1/a为时间常数，当t=(3~5)时，视为充放电结束
频域分析时，a = 1/RC，即为低通滤波器的截止（角）频率（半功率点）,截至频率则为：a/2pi
'''
a = 1000  # a = 1/RC
sample_freq = 8000
sample_interval = 1 / sample_freq
'''统一画图坐标t、f和Omega'''
t = np.arange(0, 100 / a, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))  # fft的双边频域坐标
omega = f * 2 * np.pi
'''定义系统'''
# 这是一个低通电路
lpf = ([0, a], [1, a])
# 这是一个高通电路
hpf = ([1, 0], [1, a])
'''系统的时域分析，求冲激响应'''
t, ht = signal.impulse(lpf, T=t)
'''
注意：
于低通电路，可以直接用h(t)做卷积或求fft求H(jw)，结果均为正确的，
但是对于高通电路，由于其h(t)中带有冲激项，但impluse方法无法表达出来，
如果使用h(t)做卷积，或fft求H(jw)，则结果都有误，所以这里直接使用freqresp方法求H(jw)。
'''

'''系统的频域分析，注意freqresp输入输出的横坐标实际为角频率 [rad/s]'''
omega, Hw = signal.freqresp(lpf, omega)
Hw_amp = np.abs(Hw)  # 方法不是fft，这里也不用做幅度修正了
Hw_ang = np.angle(Hw)
# 绘图
plt.figure()
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

# 标注半功率点，首先指定要标注的点
xdata, ydata = a / 2 / np.pi, sqrt(2) / 2
# 定义一个引导线
arrowprops = dict(
    arrowstyle="->",
    # connectionstyle语句定义一个直角线，没有这一句默认是斜线
    # connectionstyle="angle,angleA=0,angleB=90,rad=10"
)
#进行标注
plt.annotate('半功率点', (xdata, ydata),
             xytext=(10, 35),  # 标注文本的位置
             textcoords='offset points',  # 表示xytext位置是相对于标注点的坐标
             arrowprops=arrowprops  # 画引导线
             )

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

plt.tight_layout()
plt.show()

'''-------进一步查看滤波特性（响应能力）-------'''
# 定义一个信号
et = np.sin(0.5 * a * t) + np.sin(10 * a * t)
# 激励信号频谱
Ew = fftshift(fft(et)) * sample_interval
Ew_amp = np.abs(Ew)
'''
在频域求响应
注意：此时的Hw是用freqresp直接求出的，相当于fft方法修正了幅度，且进行了fftshift，因此需要先进行反向处理
'''
Rw = Ew * Hw  # 注意此时的Ew和Hw都进行过幅度修正（* sample_interval），因此Rw也是相当于经过幅度修正的
rt = ifft(ifftshift(Rw / sample_interval))  # 先反向修正幅度，再反向修正坐标分布

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
