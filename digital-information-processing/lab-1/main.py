import random
from math import log10
import matplotlib.pyplot as plt


# Pi
def get_pi_list(rand_list: list, n: int) -> list:
    pi_list = []

    for i in rand_list:
        temp = i / n
        pi_list.append(temp)

    return pi_list


# H
def get_hi(pi_list: list):
    h = 0

    for i in range(len(pi_list)):
        if pi_list[i] > 0:
            h += -pi_list[i] * log10(pi_list[i])

    return h


# Graphic
def build_graph(x: list, y: list):
    plt.plot(x, y)
    plt.title("Залежність ентропії появи чисел")
    plt.show()


if __name__ == "__main__":
    rand_100 = [random.randint(0, 9) for i in range(100)]
    rand_500 = [random.randint(0, 9) for i in range(500)]
    rand_1000 = [random.randint(0, 9) for i in range(1000)]

    h_list = []

    pi_list = get_pi_list(rand_100, 100)
    h = get_hi(pi_list)
    h_list.append(h)
    print(h)

    pi_list = get_pi_list(rand_500, 500)
    h = get_hi(pi_list)
    h_list.append(h)
    print(h)

    pi_list = get_pi_list(rand_1000, 1000)
    h = get_hi(pi_list)
    h_list.append(h)
    print(h)

    build_graph([100, 500, 1000], h_list)
