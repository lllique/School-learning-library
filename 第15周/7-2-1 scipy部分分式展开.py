import numpy as np
from scipy import signal

print("单根情况 (s+2)/(s**2+4*s+3)")
r, p, k = signal.residue([1, 2], [1, 4, 3])
print(r, p, k)

print("共轭复数根 (s**2+3)/(s+2)/(s**2+2*s+5)")
roots = np.roots([1, 2, 5])
print(roots)
a = np.poly([-2, roots[0], roots[1]])  # 这里手动确定了roots中的根数量
print(a)
r, p, k = signal.residue([1, 0, 3], a)
print(r, p, k)

print("重根 (s**2)/(s+2)/(s**2+2*s+1)")
a = np.poly([-2, -1, -1])
print(a)
r, p, k = signal.residue([1, 0, 0], a)
print(r, p, k)

print("分子的阶次大于分子  (s**3+5*s**2+9*s+7)/(s**2+3*s+2)")
r, p, k = signal.residue([1, 5, 9, 7], [1, 3, 2])
print(r, p, k)

print("invres逆运算")
b, a = signal.invres(r, p, k)
print(b, a)

# 时移性无法体现
