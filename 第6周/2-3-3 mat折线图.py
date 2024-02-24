import matplotlib.pylab as plt  # 绘制图形
import numpy as np

'''
参数定义
'''
sample_freq = 1024  # 采样频率（单位时长上的采样点个数）
t_length = 10  # 时域信号的总长度

'''
问题1，时间坐标的产生
'''
t = np.linspace(-t_length / 2, t_length / 2, t_length * sample_freq)
t1 = np.linspace(0, t_length, t_length * sample_freq)

'''Sa函数/sinc函数'''
sig11 = np.where(t == 0, 1, np.sin(5 * t) / (5 * t))
sig12 = np.sinc(5 * t)

'''衰减振荡函数'''
a = 0.5
sig3 = np.exp(-a * t1) * np.cos(10 * t1)
sig31 = np.exp(-a * t1)  # 包络线

'''marker演示'''
x1 = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
y1 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

# 坐标字体
lx = t_length / 2  # 横坐标
fontsize = 6  # 字体大小

plt.figure(figsize=(4, 3), dpi=120)  # 新建绘图,尺寸是英寸,100是dpi默认值
plt.rcParams['font.family'] = 'serif'  # 指定衬线字体
plt.rcParams['font.serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['font.size'] = fontsize  # 指定衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(221)
plt.grid()  # 显示网格
plt.xlim(-lx, lx)
plt.title("同参数$Sa(t)$和$Sinc(t)$", loc='left')
plt.xlabel(r'$time(s)$', fontsize=fontsize)
l1, = plt.plot(t, sig11, 'r')
l2, = plt.plot(t, sig12, 'g') #plot返回值有两个,用l2,获取第一个返回值
# 图例方式1
plt.legend(handles=[l1, l2], labels=['Sa(5t)', 'sinc(5t)'], loc='best')
# 定义横轴的位置，绑定到y轴的0
ax = plt.gca()  # gca:get current axis得到当前轴
ax.spines['bottom'].set_position(('data', 0))#实际修改的也是边框 将横坐标和纵坐标的0绑定

plt.subplot(222)
plt.grid()  # 显示网格
# plt.gca().set_visible(False) #控制显示隐藏
plt.xlim(0, lx)
plt.title("衰减振荡函数", loc='left')
plt.xlabel(r'$time(s)$')
plt.plot(t1, sig3, c='forestgreen', ls="-", lw=1)  # ,marker = "1"
plt.plot(t1, sig31, 'r--')
# 图例方式2
plt.legend(labels=['振荡函数', '包络线'])
# 隐藏坐标，包括grid
ax = plt.gca()
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False) #隐藏刻度值

plt.subplot(212)  # 如果设置错误，则会遮挡，重新设置即可
plt.grid()  # 显示网格
plt.plot(x1, y1, 'r-o', fillstyle='none')
# 如果把fmt中的线性不要了，就会出散点图
# plt.plot(x1, y1,'ro', fillstyle = 'none')
# 隐藏刻度值
ax = plt.gca()
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])

plt.suptitle("折线图的演示")  # 可选
plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()
