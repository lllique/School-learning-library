import numpy as np
import sounddevice as sd
import time

fs = 44100 #采样率
length = 1 #时长

t = np.arange(fs*length)

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
}

def getNumWave(numstr):
    low_df = 2 * np.pi * num[numstr][0] / fs
    high_df = 2 * np.pi * num[numstr][1] / fs

    discrete_sin1 = np.sin(low_df * t)
    discrete_sin2 = np.sin(high_df * t)
    DTMFsin = discrete_sin1 + discrete_sin2
    return discrete_sin1,discrete_sin2,DTMFsin

def color(i):
    if(i == 1):
        return 'black'
    if(i == 2):
        return 'red'
    if(i == 3):
        return 'orange'
    if(i == 4):
        return 'gold'
    if(i == 5):
        return 'yellow'
    if(i == 6):
        return 'green'
    if(i == 7):
        return 'cyan'
    if(i == 8):
        return 'blue'
    if(i == 9):
        return 'deeppink'

# 播放声音
for numstr in range(1,10):
    sin1,sin2,DTMFsin = getNumWave(str(numstr))
    sd.play(DTMFsin,fs)
    time.sleep(length)

# 绘图
import matplotlib.pyplot as plt
plt.figure()
plt.suptitle('DTMF wave')
len = 200
for numstr in range(1,10):
    sin1,sin2,DTMFsin = getNumWave(str(numstr))
    plt.subplot(3,3,numstr)
    plt.ylim(-2,2)
    plt.grid()
    plt.title(str(numstr))
    plt.plot(t[:len],DTMFsin[:len],c=color(numstr))

plt.tight_layout()
plt.show()