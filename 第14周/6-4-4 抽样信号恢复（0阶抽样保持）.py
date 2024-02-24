import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft
from scipy import signal

'''抽样参数'''
# 定义抽样周期
T = 1 / 4  # cos信号周期 T
# 演示参数
t_length = 10  # 信号的实际时间长度
sample_freq = 4096
sample_interval = 1 / sample_freq  # 模拟连续信号的采样间隔
'''
定义t、f
所定义信号、抽样脉冲的实际样本点个数为: t_length * sample_interval
'''
t = np.arange(-0, t_length, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))

'''
定义一个升余弦(1+cos(2pi/T* t) t∈(0,T).脉宽=T
第一过零点带宽为（4pi/T）,转为频率是1/T/2
'''
et = (0.5 + 0.5 * np.cos(2 * np.pi / T * t - np.pi)) * (np.heaviside(t, 1) - np.heaviside(t - T, 1))

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


# 定义抽样脉冲pulse
Ts = T / 8
# Ts = T / 2 #奈奎斯特抽样间隔
# Ts = T / 1.6 #不满足抽样定理
pulse = get_SamplePulse(Ts)

'''时域相乘得到抽样信号'''
sample_et = et * pulse

'''计算FFT'''
Ew = fftshift(fft(et)) * sample_interval
# PULSEw = fftshift(fft(pulse)) * sample_interval
SampleEw = fftshift(fft(sample_et)) * sample_interval

'''------------------------------------------------------------------------'''
'''抽样信号恢复'''
'''从频域定义理想低通'''
# lpf截止频率应该大于1/T，且小于（1/Ts - 1/T）
f_l = 1 / Ts / 2
ht = np.heaviside(t, 1) - np.heaviside(t - Ts, 1)
'''抽样信号通过0阶抽样保持'''
recon_et = np.convolve(sample_et, ht)[:len(t)]

# HW 高度乘以Ts，这个是抽样要求,否则还原出来的信号高度和原信号不一致
# Hw2_amp = Ts / sample_interval * (np.heaviside(f + f_l, 1) - np.heaviside(f - f_l, 1))

# 恢复的信号（时域）
RECON_Ew = fftshift(fft(recon_et * sample_interval))
'''绘图'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(221)
plt.grid()  # 显示网格
plt.xlim(0, 1)
plt.title("抽样信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, sample_et)
plt.plot(t, et, 'r--')

# 双边谱
plt.subplot(222)
plt.grid()  # 显示网格
plt.xlim(-5 * T / Ts, 5 * T / Ts)
plt.title("抽样信号（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(SampleEw))
# plt.plot(f, Hw2_amp / Ts * sample_interval * np.max(np.abs(SampleEw)), 'r--') #修正了高度使得显示更美观


plt.subplot(223)
plt.grid()  # 显示网格
plt.xlim(0, 1)
plt.title("抽样信号还原（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, recon_et)
# 双边谱
plt.subplot(224)
plt.grid()  # 显示网格
plt.xlim(-5 * T / Ts, 5 * T / Ts)
plt.title("抽样信号还原（频域）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(RECON_Ew))

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
