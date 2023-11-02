import random


def generate_matrix_file():
    with open("matrix_A.txt", "w") as matrix_A:
        n = 100
        scale = 10
        a = 1
        b = 9
        A = [[0 for _ in range(n+1)] for _ in range(n+1)]
        random.seed()

        for i in range(1, n+1):
            sum_val = 0
            for j in range(1, n+1):
                A[i][j] = a + b * random.random()
                sum_val = sum_val if i == j else sum_val + A[i][j]
            A[i][i] = sum_val * scale

        for i in range(1, n+1):
            for j in range(1, n):
                matrix_A.write(f"{A[i][j]:.16e}\t")
            matrix_A.write(f"{A[i][n]:.16e}\n")


def read_n():
    with open("matrix_A.txt", "r") as matrix_A:
        N = 0
        for line in matrix_A:
            N += 1
        return N


def norma_vector_diff(Y, X):
    max_diff = 0
    for i in range(1, len(Y)):
        diff = abs(Y[i] - X[i])
        if diff > max_diff:
            max_diff = diff
    return max_diff


def norma_matrix(X):
    max_sum = 0
    for i in range(1, len(X)):
        row_sum = sum(map(abs, X[i]))
        if row_sum > max_sum:
            max_sum = row_sum
    return max_sum


def method_gauss_zeidelya(A, B, X0, X1, n):
    kmax = 1e5
    eps = 1e-14
    print("\nMethod Gauss-Zeidelya\n\n")
    k = 1
    while True:
        for i in range(1, n+1):
            X0[i] = X1[i]
        for i in range(1, n+1):
            sum_val = 0.0
            for j in range(1, n+1):
                if j < i:
                    sum_val += A[i][j] * X1[j]
                if j > i:
                    sum_val += A[i][j] * X0[j]
            X1[i] = (B[i] - sum_val) / A[i][i]
        k += 1
        if k > kmax or norma_vector_diff(X1, X0) < eps:
            break
    if k >= kmax:
        print("Solution not found!\n")
    else:
        print("Solution founded!\n")
        print(f"Iteration: {k}\n")


def method_yacobi(A, B, X0, X1, n):
    kmax = 1e5
    eps = 1e-14
    print("\nMethod Yakobi\n\n")
    k = 1
    while True:
        for i in range(1, n+1):
            X0[i] = X1[i]
        for i in range(1, n+1):
            sum_val = 0.0
            for j in range(1, n+1):
                if j != i:
                    sum_val += A[i][j] * X0[j]
            X1[i] = (B[i] - sum_val) / A[i][i]
        k += 1
        if k > kmax or norma_vector_diff(X1, X0) < eps:
            break
    if k >= kmax:
        print("Solution not found!\n")
    else:
        print("Solution founded!\n")
        print(f"Iteration: {k}\n")


def method_simple_iteration(A, B, X0, X1, n, tau):
    kmax = 1e5
    eps = 1e-14
    print("\nSimple_iteration\n\n")
    k = 1
    while True:
        for i in range(1, n+1):
            X0[i] = X1[i]
        for i in range(1, n+1):
            sum_val = sum(X0[j] * A[i][j] for j in range(1, n+1))
            X1[i] = X0[i] - tau * sum_val + tau * B[i]
        k += 1
        if k > kmax or norma_vector_diff(X1, X0) < eps:
            break
    if k >= kmax:
        print("Solution not found!\n")
    else:
        print("Solution founded!\n")
        print(f"Iteration: {k}\n")


def main():
    with open("matrix_A.txt", "r") as matrix_A:
        n = read_n()
        print(f"{n}\n\n\n")
        A = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            row = list(map(float, matrix_A.readline().strip().split()))
            for j in range(1, n+1):
                A[i][j] = row[j-1]

        B = [0 for _ in range(n+1)]
        X0 = [0 for _ in range(n+1)]
        X1 = [0 for _ in range(n+1)]

        tau = 1 / norma_matrix(A)

        for i in range(1, n+1):
            sum_val = sum(A[i][j] for j in range(1, n+1))
            B[i] = sum_val * 2.51

        k = 1
        for i in range(1, n+1):
            X1[i] = 0.0
        method_simple_iteration(A, B, X0, X1, n, tau)

        with open("matrix_XI.txt", "w") as matrix_XI:
            for i in range(1, n+1):
                matrix_XI.write(f"{X1[i]}\n")

        with open("output.txt", "w") as output:
            output.write(f"SI\t{k}\n")

        k = 1
        for i in range(1, n+1):
            X1[i] = 0.0
        method_yacobi(A, B, X0, X1, n)

        with open("matrix_XY.txt", "w") as matrix_XY:
            for i in range(1, n+1):
                matrix_XY.write(f"{X1[i]}\n")

        with open("output.txt", "a") as output:
            output.write(f"Ya\t{k}\n")

        k = 1
        for i in range(1, n+1):
            X1[i] = 0.0
        method_gauss_zeidelya(A, B, X0, X1, n)

        with open("matrix_XG.txt", "w") as matrix_XG:
            for i in range(1, n+1):
                matrix_XG.write(f"{X1[i]}\n")

        with open("output.txt", "a") as output:
            output.write(f"GZ\t{k}\n")


if __name__ == "__main__":
    generate_matrix_file()
    main()
