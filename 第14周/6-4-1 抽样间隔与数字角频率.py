from scipy import signal
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftshift, fftfreq

'''抽样参数'''
# 定义抽样周期
T = 1 / 4  # cos信号周期 T
# 演示参数
t_length = 10  # 信号的实际时间长度
sample_freq = 1024
sample_interval = 1 / sample_freq  # 模拟连续信号的采样间隔
'''
定义t、f
所定义信号、抽样脉冲的实际样本点个数为: t_length * sample_interval
'''
t = np.arange(-0, t_length, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))

'''定义原信号 '''
# 演示不满足抽样定理情况下，可以加个小的相移0.125 * np.pi，会好看一些
sig1 = pow(0.5,t)*np.cos(2 * np.pi / T * t + 0.125 * np.pi)

'''
定义抽样脉冲pulse
假设奈奎斯特间隔（周期）Ts
则，在一个抽样周期内的实际样本个数为  Ts * sample_interval 或 Ts / sample_freq
为方便对位相乘，抽样脉冲的总的实际样本点个数应为：t_length * sample_interval
'''
def get_SamplePulse(ts):
    # 定义一个周期,注意unit_impulse要求参数为整数
    p1 = signal.unit_impulse(int(ts * sample_freq))
    # 循环拼接为一个长序列，再截断
    p = np.array([])
    while len(p) < len(t):
        p = np.append(p, p1)
    return p[:len(t)]

#定义不同的抽样脉冲，并进行抽样
ss_1 =  sig1 * get_SamplePulse(T / 8)
ss_2 =  sig1 * get_SamplePulse(T / 4)
ss_3 =  sig1 * get_SamplePulse(T / 8 * 3)
ss_4 =  sig1 * get_SamplePulse(T / 2)
ss_5 =  sig1 * get_SamplePulse(T / 4 * 3)

# 如果需要显示中文，则需要加入下面两行
ax = plt.figure(figsize=(16, 9),dpi = 100) # 新建绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 2)
plt.title(r"原信号$(0.5)^n\cdot\cos{(2\pi f_mt)}$", loc='left')
plt.xlabel(r'$time\rm{(s)}$',  loc='right')
plt.plot(t, sig1)

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(0, 2)
#plt.title(r"($f_s=8f_m$)数字角频率$\omega=2\pi f_m/fs=$$\pi /4$", loc='left')
plt.title(r"数字角频率为$\pi /4$($f_s=8f_m$)", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_1)
plt.plot(t, sig1, 'r--')

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 2)
plt.title(r"数字角频率为$\pi /2$($f_s=4f_m$)", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_2)
plt.plot(t, sig1, 'r--')

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(0, 2)
plt.title(r"数字角频率为$3\pi /4 $($f_s=3f_m /8$)", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_3)
plt.plot(t, sig1, 'r--')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 2)
plt.title(r"数字角频率为$\pi$($f_s=2f_m /8$)，等价于$(-0.5)^n$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ss_4)
plt.plot(t, sig1, 'r--')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(0, 2)
plt.title(r"数字角频率为$3\pi /2$($f_s=3f_m /4$) 不满足抽样定理！", loc='left')
plt.xlabel(r'$time\rm{(s)}$',  loc='right')
plt.plot(t, ss_5)
plt.plot(t, sig1, 'r--')

plt.suptitle("抽样频率与数字角频率($\omega=2\pi f_m/fs=$$\pi /4$)")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
