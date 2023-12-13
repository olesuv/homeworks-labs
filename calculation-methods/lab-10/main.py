import math
import numpy as np
import matplotlib.pyplot as plt

def step(xx, nn):
    if nn == 0:
        return 1
    else:
        s = 1
        for i in range(1, nn + 1):
            s *= xx
        return s

# Rosenbrock function
def F(X, n):
    return step(1 - X[0], 2) + 100.0 * step(X[1] - X[0] * X[0], 2)

def Investigating_Search_Full(X0, X1, deltaX, eps, q, n):
    for i in range(n + 1):
        X1[i] = X0[i]

    for i in range(n + 1):
        while True:
            X1[i] = X0[i] + deltaX[i]
            if F(X1, n) < F(X0, n):
                break
            else:
                X1[i] = X0[i] - deltaX[i]
                if F(X1, n) < F(X0, n):
                    break
                else:
                    deltaX[i] = deltaX[i] / q
                    X1[i] = X0[i]
                    if deltaX[i] <= eps:
                        break

    return 0

def Investigating_Search_Simple(X0, X1, deltaX, n):
    for i in range(n + 1):
        X1[i] = X0[i]

    for i in range(n + 1):
        X1[i] = X0[i] + deltaX[i]
        if F(X1, n) < F(X0, n):
            continue
        else:
            X1[i] = X0[i] - deltaX[i]
            if F(X1, n) < F(X0, n):
                continue
            else:
                X1[i] = X0[i]

    return 0

def Difference(X, Y, eps, n):
    max_diff = 0
    for i in range(n + 1):
        if abs(Y[i] - X[i]) > max_diff:
            max_diff = abs(Y[i] - X[i])

    return 1 if max_diff < eps else 0

def Sample_Search(X0, X1, X2p, p, n):
    for i in range(n + 1):
        X2p[i] = X0[i] + p * (X1[i] - X0[i])

    return 0

def main():
    output = open("output.txt", "w")
    
    i = 0
    k = 0
    kmax = 1000
    eps1 = 1e-10
    eps2 = 1e-10
    q = 2
    p = 2
    n = 1

    deltaX = [0.0] * (n + 1)
    deltaX0 = [0.01] * (n + 1)
    X0 = [0.0] * (n + 1)
    X1 = [0.0] * (n + 1)
    X2p = [0.0] * (n + 1)
    X2 = [0.0] * (n + 1)

    for i in range(n + 1):
        X0[i] = 0.0

    for i in range(n + 1):
        X1[i] = X0[i]

    while True:
        k = k + 1
        output.write(f"\nk{k}\n\n")

        for i in range(n + 1):
            X0[i] = X1[i]

        for i in range(n + 1):
            deltaX[i] = deltaX0[i]

        Investigating_Search_Full(X0, X1, deltaX, eps1, q, n)
        output.write("ISF\n")

        if Difference(X0, X1, eps2, n):
            output.write("D1\n")
            break

        for i in range(n + 1):
            X2[i] = X1[i]
            X1[i] = X0[i]

        while True:
            for i in range(n + 1):
                X0[i] = X1[i]
                X1[i] = X2[i]

            Sample_Search(X0, X1, X2p, p, n)
            output.write("SS\n")

            for i in range(n + 1):
                deltaX[i] = deltaX0[i]

            Investigating_Search_Simple(X2p, X2, deltaX, n)
            output.write("ISS\n")

            if Difference(X2p, X2, eps2, n):
                output.write("D2\n")
                break

            if F(X2, n) < F(X1, n):
                break

        if k >= kmax:
            output.write("Max Iterations\n")
        else:
            output.write(f"Number of iterations k={k}\n")

        for i in range(n + 1):
            output.write(f"{X0[i]:e}\n")

    output.close()

def generate_data():
    a = 0
    b = 1
    n = 20
    h = (b - a) / n
    x, y = 0, 0
    file1 = open("in.txt", "wt")
    
    for i in range(n + 1):
        x = a + i * h
        y = math.sin(x)
        file1.write(f"{x:e} {y:e}\n")

    file1.close()

def plot_function(file_path):
    x_values = []
    y_values = []

    with open(file_path, 'rt') as file:
        for line in file:
            x, y = map(float, line.split())
            x_values.append(x)
            y_values.append(y)

    plt.plot(x_values, y_values, label='sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Графік функції sin(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_target_function():
    x_range = np.linspace(-2, 2, 100)  
    y_values = [F([x, 0], 1) for x in x_range] 

    plt.plot(x_range, y_values, label='F(X)')
    plt.xlabel('X')
    plt.ylabel('F(X)')
    plt.title('Графік цільової функції F(X)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    generate_data()
    main()

    plot_function("in.txt")
    # Example of how method works
    plot_target_function()

