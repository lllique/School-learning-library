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

# 求y的频谱
Fw = fft(y)
#利用幅度构造y4
y4 = np.real(ifft(np.abs(Fw)))
#利用相位构造y5
y5 =  np.real(ifft(np.exp(-1j*np.angle(Fw))))

# 播放原信号
sd.play(y / np.max(np.abs(y)), Fs, blocking=True)  # 播放
time.sleep(1)
#播放y4
sd.play(y4 / np.max(np.abs(y4)), Fs, blocking=True)  # 播放
time.sleep(1)
#播放y5
sd.play(y5 / np.max(np.abs(y5)), Fs, blocking=True)  # 播放
time.sleep(1)

# 绘图
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(311)
plt.grid()  # 显示网格
plt.title("原信号")
plt.plot(t, y / np.max(np.abs(y)))

plt.subplot(312)
plt.grid()  # 显示网格
plt.title("y4")

plt.plot(t, y4 / np.max(np.abs(y4)))

plt.subplot(313)
plt.grid()  # 显示网格
plt.title("y5")

plt.plot(t, y5 / np.max(np.abs(y5)))

plt.tight_layout()
plt.show()
