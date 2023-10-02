import matplotlib.pyplot as plt
from fractions import Fraction
from functools import reduce
import numpy as np


def process_file(file_path, ax):
    results = []

    with open(file_path, "r") as f:
        data = [list(map(parse_value, line.split())) for line in f]

    for row in data:
        result = (reduce(lambda x, y: float(x) * float(y),
                         row[1:]) / max(row[1:])) ** (1/7)
        results.append(result)
        print(result)

    x_values = [row[0] for row in data]

    y_values = results

    ax.plot(x_values, y_values, label=f"Графік для файлу '{file_path}'")
    # p = np.polyfit(x_values, y_values, 1)
    # ax.plot(x_values, np.polyval(p, x_values),
    #         'r--', label=f'Лінійна регресія')


def parse_value(value):
    try:
        return float(value)
    except ValueError:
        return float(Fraction(value))


if __name__ == "__main__":
    fig, ax = plt.subplots()
    print("Tall man results:")
    process_file("tall_man.txt", ax)
    print("\nShort man results:")
    process_file("short_man.txt", ax)

    ax.set_title("Графіки для двох файлів")
    ax.set_xlabel("Ріст")
    ax.set_ylabel("Ступінь приналежності і-того елемента до нечіткої множини")
    ax.legend()
    plt.show()
