import numpy as np
import matplotlib.pylab as plt  # 绘制图形

x = np.arange(-10.0, 10.0, 0.01)  # 采样点：取-10.0到10.0，间隔为0.01
sig = np.exp((-0.5 + 10j) * x)
print(sig)
#获得实部虚部等
re_sig = sig.real
im_sig = sig.imag
abs_sig = np.abs(sig)
ang_sig = np.unwrap(np.angle(sig))  # 相位解卷绕
#ang_sig = np.angle(sig) #相位没有解卷绕，则相位取值在正负pi之间

#支持中文
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题

plt.figure()#新建绘图
plt.subplot(221)
plt.grid()  # 显示网格
plt.title("复函数-实部", loc='left')
plt.plot(x, re_sig)

plt.subplot(222)
plt.grid()  # 显示网格
plt.title("复函数-虚部", loc='left')
plt.plot(x, im_sig)

plt.subplot(223)
plt.grid()  # 显示网格
plt.title("复函数-模值", loc='left')
plt.plot(x, abs_sig)

plt.subplot(224)
plt.grid()  # 显示网格
plt.title("复函数-相位", loc='left')
plt.plot(x, ang_sig)

plt.tight_layout()
plt.show()  # 显示
