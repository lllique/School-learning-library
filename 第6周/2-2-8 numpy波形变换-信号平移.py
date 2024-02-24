import numpy as np
import matplotlib.pylab as plt  # 绘制图形
'''为方便计算采样点个数，定义一个采样间隔'''
deltaT = 0.01 #为方便计算，尽量保持该数值倒数为整数
sf = int(1 /deltaT) #单位时间内采样点的个数，默认倒数为浮点数，转为整数
tao = -3 #实际在时间轴上平移的距离
'''定义时间轴和函数'''
t = np.arange(-10.0, 10.0, deltaT)  # 采样点：取-10.0到10.0，间隔为0.01
y1 = np.piecewise(t, [t >= 0, t >= 2, t >= 3], [1, lambda x: 3 - x, 0, 0])#lambda中的x是局部变量
'''
信号平移
注意平移的数值是 平移的时间距离 * 单位距离采样点的个数
'''
#方法1：使用scipy的shift函数，注意参数为正时为右移
from scipy.ndimage import shift
y2 = shift(y1, tao * sf)

#方法2：自定义一个平移函数，注意参数为正时为右移
def NPshift(arr, num):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = 0
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = 0
        result[:num] = arr[-num:]
    else:
        result[:] = arr
    return result
y3 = NPshift(y1, tao * sf)


plt.figure()#新建绘图
plt.subplot(211) #子图1
plt.title("f(t)", loc='left')
plt.grid() #显示网格
plt.plot(t, y1)

plt.subplot(212) #子图2
plt.grid() #显示网格
plt.title("f(t)-(%d)"%tao, loc='left')
plt.plot(t, y3)

plt.tight_layout()
plt.show()  # 显示
