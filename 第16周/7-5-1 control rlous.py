import control as ct
import numpy as np
import matplotlib.pylab as plt  # 绘制图形

b=1
a=[1 ,1, -2]

#b=[1,2,6]
#a=[1,2,6,2.26,0]
n = np.arange(1,200)
k=np.power(1.038,n)-1
sys = ct.tf(b,a)
r,k = ct.rlocus(sys,k,plot= True)
plt.xlim(-2,0)
plt.show()
print(r,k)
exit()

