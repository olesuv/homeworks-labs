from cmath import sin


def f(x: float):
    return sin(x)


def tabulation(hh: float, N: int, xn: float, x0: float, x: list[int], y: list[int], h: list[int]):
    for i in range(N):
        x[i] = x0 + (i) * hh
        h[i] = hh
        y[i] = f(x[i])

    return x, y, h


def write_to_file(N: int, x: list[int], y: list[int], h: list[int]):
    f = open("index.txt", "w")

    for i in range(N):
        f.write(f"{i}\t{x[i]}\t{y[i]}\t{h[i]}")

    f.close()


if __name__ == "__main__":
    N = 50
    x0 = 0
    xn = 1
    x, y, h = [N+1], [N+1], [N+1]

    hh = (xn - x0) / N
    x, y, h = tabulation(hh, N, xn, x0, x, y, h)
    write_to_file(N, x, y, h)
