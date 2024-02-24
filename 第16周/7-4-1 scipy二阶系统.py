import numpy as np
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

'''系统'''
wpl = 10 * 2 * np.pi
wph = 100 * 2 * np.pi

'''方式1，直接定义bpf'''
bpf_a = np.poly([-wpl,-wph])
bpf_b = [wph,0]
print(bpf_a)
bpf = signal.lti(bpf_b, bpf_a)

# 零极点
p = bpf.poles
z = bpf.zeros
#波特图
omega, mag, phase = bpf.bode(w=np.logspace(0, 4, 1000))
f = omega / 2 / np.pi

'''方式2，利用级联系统的频谱关系
lpf = signal.lti([wph], [1, wph])
hpf = signal.lti([1, 0], [1, wpl])
# 零极点,汇总，并考察零极点相消情况
p = np.append(lpf.poles,hpf.poles)
z = np.append(lpf.zeros,hpf.zeros)
#波特图
omega, mag1, phase1 = lpf.bode(w=np.logspace(0, 4, 1000))
f = omega / 2 / np.pi
_, mag2, phase2 = hpf.bode(w=np.logspace(0, 4, 1000))

mag= mag1 + mag2
phase = phase1 + phase2
'''
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
'''图'''
plt.figure()
plt.subplot(1, 2, 1)
plt.grid()
poles = plt.plot(p.real, p.imag, 'x', c='b')
zeros = plt.plot(z.real, z.imag, 'o', color='none', markeredgecolor='b')

plt.subplot(2, 2, 2)
plt.grid()
plt.semilogx(f, mag)  # Bode magnitude plot
# 在半功率点绘制一条虚线,长度和频轴f相同
plt.semilogx(f, (np.max(mag)-3) * np.ones_like(f), 'r--')

plt.subplot(2, 2, 4)
plt.grid()
plt.semilogx(f, phase)  # Bode phase plot

plt.tight_layout()
plt.show()
