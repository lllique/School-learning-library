from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
b = [0, 2]
a = [1, -0.8]
N = 30
t = range(N)
#激励，可以理解为阶跃序列
x = np.ones(N)
'''
方法一
把系统作为滤波器进行分析
利用lfilter方法：Filter data along one-dimension with an IIR or FIR filter.
'''
y = signal.lfilter(b, a, x)

'''
# 方法2，
把系统作为离散线性时不变系统进行分析
利用dlsim方法，注意和lsim方法的区别：
离散系统必须给出抽样间隔（Sampling time [s] ）
有两种方式：
system = signal.TransferFunction(b, a, dt=1)
t_out, y_out = signal.dlsim(system, x, t=t)
或：
t_out, y_out = signal.dlsim((b, a, 1), x, t=t)
'''
t_out, y_out = signal.dlsim((b, a, 1), x, t=t)

# 绘图，对比一下两种方式
plt.figure()
plt.subplot(2, 1, 1)  # 画布位置1
plt.stem(t, y)

plt.subplot(2, 1, 2)  # 画布位置1
plt.stem(t_out, y_out)
plt.show()
