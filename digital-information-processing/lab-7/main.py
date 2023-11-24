import numpy as np
import matplotlib.pyplot as plt
import time

# Модельний ряд
t = np.arange(0, 480, 0.7)
X_t = np.cos(2 * np.pi * t / 10 + 1) + np.cos(2 * np.pi * t / 40 + np.pi / 2)

# Прямий ШПФ
start_time_fft = time.time()
X_freq_fft = np.fft.fft(X_t)
end_time_fft = time.time()

# Зворотний ШПФ
start_time_ifft = time.time()
x_t_reconstructed_fft = np.fft.ifft(X_freq_fft)
end_time_ifft = time.time()

print("Час виконання прямого ШПФ: %s секунд" % (end_time_fft - start_time_fft))
print("Час виконання зворотного ШПФ: %s секунд" % (end_time_ifft - start_time_ifft))

fig, axes = plt.subplots(3, 1, figsize=(8, 10))

# Графік модельного ряду
axes[0].plot(t, X_t)
axes[0].set_title('Модельний ряд')

# Графік амплітуд ШПФ
axes[1].plot(np.abs(X_freq_fft))
axes[1].set_title('Амплітуди ШПФ')

# Графік відновленого ряду
axes[2].plot(t, x_t_reconstructed_fft.real, label='Відновлений ряд')
axes[2].plot(t, X_t, label='Оригінальний ряд', linestyle='--')
axes[2].legend()
axes[2].set_title('Відновлений ряд за допомогою зворотного ШПФ')

plt.tight_layout()
plt.show()
