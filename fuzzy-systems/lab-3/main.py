import numpy as np
import matplotlib.pyplot as plt


# Універсум
x = np.linspace(150, 200, 100)

# Функція приналежності для низької людини (A)
A = 1 / (1 + np.exp(-(x - 170) / 5))

# Функція приналежності для високої людини (B)
B = 1 / (1 + np.exp(-(x - 180) / 5))

# Побудова графіків
plt.plot(x, A, label='Низька людина (A)')
plt.plot(x, B, label='Висока людина (B)')
plt.xlabel('Зріст')
plt.ylabel('Приналежність')
plt.legend()
plt.title('Графіки функцій приналежності')
plt.grid(True)
plt.show()


# Операція доповнення
def complement(A):
    return 1 - A


# Операція перетину (мінімум)
def intersection(A, B):
    return np.minimum(A, B)


# Операція об'єднання (максимум)
def union(A, B):
    return np.maximum(A, B)


# Операція різниці (віднімання A і B)
def difference(A, B):
    return np.maximum(A - B, 0)


# Операція симетричної різниці
def symmetric_difference(A, B):
    return union(difference(A, B), difference(B, A))


# Операція концентрування (підняття)
def concentration(A, alpha):
    return A ** alpha


# Операція розтягування (зниження)
def dilation(A, alpha):
    return A ** (1 / alpha)


# Функція "низька і висока людина" (A і B)
low_and_high = intersection(A, B)

# Функція "низька або висока людина" (A або B)
low_or_high = union(A, B)

# Функція "не висока людина" (доповнення B)
not_high = complement(B)

# Функція "злегка низька людина" (концентрування A з alpha=0.7)
slightly_low = concentration(A, 0.7)

# Функція "дуже висока людина" (розтягування B з alpha=2)
very_high = dilation(B, 2)

# Побудова графіків
plt.plot(x, low_and_high, label='Низька і висока людина (A і B)')
plt.plot(x, low_or_high, label='Низька або висока людина (A або B)')
plt.plot(x, not_high, label='Не висока людина (доповнення B)')
plt.plot(x, slightly_low, label='Злегка низька людина (концентрування A)')
plt.plot(x, very_high, label='Дуже висока людина (розтягування B)')
plt.xlabel('Зріст')
plt.ylabel('Приналежність')
plt.legend()
plt.title('Графіки функцій приналежності')
plt.grid(True)
plt.show()


# Перевірка комутативності перетину
result1 = intersection(A, B)
result2 = intersection(B, A)
print("Перетин комутативний:", np.allclose(result1, result2))

# Перевірка дистрибутивності
result3 = union(A, intersection(B, not_high))
result4 = intersection(union(A, B), union(A, not_high))
print("Дистрибутивність:", np.allclose(result3, result4))
