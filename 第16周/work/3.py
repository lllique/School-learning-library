import numpy as np
from scipy import signal
import matplotlib.pylab as plt

system1 = {
    "r1" : 1840,
    "r2" : 1840,
    "c1" : 1,
    "c2" : 1.17
}

system2 = {
    "r1" : 7661.3,
    "r2" : 761.3,
    "c1" : 1,
    "c2" : 6.83
}

sys1 = signal.lti([1],[system1["c1"] * system1["c2"] * system1["r1"] + system1["r2"],system1["c1"] * (system1["r1"] + system1["r2"]),1
])

sys2 = signal.lti([1],[system2["c1"] * system2["c2"] * system2["r1"] + system2["r2"],system2["c1"] * (system2["r1"] + system2["r2"]),1
])

p1 = sys1.poles
z1 = sys1.zeros
p2 = sys2.poles
z2 = sys2.zeros

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()

plt.subplot(121)
plt.title("system 1 零极点")
plt.grid()
plt.plot(p1.real , p1.imag , 'x')
plt.plot(z1.real , z2.imag , 'x')

plt.subplot(122)
plt.title("system 2 零极点")
plt.grid()
plt.plot(p2.real , p2.imag , 'x')
plt.plot(z2.real , z2.imag , 'x')

plt.tight_layout()
plt.show()


#  波特图
omega1 , mag1 , phase1 = sys1.bode(w = np.logspace(0,4,1000))
omega2 , mag2 , phase2 = sys2.bode(w = np.logspace(0,1,1000))
f1 = omega1 / 10
f2 = omega2 / 10

plt.figure()
plt.subplot(121)
plt.title('system 1 波特图')
plt.grid()
plt.semilogx(f1,mag1)

plt.subplot(122)
plt.title("system 2 波特图")
plt.grid()
plt.semilogx(f2,mag2)

plt.tight_layout()
plt.show()