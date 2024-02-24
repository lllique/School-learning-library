import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifftshift, ifft
import time
import sounddevice as sd

# 调制解调参数
fc = 1e4  # 调制载波频率（Hz）
fc2 = 1e4  # 解调载波频率（Hz） 1.2e4
theta = np.pi * 0  # 解调载波的相位差
fcc = 2 * 2000  # 解调低通滤波器宽度

# 演示参数
sample_freq = fc * 4  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
t_length = 5  # 5秒

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
    t1 = np.arange(0, 0.5, sample_interval)  # 0.5秒声音
    sin1 = np.sin(2 * np.pi * num[numstr][0] * t1)  # 生成低频部分正弦波，固定长度1秒
    sin2 = np.sin(2 * np.pi * num[numstr][1] * t1)  # 生成高频部分正弦波，固定长度1秒
    DTMFsin = sin1 + sin2  # 组合一下
    # 返回值为半秒的声音和半秒的空白
    return np.append(DTMFsin, np.zeros_like(t1))  # 再加0.5秒间隙


'''定义信号'''
sig = getNumWave('1')
sig = np.append(sig, getNumWave('2'))
sig = np.append(sig, getNumWave('3'))
sig = np.append(sig, getNumWave('4'))
sig = np.append(sig, getNumWave('5'))
'''定义载波'''
carrier = np.cos(2 * np.pi * fc * t)
'''调制过程'''
mod_sig = sig * carrier
'''计算FFT'''
# 原信号频谱
sig_fft_amp = fftshift(np.abs(fft(sig)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2
# 载波信号
carrier_fft_amp = fftshift(np.abs(fft(carrier)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2
# 调制信号频谱
mod_sig_fft_amp = fftshift(np.abs(fft(mod_sig)) * sample_interval)  # 双边幅度谱,范围为正负sample_freq/2

# 作图
fontsize = 14
ax = plt.figure(figsize=(16, 9), dpi=100)
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = fontsize - 3  # 字体大小

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("原信号", fontsize=fontsize, loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, sig, 'r')
# 双边谱
plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-fc * 1.2, fc * 1.2)
plt.title("原信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, sig_fft_amp, 'r')

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title(r"载波（$f_c=%.1f \rm{kHz}$）" % (fc / 1e3), loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, carrier)

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-fc * 1.2, fc * 1.2)
plt.title(r"载波（$f_c=%.1f \rm{kHz}$）" % (fc / 1e3), loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, carrier_fft_amp)

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("已调信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, mod_sig, 'darkviolet')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-fc * 1.2, fc * 1.2)
plt.title("已调信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, mod_sig_fft_amp, 'darkviolet')

plt.suptitle("调制过程")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# ax.savefig(r"%s 调制过程.jpg"%namestr, dpi=200)

'''
解调过程
'''
# 已调信号mod_sig，频域为mod_sig_fft_amp和mod_sig_fft_xf
# 解调载波
carrier2 = np.cos(2 * np.pi * fc2 * t + theta)
# 调制型号乘以本地载波
de_mod_sig = mod_sig * carrier2
# 解调信号频谱
de_mod_sig_fft_data = fftshift(fft(de_mod_sig))
de_mod_sig_fft_amp = np.abs(de_mod_sig_fft_data) * sample_interval  # 双边幅度谱,范围为正负sample_freq/2

'''在频域定义一个低通，并进行滤波'''
LPF_HW = 2 * np.heaviside(f + fcc / 2, 1) - 2 * np.heaviside(f - fcc / 2, 1)

'''解调信号通过低通'''
RW = de_mod_sig_fft_data * LPF_HW
RW_amp = abs(RW) * sample_interval  # 显示
rt_sig = ifft(ifftshift(RW)).real

# 如果需要显示中文，则需要加入下面两行
ax = plt.figure(figsize=(16, 9), dpi=100)
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("已调信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, mod_sig, 'darkviolet')

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 2.2, fc2 * 2.2)
plt.title("已调信号的频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, mod_sig_fft_amp, 'darkviolet')

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title(r"调制信号乘以本地载波（时域）", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, de_mod_sig)

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 2.2, fc2 * 2.2)
plt.title(r"调制信号乘以本地载波（频域）", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, de_mod_sig_fft_amp)
plt.plot(f, np.max(de_mod_sig_fft_amp) * 0.5 * LPF_HW, "b--")  # 修正低通幅度，使得图像美观

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(0, 0.01)
plt.title("恢复信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', fontsize=fontsize, loc='right')
plt.plot(t, rt_sig, 'r')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-fc2 * 2.2, fc2 * 2.2)
plt.title("恢复信号的频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', fontsize=fontsize, loc='right')
plt.plot(f, RW_amp, 'r')

plt.suptitle(r"解调过程")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# ax.savefig(r"%s 解调过程.jpg"%namestr, dpi=200)

'''播放'''
sd.play(rt_sig, sample_freq)
time.sleep(t_length * 1.1)  # 需要稍微sleep长一点时间
