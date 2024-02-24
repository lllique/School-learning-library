import control.matlab as ma
import matplotlib.pylab as plt  # 绘制图形

b = [2, 0, 1]
a = [1, 4, 6, 5, 2]
# 构造一个系统（传输函数）

sys = ma.TransferFunction(b, a)
# 波特图
mag, phase, omega = ma.bode(sys, dB=True, Hz=True, grid=True)
plt.show()  # 如果不加show()，则只会返回结果，不会出图
# 零极点图
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
p,z = ma.pzmap(sys, plot=True, title="零极点图")
plt.show()
# 打印零极点结果
print(z,p)
# 冲激响应
yout, T = ma.impulse(sys)
plt.plot(T, yout)  # 利用结果自行画图
plt.show()

#tf2zpk（得到zero, pole, gain）实际是从scipy拿过来的方法
z, p, k = ma.tf2zpk(b, a)
print(z, p, k)
