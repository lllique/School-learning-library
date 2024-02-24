import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal

# 定义方波
T1 = 2
w1 = 2 * np.pi / T1
tao = 1
n = np.arange(1, 12, 2)  # 计算哪些谐波分量
t = np.arange(-2 * T1, 2 * T1, 0.01)  # 时间轴

# 定义一个周期方波
Gate = 0.5 * signal.square(w1 * (t + T1 / 4), duty=0.5) + 0.5 # 周期方波，duty为占空比

# 直流分量幅度
ft0 = tao / T1 * np.ones(len(t))


# 计算任意谐波分量的幅度
def harmonic(n, t):
    return 2 / (n * np.pi) * np.sin(n * w1 * tao / 2) * np.cos(n * w1 * t)


# 绘制3D图形
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
plt.grid()
# 依次画图，注意默认的z轴是竖起来的轴，这里用zdir参数把y轴竖起来
ax.plot(xs=t, ys=ft0, zs=0, zdir='y', c='c')
for i in n:
    ax.plot(t, harmonic(i, t), i, zdir='y', label='谐波', c='c')
# 原始方波
ax.plot(t, Gate, np.max(n) + 1, zdir='y', label='方波', c='red')

ax.set_xlabel('时间轴')
plt.ylabel('谐波（频率分量）')#对比ax、plt两种语法风格
ax.set_zlabel('振幅')  # 注意直接用plt无法设置z轴信息
ax.set_zlim(-2, 2)  # 设置Z轴范围
ax.set_title('方波的傅里叶级数分解')  # 等价于plt.title
plt.show()
