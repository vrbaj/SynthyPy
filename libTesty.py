import sounddevice as sd
import numpy as np
from scipy import signal


# sound parameters definition
c3 = 130.831  # Hz
a4 = 440  # Hz

toneToPlay = c3
mySampleRate = 44100
soundLength = int(mySampleRate // toneToPlay)
myIntConstant = 32767
sd.default.samplerate = mySampleRate
sd.default.device = 4
sd.default.channels = 1

# tone frequency

x = np.arange(soundLength)
c3_data = np.sin(2 * np.pi * toneToPlay * x / mySampleRate)
# myarray = np.random.uniform(-1, 1,44100)  # vygeneruje 1 sekundu pro prehrani
# scaled = np.int16(myarray/np.max(np.abs(myarray)) * 32767)
# sd.play(myarray, blocking=True)
x = np.arange(soundLength)
myAudio = sd.OutputStream(channels=2)
myAudio.start()
channel2 = np.zeros((soundLength, 2))
try:
    while True:
        # leftBound = np.random.uniform(-1, 0, 1)
        # rightBound = np.random.uniform(0, 1, 1)
        # myarray = np.random.uniform(leftBound, 1, int(44100 / 2))

        c1_data = np.sin(2 * np.pi * toneToPlay * x / (mySampleRate))
        # c2_data = np.sin(2 * np.pi * 6 * toneToPlay * x / (mySampleRate))
        c2_data = np.sin(2 * np.pi * 6 * toneToPlay * x / (mySampleRate))
        synthesis = c1_data + c2_data
        channel2[:, 0] = synthesis
        channel2[:, 1] = synthesis
        # channel2 = np.array([c2_data, c2_data])# np.vstack((c1_data, c2_data))
        # channel2 = channel2.transpose()
        print(channel2.shape)
        myAudio.write(np.float32(channel2))


except KeyboardInterrupt:
    pass
print(sd.query_devices())