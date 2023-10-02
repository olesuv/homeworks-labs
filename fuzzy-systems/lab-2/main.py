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


if __name__ == "__main__":
    fig, ax = plt.subplots()
    print("Tall man results:")
    x_tall, y_tall = process_file("tall_man.txt", ax)
    print("\nShort man results:")
    x_short, y_short = process_file("short_man.txt", ax)

    ax.set_title("Графіки для двох файлів")
    ax.set_xlabel("Ріст")
    ax.set_ylabel("Ступінь приналежності і-того елемента до нечіткої множини")
    ax.legend()
    plt.show()
