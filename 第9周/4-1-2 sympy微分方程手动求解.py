from sympy import *

'''手工分两步'''
print('------方式1--------')
'''另一种分两步的写法，步骤比较清晰'''
#理论上可以求解任意阶次微分方程、自动确定任意个数的待定系数
#定义自变量和函数，对于单输入单输出系统，只需要定义t和y
t = Symbol('t')
r = symbols('r', cls=Function)
diffeq = Eq(r(t).diff(t,2) + 7*r(t).diff(t) + 6*r(t), 6*sin(2*t))
#求通解，调用dsolve函数,返回一个Eq对象
respone = dsolve(diffeq, r(t))
print(respone) #Eq(r(t), C1*exp(-6*t) + C2*exp(-t) + 3*sin(2*t)/50 - 21*cos(2*t)/50)
print('------处理待定系数--------')
#两个初始值
#一组初始值：顺序以此为y(0),y'(0),y''(0)等，根据方程阶次给定初始值
iv = [1,0]
# 手动建立两个线性方程(如果不改动语句，则只能处理二阶微分方程)：
# 建立等式：#rhs表示eq等式的右边（right），lhs表示等式的坐标
# 建立r(0)时候的系数方程
y1 = respone.subs(t,0).rhs - respone.subs(r(t),iv[0]).lhs#rhs= C1*exp(-6*t) + C2*exp(-t) + 3*sin(2*t)/50 - 21*cos(2*t)/50) , lhs=r(t)
# 建立r'(0)时候的系数方程
y2 = respone.rhs.diff(t).subs(t,0)- respone.subs(r(t),iv[1]).lhs
#手动将待定系数定义为变量求解
C1 = Symbol('C1')
C2 = Symbol('C2')
print(solve([y1,y2],[C1,C2]))
#exit()

'''进阶的写法，理论上可以适配不同阶次的微分方程，只需要修改方程和iv'''
#理论上可以求解任意阶次微分方程、自动确定任意个数的待定系数
print('------方式2--------')
#定义自变量和函数，对于单输入单输出系统，只需要定义t和y
t = Symbol('t')
r = symbols('r', cls=Function)
diffeq = Eq(r(t).diff(t,2) + 7*r(t).diff(t) + 6*r(t), 6*sin(2*t))
#求通解，调用dsolve函数,返回一个Eq对象
respone = dsolve(diffeq, r(t))
print(respone)
print('------处理待定系数--------')
#一组初始值：顺序以此为y(0),y'(0),y''(0)等，根据方程阶次给定初始值
iv = [1,0]
#1，在iv长度的范围内，依次取n作为标号，即n可以取0和1两个标号
#2.rhs表示eq等式的右边（right），lhs表示等式的坐标
# 对于responge：Eq(y(t), C1*exp(-6*t) + C2*exp(-t) + 3*sin(2*t)/50 - 21*cos(2*t)/50)
#3.当n取0时，respone的右边求了0次导数，即没有求导，并且把t替换为0，respone的左边把r(t)替换为iv[0]，也就是1
#4，当n取1时，respone的左边求了一次导，并且把t替换为0，respone的左边把r(t)替换为iv[1]，也就是0
f_eqs = [(respone.rhs.diff(t,n).subs(t,0)- respone.lhs.subs(r(t),iv[n])) for n in range(len(iv))]
print(f_eqs)#得到线性方程：[C1 + C2 - 71/50, -6*C1 - C2 + 3/25]
#respone.free_symbols中包含三个自由变量{C1, t, C2}，排除t，C1和C2作为solve的未知数
factors =solve(f_eqs,respone.free_symbols,exclude=[t])#{C1, C2}作为未知数解线性方程组
print(factors) # {C1: -13/50, C2: 42/25}
#在通解中替换待定系数：
for i in factors: #注意针对字典类型可以直接使用for循环
    # i就是字典的键（C1\C2# ），get(t)是字典的值（冒号后门），即用值来替代键
    respone = respone.subs(i,factors.get(i))
print("全解:",respone.lhs,"=",respone.rhs) #另一种输出方式
