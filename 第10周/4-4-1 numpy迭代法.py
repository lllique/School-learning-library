import numpy as np
import matplotlib.pyplot as plt

all = 100  # 100w
I = 0.049  # 年利率
period = 120  # 假定10年还完 1.0628
period = 360
# 总本金剩余情况
y = [0 for i in range(period)]
# 每月还款本金
B = [0 for i in range(period)]
# 每月还的利息
Im = [0 for i in range(period)]
# 本月还款总金额，必须大于100*0.049/12=4084(最初的月利息)
x = 0.42  # 假设每月还1万
# 最初的本金剩余
y[0] = all
flag = True

while flag == True:
    for i in range(1, period):
        Im[i] = y[i - 1] * I / 12
        B[i] = x - Im[i]
        y[i] = y[i - 1] - B[i]
        # print(y[i],B[i],Im[i])
    if y[i] < 0:
        flag = False
    x += 0.0001

print("如果希望%d个月完成还款，每月必须还款%.0f元"%(period,x * 10000))
print("此时共计还还款%.2f万"%(x  * period))
print("此时共计还利息：%.2f万"%np.sum(Im))
print("此时共计还本金：%.2f（有误差）"%np.sum(B))

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)  # 画布位置1
plt.title("剩余本金变化")
plt.bar(np.arange(period), y)

plt.subplot(1, 2, 2)  # 画布位置1
plt.title("每月还款本金占比")

plt.bar(np.arange(period)[1:], x * np.ones(period)[1:])
plt.bar(np.arange(period)[1:], B[1:], color='r')

plt.show()
