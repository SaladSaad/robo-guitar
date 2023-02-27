import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 2048  # Number of samples per buffer
RATE = 44100  # Sampling rate in Hz
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

fig, ax = plt.subplots()
x = np.linspace(0, RATE, CHUNK)
line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(-5, 120)
ax.set_xlim(20, 2000)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude (dB)')

while True:
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    fft_data = np.fft.fft(data)
    fft_data = 20*np.log10(np.abs(fft_data))
    fft_data[fft_data<20]=0 #amplitude filter out background noise under 20 dB
    line.set_ydata(fft_data)
    plt.pause(0.01)

stream.stop_stream()
stream.close()
p.terminate()