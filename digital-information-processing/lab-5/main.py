import numpy as np
import matplotlib.pyplot as plt


x = np.array([4, 2, -1, 3, -2, -6, -5, 4, 5])
y = np.array([-4, 1, 3, 7, 4, -2, -8, -2, 1])

correlation = np.correlate(x, y, mode='full')
print("Кореляція двох сигналів:", correlation)


signal_length = 1000
time = np.linspace(0, 1, signal_length, endpoint=False)
frequency = 5
amplitude = 1
signal = amplitude * np.sin(2 * np.pi * frequency * time)

autocorrelation = np.correlate(signal, signal, mode='full')
autocorrelation = autocorrelation[signal_length-1:]
autocorrelation /= np.max(autocorrelation)

plt.figure()
plt.plot(autocorrelation)
plt.title('Автокореляція випадкового сигналу')
plt.xlabel('Зсув часу')
plt.ylabel('Значення автокореляції')
plt.grid()
plt.show()
