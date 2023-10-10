import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x)


def write_input_data():
    a = 0
    b = 1
    n = 30
    h = (b - a) / n
    with open("in.txt", "w") as file1:
        for i in range(n+1):
            x = a + i * h
            y = f(x)
            file1.write(f"{x} {y}\n")


def readdata():
    with open("in.txt", "r") as file:
        lines = file.readlines()
        X, Y = [], []
        for line in lines:
            x, y = map(float, line.split())
            X.append(x)
            Y.append(y)
    return X, Y


def wkx(k, x, X):
    p = 1
    for i in range(k+1):
        p *= (x - X[i])
    return p


def rr(k, X, Y):
    S = 0
    for i in range(k+1):
        p = 1
        for j in range(k+1):
            if j != i:
                p *= (X[i] - X[j])
        S += Y[i] / p
    return S


def Nn(x, N, X, Y):
    S = Y[0]
    for k in range(1, N+1):
        S += wkx(k-1, x, X) * rr(k, X, Y)
    return S


def plot_file(filename, title):
    with open(filename, 'r') as file:
        lines = file.readlines()
        x_vals, y_vals = [], []
        for line in lines:
            x, y = map(float, line.split())
            x_vals.append(x)
            y_vals.append(y)
        plt.plot(x_vals, y_vals)
        plt.title(title)
        plt.show()


def main():
    write_input_data()
    X, Y = readdata()
    N = len(X) - 2
    print(N)
    R = 0
    x = X[0]
    h = (X[N] - X[0]) / (20 * N)

    with open("outNn.txt", "w") as file1, open("outWk.txt", "w") as file2, open("outR.txt", "w") as file3:
        for _ in range(20 * N + 1):
            file1.write(f"{x} {Nn(x, N, X, Y)}\n")
            R = abs(f(x) - Nn(x, N, X, Y))
            file2.write(f"{x} {wkx(N, x, X)}\n")
            file3.write(f"{x} {R}\n")
            x += h

    plot_file("in.txt", "Input Data")
    plot_file("outNn.txt", "Output Nn")
    plot_file("outR.txt", "Output R")
    plot_file("outWk.txt", "Output Wk")


if __name__ == "__main__":
    main()
