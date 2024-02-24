from sympy import *
import matplotlib.pyplot as plt
import numpy as np
N=10
x,y,z = symbols("x y z ")
z = 1/x
#--------------------- Put the transfer function H(z) here
H=2*z/(2*z-1)
#---------------------
a=Poly(series(H, x0=0, n=N))
Pol_i= simplify((a/1).expand())
Coeffs=np.array([])
for i in range(N): 
  coeff_i=Pol_i.subs(x,0)
  if coeff_i/coeff_i==1: 
    coef= coeff_i
    Pol_i = Pol_i -coef
  else: 
    coef= 0
  Coeffs =np.append(Coeffs,[coef]) 
  Pol_i= simplify((Pol_i)/x).expand()
fig=plt.figure(figsize=(12,4), dpi= 100)
for i,val in enumerate(Coeffs):
    plt.vlines(i, 0, val, color='red')
plt.plot (Coeffs,"go")
plt.xlabel('n', fontsize=14)
plt.ylabel('Impulse Response [n]', fontsize=14)
plt.title('Inverse Z-Transform', fontsize=14)
plt.grid()
plt.show()