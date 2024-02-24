import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
h = np.array([4, 5, 6])
# 卷积和
y = np.convolve(x, h)

plt.subplot(3, 1, 1)
plt.xlim(-1, len(y))
plt.stem(range(len(x)), x)

plt.subplot(3, 1, 2)
plt.xlim(-1, len(y))
plt.stem(range(len(x)), h)

plt.subplot(3, 1, 3)
plt.xlim(-1, len(y))
plt.stem(range(len(y)), y, basefmt="-")

plt.show()
