import datetime
import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from numpy.fft import fft, fftfreq, fftshift, ifft, ifftshift

sample_freq = 1024  # 采样频率
sample_interval = 1 / sample_freq  # 采样间隔
f_l = 25  # 截止频率单位是Hz，注意低通的总宽度实际是两倍，但带宽只算正半轴
''' ----------------------
第一部分：两种理想低通的定义方式
----------------------'''
'''定义t、f
把t的宽度加长到1000/f_l，或者适当增加sample_freq，使得总采样点数增加，
可以更好的看到视频域计算时间的差异。
'''
t = np.arange(-500 / f_l, 500 / f_l, sample_interval)
f = fftshift(fftfreq(len(t), sample_interval))
# ------------------
'''1,从时域定义理想低通
注意对照公式乘系数，使得频域门高度为1
'''
ht1 = 2 * f_l * np.sinc(2 * f_l * t)
'''求fft，得到幅度响应'''
Hw1 = fftshift(fft(fftshift(ht1))) * sample_interval
Hw1_amp = np.abs(Hw1)

'''2,从频域定义理想低通'''
Hw2_amp = np.heaviside(f + f_l, 1) - np.heaviside(f - f_l, 1)
# 可以定义时延量
t0 = 0  # 0.05
Hw2 = Hw2_amp * np.exp(t0 * -1j * f * 2 * np.pi)
'''求ifft，得到应ht，
1. Hw2或Hw2_amp相当于进行过幅度修正和fftshift，因此要反向操作一下
2. 由于时域的t是个对称区间，因此要对ifft结果再进行一次ifftshift
3. 考虑到ifft的精度问题，可能得到的ht2不是纯实的，其结果可以取个实部
'''
ht2 = ifftshift(ifft(ifftshift(Hw2 / sample_interval))).real

plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(221)
plt.grid()  # 显示网格
plt.xlim(-2 / f_l, 2 / f_l)
plt.title("在时域定义$h(t)$($Sa$函数)", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ht1)
# 双边谱
plt.subplot(222)
plt.grid()  # 显示网格
plt.xlim(- 2 * f_l, 2 * f_l)
plt.title("通过$FFT$计算$H(jf)$", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Hw1_amp)

plt.subplot(223)
plt.grid()  # 显示网格
plt.xlim(-2 / f_l, 2 / f_l)
plt.title("通过$iFFT$计算$h(t)$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, ht2, 'r')

plt.subplot(224)
plt.grid()  # 显示网格
plt.xlim(- 2 * f_l, 2 * f_l)
plt.title("在频域定义$H(jf)$（门函数）", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Hw2_amp, 'r')

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()

''' ----------------------
第二部分：两种低通的运算效果
----------------------'''
# 这里使用了上文定义的ht1和Hw1，也可以切换为ht2和Hw2，以查看不同低通定义方式的运算差别
ht = ht2
Hw = Hw2

w1 = 2 * np.pi * f_l * 0.5
w2 = 2 * np.pi * f_l * 4
# 定义一个简单周期信号
et = np.cos(w1 * t) + 0.2 * np.cos(w2 * t)
# 定义一个方波信号
tao = 4 / f_l
et = np.heaviside(t + tao / 2, 1) - np.heaviside(t - tao / 2, 1)
#信号频谱
Ew = fftshift(fft(fftshift(et))) * sample_interval
Ew_amp = np.abs(Ew)

'''1.利用时域卷积方式查看低通滤波效果'''
t1 = datetime.datetime.now()
rt1 = np.convolve(et, ht, mode='same') * sample_interval
Rw1 = fftshift(fft(fftshift(rt1))) * sample_interval
Rw1_amp = np.abs(Rw1)
t2 = datetime.datetime.now()
print("时域卷积方式的运算时间：", t2 - t1)

'''2.利用频域乘积方式查看低通滤波效果'''
t1 = datetime.datetime.now()
Rw2 = Ew * Hw  # 注意考虑幅度修正问题，根据前文代码，Rw1相当于经过了幅度修正
Rw2_amp = np.abs(Rw2)
rt2 = ifftshift(ifft(ifftshift(Rw2 / sample_interval))).real
t2 = datetime.datetime.now()
print("频域乘积方式的运算时间：", t2 - t1)

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(321)
plt.grid()  # 显示网格
plt.xlim(-5 / f_l, 5 / f_l)
plt.title("原信号", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, et)
# 双边谱
plt.subplot(322)
plt.grid()  # 显示网格
plt.xlim(- 5 * f_l, 5 * f_l)
plt.title("原信号频谱", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, np.abs(Hw) * np.max(Ew_amp), "r--")  # 标示一下低通的位置,修正高度使得图像更易读
plt.plot(f, Ew_amp)

plt.subplot(323)
plt.grid()  # 显示网格
plt.xlim(-5 / f_l, 5 / f_l)
plt.title("时域卷积方式得到的$r_1 (t)$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, rt1, 'r')

plt.subplot(324)
plt.grid()  # 显示网格
plt.xlim(- 5 * f_l, 5 * f_l)
plt.title("$R_1 (w)$", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Rw1_amp, 'r')

plt.subplot(325)
plt.grid()  # 显示网格
plt.xlim(-5 / f_l, 5 / f_l)
plt.title("频域卷积方式得到的$r_2 (t)$", loc='left')
plt.xlabel(r'$time\rm{(s)}$', loc='right')
plt.plot(t, rt2, 'g')

plt.subplot(326)
plt.grid()  # 显示网格
plt.xlim(- 5 * f_l, 5 * f_l)
plt.title("$R_2 (w)$", loc='left')
plt.xlabel(r'$frequency\rm{(Hz)}$', loc='right')
plt.plot(f, Rw2_amp, 'g')

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
# 用时域卷积方法计算

'''升余弦实验
f2 = np.arange(-f_l /2, f_l/2 , 1/f_l/2/10)
Hw2_amp = 5 + 5 * np.cos(2 * np.pi / f_l * f2)
zero_arr = np.zeros(int((sample_freq - f_l) * f_l * 10))
Hw2_amp = np.hstack([zero_arr, Hw2_amp, zero_arr])
Hw2 = Hw2_amp
'''
