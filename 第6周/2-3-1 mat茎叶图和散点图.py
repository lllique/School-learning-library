import numpy as np
import matplotlib.pyplot as plt  #和 numpy 或 scipy使用,几乎不会和sumpy使用

x = np.array([1, 2, 4, 2, 3])
n = np.array([-2, -1, 0, 1, 2])  # 绘图的横坐标，

plt.figure()  # 新建绘图 参数:plt.figure(figsize=(21,9),dpi=50) 表示显示比例和铺平状态
plt.grid()  # 显示网格
plt.plot(n, x)
# plt.scatter(n,x,c='b',marker = "<") #散点图
plt.stem(n, x, linefmt='--c2', markerfmt='<r', basefmt="-c2")  # 茎叶图 --c2中c是颜色2是粗细--是线型 markerfmt如果是只填r就是圆点,r是颜色,<是形状
plt.show()

#plt.figure.savefig(r"文件名.jpg",dpi=50) dpi可以忽略,r""可以忽略转义
#plot里面的参数: c=''颜色 ls=''线型(散点图) makerfmt=''标点