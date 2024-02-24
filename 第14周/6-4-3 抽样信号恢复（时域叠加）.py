import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fftfreq, fftshift

'''抽样参数'''
# 定义抽样周期
T = 1 / 4  # cos信号周期 T
# 演示参数
t_length = 1  # 信号的实际时间长度
sample_freq = 4096
sample_interval = 1 / sample_freq  # 模拟连续信号的采样间隔
'''
定义t、f
所定义信号、抽样脉冲的实际样本点个数为: t_length * sample_interval
'''
t = np.arange(0, t_length, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))
'''
定义一个升余弦(1+cos(2pi/T* t) t∈(0,T).脉宽=T
第一过零点带宽为（4pi/T）,转为频率是1/T/2
'''
et = (0.5 + 0.5 * np.cos(2 * np.pi / T * t - np.pi)) * (np.heaviside(t, 1) - np.heaviside(t - T, 1))
'''
如果抽样间隔为T/8，则在升余弦信号的有效范围内有7条抽样脉冲（第一条和第九条幅度是0）
构造一个全零序列，在第nTs(实际)位置（i * Ts * sample_interval）上手动赋值p(nTs)=e(i * Ts)
'''
Ts = T / 8
# Ts = T / 2
pulses = []  # 得到8（7）条独立的脉冲
for i in range(0, int(T / Ts)):
    p = np.zeros_like(t)
    # 计算位置脉冲所在的位置，t轴0点实际位置为，第 t_length / sample_interval个采样点，再计算对0点的偏移量
    # 偏移量为 (t_length + i*Ts) / sample_interval,注意i有正有负
    sp = int(i * Ts / sample_interval)
    p[sp] = (0.5 + 0.5 * np.cos(2 * np.pi / T * i * Ts - np.pi))
    # 注意，pulse是list，可以直接使用append方法，
    # 但numpy中的ndarray的append方法不是这么用的，为np.append(array1,array2)
    pulses.append(p)
    print(i, sp, p[sp])
'''定义理想低通的冲激响应'''
f_l = 1 / Ts / 2
# 为了保持sa函数的特征，定义了另一个时间轴
t1 = np.arange(-t_length / 2, t_length / 2, sample_interval)
# ht 注意修正高度
ht = 2 * f_l * np.sinc(2 * f_l * t1) * Ts
''''''
# 8（7）条线分别和ht做卷积得到的结果
results = []
for i in range(0, int(T / Ts)):
    results.append(np.convolve(pulses[i], ht, mode='same'))

'''绘图'''
plt.figure(figsize=(12, 6), dpi=100)  # 新建绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(231)
plt.grid()  # 显示网格
plt.xlim(0, 0.25)
plt.title("原信号")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et)

plt.subplot(232)
plt.grid()  # 显示网格
plt.xlim(0, 0.25)
plt.title("抽样信号（时域）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
for i in range(0, int(T / Ts)):
    plt.plot(t, pulses[i])
plt.plot(t, et, 'r--')

plt.subplot(233)
plt.grid()  # 显示网格
plt.xlim(-0.25, 0.25)
plt.title("理想低通的$h(t)$")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t1, ht)

# 双边谱
plt.subplot(235)
plt.grid()  # 显示网格
plt.xlim(0, 0.25)
# plt.ylim(-0.2, 1.1)
plt.title("单个抽样脉冲卷积$h(t)$（未叠加）")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
for i in range(0, int(T / Ts)):
    plt.plot(t, results[i])
plt.plot(t, et, 'r--')

plt.subplot(234)
plt.grid()  # 显示网格
plt.xlim(0, 0.25)
plt.ylim(-0.2, 1.1)
plt.title("内插信号叠加恢复为原信号")
plt.xlabel(r'$time\rm{(s)}$', loc='right')
result = np.zeros_like(len(results[0]))
for i in range(0, int(T / Ts)):
    result = result + results[i]
plt.plot(t, result)

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
