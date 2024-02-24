import numpy as np
from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft
#参数
fs = 8000 # 采样率，44100是CD等音频设备的常用采样率
length = 1 #时长s

'''定义时间和频率轴'''
# 定义总区间
t = np.arange(0, length, 1/fs)
# 定义频域长度区间
f = fftshift(fftfreq(len(t), 1/fs))
'''DTMF的频率组合'''
num = {
    '1': [697, 1209],
    '2': [697, 1336],
    '3': [697, 1477],
    'A': [697, 1633],
    '4': [770, 1209],
    '5': [770, 1336],
    '6': [770, 1477],
    'B': [770, 1633],
    '7': [852, 1209],
    '8': [852, 1336],
    '9': [852, 1477],
    'C': [852, 1633],
    '*': [941, 1209],
    '0': [941, 1336],
    '#': [941, 1477],
    'D': [941, 1633],
}
#函数：生成对应的sin和合并后的波形
def getNumWave(numstr):
    # 注意这和之前定义方式有所不同，这里定义的是模拟角频率
    sin1 = np.sin(2 * np.pi * num[numstr][0] * t)  #生成低频部分正弦波
    sin2 = np.sin(2 * np.pi * num[numstr][1] * t)  # 生成高频部分正弦波
    DTMFsin = sin1 + sin2 #组合一下
    return DTMFsin

'''定义信号'''
sig = getNumWave('2')
# 频轴,注意由于时间轴定义的特殊性，频率轴的定义和之前例子不同
f = fftshift(fftfreq(len(t), 1/fs))
# 频谱
Fw = fftshift(fft(sig))  # 双边幅度谱,范围为正负sample_freq/2

#绘个图
import matplotlib.pyplot as plt
# 绘图
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.subplot(211)#画布位置1
plt.xlim(0,0.05)
plt.plot(t,sig,c='purple')#波形合成之后的图
plt.title("字符2的dtmf信号波形")
plt.grid() #网格

plt.subplot(212)#画布位置2
plt.xlim(-1800,1800)
plt.plot(f,abs(Fw / fs),c='purple')#波形合成之后的图
plt.title("字符2的dtmf信号频谱")
plt.grid() #网格

plt.tight_layout()
plt.show()
