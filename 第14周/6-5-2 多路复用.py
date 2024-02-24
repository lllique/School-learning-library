import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft

# 调制解调参数
# 调制解调参数
fc1 = 1e4  # 第一路调制载波频率（Hz）
fc2 = 2e4  # 第一路调制载波频率（Hz）
fcc = 2 * 2000  # 解调低通滤波器宽度
# 演示参数
sample_freq = fc2 * 4  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
t_length = 2  # 2秒

'''定义时间和频率轴'''
# 定义总区间
t = np.arange(0, t_length, sample_interval)
# 定义频域长度区间
f = fftshift(fftfreq(len(t), sample_interval))
'''DTMF的频率组合'''
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


# 函数：生成对应的sin和合并后的波形
def getNumWave(numstr):
    # 注意这和之前定义方式有所不同，这里定义的是模拟角频率
    t1 = np.arange(0, 0.5, sample_interval)
    sin1 = np.sin(2 * np.pi * num[numstr][0] * t1)  # 生成低频部分正弦波，固定长度1秒
    sin2 = np.sin(2 * np.pi * num[numstr][1] * t1)  # 生成高频部分正弦波，固定长度1秒
    DTMFsin = sin1 + sin2  # 组合一下
    # 返回值为半秒的声音和半秒的空白
    return np.append(DTMFsin, np.zeros_like(t1))


'''定义第一路信号，DTMF 1和2'''
sig1 = getNumWave('1')
sig1 = np.append(sig1, getNumWave('2'))
'''定义第二路信号，DTMF 3和4'''
sig2 = getNumWave('3')
sig2 = np.append(sig2, getNumWave('4'))
'''定义载波'''
carrier1 = np.cos(2 * np.pi * fc1 * t)
carrier2 = np.cos(2 * np.pi * fc2 * t)

'''第一路调制过程'''
mod_sig1 = sig1 * carrier1
# 原信号频谱
sig1_fft_amp = fftshift(np.abs(fft(sig1)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2
# 载波信号频谱
carrier1_fft_amp = fftshift(np.abs(fft(carrier1)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2
# 调制信号频谱
mod_sig1_fft_amp = fftshift(np.abs(fft(mod_sig1)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2

# 第一组图
fontsize = 14
ax = plt.figure(figsize=(16, 9), dpi=100)
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = fontsize - 3  # 字体大小

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("第一路信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, sig1, 'r')

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-fc1 * 1.2, fc1 * 1.2)
plt.title(r"第一路信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, sig1_fft_amp, 'r')

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title(r"第一路载波", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, carrier1, 'c')
# 双边谱
plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-fc1 * 1.2, fc1 * 1.2)
plt.title(r"第一路载波频谱（$f_{c1}=%d\rm{Hz}$）" % fc1, loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, carrier1_fft_amp, 'c')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("第一路已调信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, mod_sig1, 'violet')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-fc1 * 1.2, fc1 * 1.2)
plt.title("第一路已调信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, mod_sig1_fft_amp, 'violet')

plt.suptitle("多路复用（1）第一路信号调制")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# ax.savefig(r"多路复用-1-第一路信号调制.jpg", dpi=200)

'''第二步：第二路调制'''
'''第二路调制过程'''
mod_sig2 = sig2 * carrier2
# 原信号频谱
sig2_fft_amp = fftshift(np.abs(fft(sig2)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2
# 载波信号频谱
carrier2_fft_amp = fftshift(np.abs(fft(carrier2)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2
# 调制信号频谱
mod_sig2_fft_amp = fftshift(np.abs(fft(mod_sig2)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2

# 第二组图
ax = plt.figure(figsize=(16, 9), dpi=100)
plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("第二路信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, sig2, 'darkred')

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 1.2, fc2 * 1.2)
plt.title(r"第二路信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, sig2_fft_amp, 'darkred')

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("第二路载波", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, carrier2, 'darkcyan')

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 1.2, fc2 * 1.2)
plt.title(r"第二路载波频谱（$f_{c2}=%d\rm{Hz}$）" % fc2, loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, carrier2_fft_amp, 'darkcyan')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("第二路已调信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, mod_sig2, 'blueviolet')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 1.2, fc2 * 1.2)
plt.title("第二路已调信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, mod_sig2_fft_amp, 'blueviolet')

plt.suptitle("多路复用（2）第二路信号调制")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# ax.savefig(r"多路复用-2-第二路信号调制.jpg", dpi=200)

'''第三步 混合并传输信号'''
mix_sig = mod_sig1 + mod_sig2  # 两路调制信号混叠
mix_sig_fft = fftshift(fft(mix_sig)) * sample_interval# 双边幅度谱,范围为正负sample_freq/2
mix_sig_fft_amp = np.abs(mix_sig_fft)

'''第四步，定义带通滤波器'''
'''在频域定义理想带通1,以fc1为中心，带宽为2000*2'''
BPF1 = np.heaviside(f + (fc1 + 2000), 1) - np.heaviside(f + (fc1 - 2000), 1) + \
       np.heaviside(f - (fc1 - 2000), 1) - np.heaviside(f - (fc1 + 2000), 1)

'''在频域定义理想带通2,以fc2为中心，带宽为2000*2'''
BPF2 = np.heaviside(f + (fc2 + 2000), 1) - np.heaviside(f + (fc2 - 2000), 1) + \
       np.heaviside(f - (fc2 - 2000), 1) - np.heaviside(f - (fc2 + 2000), 1)

'''第四步 过带通分离信号'''
# 频域相乘，得到分离后信号的频域形式
BPF_sig1_fft = mix_sig_fft * BPF1
BPF_sig1_fft_amp = np.abs(BPF_sig1_fft)
BPF_sig2_fft = mix_sig_fft * BPF2
BPF_sig2_fft_amp = np.abs(BPF_sig2_fft)
# 分离后信号的时域形式
BPF_sig1 = (ifft(ifftshift(BPF_sig1_fft / sample_interval)))
BPF_sig2 = (ifft(ifftshift(BPF_sig2_fft / sample_interval)))

'''第五步:解调并得到频谱'''
demod_sig1_fft = fft(BPF_sig1 * carrier1)
demod_sig2_fft = fft(BPF_sig2 * carrier2)

'''在频域定义一个低通，并进行滤波'''
LPF_HW = 2 * np.heaviside(f + fcc / 2, 1) - 2 * np.heaviside(f - fcc / 2, 1)

'''解调信号通过低通（频域相乘），再进行反变换'''
rt1 = ifft(demod_sig1_fft * ifftshift(LPF_HW)).real
rt2 = ifft(demod_sig2_fft * ifftshift(LPF_HW)).real

# 第三组图
ax = plt.figure(figsize=(16, 9), dpi=100)
plt.subplot(221)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("混合信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, mix_sig, 'indigo')

plt.subplot(222)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 1.2, fc2 * 1.2)
plt.title("混合信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, mix_sig_fft_amp, 'indigo')
plt.plot(f, np.max(mix_sig_fft_amp) * BPF1, c='r', ls='--')
plt.plot(f, np.max(mix_sig_fft_amp) * BPF2, c='darkred', ls='--')

plt.subplot(223)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("第一路信号解调还原", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt1, 'r')

plt.subplot(224)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("第二路信号解调还原", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt2, 'darkred')

plt.suptitle("多路复用（3）混合信号分离与解调")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# ax.savefig(r"多路复用-3-混合信号分离.jpg", dpi=200)

'''播放'''
import time
import sounddevice as sd
#第一路信号
sd.play(rt1, sample_freq)
time.sleep(t_length * 2)
#第二路信号
sd.play(rt2, sample_freq)
time.sleep(t_length)