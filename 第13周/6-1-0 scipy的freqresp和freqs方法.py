from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

a = 2 * np.pi * 1000
# 定义一段频点，范围可以用3倍截止角频率 [rad/s]
omega = np.arange(-3 * a, 3 * a)
# 如果需要对f进行画图，可以定义一个频轴
f = omega / 2 / np.pi
lpf = ([0, a], [1, a])
hpf = ([1, 0], [1, a])
# freqresp输入输出的横坐标实际为角频率 [rad/s]
omega, Hw = signal.freqresp(lpf, omega)
# freqs：Compute frequency response of analog filter.
omega, Hw = signal.freqs([0, a], [1, a], omega)

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(211)
plt.grid()
plt.title(r'幅度响应', loc='left')
plt.plot(f, np.abs(Hw))
plt.plot(f, 0.707 * np.ones_like(f), 'r--')

plt.subplot(212)
plt.grid()
plt.title(r'相位响应', loc='left')
plt.plot(f, np.angle(Hw))
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)
plt.ylim(-np.pi/2,np.pi/2)#如果y坐标设置的过多，还可以用ylim再卡一下范围

plt.tight_layout()
plt.show()
exit()

'''control库中的类似方法'''
from control import matlab

# 定义系统的语法略有不同
lpf = matlab.TransferFunction([0, a], [1, a])
hpf = matlab.TransferFunction([1, 0], [1, a])
# frequency_response输出的横坐标实际为角频率，返回值依次为幅度、相位和角频率轴，可以直接用来画图
mag, phase, omega = matlab.frequency_response(lpf, omega)
