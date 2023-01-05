#!/usr/bin/env python3

import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

blah = input("press any key to start...")

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("8 x 4 = ?")

frames = []
seconds = 3
for i in range(0,int(RATE/CHUNK*seconds)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

buf = np.frombuffer(b''.join(frames),dtype=np.int16)

plt.figure(1)
plt.axis('off')

# wave...
#plt.plot(buf)
#plt.show()

print(len(buf))

# spectrogram...
plt.specgram(buf)
#plt.show()
plt.savefig("one.png",bbox_inches='tight')
#plt.savefig("one.png",pad_inches=0.0)


print("DONE!")
