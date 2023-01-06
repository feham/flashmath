#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
#import tensorflow_io as tfio

#RATE = 44100

file_contents = tf.io.read_file("data/count-to-20.wav")
wav,sample_rate = tf.audio.decode_wav(file_contents,desired_channels=1)

print("sample_rate",sample_rate)
print("len(wav)",len(wav))
print("wav",wav)

plt.plot(wav)
plt.show()


print("DONE!")
