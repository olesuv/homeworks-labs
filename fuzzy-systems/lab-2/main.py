import matplotlib.pyplot as plt
from fractions import Fraction
from functools import reduce
import numpy as np


def process_file(file_path):
    results = []

    with open(file_path, "r") as f:
        data = [list(map(parse_value, line.split())) for line in f]

    for row in data:
        result = reduce(lambda x, y: float(x) * float(y),
                        row[1:]) ** (1/7) / max(row[1:])
        results.append(result)
        print(result)

    x_values = [row[0] for row in data]

    y_values = results

    plt.plot(x_values, y_values)
    plt.title(f"Графік для файлу '{file_path}'")
    plt.xlabel("Ріст")
    plt.ylabel("Ступінь приналежності і-того елемента до нечіткої множини")

    p = np.polyfit(x_values, y_values, 1)
    plt.plot(x_values, np.polyval(p, x_values),
             'r--', label=f'Лінійна регресія')
    # : {p[0]:.2f}x + {p[1]:.2f}
    plt.legend()

    plt.show()


def parse_value(value):
    try:
        return float(value)
    except ValueError:
        return float(Fraction(value))


if __name__ == "__main__":
    print("Tall man results:")
    process_file("tall_man.txt")
    print("\nShort man results:")
    process_file("short_man.txt")
