from random import random, randint
import numpy as np
from collections import Counter
from math import sqrt, pi, exp
import matplotlib.pyplot as plt


def std_dev(data: list) -> float:
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    std_dev = sqrt(variance)

    return std_dev


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
    y = np.cumsum(list(counts.values())) / len(sequence)
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
    print(result)
    # result = [2, 4, 5, 5, 7]
    plot_variancial(result)
    plot_histogram(result)
