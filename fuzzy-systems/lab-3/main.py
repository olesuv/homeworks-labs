import matplotlib.pyplot as plt
from fractions import Fraction
from functools import reduce
import numpy as np
from scipy.interpolate import splrep, splev


def process_file(file_path, ax):
    results = []

    with open(file_path, "r") as f:
        data = [list(map(parse_value, line.split())) for line in f]

    for row in data:
        result = (reduce(lambda x, y: float(x) * float(y),
                         row[1:]) / max(row[1:])) ** (1/7)
        results.append(result)

    print(results)

    x_values = [row[0] for row in data]
    y_values = [val / max(results) for val in results]

    # Perform S-aproximation
    tck = splrep(x_values, y_values, s=0)
    x_new = np.linspace(min(x_values), max(x_values), 1000)
    y_new = splev(x_new, tck, der=0)

    ax.plot(x_values, y_values, 'o', label=f"{file_path}")
    ax.plot(x_new, y_new, label=f"S-aproximation for '{file_path}'")

    return x_new, y_new


def parse_value(value):
    try:
        return float(value)
    except ValueError:
        return float(Fraction(value))


def complement(x_values, y_values):
    return x_values, [1 - y for y in y_values]


def intersection(x_values1, y_values1, x_values2, y_values2):
    x_new = np.linspace(max(min(x_values1), min(x_values2)),
                        min(max(x_values1), max(x_values2)), 1000)
    tck1 = splrep(x_values1, y_values1, s=0)
    tck2 = splrep(x_values2, y_values2, s=0)
    y_new1 = splev(x_new, tck1, der=0)
    y_new2 = splev(x_new, tck2, der=0)
    return x_new, [min(y1, y2) for y1, y2 in zip(y_new1, y_new2)]


def union(x_values1, y_values1, x_values2, y_values2):
    x_new = np.linspace(min(min(x_values1), min(x_values2)),
                        max(max(x_values1), max(x_values2)), 1000)
    tck1 = splrep(x_values1, y_values1, s=0)
    tck2 = splrep(x_values2, y_values2, s=0)
    y_new1 = splev(x_new, tck1, der=0)
    y_new2 = splev(x_new, tck2, der=0)
    return x_new, [max(y1, y2) for y1, y2 in zip(y_new1, y_new2)]


def difference(x_values1, y_values1, x_values2, y_values2):
    x_new = np.linspace(min(x_values1), max(x_values1), 1000)
    tck1 = splrep(x_values1, y_values1, s=0)
    tck2 = splrep(x_values2, y_values2, s=0)
    y_new1 = splev(x_new, tck1, der=0)
    y_new2 = splev(x_new, tck2, der=0)
    return x_new, [max(y1 - y2, 0) for y1, y2 in zip(y_new1, y_new2)]


def symmetric_difference(x_values1, y_values1, x_values2, y_values2):
    x_new = np.linspace(min(min(x_values1), min(x_values2)),
                        max(max(x_values1), max(x_values2)), 1000)
    tck1 = splrep(x_values1, y_values1, s=0)
    tck2 = splrep(x_values2, y_values2, s=0)
    y_new1 = splev(x_new, tck1, der=0)
    y_new2 = splev(x_new, tck2, der=0)
    return x_new, [abs(y1 - y2) for y1, y2 in zip(y_new1, y_new2)]


def concentrate(x_values, y_values, alpha):
    return x_values, [y**alpha for y in y_values]


def stretch(x_values, y_values, beta):
    return x_values, [y**beta for y in y_values]


def low_and_high(x_values):
    return x_values, [min(1 - x, x) for x in x_values]


def low_or_high(x_values):
    return x_values, [max(1 - x, x) for x in x_values]


def not_high(x_values):
    return x_values, [1 - x for x in x_values]


def slightly_low(x_values, alpha=0.2):
    return x_values, [max(0, 1 - alpha*x) for x in x_values]


def very_high(x_values, beta=0.2):
    return x_values, [min(1, beta*x) for x in x_values]


if __name__ == "__main__":
    fig, axs = plt.subplots(2, 4, figsize=(16, 8))

    tall_ax = axs[0, 0]
    short_ax = axs[0, 1]
    complement_ax = axs[0, 2]
    intersection_ax = axs[0, 3]
    union_ax = axs[1, 0]
    difference_ax = axs[1, 1]
    symmetric_difference_ax = axs[1, 2]
    concentration_ax = axs[1, 3]

    print("Результати для високого чоловіка:")
    x_tall, y_tall = process_file("tall_man.txt", tall_ax)
    print("\nРезультати для низького чоловіка:")
    x_short, y_short = process_file("short_man.txt", short_ax)

    tall_ax.set_title("Високий чоловік")
    short_ax.set_title("Низький чоловік")

    complement_ax.set_title("Доповнення")
    intersection_ax.set_title("Перетин")
    union_ax.set_title("Об'єднання")
    difference_ax.set_title("Різниця")
    symmetric_difference_ax.set_title("Симетрична різниця")
    concentration_ax.set_title("Концентрація")

    x_comp, y_comp = complement(x_tall, y_tall)
    x_inter, y_inter = intersection(x_tall, y_tall, x_short, y_short)
    x_uni, y_uni = union(x_tall, y_tall, x_short, y_short)
    x_diff, y_diff = difference(x_tall, y_tall, x_short, y_short)
    x_sym_diff, y_sym_diff = symmetric_difference(
        x_tall, y_tall, x_short, y_short)
    x_conc, y_conc = concentrate(x_tall, y_tall, 2)  # 2 is an example alpha
    x_stretch, y_stretch = stretch(
        x_tall, y_tall, 0.5)  # 0.5 is an example beta

    complement_ax.plot(x_comp, y_comp, label="Complement")
    intersection_ax.plot(x_inter, y_inter, label="Intersection")
    union_ax.plot(x_uni, y_uni, label="Union")
    difference_ax.plot(x_diff, y_diff, label="Difference")
    symmetric_difference_ax.plot(
        x_sym_diff, y_sym_diff, label="Symmetric Difference")
    concentration_ax.plot(x_conc, y_conc, label="Concentration")
    concentration_ax.plot(x_stretch, y_stretch, label="Stretch")

    plt.tight_layout()
    plt.show()
