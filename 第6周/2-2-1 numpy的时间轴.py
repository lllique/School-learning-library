import numpy as np
import matplotlib.pylab as plt  # 绘制图形
'''时间轴（区间和采样间隔等）的定义方式'''
t1 = np.arange(-10.0, 10.0, 1)
t2 = np.linspace(-10, 10, 20)
print("序列长度对比",len(t1), len(t2))
print("序列形状（维度）对比",t1.shape,t2.shape)#<class 'numpy.ndarray'>
print("序列类型",type(t1), type(t2))
print('t1:',t1)
print('t2',t2)
#显示ndarray的长度

'''对位计算'''
n = np.linspace(-10.0, 10.0, 20)#一共20个点，最后是闭区间
#有限长序列 20个点,如果增加一个点或减少一个点，则无法进行序列加减法操作
x1 = np.array([1,2,3,3,2,1,2,3,4,3,2,4,3,2,1,2,3,2,1,2])
x2 = np.sin(n)
print('x1+x2',x1+x2)
#

