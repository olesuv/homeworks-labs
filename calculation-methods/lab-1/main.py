import math
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def f(x):
    return math.sin(x)


def main():
    N = 50
    x0, xn = 0.0, 1.0
    x, y, h = [], [], []

    hh = (xn - x0) / N

    for i in range(N+1):
        x_i = x0 + i * hh
        h_i = hh
        y_i = f(x_i)
        x.append(x_i)
        h.append(h_i)
        y.append(y_i)

    with open("input.txt", "w") as finput:
        for i in range(N+1):
            finput.write(f"{i}\t{x[i]}\t{y[i]}\t{h[i]}\n")

    print("DONE")

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Input Data')
    plt.title('Input Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def progonka(y, h):
    N = len(y) - 1
    alfa, beta, hamma, delta, A, B, c = [0.0] * (N + 1), [0.0] * (N + 1), [0.0] * (
        N + 1), [0.0] * (N + 1), [0.0] * (N + 1), [0.0] * (N + 1), [0.0] * (N + 1)

    alfa[1] = hamma[1] = delta[1] = 0.0
    beta[1] = 1.0

    for i in range(2, N + 1):
        alfa[i] = h[i-1]
        beta[i] = 2 * (h[i-1] + h[i])
        hamma[i] = h[i]
        delta[i] = 3 * (((y[i] - y[i-1]) / h[i]) -
                        ((y[i-1] - y[i-2]) / h[i-1]))

    hamma[N] = 0.0
    A[1] = -hamma[1] / beta[1]
    B[1] = delta[1] / beta[1]

    for i in range(2, N):
        A[i] = -hamma[i] / (alfa[i] * A[i-1] + beta[i])
        B[i] = (delta[i] - alfa[i] * B[i-1]) / (alfa[i] * A[i-1] + beta[i])

    c[N] = (delta[N] - alfa[N] * B[N-1]) / (alfa[N] * A[N-1] + beta[N])

    for i in range(N, 1, -1):
        c[i-1] = A[i-1] * c[i] + B[i-1]

    return c


if __name__ == "__main__":
    main()

    with open("input.txt", "r") as fdata:
        N = sum(1 for line in fdata) - 1

    x, y, xm, ym, h, a, b, c, d = [], [], [], [], [], [], [], [], []

    with open("input.txt", "r") as fdata:
        x0 = 0.0
        for line in fdata:
            j, x_i, y_i, h_i = map(float, line.split())
            x.append(x_i)
            y.append(y_i)
            h.append(h_i)

    x0 = x[0]
    hh = h[0]
    c = progonka(y, h)

    for i in range(1, N):
        a_i = y[i-1]
        b_i = (y[i] - y[i-1]) / h[i] - (h[i] / 3) * (c[i+1] + 2*c[i])
        d_i = (c[i+1] - c[i]) / (3 * h[i])
        a.append(a_i)
        b.append(b_i)
        d.append(d_i)

    a.append(y[N-1])
    b.append((y[N] - y[N-1]) / h[N] - (2.0 / 3.0) * h[N] * c[N])
    d.append(-c[N] / (3 * h[N]))

    with open("output.txt", "w") as foutput:
        hh /= 20.0
        for i in range(20 * N + 1):
            xm_i = x0 + i * hh
            ym_i = f(xm_i)
            xm.append(xm_i)
            ym.append(ym_i)

        s, eps = 0, 0
        j = 1

        for i in range(20 * (N - 1) + 1):
            s = a[j] + b[j] * (xm[i] - x[j-1]) + c[j] * \
                (xm[i] - x[j-1]) ** 2 + d[j] * (xm[i] - x[j-1]) ** 3
            eps = abs(s - ym[i])
            foutput.write(f"[{i},{j}]\t{xm[i]}\t{ym[i]}\t{s}\t{eps}\n")
            if i != 0 and i % 20 == 0:
                j += 1

    cs = CubicSpline(x, y)
    s_values = cs(xm)

    plt.figure(figsize=(10, 6))
    plt.plot(xm, ym, label='Function')
    plt.plot(xm, s_values, label='Interpolated Data', linestyle='dashed')
    plt.title('Interpolated Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
