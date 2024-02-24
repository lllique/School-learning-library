import numpy as np
import matplotlib.pylab as plt  # 绘制图形

t = np.arange(-10.0, 10.0, 0.01)  # 采样点：取-10.0到10.0，间隔为0.01
#原始信号
y = np.piecewise(t, [t >= 0, t >= 2, t >= 3], [1, lambda x: 3 - x, 0, 0])#lambda中的x是局部变量

'''信号压缩扩展
场景1：直接修改定义，选择或修改合适的a即可，
此时采样的密度等都没有发生变化（时间没变）
注意一切变换对t而言，做变换时需要倍乘所有的t

'''
a = 1 #原始定义
a = 2 #y(2t)，即所有的t都变成2t
y2 = np.piecewise(t, [a * t >= 0, a * t >= 2, a * t >= 3], [ 1, lambda t: 3 - a * t, 0, 0])
a = 0.5 #y(1/2t)，即所有的t都变成1/2t
y1_2 = np.piecewise(t, [a * t >= 0, a * t >= 2, a * t >= 3], [ 1, lambda t: 3 - a * t, 0, 0])

plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题

plt.figure()#新建绘图
plt.subplot(311) #子图1
plt.grid() #显示网格
plt.plot(t, y)

plt.subplot(312) #子图2
plt.grid() #显示网格
plt.xlim((-10,10))
plt.plot(t, y2)

plt.subplot(313) #子图2
plt.grid() #显示网格
plt.xlim((-10,10))
plt.plot(t, y1_2)
plt.tight_layout()
plt.show()  # 显示


exit()

'''信号插值'''
#方法1：利用scipy的interp1d方法
#构造一个插值时间轴，表示在原有的时间轴上增加密度
t1 = np.arange(-10.0, 10.0, 0.005)
from scipy import interpolate
#f是一个插值函数
f = interpolate.interp1d(t, y1, kind='linear',fill_value="extrapolate")#kind可选#'linear','nearest'等
'''
如果下一句报错ValueError: A value in x_new is below the interpolation range.
在使用上述插值函数进行预测的时候，所给的x的取值超出了【生成该函数时候所使用的X】的取值范围，
函数给不出预测值，因此报错。
解决方法：加入参数：fill_value="extrapolate"，主要作用是预测序列两侧的值
'''
#用上面生成f函数来进行实际的插值，注意参数是一个和源信号区间相同但密度更大的区间
y7 = f(t1)
print('scipy插值长度:',len(y7))
#效果是由2000个点变成了4000个点，此时如果画图，需要重新构建一个画图时间轴
t2 = np.arange(-20.0, 20.0, 0.01)
#方法2：利用numpy的库
y8 =  np.interp(t1, t, y1)
print('numpy插值长度:',len(y8))


