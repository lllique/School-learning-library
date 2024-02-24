import numpy as np
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

R = 1
L = 1
C = 1
#可以带入不同的参数值
#L=1;C=1;R=0;无阻尼
#L=1;C=1;R=0.2;#欠阻尼
L=1;C=1;R=1;#欠阻尼
#L=1;C=1;R=2;#临界阻尼
#L=1;C=1;R=3;#过阻尼

a = [[-R / L, -1 / L], [1 / C, 0]]
b = [[1 / L], [0]]
c = [0, 1]
d = [0]
'''定义系统（状态方程）'''
sys = signal.StateSpace(a, b, c, d)  # <class 'scipy.signal._ltisys.StateSpaceContinuous'>

t = np.arange(0, 10, 0.01)
#定义不同的输入
e0 = np.zeros_like(t)  # 输入信号，相当于u(t)
e1 = np.ones_like(t)  # 输入信号，相当于u(t)
e2 = np.sin(2*t)  # 输入信号，相当于u(t)
e3 = np.exp(-t)  # 输入信号，相当于u(t)
#定义初始状态
vC0=2
iL0=1
x0 = [vC0, iL0]
#零输入响应
tout, yzi, xzi = signal.lsim(sys, e0, t, x0)
#零状态响应（输入可以为e1 ~e3）
tout, yzs, xzs = signal.lsim(sys, e2, t)
#零全响应（输入可以为e1 ~e3）
tout, y, x = signal.lsim(sys, e2, t, x0)
# 手动画图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.subplot(221)
plt.grid()
plt.title('零输入响应')
plt.plot(tout, yzi)  # 输出 = xout.T[2]
plt.plot(tout, xzi.T[0],'r--')  # 状态1

plt.subplot(222)
plt.grid()
plt.title('零状态响应')
plt.plot(tout, yzs)  # 输出 = xout.T[2]
plt.plot(tout, xzs.T[0],'r--')  # 状态1

plt.subplot(223)
plt.grid()
plt.title('全响应')
plt.plot(tout, y)  # 输出 = xout.T[2]
plt.plot(tout, x.T[0],'r--')  # 状态1

plt.tight_layout()
plt.show()


plt.figure()
plt.subplot(221)
plt.grid()
plt.title('零输入响应')
plt.plot(tout, yzi)  # 输出 = xout.T[2]
plt.plot(tout, xzi.T[0],'r--')  # 状态1

plt.subplot(222)
plt.grid()
plt.title('零状态响应')
plt.plot(tout, yzs)  # 输出 = xout.T[2]
plt.plot(tout, xzs.T[0],'r--')  # 状态1

plt.subplot(223)
plt.grid()
plt.title('全响应')
plt.plot(tout, y)  # 输出 = xout.T[2]
plt.plot(tout, x.T[0],'r--')  # 状态1

plt.tight_layout()
plt.show()