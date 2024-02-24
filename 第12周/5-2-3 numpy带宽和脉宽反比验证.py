import matplotlib.pylab as plt  # 绘制图形
import numpy as np
# rom scipy.fftpack import fft,fftfreq
# rom scipy import signal
from numpy.fft import fft, fftfreq, fftshift

sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
N = 20
tao = 2
'''定义信号'''
# 一个对称区间
t = np.arange(-N, N, sample_interval)
# 原始方波
tao = 2
f1 = np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1)
tao = 4
f2 = np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1)
tao = 8
f3 = np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1)

# ------------------
'''计算FFT'''
# 注意所有的频轴用的都是一个，因为他们的时间轴和采样密度等是一样的
f = fftshift(fftfreq(len(t), sample_interval))  # fft的双边频域坐标
f1_amp = fftshift(np.abs(fft(f1)) * sample_interval)  # 双边幅度谱
f2_amp = fftshift(np.abs(fft(f2)) * sample_interval)  # 双边幅度谱
f3_amp = fftshift(np.abs(fft(f3)) * sample_interval)  # 双边幅度谱

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_1 (t)$', loc='left')
plt.plot(t, f1, 'r')

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|F_1 (jf)|$', loc='left')
plt.plot(f, f1_amp, 'r')

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_2 (t)$', loc='left')
plt.plot(t, f2, 'g')

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|F_2(jf)|$', loc='left')
plt.plot(f, f2_amp, 'g')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_3 (t)$', loc='left')
plt.plot(t, f3, 'b')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|F_3 (jf)|$', loc='left')
plt.plot(f, f3_amp, 'b')

plt.suptitle("傅里叶变换标度变换性质")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
exit()
