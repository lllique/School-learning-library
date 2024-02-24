import numpy as np
import sounddevice as sd
import wave
import time
from numpy.fft import fftfreq, fftshift, fft, ifftshift, ifft
import matplotlib.pylab as plt  # 绘制图形

''' 读取wave '''
# 读取一个单声道的音频
f = wave.open("splat2.wav", 'r')
# 查看音频文件的声道数量、位深度、采样率、帧数等
nchannels, sampwidth, Fs, nframes = f.getparams()[:4]
print(nchannels, sampwidth, Fs, nframes)
# 通过取样点数和取样频率计算出时间轴
t = np.arange(0, nframes) / Fs
# 读取波形数据，再将波形数据转换成数组
y = np.frombuffer(f.readframes(nframes), dtype=np.int16)  # dtype或者用np.short，一样的
# 播放原信号
sd.play(y / np.max(np.abs(y)), Fs, blocking=True)  # 播放
time.sleep(1)
# 求y的频谱的共轭
Fw = fft(y)
Fw_conj = np.conj(Fw)
y_neg = ifft(Fw_conj)
y_neg = np.real(y_neg)
# 播放倒置信号
sd.play(y_neg / np.max(np.abs(y_neg)), Fs, blocking=True)  # 播放
time.sleep(1)

# 绘图
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(221)
plt.grid()  # 显示网格
plt.title("原信号")
plt.plot(t, y)

plt.subplot(222)
plt.grid()  # 显示网格
plt.title("倒置信号")
plt.plot(t, y_neg)

plt.subplot(223)
plt.grid()  # 显示网格
plt.title('原信号幅度谱示意图')
plt.plot(np.arange(0, Fs, Fs / len(t)), np.abs(Fw))

plt.subplot(224)
plt.grid()  # 显示网格
plt.title('倒置信号幅度谱示意图')
plt.plot(np.arange(0, Fs, Fs / len(t)), np.abs(Fw_conj))

plt.tight_layout()
plt.show()
