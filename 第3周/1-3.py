import numpy as np
import matplotlib.pylab as plt  # 绘制图形

t = np.linspace(-10, 10,2000)
sig = np.sin(5 * t) / (5 * t)
plt.plot(t, sig)
plt.show()
