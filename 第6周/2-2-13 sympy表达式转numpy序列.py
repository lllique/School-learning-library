import sympy as sy
import matplotlib.pylab as plt  # 绘制图形
import numpy as np

x = sy.symbols('x')

# 定义一个np的时间轴，绘图和生成序列使用
t = np.arange(-3, 3, 0.01)

# 方式1：利用np.array的条件赋值方法，在条件中写入sympy函数
y1 = np.array([5 * sy.exp(-1 * i) * sy.cos(10 * i) * sy.Heaviside(i) for i in t])

# 方式2：自定义函数，再用lambdify方法，将其转换为numpy可用的序列方法，再生成序列
f = 5 * sy.exp(-1 * x) * sy.cos(10 * x) * sy.Heaviside(x)
f_np = sy.lambdify(x, f, "numpy")
y2 = f_np(t) # 不能直接用f

# 方式3：自定义函数，再用lambdify方法，将其转换单值函数，再利用np.array方法生成序列
f = 5 * sy.exp(-1 * x) * sy.cos(10 * x) * sy.Heaviside(x)
f_1 = sy.lambdify(x, f)
y3 = np.array([f_1(i) for i in t])  # 不能直接用f
y4 = f_1(t)  # 测试发现也可以执行，即lambdify参数中不加"numpy"也行

# 绘图
plt.grid()  # 显示网格
plt.plot(t, y1)
plt.show()
