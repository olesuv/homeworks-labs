import random
import numpy as np
import matplotlib.pyplot as plt

num_of_elements = int(input("Введіть кількість елементів: "))

arr = []


def generator(n: int, arr: list) -> None:
    arr.clear()
    for x in range(n):
        arr.append(random.randint(1, 6))


generator(num_of_elements, arr)
print(arr)
print(f"Вибіркове математичне сподівання: {np.mean(arr)}")
print(f"Вибіркова дисперсія: {np.var(arr, ddof=1)}")
print(f"Вибіркове середньокв. відхилення: {np.std(arr, ddof=1)}")


def xn_on(arr: list) -> list:
    x = 10
    xn_result = []
    on_result = []

    for i in range(4):
        generator(x, arr)
        xn_result.append(np.mean(arr))
        on_result.append(np.std(arr, ddof=1))
        x *= 10

    return [xn_result, on_result]


figure, axis = plt.subplots(1, 2)

axis[0].hist(arr, bins=6, range=(1, 7), align='left', edgecolor='black')
axis[0].set_xlabel("Числа")
axis[0].set_ylabel("Кількість")
axis[0].set_title("Залежність частоти випадання\nk-го числа від номера k")
axis[0].axhline(y=num_of_elements/6, color='r', linestyle='--')
axis[0].text(0, num_of_elements/6, '1/6', ha='right', va='center', color='r')

result = xn_on(arr)
axis[1].plot([np.log(10), np.log(100),
             np.log(1000), np.log(10000)], result[0], label="xN/lg(N)")
axis[1].plot([np.log(10), np.log(100),
             np.log(1000), np.log(10000)], result[1], label="oN/lg(N)")
axis[1].set_xlabel("lgN")
axis[1].set_ylabel("xN, oN")
axis[1].set_title("Відношення залежності xN та oN від lgN")

figure.tight_layout()
plt.legend()
plt.show()
