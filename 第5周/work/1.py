import numpy as np
import matplotlib.pylab as plt

t = np.arange(-1.0 , 10.0 , 0.01)

ha_plus = np.heaviside(t + np.pi,1/2)
ha_minus = np.heaviside(t - np.pi,1/2)

fn1 = np.sinc(t / np.pi) * (ha_plus - ha_minus)
fn2 = np.sinc(t) * (ha_plus - ha_minus)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
plt.subplot(211)
plt.grid()
plt.plot(t,fn1)

plt.subplot(212)
plt.grid()
plt.plot(t,fn2)

plt.tight_layout()
plt.show()