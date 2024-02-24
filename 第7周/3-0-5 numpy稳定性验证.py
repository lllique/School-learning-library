import numpy as np
# 构造一个单位样值信号
x = np.zeros(10)
x[0] = 1
print('x=',x)
# 系统(相当于冲激响应)
h = np.log(x)
# 查看是否绝对可和
print(np.sum(abs(h)))


