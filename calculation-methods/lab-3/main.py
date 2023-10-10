import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x)


def fact(k):
    if k == 0 or k == 1:
        return 1
    return k * fact(k-1)


def Cnk(n, k):
    return fact(n) / (fact(k) * fact(n - k))


def step(n):
    if n % 2:
        return -1
    else:
        return 1


def deltaf(n, f):
    r = 0
    for k in range(n+1):
        r += f[k]*step(n-k)*Cnk(n, k)
    return r


def factmn(t, k):
    mn = 1
    if k == 0:
        mn = 1
    else:
        for i in range(k):
            mn *= (t - i)
    return mn


def fappr(n, t, f):
    res = 0
    for k in range(n+1):
        res += deltaf(k, f) * factmn(t, k) / fact(k)
    return res


def Eps(appr, in_val):
    return abs(appr - in_val)


def generate_files(n):
    a = 0
    b = 1.0
    h = (b - a) / n

    x = [a + i*h for i in range(n+1)]
    f_values = [f(val) for val in x]

    with open(f"in_{n}.txt", "wt") as file1:
        for i in range(n+1):
            x_i = a + i*h
            y_i = f(x_i)
            print(f"{x_i} \t {y_i}", file=file1)

    with open(f"fappr_{n}.txt", "w") as file2, open(f"R_{n}.txt", "w") as file3:
        t = 0
        ht = (n - 0.0) / (20.0 * n)
        for j in range(20 * n + 1):
            f_appr_val = fappr(n, t, f_values)
            func_val = f(a + h*t)
            eps_val = Eps(func_val, f_appr_val)

            print(f"{t} \t {f_appr_val}", file=file2)
            print(f"{t} \t {eps_val}", file=file3)

            t += ht


def plot_files(file_names, titles):
    for file_name, title in zip(file_names, titles):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            x = [float(line.split()[0]) for line in lines]
            y = [float(line.split()[1]) for line in lines]

            plt.plot(x, y, label=title)


def main():
    n_values = [10, 15, 20]
    in_files = [f'in_{n}.txt' for n in n_values]
    fappr_files = [f'fappr_{n}.txt' for n in n_values]
    R_files = [f'R_{n}.txt' for n in n_values]

    in_titles = [f'Input for n={n}' for n in n_values]
    fappr_titles = [f'Approximation for n={n}' for n in n_values]
    R_titles = [f'Error for n={n}' for n in n_values]

    generate_files(20)

    plt.figure(figsize=(10, 6))

    # Plotting input files
    plt.subplot(3, 1, 1)
    plot_files(in_files, in_titles)
    plt.legend()

    # Plotting approximation files
    plt.subplot(3, 1, 2)
    plot_files(fappr_files, fappr_titles)
    plt.legend()

    # Plotting error files
    plt.subplot(3, 1, 3)
    plot_files(R_files, R_titles)
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
