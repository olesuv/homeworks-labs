import math
import matplotlib.pyplot as plt


def func(x):
    return math.sin(x)


def read_n():
    with open("in.txt", "r") as fdata:
        N = sum(1 for _ in fdata) - 1
    return N


def step(x, n):
    if n == 0:
        return 1
    else:
        return x**n


def bkj(B, X, n, m):
    for k in range(m+1):
        for j in range(m+1):
            B[k][j] = sum(step(X[i], k+j) for i in range(n+1))


def cj(C, X, F, n, m):
    for j in range(m+1):
        C[j] = sum(F[i]*step(X[i], j) for i in range(n+1))


def GAUSS(A, B, X, m):
    for k in range(m):
        p = max(range(k, m+1), key=lambda i: abs(A[i][k]))
        A[k], A[p] = A[p], A[k]
        B[k], B[p] = B[p], B[k]

        for i in range(k+1, m+1):
            t = A[i][k] / A[k][k]
            for j in range(k, m+1):
                A[i][j] -= t * A[k][j]
            B[i] -= t * B[k]

    X[m] = B[m] / A[m][m]

    for k in range(m-1, -1, -1):
        sum_val = sum(A[k][j] * X[j] for j in range(k+1, m+1))
        X[k] = (B[k] - sum_val) / A[k][k]


def AprokMn(A, x, m):
    return sum(A[j] * step(x, j) for j in range(m+1))


def dysp(X, A, n, m):
    D = sum(step(func(X[i]) - AprokMn(A, X[i], m), 2) for i in range(n+1))
    return math.sqrt(D / (n+1))


def plot_dispersions(X, F, n):
    m_values = list(range(1, 11))
    dispersions = []

    for m in m_values:
        B = [[0] * (m + 1) for _ in range(m + 1)]
        C = [0] * (m + 1)
        A = [0] * (m + 1)

        bkj(B, X, n, m)
        cj(C, X, F, n, m)
        GAUSS(B, C, A, m)

        D = dysp(X, A, n, m)
        dispersions.append(D)

    plt.plot(m_values, dispersions, marker='o')
    plt.xlabel('Ступінь апроксимуючого многочлена (m)')
    plt.ylabel('Дисперсія')
    plt.title('Залежність дисперсії від ступеня m')
    plt.show()


def main():
    with open("in.txt", "r") as input_file:
        n = sum(1 for _ in input_file) - 1

    m = 4
    X, F = [], []

    with open("in.txt", "r") as input_file:
        for line in input_file:
            x, f = map(float, line.strip().split())
            X.append(x)
            F.append(f)

    B = [[0] * (m+1) for _ in range(m+1)]
    C = [0] * (m+1)
    A = [0] * (m+1)

    bkj(B, X, n, m)
    cj(C, X, F, n, m)
    GAUSS(B, C, A, m)

    with open("matrix_A.txt", "w") as matrix_A, \
            open("matrix_B.txt", "w") as matrix_B, \
            open("matrix_C.txt", "w") as matrix_C:

        for k in range(m+1):
            matrix_B.write('\t'.join(map(str, B[k])) + '\n')
            matrix_C.write(str(C[k]) + '\n')
            matrix_A.write(str(A[k]) + '\n')

    D = dysp(X, A, n, m)

    with open("output.txt", "w") as output:
        output.write(f"dispersion \t{D}\n")

    h = (X[-1] - X[0]) / (20 * n)
    DE = 0

    with open("plot.txt", "w") as plot:
        for i in range(20 * n + 1):
            x = X[0] + i * h
            err = abs(func(x) - AprokMn(A, x, m))
            plot.write(f"{x}\t{func(x)}\t{AprokMn(A, x, m)}\t{err}\n")
            DE += (func(x) - AprokMn(A, x, m))**2

    DE = math.sqrt(DE / (20 * n + 1))

    with open("output.txt", "a") as output:
        output.write(f"dispersionE \t{DE}\n")

    plot_dispersions(X, F, n)

    x_values, func_values, approx_values, err_values = [], [], [], []
    with open("plot.txt", "r") as plot_file:
        for line in plot_file:
            x, func_val, approx_val, err = map(float, line.strip().split())
            x_values.append(x)
            func_values.append(func_val)
            approx_values.append(approx_val)
            err_values.append(err)

    plt.figure()
    plt.plot(x_values, func_values, label='Функція')
    plt.plot(x_values, approx_values, label='Апроксимація')
    plt.plot(x_values, err_values, label='Похибка')

    plt.xlabel('x')
    plt.ylabel('Значення')
    plt.legend()
    plt.title('Графіки функції, апроксимації та похибки')
    plt.show()


if __name__ == "__main__":
    main()
