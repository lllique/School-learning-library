import numpy as np
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

'''定义系统（状态方程）'''
L = 1
C = 1
R = 0  # 无阻尼
sys0 = signal.StateSpace([[-R / L, -1 / L], [1 / C, 0]], [[1 / L], [0]], [0, 1], [0])
L = 1
C = 1
R = 0.2  # 欠阻尼
sys1 = signal.StateSpace([[-R / L, -1 / L], [1 / C, 0]], [[1 / L], [0]], [0, 1], [0])
L = 1
C = 1
R = 2  # 临界阻尼
sys2 = signal.StateSpace([[-R / L, -1 / L], [1 / C, 0]], [[1 / L], [0]], [0, 1], [0])
L = 1
C = 1
R = 3  # 过阻尼
sys3 = signal.StateSpace([[-R / L, -1 / L], [1 / C, 0]], [[1 / L], [0]], [0, 1], [0])

t = np.arange(0, 10, 0.01)
# 定义输入
e = np.ones_like(t)  # 输入信号，相当于u(t)
e1 = np.sin(2 * t)  # 输入信号，相当于u(t)

# 零状态响应
tout, y0, x0 = signal.lsim(sys0, e, t)
tout, y1, x1 = signal.lsim(sys1, e, t)
tout, y2, x2 = signal.lsim(sys2, e, t)
tout, y3, x3 = signal.lsim(sys3, e, t)
# 手动画图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.subplot(221)
plt.grid()
plt.title('无阻尼')
plt.plot(tout, y0)  # 输出 = xout.T[2]
plt.plot(tout, x0.T[0], 'r--')  # 状态1

plt.subplot(222)
plt.grid()
plt.title('欠阻尼')
plt.plot(tout, y1)  # 输出 = xout.T[2]
plt.plot(tout, x1.T[0], 'r--')  # 状态1

plt.subplot(223)
plt.grid()
plt.title('临界阻尼')
plt.plot(tout, y2)  # 输出 = xout.T[2]
plt.plot(tout, x2.T[0], 'r--')  # 状态1

plt.subplot(224)
plt.grid()
plt.title('过阻尼')
plt.plot(tout, y3)  # 输出 = xout.T[2]
plt.plot(tout, x3.T[0], 'r--')  # 状态1

plt.tight_layout()
plt.show()


plt.figure()
plt.subplot(221)
plt.grid()
plt.title('无阻尼')
plt.plot(x0.T[1], x0.T[0])


plt.subplot(222)
plt.grid()
plt.title('欠阻尼')
plt.plot(x1.T[1], x1.T[0])

plt.subplot(223)
plt.grid()
plt.title('临界阻尼')
plt.plot(x2.T[1], x2.T[0])

plt.subplot(224)
plt.grid()
plt.title('过阻尼')
plt.plot(x3.T[1], x3.T[0])

plt.tight_layout()
plt.show()
