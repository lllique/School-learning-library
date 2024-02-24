from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

f = 2000  # 模拟角频率
fs = 100*f  # 抽样频率
a = 500 * 2 * np.pi # 截止频率为500hz

t = np.arange(0, 5/f,1/fs)
# 定义一个余弦
e1 = np.cos(2 * np.pi * f * t)
# 定义周期方波
e2 = signal.square(2 * np.pi * f * t, duty=0.5)
# 选一个信号
e = e1

system = ([0,a], [1, a])
tout, yout, _ = signal.lsim(system, U=e, T=t)

# 绘图
plt.grid()
plt.plot(tout, yout)
plt.plot(t, e, 'r--')
plt.xlim(0,5/f)
plt.show()
