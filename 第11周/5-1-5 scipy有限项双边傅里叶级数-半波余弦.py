import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal, integrate

# 定义半波余弦，方法为余弦乘以同周期方波
T = 2 * np.pi
w1 = 2 * np.pi / T
duty = 0.5  # 占空比

# 范围
t = np.arange(-3 * T, 3 * T, 0.01)
n = np.arange(-21, 21)  # 谐波标号，同时也是频轴
n_dense = np.arange(-21, 21, 0.01)  # 为了画出连续的包络线用的频轴

# 定义半波余弦，方法为余弦乘以同周期(同角频率)的方波，注意相位一致
Gate = 0.5 * signal.square(w1 * (t + T / 4), duty=0.5) + 0.5  # 周期方波，duty为占空比
half_cos = np.cos(w1 * t) * Gate
# 第二种定义半波余弦的方法，利用where，第一个参数是条件，后面是条件为真和假时候的值 前面的函数>0的时候是前面的函数,<0时候是后面的值
half_cos = np.where(np.cos(w1 * t) >= 0, np.cos(w1 * t), 0)

# 记录各次谐波的叠加情况
f = np.zeros_like(t)
harms = []  # 记录各次谐波

for i in n:
    # 计算n=1、2、3、4……时的系数fn
    # 需要手动拆出实部和虚部
    f_inside_real = lambda x: np.real(np.cos(w1 * x) * np.exp(-1j * i * w1 * x))
    fn_real = integrate.quad(f_inside_real, -T / 4, T / 4)
    fn_real = fn_real[0] / T
    # 需要手动拆出实部和虚部
    f_inside_imag = lambda x: np.imag(np.cos(w1 * x) * np.exp(-1j * i * w1 * x) / T)
    fn_imag = integrate.quad(f_inside_imag, -T / 4, T / 4)
    fn_imag = fn_imag[0] / T
    # 叠加得到真实的fn，注意虚部要乘以1j
    fn = fn_real + 1j * fn_imag
    # 把谐波模值记录到数组，后续进行画图
    harms.append(abs(fn))
    # 构造完整的谐波：fn*基底函数
    f_harmonic = fn * np.exp(1j * i * w1 * t)
    f = f + f_harmonic
print(f)
# 画幅度频谱图，利用numpy+matplotlib

plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 1, 1)
plt.grid()  # 显示网格
plt.title(r"谐波叠加", loc='left')
plt.plot(t, abs(f))  # 谐波叠加情况
plt.plot(t, half_cos, 'r--')  # 对照组方波
plt.xlabel(r'$time\rm{(s)}$', loc='right')

plt.subplot(2, 1, 2)
plt.grid()  # 显示网格
plt.title("幅度谱", loc='left')
plt.stem(n, harms)
# 画出幅度谱的包络线
plt.plot(n_dense, abs(-1 * np.cos(np.pi * n_dense / 2) / (np.pi * (np.power(n_dense, 2) - 1))), 'r--')  # 对照组方波
plt.xlabel(r"$n\omega_1$", loc='right')
plt.xlim(-5, 5)

plt.tight_layout()
plt.show()
