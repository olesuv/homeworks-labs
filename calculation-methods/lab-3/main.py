import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x)


def fact(k):
    if k == 0 or k == 1:
        return 1
    return k * fact(k - 1)


def Cnk(n, k):
    return fact(n) / (fact(k) * fact(n - k))


def step(n):
    return -1 if n % 2 else 1


def deltaf(n, f_vals):
    r = 0
    for k in range(n + 1):
        r += f_vals[k] * step(n - k) * Cnk(n, k)
    return r


def factmn(t, k):
    mn = 1
    if k != 0:
        for i in range(k):
            mn *= (t - i)
    return mn


def fappr(n, t, f_vals):
    res = 0
    for k in range(n + 1):
        res += deltaf(k, f_vals) * factmn(t, k) / fact(k)
    return res


def Eps(appr, in_val):
    return abs(appr - in_val)


def main():
    a = 0
    b = 1
    n_values = [10, 15, 20]  # Different values of n

    for n in n_values:
        h = (b - a) / n

        # Write data to in.txt
        with open(f"in_{n}.txt", "w") as file1:
            for i in range(n + 1):
                x = a + i * h
                y = f(x)
                file1.write(f"{x} \t {y}\n")

        # Read data from in.txt
        x_vals, f_vals = [], []
        with open(f"in_{n}.txt", "r") as file1:
            for line in file1:
                x_val, f_val = map(float, line.split())
                x_vals.append(x_val)
                f_vals.append(f_val)

        # Calculate and write data to fappr_n.txt and R_n.txt
        with open(f"fappr_{n}.txt", "w") as file2, open(f"R_{n}.txt", "w") as file3:
            t = 0
            ht = (n - 0.0) / (20.0 * n)
            for _ in range(20 * n + 1):
                file2.write(f"{t} \t {fappr(n, t, f_vals)}\n")
                file3.write(f"{t} \t {Eps(f(t), fappr(n, t, f_vals))}\n")
                t += ht

    # Plotting
    plt.figure(figsize=(15, 5))

    for n in n_values:
        # Plot data from fappr_n.txt
        fappr_x, fappr_y = [], []
        with open(f"fappr_{n}.txt", "r") as file2:
            for line in file2:
                x_val, y_val = map(float, line.split())
                fappr_x.append(x_val)
                fappr_y.append(y_val)
        plt.subplot(1, len(n_values), n_values.index(n) + 1)
        plt.title(f'Data for n = {n}')
        plt.plot(fappr_x, fappr_y, label=f'fappr(x) n={n}')
        plt.xlabel('x')
        plt.ylabel('fappr(x)')
        plt.legend()

        # Plot data from R_n.txt
        R_x, R_y = [], []
        with open(f"R_{n}.txt", "r") as file3:
            for line in file3:
                x_val, y_val = map(float, line.split())
                R_x.append(x_val)
                R_y.append(y_val)
        plt.plot(R_x, R_y, label=f'Eps(x) n={n}')
        plt.xlabel('x')
        plt.ylabel('Eps(x)')
        plt.legend()

    # Show all plots
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
