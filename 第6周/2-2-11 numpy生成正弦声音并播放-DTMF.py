import numpy as np
import sounddevice as sd
import time

#采样宽度(每一帧的字节数)
#采样率(每秒有多少帧数据)
#持续时间 = 采样率/采样宽度

#参数
fs = 44100 # 采样率，44100是CD等音频设备的常用采样率
length = 1 #时长s

t = np.arange(fs * length) #自然数列，相当于定义了n
'''
#DTMF的频率组合，
注意这是一个字典（dict）结构，即键值对（key-value）的集合，
键是个字符串，即拨号键，值是数组（方括号内）
'''
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

#字典类型，支持用键查值
print("键值对的使用：",num["D"],num["D"][0],num["D"][1])
#函数：生成对应的sin和合并后的波形
def getNumWave(numstr):
    # num[numstr][0]，即DTMF的低频（Hz）
    # num[numstr][1]为高频值（Hz），
    #频率乘以2pi，得到模拟角频率(Angular frequency）
    # 需要计算数字角频率 = 模拟角频率 * 抽样间隔，抽烟间隔 = 1 / fs
    low_df = 2 * np.pi * num[numstr][0]
    high_df = 2 * np.pi * num[numstr][1]

    # 2pi *频率
    discrete_sin1 = np.sin(low_df * t)  #生成低频部分正弦波
    discrete_sin2 = np.sin(high_df * t)  # 生成高频部分正弦波
    DTMFsin = discrete_sin1 + discrete_sin2 #组合一下
    return discrete_sin1,discrete_sin2,DTMFsin

#播放
numstr = '2'
sin1,sin2,DTMFsin = getNumWave(numstr)
sd.play(DTMFsin, fs)  # 播放
time.sleep(length)

#绘个图
import matplotlib.pyplot as plt
plt.figure()
len = 200 #折线图长度
plt.subplot(221)#画布位置1
plt.grid() #网格
plt.plot(t[:len],sin1[:len],c='blue',label = str(num[numstr][0])+'Hz')#折线图
plt.legend(loc = 'lower right') #图例
plt.subplot(222)#画布位置2
plt.grid() #网格
plt.plot(t[:len],sin2[:len],c='red', label = str(num[numstr][1])+'Hz')#折线图
plt.legend(loc = 'lower right') #图例
plt.subplot(212)#画布位置3
plt.plot(t[:len*2],DTMFsin[:len*2],c='purple')#波形合成之后的图
plt.suptitle('DTMF: ' + numstr)
plt.grid() #网格
plt.show()



# 2 * np.pi * f #就是模拟角频率Ω
# 1/fs就是Ts，Ts*Ω就是数字角频率w
# 此时的myarray就是n
# discrete_sin就是sin(nw)
#print('数组内容:',discrete_sin)
#sd.play(discrete_sin, fs) #播放
#time.sleep(2)