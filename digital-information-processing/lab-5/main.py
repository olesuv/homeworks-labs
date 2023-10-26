import matplotlib.pyplot as plt
import numpy as np


# 2 Завдання
def correlation(x1, x2):
    n = len(x1)
    r = np.zeros(2*n - 1)

    for j in range(-n+1, n):
        if j < 0:
            r[n-1+j] = np.sum(x1[-j:] * x2[:n+j])
        else:
            r[n-1+j] = np.sum(x1[:n-j] * x2[j:])

    return r


# Приклад сигналів x1 та x2
x1 = np.array([4, 2, -1, 3, -2, -6, -5, 4, 5])
x2 = np.array([-4, 1, 3, 7, 4, -2, -8, -2, 1])

# Обчислюємо кореляцію
result = correlation(x1, x2)

# Відображення результату
plt.plot(result)
plt.xlabel('Затримка (j)')
plt.ylabel('Кореляція')
plt.title('Графік кореляції')
plt.show()


# 3 Завдання
def correlation_coefficient(x1, x2):
    numerator = np.sum(x1 * x2)
    denominator = np.sqrt(np.sum(x1**2) * np.sum(x2**2))
    return numerator / denominator


def auto_correlation(x):
    N = len(x)
    r = np.zeros(N)
    for n in range(N):
        numerator = np.sum(x[:N-n] * x[n:])
        denominator = np.sum(x**2)
        r[n] = numerator / denominator
    return r


# Значення x1(n), x2(n), x3(n), x4(n) з таблиці
x1 = np.array([0, 3, 5, 5, 5, 2, 0.5, 0.25, 0])
x2 = np.array([1, 2, 1, 1, 1, 0, 0, 0, 0])
x3 = np.array([0, 9, 15, 15, 15, 6, 1.5, 0.75, 0])
x4 = np.array([2, 2, 2, 2, 2, 0, 0, 0, 0])

# Обчислюємо коефіцієнти кореляції
r12 = correlation_coefficient(x1, x2)
r13 = correlation_coefficient(x1, x3)
r14 = correlation_coefficient(x1, x4)
r23 = correlation_coefficient(x2, x3)
r24 = correlation_coefficient(x2, x4)
r34 = correlation_coefficient(x3, x4)

# Обчислюємо автокореляцію для x1(n)
r11 = auto_correlation(x1)

print("Коефіцієнти кореляції:")
print(f"r12 = {r12}")
print(f"r13 = {r13}")
print(f"r14 = {r14}")
print(f"r23 = {r23}")
print(f"r24 = {r24}")
print(f"r34 = {r34}")

print("\nАвтокореляція для x1(n):")
print(r11)

plt.plot(r11)
plt.title("Автокореляція x1(n)")
plt.xlabel("Затримка (n)")
plt.ylabel("Автокореляція")
plt.show()
