import control as ct
import matplotlib.pylab as plt  # 绘制图形

b = [2, 0, 1]
a = [1, 4, 6, 5, 2]
# 构造一个系统（传输函数）
sys = ct.tf(b, a)
# 波特图
mag, phase, omega = ct.bode_plot(sys, dB=True, Hz=True, grid=True)
plt.show()  # 如果不加show()，则只会返回结果，不会出图
# 零极点图
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
p,z  = ct.pzmap(sys, plot=True, title="零极点图")
plt.show()
# 打印零极点结果
print(p,z)
# 冲激响应
T, yout = ct.impulse_response(sys)
plt.plot(T, yout)  # 利用结果自行画图
plt.show()
