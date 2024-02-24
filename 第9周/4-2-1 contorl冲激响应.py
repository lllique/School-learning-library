import control.matlab as cm
import numpy as np
import matplotlib.pyplot as plt

L=1;C=1;R=0.2;
t1 = np.arange(0, 30, 0.01)
# 对于control库，T是必须的参数,且输出值顺序和scipy相反
system = cm.TransferFunction([1/L/C], [1, R/L,1/L/C])
y,t = cm.impulse(system, T=t1)
#绘图
plt.plot(t, y)
plt.show()

