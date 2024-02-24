from sympy import *
import matplotlib.pylab as plt  # 绘制图形
from sympy.physics.control import *

plt.rcParams['font.sans-serif']=['STSong']#中文字体
plt.rcParams['axes.unicode_minus'] = False #解决图像中的负号'-'显示为方块的问题

s = symbols('s')
#分子/分母
tf1 = TransferFunction(s**2 + 1, s**4 + 4*s**3 + 6*s**2 + 5*s + 2, s)
#零极点图
pole_zero_plot(tf1)
#波特图
bode_plot(tf1, initial_exp=0.2, final_exp=0.7)
#冲激响应
impulse_response_plot(tf1)
#阶跃响应
step_response_plot(tf1)
#判断这个系统是否稳定
print(tf1.is_stable())

'''
https://docs.sympy.org/latest/modules/physics/control/control_plots.html
'''