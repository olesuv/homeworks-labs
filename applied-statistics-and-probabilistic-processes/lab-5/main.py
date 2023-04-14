from random import random, uniform, randint
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


def plot_histogram(sequence):
    plt.plot(sequence, drawstyle="steps")
    plt.xlabel("Накопичена частота")
    plt.ylabel("Значенння")
    plt.title("Діаграма накопичених частот")
    plt.show()


if __name__ == "__main__":
    A = 0
    B = 20
    N = 30
    STD = 15

    # result = generate_random_list_x(A, B, STD, N)
    # print(result)

    result = [2, 4, 5, 5, 7]
    plot_histogram(result)
