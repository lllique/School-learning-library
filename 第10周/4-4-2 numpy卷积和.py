import numpy as np

x = np.array([1, 2, 3])
h = np.array([4, 5, 6, 7])
# x = np.array([1,1,1,1])
# h = np.array([1,1,1,1])
'''
方式1，直接利用numpy的卷积函数，注意mode参数的选择：
convolve(a, b, mode=‘full’)，参数：
　　　a:(N,)输入的一维数组
　　　b:(M,)输入的第二个一维数组
　　　mode:{‘full’, ‘valid’, ‘same’}参数可选
　　　　　‘full’　默认值，返回每一个卷积值，长度是N+M-1,在卷积的边缘处，信号不重叠，存在边际效应。
　　　　　‘same’　返回的数组长度为max(M, N),边际效应依旧存在。
　　　　　‘valid’ 　返回的数组长度为max(M,N)-min(M,N)+1,此时返回的是完全重叠的点,常用于cnn等算法中。
'''

y = np.convolve(x, h)  # 卷积和，默认mode为full
print('defult mode:', y)
y = np.convolve(x, h, mode='full')
print('full mode (length = 3+4-1):', y)
y = np.convolve(x, h, mode='same')
print('same mode (length = 4):', y)
y = np.convolve(x, h, mode='valid')
print('valid mode (length = 4 -3 + 1):', y)
'''
结果：
full mode (length = 3+4-1): [ 4 13 28 34 32 21]
same mode (length = 4): [13 28 34 32]
valid mode (length = 4 -3 + 1): [28 34]
注意！
same模式在需要画图的场景可能会很方便。
但Same和valid都会从两侧进行裁剪，在实际使用时，可能会导致有效结果缺失
此时可以调整时间轴的有效范围，并再函数两侧补零
'''
# 两侧补零，使得卷积函数和卷积结果的长度一致，且没有结果缺失
x = np.array([0, 1, 2, 3, 0, 0])
h = np.array([0, 4, 5, 6, 7, 0])
y = np.convolve(x, h, mode='same')
print('same mode (补零):', y)

'''方式2，引入scipy的卷积函数，参数效果相同
import scipy.signal as sgn
y = sgn.convolve(x, h)  # 卷积和
print(y)
'''
