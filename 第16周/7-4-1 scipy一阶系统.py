import numpy as np
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

'''系统'''
wp = 10 * 2 * np.pi
sys = [None for _ in range(2)]
sys[0] = signal.lti([wp], [1, wp])
sys[1] = signal.lti([1, 0], [1, wp])

plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
'''图'''
plt.figure()
for i in range(2):
    # 零极点
    p = sys[i].poles
    z = sys[i].zeros
    plt.subplot(2, 3, 3 * i + 1)
    plt.title('sys%d零极点' % i, loc='left')
    plt.xlim(-100, 100)
    plt.grid()
    poles = plt.plot(p.real, p.imag, 'x', c='b')
    zeros = plt.plot(z.real, z.imag, 'o', color='none', markeredgecolor='b')
    #波特图
    omega, mag, phase = sys[i].bode(w=np.logspace(0, 4, 1000))
    f = omega / 2 / np.pi

    plt.subplot(2, 3, 3 * i + 2)
    plt.grid()
    plt.title('sys%d幅度响应(dB)' % i, loc='left')
    plt.semilogx(f, mag)  # Bode magnitude plot

    plt.subplot(2, 3, 3 * i + 3)
    plt.grid()
    plt.title('sys%d相位响应(deg)' % i, loc='left')
    plt.semilogx(f, phase)  # Bode phase plot

plt.tight_layout()
plt.show()
