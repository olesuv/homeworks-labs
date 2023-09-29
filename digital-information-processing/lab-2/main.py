import numpy as np
import matplotlib.pyplot as plt


def sin_function(x):
    return np.sin(np.pi * x)


def cos_function(x):
    return np.cos(np.pi * x)


def signum_function(a):
    return np.sign(a)


def rect_function(x):
    return np.where(np.abs(x) < 0.5, 1, 0)


def compute_fourier_transform(func, x_values):
    N = len(x_values)
    k = np.arange(N)
    X = np.zeros(N, dtype=complex)
    for n in range(N):
        X[n] = np.sum(func(x_values) * np.exp(-2j * np.pi * n * x_values / N))
    return X


# Генеруємо значення x від -1 до 1
x_values = np.linspace(-1, 1, 1000)

# Обчислюємо значення функцій та їх Фур'є-образи
sin_values = sin_function(x_values)
cos_values = cos_function(x_values)
signum_values = signum_function(x_values)
rect_values = rect_function(x_values)

sin_fourier = compute_fourier_transform(sin_function, x_values)
cos_fourier = compute_fourier_transform(cos_function, x_values)
signum_fourier = compute_fourier_transform(signum_function, x_values)
rect_fourier = compute_fourier_transform(rect_function, x_values)

# Побудова графіків
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x_values, sin_values)
plt.title("sin(pi*x)")

plt.subplot(2, 2, 2)
plt.plot(x_values, cos_values)
plt.title("cos(pi*x)")

plt.subplot(2, 2, 3)
plt.plot(x_values, signum_values)
plt.title("signum(a)")

plt.subplot(2, 2, 4)
plt.plot(x_values, rect_values)
plt.title("rect(x)")

plt.tight_layout()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(np.abs(sin_fourier))
plt.title("Фур'є образ sin(pi*x)")

plt.subplot(2, 2, 2)
plt.plot(np.abs(cos_fourier))
plt.title("Фур'є образ cos(pi*x)")

plt.subplot(2, 2, 3)
plt.plot(np.abs(signum_fourier))
plt.title("Фур'є образ signum(a)")

plt.subplot(2, 2, 4)
plt.plot(np.abs(rect_fourier))
plt.title("Фур'є образ rect(x)")

plt.tight_layout()

plt.show()
