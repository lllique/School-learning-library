import numpy as np
from scipy import signal
import matplotlib.pylab as plt


plt.figure()
for a in [-0.5,0,0.5]:
    
    system = signal.lti([1,0],[1,a])

    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.sans-serif'] = ['SimSun']
    plt.rcParams['axes.unicode_minus'] = False



    p = system.poles
    z = system.zeros

    if(a == -0.5):
        plt.subplot(131)
    elif(a == 0):
        plt.subplot(132)
    else:
        plt.subplot(133)
    
    plt.title(f"System零极点 a = {a}")
    plt.xlim(-100 , 100)
    plt.grid()
    plt.plot(p.real,p.imag,'x')
    plt.plot(z.real,z.imag,'x')

plt.tight_layout()
plt.show()