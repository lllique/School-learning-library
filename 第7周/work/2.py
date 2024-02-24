import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import shift

t = np.linspace(-10, 10, 1000)
u = np.heaviside(t, 1)

y = u + shift(u,-50,cval=1)


plt.figure()
plt.subplot(211)
plt.grid()
plt.title('function input')
plt.plot(t,u)

plt.subplot(212)
plt.grid()
plt.title('function output')
plt.plot(t,y)

plt.tight_layout()
plt.show()