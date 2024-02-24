import time
import wave
import numpy as np
import sounddevice as sd
from numpy.fft import fftfreq, fftshift, fft
import matplotlib.pyplot as plt

f = wave.open('dtmf1.wav', 'rb')
# 一次性返回所有格式信息，元组：(声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型)
params = f.getparams()
#第一种参数获取方式
nchannels, sampwidth, framerate, nframes = params[:4]
#第二种参数获取方式
channel = f.getnchannels()  # 通道数
sampwidth = f.getsampwidth()  # 比特宽度 每一帧的字节数
framerate = f.getframerate()  # 帧率  每秒有多少帧
frames = f.getnframes()  # 帧数
duration = frames / framerate  # 音频持续时间 单位：秒
audio = f.readframes(frames)  # 按帧读音频，返回二进制数据
print(channel, sampwidth, framerate, frames, duration)

y = np.frombuffer(audio, dtype=np.int32)  # int32而非int16，是根据sampwidth*channel计算，即采用双字节
print(len(y), y)
y = y / np.max(np.abs(y))  # 归一化
# normalise the data to between -1 and 1. If your data wasn't/isn't normalised
# it will be very noisy when played here
# 应该和sounddevice库有些关系
# sd.play(y, framerate,blocking=True) #播放
# time.sleep(10)
# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义一个1秒的时间轴，数据点个数为 framerate
t1 = np.arange(framerate * 0.3)
# 频轴
f = fftshift(fftfreq(len(t1), 1 / framerate))
# 截取第n秒的数据
for i in range(6):
    y_slice = y[int(framerate * (i + 0.7)):framerate * (i + 1)]
    sd.play(y_slice, framerate, blocking=True)  # 播放
    time.sleep(1)
    # 频谱
    Fw = fftshift(fft(y_slice))

    plt.subplot(3, 2, i + 1)  # 画布位置2
    plt.xlim(-1700, 1700)
    plt.xticks([-1477,-1336,-770,-697,0, 697, 770, 1209, 1336, 1477],[])
    plt.plot(f, abs(Fw / framerate), c='purple')  # 波形合成之后的图
    plt.title("第%d秒" % (i + 1))
    plt.grid()  # 网格

plt.tight_layout()
plt.show()

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
