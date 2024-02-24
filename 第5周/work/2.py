import numpy as np
import matplotlib.pylab as plt

x = np.arange(-1,10,1)
sig = np.exp((-0.5 + 10j) * x)

re_sig = sig.real
im_sig = sig.imag
abs_sig = np.abs(sig)
ang_sig = np.unwrap(np.angle(sig))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
plt.subplot(221)
plt.grid()
plt.title("实部",loc='left')
plt.stem(x,re_sig)

plt.subplot(222)
plt.grid()
plt.title("虚部",loc='left')
plt.stem(x,im_sig)

plt.subplot(223)
plt.grid()
plt.title("模值",loc='left')
plt.stem(x,abs_sig)

plt.subplot(224)
plt.grid()
plt.title("相位_解卷绕",loc='left')
plt.stem(x,ang_sig)

plt.tight_layout()
plt.show()