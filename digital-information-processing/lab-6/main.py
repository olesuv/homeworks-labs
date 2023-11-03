import matplotlib.pyplot as plt
import numpy as np
import time

# Функція для прямого ДПФ
def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex64)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Функція для зворотного ДПФ
def IDFT(X):
    N = len(X)
    x = np.zeros(N, dtype=np.complex64)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
        x[n] /= N
    return x

# Модельний ряд
t = np.arange(0, 480, 0.7)
X_t = np.cos(2 * np.pi * t / 10 + 1) + np.cos(2 * np.pi * t / 40 + np.pi / 2)

# Пряме ДПФ
start_time = time.time()
X_freq = DFT(X_t)
end_time = time.time()

# Зворотне ДПФ
start_time_idft = time.time()
x_t_reconstructed = IDFT(X_freq)
end_time_idft = time.time()

# Коментарі до коду
# Функція DFT використовує подвійний цикл для обчислення кожного компоненту ДПФ.
# Функція IDFT реалізована аналогічно, але використовує зворотний знак у показнику експоненти.

# Визначення часу роботи програми
time_dft = end_time - start_time
time_idft = end_time_idft - start_time_idft

print(f"Час роботи прямого ДПФ: {time_dft} секунд")
print(f"Час роботи зворотного ДПФ: {time_idft} секунд")

plt.figure(figsize=(12, 10))

# Графік виразу функції X(t)
plt.subplot(4, 1, 1)
plt.plot(t, X_t)
plt.title('Графічний вираз функції X(t)')
plt.xlabel('Час (t)')
plt.ylabel('X(t)')

# Графік фази ДПФ
plt.subplot(4, 1, 2)
phase = np.angle(X_freq)
plt.plot(np.arange(len(phase)), phase)
plt.title('Графік фази ДПФ')
plt.xlabel('Частота')
plt.ylabel('Фаза')

# Графік амплітуди ДПФ
plt.subplot(4, 1, 3)
amplitude = np.abs(X_freq)
plt.plot(np.arange(len(amplitude)), amplitude)
plt.title('Графік амплітуди ДПФ')
plt.xlabel('Частота')
plt.ylabel('Амплітуда')

# Графік зворотного перетворення
plt.subplot(4, 1, 4)
plt.plot(t, np.real(x_t_reconstructed), label='Реальна частина')
plt.plot(t, np.imag(x_t_reconstructed), label='Уявна частина')
plt.title('Графік зворотного перетворення')
plt.xlabel('Час (t)')
plt.ylabel('X(t)')
plt.legend()

# Відображення графіків
plt.tight_layout()
plt.show()
