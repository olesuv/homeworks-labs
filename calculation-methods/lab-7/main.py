import random
import math


def generate_matrix_A():
    with open("matrix_A.txt", "w") as matrix_A:
        n = 100
        a, b = 1.0, 9.0
        for i in range(1, n+1):
            for j in range(1, n):
                r_numb = a + b * random.random()
                matrix_A.write(f"{r_numb}\t")
            r_numb = a + b * random.random()
            matrix_A.write(f"{r_numb}\n")


def norma_vector(x, n):
    max_val = 0
    for i in range(1, n+1):
        if abs(x[i]) > max_val:
            max_val = abs(x[i])
    return max_val


def LU_find(L, U, A, n):
    for k in range(1, n+1):
        for i in range(k, n+1):
            sum_val = 0.0
            for j in range(1, k):
                sum_val += L[i][j] * U[j][k]
            L[i][k] = A[i][k] - sum_val
        for i in range(k+1, n+1):
            sum_val = 0.0
            for j in range(1, k):
                sum_val += L[k][j] * U[j][i]
            U[k][i] = (A[k][i] - sum_val) / L[k][k]


def LU_solve(L, U, B, X, n):
    Z = [0] * (n+1)
    Z[1] = B[1] / L[1][1]
    for k in range(2, n+1):
        sum_val = 0.0
        for j in range(1, k):
            sum_val += L[k][j] * Z[j]
        Z[k] = (B[k] - sum_val) / L[k][k]
    X[n] = Z[n]
    for k in range(n-1, 0, -1):
        sum_val = 0.0
        for j in range(k+1, n+1):
            sum_val += U[k][j] * X[j]
        X[k] = Z[k] - sum_val


def new_B(A, X, B0, n):
    for i in range(1, n+1):
        sum_val = 0
        for j in range(1, n+1):
            sum_val += A[i][j] * X[j]
        B0[i] = sum_val


def main():
    generate_matrix_A()

    with open("matrix_A.txt", "r") as matrix_A, \
            open("matrix_B.txt", "w") as matrix_B, \
            open("matrix_X.txt", "w") as matrix_X, \
            open("matrix_L.txt", "w") as matrix_L, \
            open("matrix_U.txt", "w") as matrix_U:

        n = 100
        N = n + 1
        x_0 = 0.51
        eps = 1e-13
        r_eps = 0

        B = [0] * N
        B0 = [0] * N
        X = [0] * N
        R = [0] * N
        dX = [0] * N

        A = [[0] * N for _ in range(N)]
        L = [[0] * N for _ in range(N)]
        U = [[0] * N for _ in range(N)]

        for i in range(1, n+1):
            row = list(map(float, matrix_A.readline().split()))
            for j, val in enumerate(row):
                A[i][j+1] = val

        for i in range(1, n+1):
            sum_val = sum(A[i][1:n+1])
            B[i] = sum_val * x_0
            matrix_B.write(f"{B[i]}\n")

        for i in range(1, n+1):
            for j in range(1, n+1):
                L[i][j] = 0.0
                U[i][j] = 0.0
                if i == j:
                    U[i][j] = 1.0

        LU_find(L, U, A, n)

        for i in range(1, n+1):
            matrix_L.write("\t".join(map(str, L[i][1:n+1])) + "\n")
            matrix_U.write("\t".join(map(str, U[i][1:n+1])) + "\n")

        LU_solve(L, U, B, X, n)

        dX[1:n+1] = [X[i] - x_0 for i in range(1, n+1)]
        r_eps = norma_vector(dX, n)

        print(f"Start solution = {r_eps}")

        k = 0
        kmax = int(1e+6)

        while r_eps >= eps:
            new_B(A, X, B0, n)

            for i in range(1, n+1):
                R[i] = B[i] - B0[i]

            LU_solve(L, U, R, dX, n)

            for i in range(1, n+1):
                X[i] += dX[i]

            k += 1

            if k >= kmax:
                print("Max iteration")
                break

            r_eps = norma_vector(dX, n)

        print(f"Number of iterations = {k}")

        for i in range(1, n+1):
            matrix_X.write(f"{X[i]}\n")


if __name__ == "__main__":
    main()
