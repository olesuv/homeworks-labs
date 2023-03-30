import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import random
import math


def sample_mean(data):
    return sum(data) / len(data)


def sample_variance(data):
    mean = sample_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)


def theoretical_mean(probabilities, values):
    return sum(prob * val for prob, val in zip(probabilities, values))


def theoretical_variance(probabilities, values, mean):
    return sum(prob * (val - mean) ** 2 for prob, val in zip(probabilities, values))


def plot_histogram(values, bins=15):
   # Create histogram
    hist, bin_edges = np.histogram(values, bins=bins, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    # Plot histogram
    fig, ax = plt.subplots()
    ax.bar(bin_centers, hist, width=0.7 * (bin_centers[1]-bin_centers[0]),
           alpha=0.5, color='g', edgecolor='black')

    # Fit a normal distribution to the data
    mu, std = norm.fit(values)

    # Plot the normal distribution function
    x = np.linspace(min(values), max(values), 100)
    y = norm.pdf(x, mu, std)
    # ax.plot(x, y, 'r--', linewidth=2) будує лінію нормальної

    # налаштування осей та міток
    plt.xlabel('Значення')
    plt.ylabel('Відносна частота')
    plt.title(
        r'$\mathrm{Histogram\ of\ Values:}\ \mu=%.2f,\ \sigma=%.2f$' % (mu, std))
    plt.legend(['Нормальний розподіл', 'Гістограма'], loc='best')
    plt.show()


def generate_poisson_sequence(n, lmbda):
    """
    Генерує послідовність з n значень, розподілених за законом Пуассона з параметром lmbda.

    :param n: кількість значень у послідовності
    :param lmbda: параметр розподілу
    :return: список з n значень, розподілених за законом Пуассона з параметром lmbda
    """
    sequence = []

    for i in range(n):
        k = 0
        r = random.uniform(0, 1)
        while r >= math.exp(-lmbda):
            r *= random.uniform(0, 1)
            k += 1
        sequence.append(k)

    return sequence


if __name__ == "__main__":
    xi_pi_15 = [
        (13, 0.08),
        (16, 0.14),
        (28, 0.25),
        (33, 0.16),
        (39, 0.25),
        (47, 0.09),
        (52, 0.03)
    ]

    N = 1000

    dic_keys = [t[0] for t in xi_pi_15]
    dic_values = [t[1] for t in xi_pi_15]

 # розбиваємо [0,1] на інтервали згідно з ймовірностями

    intervals = []
    interval_end = 0

    for xi, pi in xi_pi_15:
        interval_start = interval_end
        interval_end += pi
        intervals.append((xi, interval_start, interval_end))

    # генеруємо N випадкових чисел та визначаємо, в який інтервал вони попадають

    rand_numbers = np.random.rand(N)
    values = []

    for rand_num in rand_numbers:
        for xi, interval_start, interval_end in intervals:
            if rand_num >= interval_start and rand_num < interval_end:
                values.append(xi)
                print(
                    f"Згенеровано число: {rand_num:.2f}, випадкова величина X = {xi}")
                break

    print("Згенерована послідовність випадкових чисел:")
    print(values)

    print(f"Вибіркове математичне сподівання: {sample_mean(values):.2f}")
    print(f"Вибіркова дисперсія: {sample_variance(values):.2f}")

    print(
        f"Теоретичне математичне сподівання: {theoretical_mean(dic_values, dic_keys):.2f}")
    print(
        f"Теоретична дисперсія: {theoretical_variance(dic_values, dic_keys, sample_mean(values)):.2f}")

    intervals_count = {xi: 0 for xi, _, _ in intervals}
    for val in values:
        intervals_count[val] += 1

    print("Таблиця 2 – Частотна таблиця")
    print("Інтервал | Частота потрапляння | Відносна частота потрапляння")
    for xi, interval_start, interval_end in intervals:
        freq = intervals_count[xi]
        rel_freq = freq / N
        print(f"{xi:8} | {freq:20} | {rel_freq:.2f}")

    # plot_histogram(values)

    print("\nПослідовність значень Х, за законом Пуассона:")
    poisson_result = generate_poisson_sequence(100, 15)
    print(poisson_result)

    print(
        f"Вибіркове математичне сподівання: {sample_mean(poisson_result):.2f}")
    print(f"Вибіркова дисперсія: {sample_variance(poisson_result):.2f}")

    print(
        f"Теоретичне математичне сподівання: {theoretical_mean(dic_values, dic_keys):.2f}")
    print(
        f"Теоретична дисперсія: {theoretical_variance(dic_values, dic_keys, sample_mean(poisson_result)):.2f}")
