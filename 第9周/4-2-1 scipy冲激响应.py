from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
a = 2
t1 = np.arange(0, 5, 0.01)
# [0, a]是右侧的系数， [1, a]是左侧侧的参数
#例2，注意数组最右边的0可以省略
system = ([0, a], [1, a])
#等价于
#system = ([a], [1, a])
#例3
#system = ([1, 0], [1, a])
#例4
#L=1;C=1;R=0.2;
#system = ([1/L/C], [1, R/L,1/L/C])
#t1 = np.arange(0, 30, 0.01)

# T不是必须的参数,加入T参数后，输出的t=t1
t, y = signal.impulse(system, T=t1)
#绘图
plt.plot(t, y)
plt.show()

