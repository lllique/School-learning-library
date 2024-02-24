import numpy as np  
import matplotlib.pyplot as plt  
  
n = np.arange(-3,8,0.1)  
  
h = np.heaviside(n,0.5) - np.heaviside(n - 5,0.5)  
x = (np.heaviside(n,0.5) - np.heaviside(n - 5,0.5)) * n  
  
y = np.convolve(h,x)  
  
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  
  
plt.figure()  
  
plt.subplot(311)  
plt.grid()  
plt.title('h(n)')  
plt.xlabel("n")  
plt.stem(range(len(n)),h) 
  
plt.subplot(312)  
plt.grid()  
plt.title('x(n)')  
plt.xlabel("n")  
plt.stem(range(len(n)),x) 
  
plt.subplot(313)  
plt.grid()  
plt.title('y(n)')  
plt.xlabel("n")  
plt.stem(range(len(y)),y)
  
plt.tight_layout()  
plt.show()