import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-3 ,8 ,0.01)

h = np.heaviside(t , 0.5) - np.heaviside(t - 5 , 0.5)
x = (np.heaviside(t , 0.5) - np.heaviside(t - 5 , 0.5)) * t

f = np.convolve(x , h)

plt.figure()

plt.subplot(311)
plt.grid()
plt.title("h(t)")
plt.xlabel("t")
plt.plot(t,h)

plt.subplot(312)
plt.grid()
plt.title("x(t)")
plt.xlabel("t")
plt.plot(t,x)

plt.subplot(313)
plt.grid()
plt.title("f(t)")
plt.xlabel("t")
plt.plot(range(len(f)),f)

plt.tight_layout()
plt.show()