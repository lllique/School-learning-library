import matplotlib.pylab as plt
import numpy as np
from numpy.fft import fftfreq,fftshift,fft,ifftshift,ifft


采样频率 = 2048
采样间隔 = 1/采样频率

t = np.arange(0,5,采样间隔)
f1 = np.heaviside(t,0.5) - np.heaviside(t - 2,0.5) #门函数
f2 = np.exp(-3 * t) * np.heaviside(t,0.5) #指数函数

频轴 = fftshift(fftfreq(len(t) , 采样间隔))

fw1 = fftshift(fft(f1))

#取模值
fw1_amp = np.abs(fw1 * 采样间隔)


fw2 = fftshift(fft(f2))
fw2_amp = np.abs(fw2)

plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False 


plt.subplot(121)
plt.grid()
plt.title("f1幅度谱")
plt.xlim(0,5)
plt.xlabel(r'$time\rm{(s)}$',loc="right")
plt.plot(频轴,fw1_amp)


plt.subplot(122)
plt.grid()
plt.title("f2幅度谱")
plt.xlim(0,5)
plt.xlabel(r'$time\rm{(s)}$',loc="right")
plt.plot(频轴,fw2_amp)

plt.tight_layout()
plt.show()