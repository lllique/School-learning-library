import numpy as np
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

'''示例系统'''
b = [2, 0, 1]
a = [1, 4, 6, 5, 2]

'''重根系统'''
#Ys = (s**2)/(s+2)/(s**2+2*s+1)
b = [2, 0, 0]
a = [1, 4, 5, 2]
#[-3.+0.j  1.+0.j  4.+0.j] [-1.+0.j -1.+0.j -2.+0.j] []

'''一个带通系统
R=20
L=2
C=0.1
b = [R]
a = [R*L*C,L,R]
'''
sys = signal.lti(b, a)
'''
#波特图
输出为角频率、以分贝[dB]表示的幅度和以角度[deg]表示的相位
'''
omega, mag, phase = sys.bode(w=np.logspace(-1, 2, 1000))
f = omega / 2 / np.pi

'''
semilogx等方法绘图时，如果选择中文字体为宋体、黑体等，
此时坐标指数上的负号无法通过axes.unicode_minus选项来正确显示，
此时最佳办法是使用微软雅黑这种带有unicode减号的字体（\u2212）
'''
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 指定非衬线字体
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格

plt.figure()
plt.subplot(211)
plt.grid()
plt.title(r'幅度响应', loc='left')
plt.semilogx(f, mag)  # Bode magnitude plot

plt.subplot(212)
plt.title(r'相位响应', loc='left')
plt.grid()
plt.semilogx(f, phase)  # Bode phase plot
plt.tight_layout()
plt.show()

# 零极点
p = sys.poles
z = sys.zeros
print(z, p)
# 手动画图
plt.figure()
plt.title('零极点')
plt.xlabel('Re', loc='right')
plt.ylabel('Im', loc='top')
plt.grid()
poles = plt.plot(p.real, p.imag, 'x', c='b')
zeros = plt.plot(z.real, z.imag, 'o', color='none', markeredgecolor='b')
plt.tight_layout()
plt.show()
''''''
#冲激响应
t, y = sys.impulse()
plt.figure()
plt.grid()
plt.plot(t, y)
plt.show()


'''
#方式2，利用零极点算频谱特性,从函数名看应用主要用于z变换，但在s变换中也是对的
z, p, k = signal.tf2zpk(b, a)#输出零点z、极点p和增益k
omega, Hw = signal.freqs_zpk(z, p, k,worN=np.logspace(-1, 2, 1000))
'''
