import numpy as np
import matplotlib.pyplot as plt
#import matplotlib
#from matplotlib.pyplot import *

D = 1.5e-7j; E = 1+2j
D += E
print(D)

A = input("输入一个数字：")
print(A)

n = np.arange(0,10,1) #绘图的横坐标，长度自定
x = np.power(0.5,n) #幂级数，用np.pow
plt.figure()#新建绘图
plt.grid() #显示网格
plt.xlabel('n',loc = 'right')  # x轴
plt.stem(n,x, basefmt="-") #单位样值的棉棒图
# 设置字体，支持中文
plt.rcParams['font.sans-serif']=['STSong']
plt.title('幂级数')  # 标题
plt.tight_layout() #紧凑布局，防止标题重叠
plt.show()  # 显示
