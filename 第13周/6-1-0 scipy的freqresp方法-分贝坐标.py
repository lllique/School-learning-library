from math import sqrt

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

f_l = 1000
a = f_l * np.pi * 2
'''
分贝坐标一般画单边谱（数值和双边谱一致，但是只画一半）
考虑到绘图美观等问题，f可以从1Hz开始设置
'''
f = np.arange(0.1, 100 * f_l)
omega = f * 2 * np.pi
# 计算系统频率响应
lpf = ([0, a], [1, a])
hpf = ([1, 0], [1, a])
# freqresp输入输出的横坐标为角频率 [rad/s]
omega, Hw = signal.freqresp(hpf, omega)

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(211)
plt.grid()
plt.title(r'幅度响应', loc='left')

'''
绘制分贝坐标的方法1
# semilogx会把x轴转为对数坐标（log 10）,
类似的函数semilogy、loglog函数（x、y都取log10）
'''
plt.semilogx(f, 20 * np.log10(np.abs(Hw)))
# 在半功率点绘制一条虚线,长度和频轴f相同
plt.semilogx(f, -3 * np.ones_like(f), 'r--')

''''''
# 注意画波特图时，相位谱的纵坐标保持不变，横坐标变为log坐标
plt.subplot(212)
plt.grid()
plt.title(r'相位响应', loc='left')
# semilogx会把x轴数据取log
plt.semilogx(f, np.angle(Hw))

'''把纵坐标刻度值 设置为：显示：1π、2π……的形式'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)
#plt.ylim(-1.8,0.1)#如果y坐标空余过大，还可以用ylim再卡一下范围

plt.tight_layout()
plt.show()
