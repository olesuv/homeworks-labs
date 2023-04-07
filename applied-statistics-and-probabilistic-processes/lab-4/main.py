from random import uniform
from numpy import var
import matplotlib.pyplot as plt


def sample_mean(data: list) -> float:
    return sum(data) / len(data)


def sample_variance(data: list):
    return var(data, ddof=1)


def f_15(x: int) -> float:
    if 0 <= x <= 2:
        return -0.125 * x + 0.25
    elif 2 < x < 4:
        return 0.125 * x - 0.25
        # return 0.125 * x + -0.25
    elif x == 4:
        return 0.125 * x + -0.75
    elif 4 < x <= 6:
        return -0.125 * x + 0.75
    else:
        return 0


def neyman_method(a: int, b: int, m: float, f, n_samples: int) -> list:
    samples = []

    while len(samples) < n_samples:
        r1 = uniform(0, 1)
        r2 = uniform(0, 1)

        x0 = a + r1 * (b - a)
        n = r2 * m

        if n <= f(x0):
            samples.append(x0)

    return samples


def plot_histogram(sequence, bins=20, width=0.8):
    plt.hist(sequence, bins=bins, rwidth=width)

    plt.title("Histogram of the Sequence")

    plt.xlabel("Value")

    plt.ylabel("Frequency")

    plt.show()


if __name__ == "__main__":
    MIN = 0
    MAX = 6
    M = 0.5
    F = f_15
    N = 1000

    result = neyman_method(MIN, MAX, M, F, N)
    result_mean = sample_mean(result)
    result_variance = sample_variance(result)

    print(f"Метод виключення (Неймана): {result}")
    print(f"Математичне сподівання: {result_mean:.2f}")
    print(f"Дисперсія: {result_variance:.2f}")

    plot_histogram(result)
