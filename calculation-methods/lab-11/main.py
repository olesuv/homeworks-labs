import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return y + x ** 2

def fe(x):
    return -x ** 2 - 2.0 * x + 2.0 * math.exp(x) - 2.0

def runge_kutta():
    a, b, h = 0, 5, 0.01
    x1, y1 = a, 0
    x0, y0 = x1, y1
    epse = abs(fe(x0) - y0)
    eps = 0.0
    with open("output_rk.txt", "wt") as output:
        output.write(f"{x0}\t{fe(x0)}\t{y0}\t{epse}\t{eps}\n")
        while x1 < b:
            x0, y0 = x1, y1
            x1 = x0 + h
            k1 = f(x0, y0)
            k2 = f(x0 + h * 0.5, y0 + h * k1 * 0.5)
            k3 = f(x0 + h * 0.5, y0 + h * k2 * 0.5)
            k4 = f(x0 + h, y0 + h * k3)
            y1 = y0 + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x12 = x0 + h / 2
            k1 = f(x0, y0)
            k2 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k1 * 0.5)
            k3 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k2 * 0.5)
            k4 = f(x0 + h / 2, y0 + h / 2 * k3)
            y12 = y0 + h / 2 * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x0, y0 = x12, y12
            k1 = f(x0, y0)
            k2 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k1 * 0.5)
            k3 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k2 * 0.5)
            k4 = f(x0 + h / 2, y0 + h / 2 * k3)
            y1n = y0 + h / 2 * (k1 + 2 * k2 + 2 * k3 + k4) / 6
            epse = abs(fe(x1) - y1)
            eps = 16.0 / 15.0 * abs(y1 - y1n)
            output.write(f"{x1}\t{fe(x1)}\t{y1}\t{epse}\t{eps}\n")

def automatic_step():
    a, b, h = 0.0, 5.0, 0.01
    x1, y1 = a, 0
    x0, y0 = x1, y1
    epse = abs(fe(x0) - y0)
    eps_rk = 0.0
    eps = 1e-12
    with open("output_h.txt", "wt") as output:
        output.write(f"{x1}\t{fe(x1)}\t{y1}\t{epse}\t{eps_rk}\t{h}\n")
        while x1 < b:
            while True:
                x0, y0 = x1, y1
                x1 = x0 + h
                k1 = f(x0, y0)
                k2 = f(x0 + h * 0.5, y0 + h * k1 * 0.5)
                k3 = f(x0 + h * 0.5, y0 + h * k2 * 0.5)
                k4 = f(x0 + h, y0 + h * k3)
                y1 = y0 + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
                x12 = x0 + h / 2
                k1 = f(x0, y0)
                k2 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k1 * 0.5)
                k3 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k2 * 0.5)
                k4 = f(x0 + h / 2, y0 + h / 2 * k3)
                y12 = y0 + h / 2 * (k1 + 2 * k2 + 2 * k3 + k4) / 6
                x0, y0 = x12, y12
                k1 = f(x0, y0)
                k2 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k1 * 0.5)
                k3 = f(x0 + h / 2 * 0.5, y0 + h / 2 * k2 * 0.5)
                k4 = f(x0 + h / 2, y0 + h / 2 * k3)
                y1n = y0 + h / 2 * (k1 + 2 * k2 + 2 * k3 + k4) / 6
                if x1 >= b:
                    break
                epse = abs(fe(x1) - y1)
                eps_rk = 16.0 / 15.0 * abs(y1 - y1n)
                output.write(f"{x1}\t{fe(x1)}\t{y1}\t{epse}\t{eps_rk}\t{h}\n")
                if not (eps_rk <= eps and eps_rk >= eps / 32.0):
                    break
            if eps_rk > eps:
                x1 = x0
                y1 = y0
                h = h / 2.0
            if eps_rk < eps / 32:
                h = h * 2.0

def plot_error(file_path, title):
    data = np.loadtxt(file_path, delimiter='\t')
    x = data[:, 0]
    fe_x = data[:, 1]
    y = data[:, 2]
    error = data[:, 3]

    plt.figure()
    plt.plot(x, error, label='Error')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    runge_kutta()
    automatic_step()

    plot_error("output_rk.txt", "Runge-Kutta Error")
    plot_error("output_h.txt", "Automatic Step Error")
