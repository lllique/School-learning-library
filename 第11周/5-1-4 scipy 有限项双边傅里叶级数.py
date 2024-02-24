import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal, integrate

# 定义方波
T = 2 * np.pi
w1 = 2 * np.pi / T
# todo 固定T，修改占空比，即可看到不同脉冲宽度tao对傅里叶级数的影响
duty = 0.5  # 占空比
tao = T * duty
# 范围
t = np.arange(-3 * T, 3 * T, 0.01)
n = np.arange(-21, 21)  # 谐波标号，同时也是频轴
n_dense = np.arange(-21, 21, 0.01)  # 为了画出连续的包络线用的频轴

# 定义一个周期方波做对照
Gate = 0.5 * signal.square(w1 * t, duty=duty) + 0.5  # 周期方波，duty为占空比

# 记录各次谐波的叠加情况，由于是ndarray叠加，所以要先构造一个长度一致的空序列
f = np.zeros_like(t)
harms = []  # 记录各次谐波
harms_power = []  # 记录谐波功率（功率谱）
for i in n:
    # 计算n=1、2、3、4……时的系数fn
    # 需要手动拆出实部和虚部
    f_inside_real = lambda x: np.real(np.exp(-1j * i * w1 * x))
    fn_real = integrate.quad(f_inside_real, 0, tao)  # (3.325853178611109e-16, 1.8864874255052047e-14) <class 'tuple'>
    fn_real = fn_real[0] / T
    # 需要手动拆出实部和虚部
    f_inside_imag = lambda x: np.imag(np.exp(-1j * i * w1 * x))
    fn_imag = integrate.quad(f_inside_imag, 0, tao)  # (3.325853178611109e-16, 1.8864874255052047e-14) <class 'tuple'>
    fn_imag = fn_imag[0] / T
    # 叠加得到真实的fn，注意虚部要乘以1j
    fn = fn_real + 1j * fn_imag
    # 把谐波模值记录到数组，后续进行画图
    harms.append(abs(fn))
    # 把谐波功率记录到数组，fn*fn的共轭就是fn的平方，也就是这个谐波的功率
    # 理论上不需要abs，这里加abs是为了去掉warning
    harms_power.append(abs(fn * np.conj(fn)))

    # 构造完整的谐波：fn*基底函数
    f_harmonic = fn * np.exp(1j * i * w1 * t)
    f = f + f_harmonic
print(f)
# 画幅度频谱图，利用numpy+matplotlib

plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(3, 1, 1)
plt.grid()  # 显示网格
plt.title(r"谐波叠加", loc='left')
plt.plot(t, Gate, 'r--')  # 对照组方波
plt.plot(t, abs(f))  # 谐波叠加情况
plt.xlabel(r'$time\rm{(s)}$', loc='right')

plt.subplot(3, 1, 2)
plt.grid()  # 显示网格
plt.title("幅度谱", loc='left')
plt.stem(n, harms)
# 画出幅度谱的包络线
plt.plot(n_dense, abs(duty * np.sin(n_dense * w1 * tao / 2) / (n_dense * w1 * tao / 2)), 'r--')  # 对照组方波
plt.xlabel(r"$n\omega_1$", loc='right')
plt.xlim(-5, 5)

plt.subplot(3, 1, 3)
plt.grid()  # 显示网格
plt.title("功率谱", loc='left')
plt.stem(n, harms_power)
plt.xlabel(r"$n\omega_1$", loc='right')
plt.xlim(-5, 5)

plt.tight_layout()
plt.show()
