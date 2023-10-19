import numpy as np


def f(x, y):
    return np.convolve(x, y)


x = [1, 5, 6]
y = [6, 7, 1]

x1 = [2, 8, 7, 3, 4, 5, 1, 0]
y1 = [1, 2, 8, 3, 4]

x2 = [2, 4, 0, 9, 1, 2, 7]
y2 = [0, 8, 2, 1, 6, 4, 2]

# 14
# print(f"x = {x}, y = {y}\nЗгортка: {f(x, y)}")
# print(f"\nx = {x1}, y = {y1}\nЗгортка: {f(x1, y1)}")
# print(f"\nx = {x2}, y = {y2}\nЗгортка: {f(x2, y2)}")

print(f"xk {x}")
print(f"yk {y}")
print(f"fm {f(x, y)}")
print(f"m {len(f(x, y))}\n")


print(f"xk {x1}")
print(f"yk {y1}")
print(f"fm {f(x1, y1)}")
print(f"m {len(f(x1, y1))}\n")


print(f"xk {x2}")
print(f"yk {y2}")
print(f"fm {f(x2, y2)}")
print(f"m {len(f(x2, y2))}\n")
