import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifft

# 公共参数
E = 1
tao = 1
sample_freq = 4096  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔v
# 时间轴
t = np.arange(0, 20 * tao, sample_interval)
# 定义时域信号：门函数
ft = E * np.heaviside(t, 1) - E * np.heaviside(t - tao, 1)
# 定义时域信号：指数函数
ft1 = tao * np.exp(-tao * t)
# 频轴，范围为正负sample_freq/2
f = fftshift(fftfreq(len(t), sample_interval))
'''
fft
1，由于时间轴为0开始的非对称区间，所以fft之前不需要进行fftshift
2，fft出来的结果需要再做一次fftshfit，才能对应到之前定义的f轴上
'''
Fw = fftshift(fft(ft))
# 模值为：
Fw_amp = np.abs(Fw * sample_interval)
# 对于门函数频谱，可以直接用Fw或Fw取实部，可以更好的展示Sa函数的样子
# Fw_amp = Fw.real * sample_interval
Fw_ang = np.angle(Fw)

'''
ifft
1，由于Fw之前做过fftshift，所以这里在ifft之前做一次ifftshift
2，由于计算Fw的ft，没进行过fftshift，因此ifft的结果，不需要再进行ifftshift
'''
ft2 = ifft(fftshift(Fw))

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(221)
plt.grid()  # 显示网格
plt.title("原信号")
plt.xlim(0, 3 * tao)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ft)

plt.subplot(222)
plt.grid()  # 显示网格
plt.xlim(-3 / tao, 3 / tao)
plt.title("幅度谱（演示）")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Fw_amp)

plt.subplot(223)
plt.grid()  # 显示网格
plt.title("反变换得到的时域信号")
plt.xlim(0, 3 * tao)
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ft2)

plt.subplot(224)
plt.grid()  # 显示网格
plt.xlim(-3 / tao, 3 / tao)
plt.title("相位谱")
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Fw_ang)
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)
plt.ylim(-np.pi*1.1,np.pi*1.1)#如果y坐标设置的过多，还可以用ylim再卡一下范围

plt.tight_layout()
plt.show()
