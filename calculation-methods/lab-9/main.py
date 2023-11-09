import math
import matplotlib.pyplot as plt


def read_m():
    with open("input_A.txt", "r") as input_A:
        M = 0
        for line in input_A:
            M += 1
        return M - 1

def power(x, n):
    mult = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        mult *= x
    return mult

def f(x, a, b, m):
    b[m] = a[m]
    for i in range(m - 1, -1, -1):
        b[i] = a[i] + x * b[i + 1]
    return b[0]

def main():
    input_A = open("input_A.txt", "r")
    output = open("output_alg.txt", "w")
    
    x0 = 2.51
    eps = 1e-12
    kmax = 1e+4
    
    alpha0 = 1.0
    beta0 = 1.0
    
    alpha1, beta1 = alpha0, beta0
    p0, q0, p1, q1 = 0, 0, 0, 0
    
    m = read_m()
    
    print(m)
    
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    c = [0] * (m + 1)
    
    for j in range(m + 1):
        a[j] = float(input_A.readline())
    
    print("\nMethod Newton_Gornera")
    x1 = x0
    k = 0
    while True:
        x0 = x1
        b[m] = a[m]
        for i in range(m - 1, -1, -1):
            b[i] = a[i] + x0 * b[i + 1]
        c[m] = b[m]
        for i in range(m - 1, 0, -1):
            c[i] = b[i] + x0 * c[i + 1]
        x1 = x0 - b[0] / c[1]
        k += 1
        if k > kmax or abs(x1 - x0) <= eps or abs(f(x0, a, b, m)) <= eps:
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x1:.10f}")
        print(f"With iteration {k}")
    
    output.write("\nMethod Newton_Gornera\n")
    if k > kmax:
        output.write("Solution not found\n")
    else:
        output.write(f"Solution = {x1:.10f}\n")
        output.write(f"With iteration {k}\n")

    print("\nMethod Lina")
    alpha1 = alpha0
    beta1 = beta0
    k = 0
    while True:
        alpha0 = alpha1
        beta0 = beta1
        p0 = -2 * alpha0
        q0 = alpha0 * alpha0 + beta0 * beta0
        b[m] = a[m]
        b[m - 1] = a[m - 1] - p0 * b[m]
        for i in range(m - 2, 1, -1):
            b[i] = a[i] - p0 * b[i + 1] - q0 * b[i + 2]
        q1 = a[0] / b[2]
        p1 = (a[1] * b[2] - a[0] * b[3]) / (b[2] * b[2])
        alpha1 = -p1 / 2
        beta1 = math.sqrt(abs(q1 - alpha1 * alpha1))
        k += 1
        if k > kmax or abs(alpha1 - alpha0) <= eps or abs(beta1 - beta0) <= eps:
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {alpha1:.10f} {beta1:.10f}")
        print(f"With iteration {k}")

    output.write("\nMethod Lina\n")
    if k > kmax:
        output.write("Solution not found\n")
    else:
        output.write(f"Solution = {alpha1:.10f} {beta1:.10f}\n")
        output.write(f"With iteration {k}\n")

    input_A.close()
    output.close()

if __name__ == "__main__":
    main()
