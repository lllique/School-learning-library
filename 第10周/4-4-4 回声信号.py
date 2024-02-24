import wave
import numpy as np
import matplotlib.pylab as plt  # 绘制图形
import sounddevice as sd
import time

''' 读取wave '''
# 读取一个单声道的音频
f = wave.open("splat2.wav", 'r')# 只读模式
# 查看音频文件的声道数量、位深度、采样率、帧数等
nchannels, sampwidth, Fs, nframes = f.getparams()[:4]
print(nchannels, sampwidth, Fs, nframes)
# 通过取样点数和取样频率计算出时间轴
t = np.arange(0, nframes) / Fs
# 读取波形数据，再将波形数据转换成数组
y = np.frombuffer(f.readframes(nframes), dtype=np.int16)  # dtype或者用np.short，一样的 位深度为2的时候用int16,深度为4的时候用int32
f.close()  # 关闭文件
''' 回声信号产生系统的脉冲响应 '''
h = np.hstack([1, np.zeros(int(Fs * 0.25)), 0.5])

# 利用卷积和产生带有回声的信号
y_echo = np.convolve(y, h)

# 构造新的时间轴(画图)
print(np.max(y))
t_echo = np.arange(0, y_echo.shape[0]) / Fs
print(np.max(y_echo))

''' 播放声音'''
sd.play(y / np.max(np.abs(y)), Fs, blocking=True)  # 播放
time.sleep(1)
sd.play(y_echo / np.max(np.abs(y_echo)), Fs, blocking=True)  # 播放
time.sleep(1)

''' 画波形图 '''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入信号画图
plt.figure()
plt.subplot(211)
plt.plot(t, y)
plt.title('原声音信号')

plt.subplot(212)
plt.title('带有回声的信号')
plt.plot(t_echo, y_echo)

plt.tight_layout()
plt.show()

