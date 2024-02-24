import numpy as np
from scipy import signal

t = np.linspace(0, 1, 100)
# 相当于”角频率”为 10pi，即周期为2pi/10pi = 0.2s
y1 = signal.sawtooth(2 * np.pi * 5 * t) #锯齿波
y2 = signal.square(2 * np.pi * 5 * t,duty=0.2) #周期方波，duty为占空比
y3 = signal.unit_impulse(len(t)) #单位冲激信号，实际是单位样值信号，高度为1，默认位置在序列中心
y4 = signal.unit_impulse(len(t),int(len(t)/2)) #第二个参数是位置
print(y4)

import matplotlib.pyplot as plt
plt.grid()
plt.plot(t, y1)
plt.show()
