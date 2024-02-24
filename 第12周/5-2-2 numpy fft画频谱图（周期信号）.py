import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifft

# 公共参数
sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔


# 采样间隔一致，宽的窗采样点数变多
def make_windows(width):
    t = np.arange(0, width, sample_interval)
    ft = np.cos(2 * np.pi * 100 * t)
    f = fftshift(fftfreq(len(t), sample_interval))
    print(len(f))
    Fw_amp = fftshift(np.abs(fft(ft))) * sample_interval
    return f, Fw_amp

# 采样点数一样多，宽的窗采样间隔变大
def make_windows2(width, rate):
    t = np.arange(0, width, sample_interval / 8 * rate * width)  # 采样点一样多
    ft = np.cos(2 * np.pi * 100 * t)
    f = fftshift(fftfreq(len(t), sample_interval / 8 * rate * width))
    print(len(f))
    Fw_amp = fftshift(np.abs(fft(ft))) * sample_interval / 8 * rate * width
    return f, Fw_amp

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

for i in range(0, 4):
    tao = pow(2, i) * 10  # 窗的宽度10、20、40、80s
    f1, Fw_amp1 = make_windows(tao)
    # f1, Fw_amp1 = make_windows2(tao, 10)
    plt.subplot(2, 2, i + 1)
    plt.grid()  # 显示网格
    plt.title("窗函数宽度=%d(s)" % tao)
    plt.xlim(99, 101)
    #plt.plot(f1, Fw_amp1)
    plt.stem(f1, Fw_amp1)

plt.tight_layout()
plt.show()
