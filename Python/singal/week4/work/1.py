import matplotlib.pylab as plt
import sympy as sy

w = 2 #待定数据
t0 = 2 #待定数据
t = sy.Symbol('t')

print("变量列表:w = %d , t0 = %d"%(w,t0))

x1 = sy.sin(w * t) * sy.Heaviside(t)
x2 = sy.sin(w * (t - t0)) * sy.Heaviside(t)
x3 = sy.sin(w * t) * sy.Heaviside(t - t0)
x4 = sy.sin(w * (t - t0)) * sy.Heaviside(t - t0)

# 显示中文必要条件
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

p1 = sy.plot(x1,(t,-5,5),title='x1',xlabel='t',show=False)
p2 = sy.plot(x2,(t,-5,5),title='x2',xlabel='t',show=False)
p3 = sy.plot(x3,(t,-5,5),title='x3',xlabel='t',show=False)
p4 = sy.plot(x4,(t,-5,5),title='x4',xlabel='t',show=False)

#组合显示
sy.plotting.PlotGrid(2,2,p1,p2,p3,p4)