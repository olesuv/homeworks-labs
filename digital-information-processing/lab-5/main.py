import matplotlib.pyplot as plt
from random import randint

# Генеруємо випадковий сигнал
rand_signals = []
for n in range(100):
    rand_signals.append(randint(1, 10))

# Функція для обчислення кореляції
def correlation(signal1, signal2):
    mean1 = sum(signal1) / len(signal1)
    mean2 = sum(signal2) / len(signal2)
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(signal1, signal2))
    denominator = (sum((x - mean1)**2 for x in signal1) * sum((y - mean2)**2 for y in signal2))**0.5
    
    if denominator != 0:
        return numerator / denominator
    else:
        return 0.0  # Якщо denominator дорівнює нулю, повертаємо 0.0

# Обчислюємо кореляцію між двома випадковими сигналами
correlation_result = correlation(rand_signals, rand_signals)

# Виводимо результат кореляції
print(f"Кореляція: {correlation_result}")

# Функція для обчислення автокореляції
def autocorrelation(signal):
    return [correlation(signal[:-k], signal[k:]) for k in range(1, len(signal))]

# Обчислюємо автокореляцію
autocorrelation_result = autocorrelation(rand_signals)

# Виводимо результат автокореляції
plt.plot(autocorrelation_result)
plt.title("Графік автокореляції")
plt.show()