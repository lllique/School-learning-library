import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift
from scipy.ndimage import shift

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
'''
信号平移
使用scipy的shift函数，注意参数为正时为右移
注意平移的数值是 平移的时间距离 * 单位距离采样点的个数
'''
f2 = shift(f1, 2 * sample_freq)
f3 = shift(f1, -2 * sample_freq)

# ------------------
'''计算FFT'''
# 注意所有的频轴用的都是一个，因为他们的时间轴和采样密度等是一样的
f = fftshift(fftfreq(len(t), sample_interval))  # fft的双边频域坐标
fw1 = fftshift(fft(fftshift(f1)))  # 双边幅度谱
fw2 = fftshift(fft(fftshift(f2)))  # 双边幅度谱
fw3 = fftshift(fft(fftshift(f3)))  # 双边幅度谱
# 幅度谱
f1_amp = np.abs(fw1) * sample_interval
f2_amp = np.abs(fw2) * sample_interval
f3_amp = np.abs(fw3) * sample_interval
# 相位谱
f1_ang = np.unwrap(np.angle(fw1))
f2_ang = np.unwrap(np.angle(fw2))
f3_ang = np.unwrap(np.angle(fw3))
# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(331)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_1 (t)$', loc='left')
plt.plot(t, f1)

plt.subplot(332)
plt.grid()  # 显示网格
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('幅度谱', loc='left')
plt.plot(f, f1_amp)

plt.subplot(333)
plt.grid()  # 显示网格
# plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('相位谱(解卷绕)', loc='left')
plt.plot(f, f1_ang)

plt.subplot(334)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_2 (t)$', loc='left')
plt.plot(t, f2, 'r')

plt.subplot(335)
plt.grid()  # 显示网格
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('幅度谱', loc='left')
plt.plot(f, f2_amp, 'r')

plt.subplot(336)
plt.grid()  # 显示网格
# plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('相位谱(解卷绕)', loc='left')
plt.plot(f, f2_ang, 'r')

plt.subplot(337)
plt.grid()  # 显示网格
plt.xlim(-5, 5)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.title(r'$f_3 (t)$', loc='left')
plt.plot(t, f3, 'g')

plt.subplot(338)
plt.grid()  # 显示网格
plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('幅度谱', loc='left')
plt.plot(f, f3_amp, 'g')

plt.subplot(339)
plt.grid()  # 显示网格
# plt.xlim(-2, 2)
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.title('相位谱(解卷绕)', loc='left')
plt.plot(f, f3_ang, 'g')

plt.suptitle("傅里叶变换的时移性质")
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
