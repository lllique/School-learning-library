import matplotlib.pylab as plt  # 绘制图形
import numpy as np
import sounddevice as sd
import wave

from numpy.fft import fftshift, fft, fftfreq, ifftshift, ifft

'''
from moviepy import editor
#mp4提取音频，需要 pip install moviepy
video = editor.VideoFileClip(r"D:\Downloads\2023-11-23_14-13-55.MP4")
audio = video.audio
#可以转mp3或wav，扩展名小写
audio.write_audiofile(r"D:\Downloads\2023-11-23_14-13-55.wav")
'''


# 打开文件
f = wave.open(r"D:\Downloads\2023-11-23_14-13-55.wav", 'rb')

'''参数读取：分别获得各种信息'''
channel = f.getnchannels()  # 通道数
sampwidth = f.getsampwidth()  # 比特宽度 每一帧的字节数
samplerate = f.getframerate()  # 帧率  每秒有多少帧
frames = f.getnframes()  # 帧数
duration = frames / samplerate  # 计算音频持续时间 单位：秒
print(channel, sampwidth, samplerate, frames, duration)

'''按帧读实际音频数据'''
audio = f.readframes(frames)  # 格式为<class 'bytes'>
# 将格式转为ndarray
# 由于是双声道数据，因此进行一下拆分，np.int16是根据sampwidth=2（两字节）来确定的
data = np.frombuffer(audio, dtype=np.int16)  # 所有数据读到1D array，顺序是左右声道交替读取
data.shape = frames, channel  # 如果已知声道，也可以写为-1, 2，表示格式改为：无论有多少行，每行两列数据
dataT = data.T  # 转置，变为两行数据，一个声道一行
# 对两个声道求平均值
dataT_mix = (dataT[0] / 2 + dataT[1] / 2).astype(np.int16)
dataT_mix = dataT_mix[int(0.5*samplerate):int(1.5*samplerate)]#截短
'''
注意音频数据的格式问题：
1，32位浮点数，但进行了归一化：normalise the data to between -1 and 1
2，8、16、24、32位整数（PCM）
因此：
如果对音频数据进行处理，要么保持数据仍为整数，如果数据变为浮点数，则需要进行归一化
If your data wasn't/isn't normalised it will be very noisy when played here
归一化方法，对于一个1D的array；
data = data / np.max(np.abs(data))
'''

print("播放一个声道-两个喇叭播放相同声音")
#sd.play(dataT[0][int(0.5*samplerate):int(1.5*samplerate)], samplerate, blocking=True)  # 播放声道1
#sd.play(dataT[1][int(0.5*samplerate):int(1.5*samplerate)], samplerate, blocking=True)  # 播放声道2
print("播放声道1-只有一个喇叭响")
# sd.play(dataT[0][int(0.5*samplerate):int(1.5*samplerate)], samplerate, blocking=True,mapping = 1)#左边响
# sd.play(dataT[1][int(0.5*samplerate):int(1.5*samplerate)], samplerate, blocking=True,mapping = 2) #右边响
print("播放立体声")
# 注意直接用没有转置的数据data
# sd.play(data, samplerate, blocking=True,mapping = None)  # 播放 ,mapping = None参数可以省略
print("两个声道混合成一个声道播放")
sd.play(dataT_mix, samplerate, blocking=True)  # 播放

#fft
FFT_data = fftshift(fft(dataT_mix) )
FFT_data_amp = np.abs(FFT_data / samplerate)
#频轴
f = fftshift(fftfreq(len(FFT_data),1/samplerate))
#时间轴
t = np.arange(0,1,1/samplerate)

#定义一个低通
lpf = np.heaviside(f+1000,0)-np.heaviside(f-1000,0)
#定义一个高通
hpf = 1-lpf
#尝试把高通变成带通
bpf = np.heaviside(f+6000,0) - np.heaviside(f+1000,0) + \
            np.heaviside(f-1000,0) - np.heaviside(f-6000,0)

#分离高低频
data_lpf = ifft(ifftshift(FFT_data * lpf )).real.astype(np.int16)
data_hpf = ifft(ifftshift(FFT_data * hpf )).real.astype(np.int16)

#播放一下
sd.play(data_lpf/np.max(np.abs(data_lpf)), samplerate, blocking=True)  # 播放
sd.play(data_hpf/np.max(np.abs(data_hpf)), samplerate, blocking=True)  # 播放

# 绘图
plt.rcParams['mathtext.fontset'] = 'stix'  # 公式字体风格
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定非衬线字体
plt.rcParams['axes.unicode_minus'] = False  # 解决图像中的负号'-'显示为方块的问题

plt.grid()  # 显示网格
plt.xlim(0,10000)
plt.plot(f, FFT_data_amp)
plt.plot(f, lpf*25,"r--")
plt.plot(f, hpf*25,"b--")
plt.show()




