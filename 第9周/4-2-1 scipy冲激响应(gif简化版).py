
from scipy import signal
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt

# 计算impulse的辅助时间轴
t1 = np.arange(0, 5, 0.01)
'''这里的做动画方法，不是常规的做法，效率不高，但好理解'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 初始化画布
fig, ax = plt.subplots()


def animate(i):
    # 计算曲线
    a = i * 0.1 + 0.2  # 注意i从0开始
    system = ([0, a], [1, a])
    t, y = signal.impulse(system, T=t1)
    # 更新曲线，清除之前的东西，完全重画
    plt.clf()
    plt.grid()
    plt.axis([0, 5, 0, 2])# 直接给出轴范围,x轴0-5,y轴0-2
    plt.plot(t, y)
    plt.title("a对冲激响应的影响（a=%.2f）" % a)


# 生成动画、存储并显示
ani = animation.FuncAnimation(fig=fig, func=animate, frames=20, interval=200)
#20帧 fig确定画布 interval是帧的间隔
ani.save("a-tau.gif", writer='pillow')
plt.show()
