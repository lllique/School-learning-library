import numpy as np
#from scipy.linalg import solve
from numpy.linalg import solve
# 1,求特征根
x = np.array([1, 7, 6])
x = np.array([1, 7, 16, 12])
print(np.roots(x))
print("-----------------------")
# 2,解线性方程组
# 注意np.mat定义的不是数组，而是矩阵，可以打印a和b查看其类型
a = np.mat([[3, 0, 0], [4, 3, 0], [2, 2, 3]])
b = np.mat([1, 2, 0]).T  # 常数项列矩阵，需要转秩为列,需要把行矩阵转秩为列才能计算
# 或者
b = np.mat([[1], [2], [0]])
# 查看a和b的内容和格式
print(a, type(a))
print(b, type(b))
# 求解
x = solve(a, b)
print(x)
# 小技巧：此时x是一个三行一列的matrix，如果希望得到list或ndadday：
x = x.T.tolist()[0]
# 即把x转置为一行三列，并转为数组，但此时x为只有一行的二维数组，所以用[0]把仅有的一行取出来
print(x, type(x))  # 得到一个一维的list，通过np.array(x)等方法还可以转为ndarray

print("-----------------------")
#3，例题中求待定系数的问题
a = np.mat([[1, 1], [-1, -6]])
b = np.mat([71/50, -3/25]).T  # 常数项列矩阵，需要转秩为列