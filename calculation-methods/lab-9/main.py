import math

def f(x):
    return math.cos(x)

def fp1(x):
    return -math.sin(x)

def fp2(x):
    return -math.cos(x)

def power(x, n):
    mult = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        mult *= x
    return mult

def Simple_Iteration(kmax, eps, x0):
    print("\nMethod simple iteration")
    x1 = x0
    tau = -1.0 / fp1(x0)
    k = 0
    while True:
        x0 = x1
        x1 = x0 + tau * f(x0)
        k += 1
        if k > kmax or (abs(x1 - x0) <= eps) or (abs(f(x1)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x1}")
        print(f"With iteration {k}")

def Method_Newton(kmax, eps, x0):
    print("\nMethod Newton")
    x1 = x0
    k = 0
    while True:
        x0 = x1
        x1 = x0 - f(x0) / fp1(x0)
        k += 1
        if k > kmax or (abs(x1 - x0) <= eps) or (abs(f(x1)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x1}")
        print(f"With iteration {k}")

def Method_Chebysheva(kmax, eps, x0):
    print("\nMethod Chebusheva")
    x1 = x0
    k = 0
    while True:
        x0 = x1
        x1 = x0 - f(x0) / fp1(x0) - 0.5 * power(f(x0), 2) * fp2(x0) / power(fp1(x0), 3)
        k += 1
        if k > kmax or (abs(x1 - x0) <= eps) or (abs(f(x1)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x1}")
        print(f"With iteration {k}")

def Method_Hord(kmax, eps, x0):
    print("\nMethod Hord")
    tau = -1.0 / fp1(x0)
    x1 = x0 + tau * f(x0)
    x2 = x1
    x1 = x0
    k = 0
    while True:
        x0 = x1
        x1 = x2
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        k += 1
        if k > kmax or (abs(x2 - x1) <= eps) or (abs(f(x2)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x2}")
        print(f"With iteration {k}")

def rr(x0, x1):
    return (f(x1) - f(x0)) / (x1 - x0)

def delta(x1, x2, root, rr1, rr2, ind):
    if ind == 0:
        return (-(x2 - x1) * rr2 + rr1 + root) / (2 * rr2)
    if ind == 1:
        return (-(x2 - x1) * rr2 + rr1 - root) / (2 * rr2)

def Method_Parabol(kmax, eps, x0):
    print("\nMethod Parabol")
    tau = -1.0 / fp1(x0)
    x1 = x0 + tau * f(x0)
    x2 = x1 + tau * f(x1)
    x3 = x2
    x2 = x1
    x1 = x0
    k = 0
    while True:
        x0 = x1
        x1 = x2
        x2 = x3
        rr1 = rr(x1, x2)
        rr2 = (rr(x1, x2) - rr(x0, x1)) / (x2 - x0)
        root = math.sqrt(power((x2 - x1) * rr2 + rr1, 2) - 4 * rr2 * f(x2))
        delta1 = delta(x1, x2, root, rr1, rr2, 0)
        delta2 = delta(x1, x2, root, rr1, rr2, 1)
        if abs(delta1) < abs(delta2):
            delta0 = delta1
        else:
            delta0 = delta2
        x3 = x2 + delta0
        k += 1
        if k > kmax or (abs(x3 - x2) <= eps) or (abs(f(x3)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x3}")
        print(f"With iteration {k}")

def Method_Reverse_Interpolation(kmax, eps, x0):
    print("\nMethod Reverse Interpolation")
    tau = -1.0 / fp1(x0)
    x1 = x0 + tau * f(x0)
    x2 = x1
    x1 = x0
    k = 0
    while True:
        x0 = x1
        x1 = x2
        x2 = -x0 * f(x1) / (f(x0) - f(x1)) - x1 * f(x0) / (f(x1) - f(x0))
        k += 1
        if k > kmax or (abs(x2 - x1) <= eps) or (abs(f(x2)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x2}")
        print(f"With iteration {k}")

def Method_Eitkena(kmax, eps, x0):
    print("\nMethod Eitkena")
    tau = -1.0 / fp1(x0)
    x3 = x0
    k = 0
    while True:
        x0 = x3
        x1 = x0 + tau * f(x0)
        x2 = x1 + tau * f(x1)
        x3 = x2 + power(x2 - x1, 2) / (2 * x1 - x2 - x0)
        k += 1
        if k > kmax or (abs(x3 - x2) <= eps) or (abs(f(x3)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x3}")
        print(f"With iteration {k}")


def read_m():
    with open("input_A.txt", "r") as input_A:
        M = sum(1 for line in input_A)
    return M - 1

def f_new(x, a, b, m):
    b[m] = a[m]
    for i in range(m - 1, -1, -1):
        b[i] = a[i] + x * b[i + 1]
    return b[0]

def main():
    x0, x1, x2, x3 = 5, 0, 0, 0
    eps = 1e-10
    k_max = int(1e4)
    
    Simple_Iteration(k_max, eps, x0)
    
    Method_Newton(k_max, eps, x0)
    
    Method_Chebysheva(k_max, eps, x0)
    
    Method_Hord(k_max, eps, x0)
    
    Method_Parabol(k_max, eps, x0)
    
    Method_Reverse_Interpolation(k_max, eps, x0)
    
    Method_Eitkena(k_max, eps, x0)

    with open("input_A.txt", "r") as input_A:
        a = [float(line) for line in input_A]

    m = len(a) - 1
    print(f"\nM: {m}")

    x0 = 2.51
    x1 = x0
    eps = 1e-12
    kmax = 1e4
    alpha0 = 1.0
    beta0 = 1.0
    alpha1, beta1 = 0.0, 0.0
    p0, q0, p1, q1 = 0.0, 0.0, 0.0, 0.0

    b = [0.0] * (m + 1)
    c = [0.0] * (m + 1)

    print("\nMethod Newton_Gornera\n")
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
        if k > kmax or (abs(x1 - x0) <= eps) or (abs(f_new(x0, a, b, m)) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {x1}")
        print(f"With iteration {k}")

    print("\nMethod Lina\n")
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
        if k > kmax or (abs(alpha1 - alpha0) <= eps) or (abs(beta1 - beta0) <= eps):
            break

    if k > kmax:
        print("Solution not found")
    else:
        print(f"Solution = {alpha1}\t{beta1}")
        print(f"With iteration {k}")


if __name__ == "__main__":
    main()
