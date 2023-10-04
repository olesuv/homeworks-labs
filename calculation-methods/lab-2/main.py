import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x)


def generate_input_file():
    a = 0
    b = 1
    n = 20
    h = (b - a) / n

    with open("in.txt", "wt") as file1:
        for i in range(n+1):
            x = a + i*h
            y = f(x)
            file1.write(f"{x:e} {y:e}\n")


def read_data():
    X = []
    Y = []

    with open("in.txt", "rt") as file:
        for line in file:
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


def plot_file(filename, title, xlabel, ylabel):
    with open(filename, 'r') as file:
        data = [list(map(float, line.split())) for line in file]
        x, y = zip(*data)

    plt.figure()
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def main():
    generate_input_file()
    X, Y = read_data()
    N = len(X) - 2

    with open("outNn.txt", "wt") as file1, open("outWk.txt", "wt") as file2, open("outR.txt", "wt") as file3:
        h = (X[N] - X[0]) / (20 * N)
        x = X[0]
        for _ in range(20*N+1):
            file1.write(f"{x:e} {Nn(x, N, X, Y):e}\n")
            R = abs(f(x) - Nn(x, N, X, Y))
            file2.write(f"{x:e} {wkx(N, x, X):e}\n")
            file3.write(f"{x:e} {R:e}\n")
            x += h


if __name__ == "__main__":
    main()
    plot_file("outNn.txt", "Nn vs x", "x", "Nn(x)")
    plot_file("outWk.txt", "wkx vs x", "x", "wkx(x)")
    plot_file("outR.txt", "R vs x", "x", "R(x)")
