import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import *

sample_freq = 2048
sample_interval = 1 / sample_freq

t = np.linspace(0,5,5 * sample_freq)

f1 = np.heaviside(t,0.5) - np.heaviside(t - 2,0.5)
f2 = np.exp(-3 * t) * np.heaviside(t,0.5)

f = fftshift(fftfreq(len(t),sample_interval))
ew_f1 = fftshift(np.abs(fft(f1))) * sample_interval
ew_f2 = fftshift(np.abs(fft(f2))) * sample_interval

p = ew_f1 * ew_f2

pf = abs(ifft(p,len(p)))

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False 

plt.subplot(111)
plt.grid()
plt.xlabel('x',loc="right")
plt.plot(t,pf,c="orange")

plt.tight_layout()
plt.show()