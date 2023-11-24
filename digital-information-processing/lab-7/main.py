import numpy as np
import matplotlib.pyplot as plt
import time

# Функція для обчислення ШПФ
def calculate_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

# Функція для обчислення зворотного ШПФ
def calculate_idft(X):
    N = len(X)
    k = np.arange(N)
    n = k.reshape((N, 1))
    e = np.exp(2j * np.pi * k * n / N)
    x = np.dot(e, X) / N
    return x

# Задання формули 12
def formula_12(t):
    return np.cos(2 * np.pi * t / 10 + 1) + np.cos(2 * np.pi * t / 40 + np.pi / 2)

# Створення модельного ряду
t_values = np.arange(0.7, 480, 0.1)
x_values = formula_12(t_values)

# Створення плоту для графіків
fig, axes = plt.subplots(4, 1, figsize=(8, 10))

# Виведення графіка модельного ряду
axes[0].plot(t_values, x_values)
axes[0].set_title('Модельний ряд (Формула 12)')
axes[0].set_xlabel('Час')
axes[0].set_ylabel('Значення')

# Обчислення прямого ШПФ та виведення графіка амплітуд
start_time = time.time()
X = calculate_dft(x_values)
end_time = time.time()
execution_time_forward = end_time - start_time

axes[1].plot(np.abs(X))
axes[1].set_title('Амплітуди ШПФ')
axes[1].set_xlabel('Частота')
axes[1].set_ylabel('Амплітуда')

# Обчислення зворотного ШПФ та виведення графіка відновленого ряду
start_time = time.time()
x_reconstructed = calculate_idft(X)
end_time = time.time()
execution_time_inverse = end_time - start_time

axes[2].plot(t_values, x_reconstructed.real, label='Відновлений ряд')
axes[2].plot(t_values, x_values, label='Оригінальний ряд', linestyle='--')
axes[2].legend()
axes[2].set_title('Відновлений ряд за допомогою зворотного ШПФ')
axes[2].set_xlabel('Час')
axes[2].set_ylabel('Значення')

# Виведення часу виконання прямого та зворотного ШПФ
print(f"Час виконання прямого ШПФ: {execution_time_forward} секунд")
print(f"Час виконання зворотного ШПФ: {execution_time_inverse} секунд")

# Виведення графіка фазової характеристики ШПФ
axes[3].plot(np.angle(X))
axes[3].set_title('Фазова характеристика ШПФ')
axes[3].set_xlabel('Частота')
axes[3].set_ylabel('Фаза')

# Відображення плоту
plt.tight_layout()
plt.show()
