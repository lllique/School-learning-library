import sympy as sy
t,s = sy.symbols('t s')

system1 = {
    "r1" : 1840,
    "r2" : 1840,
    "c1" : 1,
    "c2" : 1.17
}

ht = 1 / (system1["c1"] * system1["c2"] * system1["r1"] * system1["r2"] * t * t + system1["c1"] * (system1["r1"] + system1["r2"]) * t + 1)

# hs = sy.laplace_transform(ht,t,s)
# ahs = sy.inverse_laplace_transform(hs[0],s,t)
# print(ahs)

ahs = sy.inverse_laplace_transform(ht,t,s)
print(ahs)

# -> 0.00131812839693659*exp(-0.000464511334076551*s)*sin(0.000191522929469419*s)*Heaviside(s)