import numpy as np
from scipy import signal

print("例4")
r,p,k = signal.residuez([1,0,0],[1,-1.5,0.5])
print(r,p,k)


print("例5")
r,p,k = signal.residuez([1, 0 ,0, -3],[1, -5, 6,0])
print(r,p,k)