import matplotlib.pylab as plt  # 绘制图形
import numpy as np

'''定义连续信号'''
t = np.linspace(-10, 10, 2000)
sig1 = np.sinc(0.5 * t)
'''定义离散信号'''
n = np.linspace(-10, 10, 20)
sig2 = np.sinc(0.5 * n)

plt.plot(t, sig1, "r--")  # 参数r--表示显示红色的虚线
plt.stem(n, sig2)
plt.show()
