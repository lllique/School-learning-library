import numpy as np
#对于复变函数
n = np.arange(0,21)
x = np.exp(1j*np.pi/8*n)
#方法1：复数求模:利用abs求模值，pow求平方
e1 = np.sum(np.power(abs(x),2))
#e1 = np.sum(pow(abs(x),2))
print(e1) #能量为21
# #方法2：复数乘以其共轭（np.conj），得到平方和
# #但此时的结果为21+0j，所以再用abs求模
e2 = np.sum(abs(x*np.conj(x)))
print(e2) #能量为21
