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
plt.ylim(0,3000)
plt.specgram(y,Fs = framerate)
y1 = [0,697,770,852,941,1209,1336,1477,1633,2400,2500]
plt.yticks(y1)
plt.show()