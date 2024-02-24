import numpy as np

n = np.arange(0, 21)  # 不写抽样间隔，则默认间隔为1
x = np.exp(1j * np.pi / 8 * n)
# 方法1：复数求模:利用abs求模值，pow求平方
# e = np.sum(np.power(abs(x),2))
e = np.sum(pow(abs(x), 2))
print("pow+abs方法:", e)  # 能量为21
# 方法2：复数乘以其共轭（np.conj），得到平方和,但实际格式为 模值的平方和+0j
e = np.sum(x * np.conj(x))
print("乘共轭方法-1:", e)  # 注意输出可能是 (21+9.674501701529713e-17j)，这个虚部近似为0，这里有精度的问题
# 因此对于每个值再求abs，然后再求和，
e = np.sum(abs(x * np.conj(x)))
print("乘共轭方法-2:", e)
# 当然也可以先求和，再用abs求模值（即去掉虚部）
# #但直接计算结果为21+0j，所以再用abs求模
e = abs(np.sum(x * np.conj(x)))
print("乘共轭方法-3:", e)
# 方法3：用内积方法dot，即相乘再求和，直接计算结果仍为21+0j，
e = np.dot(x, np.conj(x))  # dot
print("dot+乘共轭方法-1:", e)
# 所以再用abs求模（注意abs的位置）
e = abs(np.dot(x, np.conj(x)))
print("dot+乘共轭方法-2:", e)
# 扩展话题：
# cumsum()函数用于实现逐个累加运算，得到一个序列
# 可以用来近似表示连续信号的运动积分。
x = [1, 2, 3, 4]
print("逐个累加运算，得到一个序列", np.cumsum(x))
