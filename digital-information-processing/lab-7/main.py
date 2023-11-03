import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

# Задання параметрів
t = np.arange(0, 480, 0.7)  # Генерація послідовності t
X_t = np.cos(2 * np.pi * t / 10 + 1) + np.cos(2 * np.pi * t / 40 + np.pi / 2)  # Обчислення X(t)

frequencies, periodogram = plt.psd(X_t, NFFT=len(t), Fs=1/(t[1]-t[0]))

# Пряме ШПФ
X_f = np.fft.fft(X_t)  # Виконання прямого ШПФ
frequencies_fft = np.fft.fftfreq(len(t), t[1]-t[0])
periodogram_fft = np.abs(X_f)**2

# Зворотне ШПФ
X_t_reconstructed = np.fft.ifft(X_f)  # Виконання зворотного ШПФ

# Оцінка часу виконання ШПФ
import time

start_time = time.time()
X_f = np.fft.fft(X_t)
end_time = time.time()

execution_time = end_time - start_time

# Виведення результатів
# print("Результат прямого ШПФ:", X_f)
# print("Результат зворотного ШПФ:", X_t_reconstructed)
print(f"Час виконання ШПФ: {execution_time} секунд")

# Побудова графіків
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Графік функції
axs[0].plot(t, X_t)
axs[0].set_title('Графік функції X(t)')

# Періодограма (вихідна)
axs[1].plot(frequencies, periodogram)
axs[1].set_title('Періодограма (вихідна)')

# Періодограма (ШПФ)
axs[2].plot(frequencies_fft, periodogram_fft)
axs[2].set_title('Періодограма (ШПФ)')

# Налаштування відступів між сабплотами
plt.tight_layout()

# Показати графіки
plt.show()

