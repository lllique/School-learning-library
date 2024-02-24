import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sgn

sample_freq = 2048
sample_interval = 1 / sample_freq

tao = 1

t = np.linspace(0,5,5 * sample_freq)

f1 = np.heaviside(t,0.5) - np.heaviside(t-2,0.5)
f2 = np.exp(-3 * t) * np.heaviside(t,0.5)


t1 = datetime.datetime.now()
r1 = np.convolve(f1 , f2 , mode="full") * sample_interval
t2 = datetime.datetime.now()

print("卷积计算时间:",t2 - t1)
r1 = r1[:len(t)]

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
plt.subplot(111)
plt.title("卷积积分", loc='center')
plt.plot(t, r1, c='r')
plt.grid()

plt.tight_layout()
plt.show()