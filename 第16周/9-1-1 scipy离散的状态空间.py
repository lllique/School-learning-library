import numpy as np
from scipy import signal
import matplotlib.pylab as plt  # 绘制图形

a = [[0, 1 / 2, -1 / 2], [-1, -1, 0], [1, 0, -1]]#3*3
b = [[0], [1], [0]]#1*3
c = [0, 0, 1]#3*1
d = [0]#[0,0,0]
#利用scipy
'''定义系统（状态方程）'''
sys = signal.StateSpace(a, b, c, d).to_discrete(1)#<class 'scipy.signal._ltisys.StateSpaceContinuous'>

print('转为传输函数形式的系统，输出仍为系统')
print(sys.to_tf())
print('零极点形式的系统，输出仍为系统')
print(sys.to_zpk())
print('得到系统函数（B、A）,逆运算为tf2ss')
print(signal.ss2tf(a, b, c, d))
print('得到零极点（z、p、k），逆运算为zpk2ss')
print(signal.ss2zpk(a, b, c, d))
#求响应，输出的xout为状态变量
t = np.arange(0,10,0.01)
e = np.ones_like(t)# 输入信号，相当于u(t)
x0 = [0, 0,0]  # 初始状态，实际也是默认情况
tout, yout, xout = signal.dlsim(sys,e,t,x0)
print(yout.shape)
print(xout.shape)#其形状为(1000, 3)，画图时可能需要转置

# 手动画图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure()
plt.grid()
plt.stem(tout, yout)#输出 = xout.T[2]
plt.stem(tout, xout.T[0],linefmt='--c2')#状态1
plt.show()
