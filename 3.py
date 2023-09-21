import matplotlib.pylab as plt
import sympy as sy

w = sy.Symbol('w')
h = sy.symbols('h',cls=sy.Function)
# zero = sy.Symbol('zero')
# zero = 0

h = sy.exp((sy.Heaviside(w - 5) - sy.Heaviside(w + 5)) * w * sy.I)

#显示中文的必要条件
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

p1 = sy.plot(sy.Abs(h),(w,-10,10),title='H(w)的相位',xlabel='w',ylabel='H(w)的相位',show=False)
p2 = sy.plot(sy.arg(h),(w,-10,10),title='H(w)的模值',xlabel='w',ylabel='H(w)的模值',show=False)

sy.plotting.PlotGrid(2,1,p1,p2)

# import matplotlib.pylab as plt
# import sympy as sy

# w = sy.Symbol('w')
# h = sy.symbol('h',cls=Function)

# h = sy.Piecewise(
#     (0, sy.Heaviside(w - 5) + sy.Heaviside(w + 5) != 0),
#     (sy.exp(-2 * sy.I * w), sy.Heaviside(w - 5) + sy.Heaviside(w + 5) == 0)
# )

# # 显示中文的必要条件
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# p1 = sy.plot(sy.Abs(h), (w, -10, 10), title='H(w)的相位', xlabel='w', ylabel='H(w)的相位', show=False)
# p2 = sy.plot(sy.arg(h), (w, -10, 10), title='H(w)的模值', xlabel='w', ylabel='H(w)的模值', show=False)

# display = sy.plotting.PlotGrid(2,1,p1,p2)
# display.show
