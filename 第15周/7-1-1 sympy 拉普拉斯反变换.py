import sympy as sy
t,s = sy.symbols('t s')

print("变换对")
yt = sy.exp(-2*t)*sy.Heaviside(t) +  sy.exp(-3*t)*sy.Heaviside(t)
Ys = sy.laplace_transform(yt,t,s)
#注意Ys是一个tuple，反变换要取Ys[0]
#但如果正变换时用了noconds=True，则Ys就只是表达式
yt = sy.inverse_laplace_transform(Ys[0],s,t)
print(yt)

print("一般情况")
Ys = (s+2)/(s**2+4*s+3)
yt = sy.inverse_laplace_transform(Ys,s,t)
print(yt)

print("共轭复数根")
Ys = (s**2+3)/(s+2)/(s**2+2*s+5)
yt = sy.inverse_laplace_transform(Ys,s,t)
print(yt)

print("重根")
Ys = (s**2)/(s+2)/(s**2+2*s+1)
yt = sy.inverse_laplace_transform(Ys,s,t)
print(yt)


print("时移性")
Ys = sy.exp(-2*s)/(s**2+3*s+2)
yt = sy.inverse_laplace_transform(Ys,s,t)
print(yt)

print("分子的阶次大于分子")
Ys = (s**3+5*s**2+9*s+7)/(s**2+3*s+2)
yt = sy.inverse_laplace_transform(Ys,s,t)
print(yt)#结果有误，无法计算含有冲激偶的情况