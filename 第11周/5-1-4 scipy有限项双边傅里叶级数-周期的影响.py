import matplotlib.pylab as plt  # 绘制图形
import numpy as np

from scipy import signal, integrate

# todo 固定tao，修改占空比，即可看到不同T对傅里叶级数的影响
tao = np.pi  # tao是固定值
duty = 0.2
T = tao / duty  # 占空比越大，则T越小，占空比越小，则T越大
w1 = 2 * np.pi / T
# 范围
t = np.arange(-20, 20, 0.01)
'''arange中是谐波个数，乘以w1就是谐波角频率，n_w1就是角频率轴'''
n_w1 = np.arange(-21, 21) * w1
# 为了画出连续的包络线，定义一个稠密的频轴
n_dense_w1 = np.arange(-21, 21, 0.01) * w1
# 定义一个周期方波做对照
Gate = 0.5 * signal.square(w1 * t, duty=duty) + 0.5  # 周期方波，duty为占空比

# 记录各次谐波的叠加情况，由于是ndarray叠加，所以要先构造一个长度一致的空序列
f = np.zeros_like(t)
harms = []  # 记录各次谐波
# 相当于叠加21个cos谐波和直流分量
for i in n_w1:
    # 计算n=1、2、3、4……时的系数fn
    # 需要手动拆出实部和虚部
    f_inside_real = lambda x: np.real(np.exp(-1j * i * x))
    fn_real = integrate.quad(f_inside_real, 0, tao)  # (3.325853178611109e-16, 1.8864874255052047e-14) <class 'tuple'>
    fn_real = fn_real[0] / T
    # 需要手动拆出实部和虚部
    f_inside_imag = lambda x: np.imag(np.exp(-1j * i * x))
    fn_imag = integrate.quad(f_inside_imag, 0, tao)  # (3.325853178611109e-16, 1.8864874255052047e-14) <class 'tuple'>
    fn_imag = fn_imag[0] / T
    # 叠加得到真实的fn，注意虚部要乘以1j
    fn = fn_real + 1j * fn_imag
    # 把谐波模值记录到数组，后续进行画图
    harms.append(abs(fn))
    # 构造完整的谐波：fn*基底函数
    f_harmonic = fn * np.exp(1j * i * t)
    # 进行叠加
    f = f + f_harmonic

# 画幅度频谱图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2, 1, 1)
plt.grid()  # 显示网格
plt.title(r"谐波叠加", loc='left')
plt.plot(t, Gate, 'r--')  # 对照组方波
plt.plot(t, abs(f))  # 谐波叠加情况
plt.xlabel(r'$time\rm{(s)}$', loc='right')

plt.subplot(2, 1, 2)
plt.grid()  # 显示网格
plt.title("幅度谱", loc='left')
plt.stem(n_w1, harms)
# 画出幅度谱的包络线
plt.plot(n_dense_w1, abs(duty * np.sin(n_dense_w1 * tao / 2) / (n_dense_w1 * tao / 2)), 'r--')  # 对照组方波
plt.xlabel(r"$n\omega_1$", loc='right')
plt.xlim(-5, 5)
plt.ylim(0, 1.1)

plt.tight_layout()
plt.show()
