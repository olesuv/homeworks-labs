from random import random, randint
from numpy import cumsum
from collections import Counter
from math import sqrt, pi, exp
import matplotlib.pyplot as plt


def custom_mean(data: list, N: int) -> float:
    result = (1 / N) * sum(data)
    return result


def custom_variance(data: list, N: int) -> float:
    mu = custom_mean(data, N)
    result = sum((x - mu) ** 2 for x in data) / (N - 1)
    return result


def custom_devidation(data: list, N: int) -> float:
    result = sqrt(custom_variance(data, N))
    return result


def generate_random_list_x(a: int, b: int, sigma: int, list_amount: int) -> list:
    sample = []

    while len(sample) < list_amount:
        x = randint(a, b)
        p = exp(-((x - (a+b)/2) / sigma)**2/2) / (sigma * sqrt(2*pi))

        if random() < p:
            sample.append(x)

    sample.sort()
    return sample


def plot_variancial(sequence: list) -> None:
    counts = Counter(sequence)
    x = list(counts.keys())
    y = cumsum(list(counts.values())) / len(sequence)
    plt.plot(x, y, drawstyle="steps")
    plt.xticks(x)
    plt.title("Діаграма накопичених частот")
    plt.xlabel("Значення")
    plt.ylabel("Накопичена частота")
    plt.grid()
    plt.show()


def plot_histogram(sequence: list, bins=20) -> None:
    bins = list(range(int(min(sequence)), int(max(sequence))+2))
    plt.hist(sequence, bins=bins, width=1, edgecolor="black")
    plt.xticks(range(int(min(sequence)), int(max(sequence))+1))
    plt.title("Діаграма накопичених частот")
    plt.xlabel("Значення")
    plt.ylabel("Частота випадання")
    plt.show()


if __name__ == "__main__":
    A = 0
    B = 20
    N = 30
    STD = 15

    result = generate_random_list_x(A, B, STD, N)
    # result = [2, 4, 5, 5, 7]

    print(
        f"{result}\n"
        f"Математичне сподівання: {custom_mean(result, N):.2f}, "
        f"Дисперсія: {custom_variance(result, N):.2f}, "
        f"Середньоквадратичне відхилення: {custom_devidation(result, N):.2f}"
    )

    plot_variancial(result)
    plot_histogram(result)
