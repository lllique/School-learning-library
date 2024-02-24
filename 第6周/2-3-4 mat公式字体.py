import matplotlib.pylab as plt  # 绘制图形

plt.figure()  # 新建绘图
#指定全局字体
plt.rcParams['font.family'] = 'serif'  # 指定衬线字体
plt.rcParams['font.serif'] = ['SimSun']  # 指定默认字体
#plt.rcParams['font.family'] = 'sans-serif'  # 指定衬线字体
#plt.rcParams['font.sans-serif'] = ['SimSun'] #指定非衬线字体
plt.rcParams['font.size'] = 12  #字体大小
# 解决使用中文字体时，图像中的负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
# 公式字体风格
plt.rcParams['mathtext.fontset'] = 'stix'


plt.text(0.2, 0.2, r"$ \mu \alpha \tau \pi \lambda \omega  \iota \beta $")
plt.text(0.2, 0.4, r"$ \lim_{x \rightarrow \infty} \frac{1}{x} $")
plt.text(0.2, 0.8, r"$ a \leq  b  \leq  c  \Rightarrow  a  \leq  c$")
plt.text(0.4, 0.2, r"$ \sum_{i=1}^{\infty}\ x_i^3$")
plt.text(0.4, 0.4, r"$ \sin(\frac{3\pi}{2}) = \cos(\pi)$")
plt.text(0.4, 0.6, r"$ \sqrt[3]{x} = \sqrt{y}$")
plt.text(0.6, 0.6, r"$ \neg (a \wedge b) \Leftrightarrow \neg a \ \vee \neg b$")
plt.text(0.6, 0.2, r"$ \int_a^b f(x)dx$")
plt.title(r"公式$f(x)$", loc='left')

plt.tight_layout()  # 紧凑布局，防止标题重叠
plt.show()

'''
宋体 SimSun

黑体 SimHei

微软雅黑 Microsoft YaHei

微软正黑体 Microsoft JhengHei

新宋体 NSimSun

新细明体 PMingLiU

细明体 MingLiU

标楷体 DFKai-SB

仿宋 FangSong

楷体 KaiTi

仿宋_GB2312 FangSong_GB2312

楷体_GB2312 KaiTi_GB2312

'''