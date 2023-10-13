import numpy as np
import matplotlib.pyplot as plt


def rect(x):
    return (np.abs(x) <= 0.5).astype(float)


x2 = np.arange(-5, 5, 0.001)
plt.title('Прямокутна функція')
plt.plot(x2, rect(x2), label="Прямокутна функція")
plt.plot(x2, np.sinc(np.pi*x2), label="Фур'є образ", color="red")
plt.legend()
plt.show()
