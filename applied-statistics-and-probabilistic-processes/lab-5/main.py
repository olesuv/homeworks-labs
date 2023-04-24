from random import random, randint
from numpy import cumsum, arange, histogram
from collections import Counter
from math import sqrt, pi, exp, log10
import matplotlib.pyplot as plt
import xlsxwriter


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


def generate_random_list_x_y(a: int, b: int, sigma: int, list_amount: int) -> list:
    sample = []

    while len(sample) < list_amount:
        x = randint(a, b)
        y = randint(a, b)

        p_x = exp(-((x - (a+b)/2) / sigma)**2/2) / (sigma * sqrt(2*pi))
        p_y = exp(-((y - (a+b)/2) / sigma)**2/2) / (sigma * sqrt(2*pi))

        if random() < p_x and random() < p_y:
            sample.append([x, y])

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

    hist, _ = histogram(sequence, bins=bins)
    hist = hist / len(sequence)

    plt.bar(bins[:-1], hist, width=1, edgecolor="black")
    plt.xticks(range(int(min(sequence)), int(max(sequence))+1))
    plt.ylim(0, 1)
    plt.title("Діаграма накопичених частот")
    plt.xlabel("Значення")
    plt.ylabel("Частота випадання")
    plt.show()


def plot_scattering_fields(sequence: list) -> None:
    x = [d[0] for d in sequence]
    y = [d[1] for d in sequence]

    plt.scatter(x, y)
    plt.title("Поля розсіяння")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


def create_intervals(data_amount: int, data: list) -> tuple:
    intervals_x = [0]
    intervals_y = [0]

    max_x = max(row[0] for row in data)
    min_x = min(row[0] for row in data)
    max_y = max(row[1] for row in data)
    min_y = min(row[1] for row in data)

    k = round(1 + 3.2 * log10(data_amount))
    interval = round((max_x - min_x) / k)

    temp_interval_x = 0
    while temp_interval_x < max_x:
        temp_interval_x += interval
        intervals_x.append(temp_interval_x)

    temp_interval_y = 0
    while temp_interval_y < max_y:
        temp_interval_y += interval
        intervals_y.append(temp_interval_y)

    return intervals_x, intervals_y


def match_intervals(data: list, intervals_x: list, intervals_y: list) -> None:
    table = []
    for i in range(len(intervals_y)-1):
        row = []
        for j in range(len(intervals_x)-1):
            count = 0
            matched_points = []
            for point in data:
                if intervals_x[j] <= point[0] < intervals_x[j+1] and intervals_y[i] <= point[1] < intervals_y[i+1]:
                    count += 1
                    matched_points.append(point)
            row.append(count)
            if matched_points:
                print(f"\n{matched_points} belongs to interval {j}-{i}")
        table.append(row)

    print("\nIntervals of x-axis:")
    for i in range(len(intervals_x)-1):
        print(
            f"{i}: {intervals_x[i]} - {intervals_x[i+1]}: {sum(row[i] for row in table)}")

    print("\nIntervals of y-axis:")
    for i in range(len(intervals_y)-1):
        print(f"{i}: {intervals_y[i]} - {intervals_y[i+1]}: {sum(table[i])}")


if __name__ == "__main__":
    A = 0
    B = 30
    N = 30
    STD = 15

    # result = generate_random_list_x(A, B, STD, N)
    result = [2, 4, 5, 5, 7]

    # print(
    #     f"{result}\n"
    #     f"Математичне сподівання: {custom_mean(result, N):.2f}, "
    #     f"Дисперсія: {custom_variance(result, N):.2f}, "
    #     f"Середньоквадратичне відхилення: {custom_devidation(result, N):.2f}"
    # )

    # plot_variancial(result)
    # plot_histogram(result)

    result = generate_random_list_x_y(A, B, STD, N)
    print(f"Generated points: \n{result}")

    intervals_x = create_intervals(N, result)[0]
    intervals_y = create_intervals(N, result)[1]
    print(f"\nIntervals by x: {intervals_x}")
    print(f"Intervals by y: {intervals_y}")

    match_intervals(result, intervals_x, intervals_y)

    plot_scattering_fields(result)
