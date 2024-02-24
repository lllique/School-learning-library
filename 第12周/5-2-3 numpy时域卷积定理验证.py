import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift

sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
N = 20
'''定义信号'''
# 一个对称区间
t = np.linspace(-N, N, int(2 * N / sample_interval))

# 方波
et = np.piecewise(t, [t < 0, t >= 0, t >= N / 10], [0, 1, 0]).astype(int)
# 另一个方波（一摸一样的方波）
ht = et
#卷积积分
rt = np.convolve(et, ht, mode='same') * sample_interval

# ------------------
'''计算FFT'''
# 注意所有的频轴用的都是一个，因为他们的时间轴和采样密度等是一样的
# 如果卷积时采用了full模式，则时轴发生变化，频轴也要重新计算
f = fftshift(fftfreq(len(t), sample_interval))  # fft的双边频域坐标
ew_amp = fftshift(np.abs(fft(et))) * sample_interval  # 双边幅度谱
hw_amp = fftshift(np.abs(fft(ht))) * sample_interval  # 双边幅度谱
rw_amp = fftshift(np.abs(fft(rt))) * sample_interval  # 双边幅度谱

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(-2, 8)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$e(t)$', loc='left')
plt.plot(t, et, 'r')

plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|E(jf)|$', loc='left')
plt.plot(f, ew_amp, 'r')

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(-2, 8)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$h(t)$', loc='left')
plt.plot(t, ht)

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title(r'$|H(jf)|$', loc='left')
plt.plot(f, hw_amp)

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(-2, 8)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$r(t)$', loc='left')
plt.plot(t, rt, 'darkviolet')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.title(r'$|R(jf)|$', loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, rw_amp, 'darkviolet')

plt.suptitle("时域卷积定理验证")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
exit()
