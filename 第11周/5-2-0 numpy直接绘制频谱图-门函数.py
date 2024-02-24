import matplotlib.pylab as plt  # 绘制图形
import numpy as np
from scipy import signal, integrate

# 公共参数
E = 1
tao = 1
a = 2
t = np.arange(-3 * tao, 3 * tao, 0.01)
# 定义时域信号：门函数
ft = E * np.heaviside(t + tao / 2, 1) - E * np.heaviside(t - tao / 2, 1)

# 直接定义频谱
w = np.arange(-3 * 2 * np.pi / tao, 3 * 2 * np.pi / tao, 0.01)  # 带宽和脉宽为反比
Fw = E * tao * np.sin(w * tao / 2) / (w * tao / 2) #实函数可以直接画图

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(2, 2, 1)
plt.grid()  # 显示网格
plt.title("时域信号", loc='left')
plt.plot(t, ft)  # 谐波叠加情况
plt.xlabel(r'$time\rm{(s)}$', loc='right')

plt.subplot(2, 2, 2)
plt.grid()  # 显示网格
plt.title("频谱函数", loc='left')
plt.plot(w, Fw)
plt.xlabel("$Angular$ $frequency(\omega)$", loc='right')

plt.subplot(2, 2, 3)
plt.grid()  # 显示网格
plt.title("幅度谱", loc='left')
plt.plot(w, np.abs(Fw))
plt.xlabel("$Angular$ $frequency(\omega)$", loc='right')

plt.subplot(2, 2, 4)
plt.grid()  # 显示网格
plt.title("相位谱", loc='left')
plt.plot(w, np.angle(Fw))
plt.xlabel("$Angular$ $frequency(\omega)$", loc='right')
'''把纵坐标刻度值 设置为：显示：1π、2π……的形式
首先定义一个合适的纵坐标范围（linspace或arange），所有数值都在π的整数或0.5倍上！否则刻度会出现”0.3333333π“之类的情况。
然后是使用map方法把数值应为为所需形式：定义一个lambda函数，所有的x除以pi得到相对于pi的倍数，然后再附加字符”π“，
map函数会形成字符串序列存储label，字符串引号前面的f表示内部大括号内为变量值，lambda表达式表示这个变量是由里面的函数定义的。
最后使用yticks使这个坐标标签生效，参数分别为映射前和映射后的序列。
效果：比如某个函数值3.14，会映射为1π，并对应到合适的纵坐标上。
'''
y = np.linspace(- np.pi, np.pi, 5)
labels = map(lambda x: f"${x / np.pi}π$", y)
plt.yticks(y, labels)
plt.ylim(-0.1,np.pi*1.1)#如果y坐标设置的过多，还可以用ylim再卡一下范围

plt.tight_layout()
plt.show()
