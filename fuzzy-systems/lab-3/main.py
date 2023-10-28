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


def membership_low_high(x):
    # Функція приналежності "низька і висока людина"
    return np.minimum(1 - np.abs(x - 0.5), np.abs(x - 0.75))

def membership_low_or_high(x):
    # Функція приналежності "низька або висока людина"
    return np.maximum(x, 1 - x)

def membership_not_high(x):
    # Функція приналежності "не висока людина"
    return 1 - np.minimum(x, 1 - x)

def membership_slightly_low(x):
    # Функція приналежності "злегка низька людина"
    return np.maximum(0, 1 - x**2)

def membership_very_high(x):
    # Функція приналежності "дуже висока людина"
    return x**2


def check_commutativity(func, operation_name):
    # Перевірка комутативності
    x = np.linspace(0, 1, 100)
    result1 = func(x)
    result2 = func(1 - x)

    plt.figure()
    plt.plot(x, result1, label=f"{operation_name}(x)")
    plt.plot(x, result2, label=f"{operation_name}(1 - x)")
    plt.title(f"Перевірка комутативності для {operation_name}")
    plt.legend()
    plt.show()

def check_associativity(func, operation_name):
    # Перевірка асоціативності
    x = np.linspace(0, 1, 100)
    result1 = func(func(x))
    result2 = func(x)

    plt.figure()
    plt.plot(x, result1, label=f"{operation_name}({operation_name}(x))")
    plt.plot(x, result2, label=f"{operation_name}(x)")
    plt.title(f"Перевірка асоціативності для {operation_name}")
    plt.legend()
    plt.show()

def check_distributivity(func1, func2, operation_name1, operation_name2):
    # Перевірка дистрибутивності
    x = np.linspace(0, 1, 100)
    result1 = func1(operation_name1(x))
    result2 = operation_name2(func1(x))

    plt.figure()
    plt.plot(x, result1, label=f"{operation_name1}({operation_name2}(x))")
    plt.plot(x, result2, label=f"{operation_name2}({operation_name1}(x))")
    plt.title(f"Перевірка дистрибутивності для {operation_name1} та {operation_name2}")
    plt.legend()
    plt.show()

def check_involution(func, operation_name):
    # Перевірка інволюції
    x = np.linspace(0, 1, 100)
    result1 = func(func(x))
    result2 = 1 - func(x)

    plt.figure()
    plt.plot(x, result1, label=f"{operation_name}({operation_name}(x))")
    plt.plot(x, result2, label=f"1 - {operation_name}(x)")
    plt.title(f"Перевірка інволюції для {operation_name}")
    plt.legend()
    plt.show()

def check_de_morgan_laws(func1, func2, operation_name1, operation_name2):
    # Перевірка законів де Моргана
    x = np.linspace(0, 1, 100)
    result1 = operation_name1(func1(x))
    result2 = func2(x)

    plt.figure()
    plt.plot(x, result1, label=f"{operation_name1}({operation_name2}(x))")
    plt.plot(x, result2, label=f"{operation_name2}({operation_name1}(x))")
    plt.title(f"Перевірка законів де Моргана для {operation_name1} та {operation_name2}")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    fig, axs = plt.subplots(1, 2)

    tall_ax = axs[0]
    short_ax = axs[1]

    print("Результати для високого чоловіка:")
    x_tall, y_tall = process_file("tall_man.txt", tall_ax)
    print("\nРезультати для низького чоловіка:")
    x_short, y_short = process_file("short_man.txt", short_ax)

    tall_ax.set_title("Високий чоловік")
    short_ax.set_title("Низький чоловік")

    plt.tight_layout()
    plt.show()


    # Генеруємо значення x для відображення функцій приналежності
    x = np.linspace(0, 1, 100)

    # Викликаємо функції приналежності та будуємо графіки
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    functions = [
        ("Низька і висока людина", membership_low_high),
        ("Низька або висока людина", membership_low_or_high),
        ("Не висока людина", membership_not_high),
        ("Злегка низька людина", membership_slightly_low),
        ("Дуже висока людина", membership_very_high)
    ]

    for (title, func), ax in zip(functions, axs.flatten()):
        ax.plot(x, func(x))
        ax.set_title(title)

    plt.tight_layout()
    plt.show()

    # Перевірка комутативності
    check_commutativity(membership_low_high, "низька і висока людина")
    check_commutativity(membership_low_or_high, "низька або висока людина")

    # Перевірка асоціативності
    check_associativity(membership_low_high, "низька і висока людина")
    check_associativity(membership_low_or_high, "низька або висока людина")

    # Перевірка дистрибутивності
    check_distributivity(membership_low_high, membership_low_or_high, "низька і висока людина", "низька або висока людина")

    # Перевірка інволюції
    check_involution(membership_low_high, "низька і висока людина")
    check_involution(membership_low_or_high, "низька або висока людина")

    # Перевірка законів де Моргана
    check_de_morgan_laws(membership_low_high, membership_low_or_high, "низька і висока людина", "низька або висока людина")
