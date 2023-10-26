import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x)


def progonka(y, h):
    N = len(y) - 1
    alfa, beta, hamma, delta, A, B, c = [0.0] * (N+1), [0.0] * (N+1), [0.0] * (
        N+1), [0.0] * (N+1), [0.0] * (N+1), [0.0] * (N+1), [0.0] * (N+1)

    alfa[1] = hamma[1] = delta[1] = 0.0
    beta[1] = 1.0

    for i in range(2, N+1):
        alfa[i] = h[i-1]
        beta[i] = 2*(h[i-1]+h[i])
        hamma[i] = h[i]
        delta[i] = 3*(((y[i]-y[i-1])/h[i])-((y[i-1]-y[i-2])/h[i-1]))

    hamma[N] = 0.0
    A[1] = -hamma[1] / beta[1]
    B[1] = delta[1] / beta[1]

    for i in range(2, N):
        A[i] = -hamma[i] / (alfa[i]*A[i-1] + beta[i])
        B[i] = (delta[i] - alfa[i]*B[i-1]) / (alfa[i]*A[i-1] + beta[i])

    c[N] = (delta[N] - alfa[N]*B[N-1]) / (alfa[N]*A[N-1] + beta[N])

    for i in range(N, 1, -1):
        c[i-1] = A[i-1]*c[i] + B[i-1]

    return c


def main():
    with open("input.txt", "r") as fdata:
        N = 0
        for line in fdata:
            N += 1
        N = N - 1

        x, y, xm, ym, h, a, b, c, d = [0.0] * (N+1), [0.0] * (N+1), [0.0] * (20*N+1), [0.0] * (
            20*N+1), [0.0] * (N+1), [0.0] * (N+1), [0.0] * (N+1), [0.0] * (N+1), [0.0] * (N+1)
        x0 = 0.0

        fdata.seek(0)
        for i, line in enumerate(fdata):
            j, x[i], y[i], h[i] = map(float, line.strip().split())

        x0 = x[0]
        hh = h[0]
        c = progonka(y, h)

        for i in range(1, N):
            a[i] = y[i-1]
            b[i] = (y[i] - y[i-1]) / h[i] - (h[i] / 3) * (c[i+1] + 2*c[i])
            d[i] = (c[i+1] - c[i]) / (3*h[i])

        a[N] = y[N-1]
        b[N] = (y[N] - y[N-1]) / h[N] - (2.0/3.0) * h[N] * c[N]
        d[N] = -c[N] / (3*h[N])

        with open("output.txt", "w") as foutput:
            hh /= 20.0

            for i in range(20*N+1):
                xm[i] = x0 + i*hh
                ym[i] = f(xm[i])

            s, eps = 0, 0
            j = 1

            for i in range(20*(N-1)+1):
                s = a[j] + b[j]*(xm[i] - x[j-1]) + c[j] * \
                    (xm[i] - x[j-1])**2 + d[j]*(xm[i] - x[j-1])**3
                eps = abs(s - ym[i])
                foutput.write(f"[{i},{j}]\t{xm[i]}\t{ym[i]}\t{s}\t{eps}\n")

                if i != 0 and i % 20 == 0:
                    j += 1


def read_data(filename):
    x, y = [], []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            x.append(float(data[1]))
            y.append(float(data[2]))
    return x, y


def plot_graph(x, y, label):
    plt.plot(x, y, label=label)


if __name__ == "__main__":
    main()

    # Зчитування даних з файлів
    x_input, y_input = read_data('input.txt')
    x_output, y_output = read_data('output.txt')

    # Побудова графіків
    plot_graph(x_input, y_input, 'Input')
    plot_graph(x_output, y_output, 'Output')

    # Додаткові параметри для відображення графіків
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()
