import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Задання параметрів
t = np.linspace(0, 480, 1000)  # Генерація послідовності t
X_t = np.cos(2 * np.pi * t / 10 + 1) + np.cos(2 * np.pi * t / 40 + np.pi / 2)  # Обчислення X(t)

# ШПФ за допомогою scipy.fft
X_f = fft(X_t)  # Виконання прямого ШПФ
frequencies_fft = fftfreq(len(t), t[1] - t[0])
periodogram_fft = np.abs(X_f) ** 2

# Зворотне ШПФ
X_t_reconstructed = np.fft.ifft(X_f)  # Виконання зворотного ШПФ

# Час виконання ШПФ
start_time = time.time()
X_f = fft(X_t)
end_time = time.time()
execution_time = end_time - start_time
print(f"Час виконання ШПФ: {execution_time} секунд")


# Відображення графіків
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, X_t)
plt.title('Сигнал X(t)')
plt.subplot(2, 1, 2)
plt.plot(frequencies_fft, periodogram_fft)
plt.title('Періодограма (ШПФ)')
plt.xlabel('Частота')
plt.ylabel('Потужність')
plt.show()