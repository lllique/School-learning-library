# import numpy as np
# from numpy.fft import fftfreq,fftshift,fft
# from scipy import signal
# import matplotlib.pyplot as plt

# a = 100
# sample_freq = 1000
# sample_interval = 1 / sample_freq
# t = np.arange(0,100 / a,sample_interval)
# lpf = ([0 , a] , [1 , a])
# t , ht = signal.impulse(lpf,T = t)


# hw = fftshift(fft(ht)) * sample_interval

# hw_amp =  np.abs(hw)

# plt.rcParams['font.sans-serif'] = ['SimSun']
# plt.rcParams['axes.unicode_minus'] = False 

# plt.subplot(111)
# plt.grid()
# plt.xlim(0,5/a)
# plt.plot(t,hw_amp)

# plt.show()


import numpy as np
import matplotlib.pyplot as plt

a = 10
# 定义频率范围
f = np.arange(-2000, 2000,1 / a)

# 计算理想高通滤波器的频率响应
H = (0 - np.heaviside(f - 1000,0) + np.heaviside(f + 1000,0))
H = 1 - H

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False 

# 绘制频谱图
plt.plot(f, H)
plt.grid()
plt.xlim(-2000,2000)
plt.show()



