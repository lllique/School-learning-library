import numpy as np
import matplotlib.pyplot as plt
n = np.arange(0,10,1) #绘图的横坐标，长度自定
x = np.power(0.5,n) #幂级数，用np.pow
plt.grid() #显示网格
plt.stem(n,x, basefmt="-")
plt.show()
