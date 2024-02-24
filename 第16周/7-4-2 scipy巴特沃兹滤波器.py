from matplotlib import patches
import numpy as np
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

wc=10*2*np.pi
# wc=0.5
N = 3
z = []
p = np.array([wc * np.exp(1j * 2 * np.pi / N), wc * np.exp(1j * 3 * np.pi / N), wc * np.exp(1j * 4 * np.pi / N)])
k = np.power(wc, N)

# 频响特性
omega, Hw = signal.freqs_zpk(z, p, k)
mag = 20 * np.log10(np.abs(Hw))
phase = np.angle(Hw)
f = omega / 2 / np.pi

# 手动画图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.subplot(211)
plt.grid()
plt.title(r'幅度响应', loc='left')
plt.semilogx(f, mag)  # Bode magnitude plot
# 在半功率点绘制一条虚线,长度和频轴f相同
plt.semilogx(f, -3 * np.ones_like(f), 'r--')

plt.subplot(212)
plt.title(r'相位响应', loc='left')
plt.grid()
plt.semilogx(f, phase)  # Bode phase plot
# plt.ylim(-3.2,3.2)
plt.tight_layout()
plt.show()

# 零极点手动画图
#plt.figure(figsize=(5, 5))  # 规定比例，否则辅助圆可能是椭圆
plt.title('零极点')
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
poles = plt.plot(p.real, p.imag, 'x', c='b')
# zeros = plt.plot(z.real, z.imag, 'o', color='none', markeredgecolor='b')
# 画个辅助圆
ax1 = plt.subplot()
unit_circle = patches.Circle((0, 0), radius=wc, fill=False, color='r', ls='--')
ax1.add_patch(unit_circle)
ax1.axis('scaled')# 保持坐标系统正圆

plt.tight_layout()
plt.show()

'''第二种方法'''
p = np.array([wc * np.exp(1j*2*np.pi/N),wc * np.exp(1j*3*np.pi/N),wc * np.exp(1j*4*np.pi/N)])
b = np.power(wc,N)
a = np.poly(p)
sys  = signal.lti(b, a)
omega, mag, phase = sys.bode( )
#手动画图（略）
'''第三种方法'''
fc = wc /2 /np.pi
b, a = signal.butter(N, fc, 'low', analog=True)
#得到b、a之后，同第二种方法
'''其他:(b,a)和(z、p、k)的互转'''
b, a = signal.zpk2tf(z, p, k)
z, p, k = signal.tf2zpk(b, a)

