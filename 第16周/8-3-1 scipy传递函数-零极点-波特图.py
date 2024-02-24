import numpy as np
from matplotlib import patches
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

'''示例系统'''
b = [1, 0 ,0, -3]
a = [1, -5, 6, 0]

'''一个重根系统
无法体现二阶零极点
'''
b=[1, 0.5,0,0]
a=[1, -1.25, 0.75, -0.125]


dsys = signal.dlti(b, a)
'''
#波特图
输出为角频率、以分贝[dB]表示的幅度和以角度[deg]表示的相位
'''
omega, mag, phase = dsys.bode()
#f = omega / 2 / np.pi
# 手动画图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.subplot(211)
plt.grid()
plt.title(r'幅度响应', loc='left')
plt.semilogx(omega, mag)  # Bode magnitude plot

plt.subplot(212)
plt.title(r'相位响应', loc='left')
plt.grid()
plt.semilogx(omega, phase)  # Bode phase plot
plt.tight_layout()
plt.show()

# 零极点
p = dsys.poles
z = dsys.zeros
print(z, p)
# 手动画图
plt.figure()
plt.title('零极点')
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
poles = plt.plot(p.real, p.imag, 'x', c='b')
zeros = plt.plot(z.real, z.imag, 'o', color='none', markeredgecolor='b')

# 画个单位圆
ax1 = plt.subplot()
unit_circle = patches.Circle((0, 0), radius=1, fill=False, color='r', ls='--')
ax1.add_patch(unit_circle)
ax1.axis('scaled')# 保持坐标系统正圆

plt.tight_layout()
plt.show()
''''''
#单位样值响应，相当于dimpluse
n, y = dsys.impulse(n=10)
print(n)
print(y)
plt.figure()
plt.grid()
'''y是一个二维数组，用np.squeeze可以删除不必要的维度，或者使用y[0]画图'''
plt.stem(n, np.squeeze(y))
plt.show()


'''
#方式2，利用零极点算频谱特性,从函数名看应用主要用于z变换，但在s变换中也是对的
z, p, k = signal.tf2zpk(b, a)#输出零点z、极点p和增益k
omega, Hw = signal.freqs_zpk(z, p, k,worN=np.logspace(-1, 2, 1000))
'''
