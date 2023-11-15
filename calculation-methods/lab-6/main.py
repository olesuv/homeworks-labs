import math
import matplotlib.pyplot as plt

a = 0
b = 10
iter = 0
eps = 1e-12


def f(x):
    return math.sin(x)


def F(x):
    return -math.cos(x)


def I(N):
    global h
    Int_N = f(a) + f(b)
    h = (b - a) / N

    for i in range(1, N):
        if (i % 2) == 0:
            Int_N += 2 * f(a + i * h)
        else:
            Int_N += 4 * f(a + i * h)

    Int_N *= h / 3
    return Int_N


def Adapt_alg(a, b):
    global h, iter, eps
    stack = [(a, b)]
    simp = 0

    while stack:
        a, b = stack.pop()
        h = (b - a) / 2

        Int1 = h / 3 * (f(a) + 4 * f(a + h) + f(b))
        Int2 = h / 6 * (f(a) + 4 * f(a + h / 2) + f(a + h)) + \
            h / 6 * (f(a + h) + 4 * f(a + (3 / 2) * h) + f(b))

        if abs(Int2 - Int1) < eps:
            simp += Int2
        else:
            iter += 1
            stack.extend([(a, a + h), (a + h, b)])

    return simp


def main():
    global a, b, iter, eps
    I0 = F(b) - F(a)

    file1 = open("inE.txt", "wt")
    file2 = open("inAdE.txt", "wt")

    N = 8
    while True:
        N += 2
        epsI = abs(I(N) - I0)
        file1.write(f"{N} {epsI}\n")

        if epsI <= 1e-10:
            break

    Nopt = N
    epsopt = abs(I(Nopt) - I0)
    file1.write(f"Nopt = {Nopt} \t epsopt = {epsopt}\n")

    N0 = Nopt // 10
    N0 -= N0 % 8
    file1.write(f"N0 = {N0}\n")

    eps0 = abs(I(N0) - I0)
    file1.write(f"eps0 = {eps0}\n")

    Ir = I(N0) + (I(N0) - I(N0 // 2)) / 15
    file1.write(f"Ir = {Ir}\n")

    epsR = abs(Ir - I0)
    file1.write(f"epsR = {epsR}\n")

    Ie = (I(N0 // 2) * I(N0 // 2) - I(N0) * I(N0 // 4)) / \
        (2 * I(N0 // 2) - (I(N0) + I(N0 // 4)))
    file1.write(f"Ie = {Ie}\n")

    p = (1 / math.log(2)) * \
        math.log(abs((I(N0 // 4) - I(N0 // 2)) / (I(N0 // 2) - I(N0))))
    file1.write(f"p = {p}\n")

    epsE = abs(Ie - I0)
    file1.write(f"epsE = {epsE}\n")

    Adapt_alg(a, b)
    file1.write(f"eps = {eps} Adapt_alg = {Adapt_alg(a, b)} iter = {iter}\n")

    for eps in [1e-12 * (1.5 ** i) for i in range(9)]:
        iter = 0
        Adapt_alg(a, b)
        file2.write(f"{eps} {iter}\n")

    file1.close()
    file2.close()

    in_e_val = read_txt("inE.txt")
    in_ad_e_val = read_txt("inAdE.txt")

    plotting(in_e_val, in_ad_e_val)


def tabulation():
    a = 0.1
    b = 1.1
    n = 50
    h = (b - a) / n

    output = open("in.txt", "wt")

    for i in range(n+1):
        x = a + i*h
        y = f(x)
        output.write(f"{x} \t {y}\n")

    output.close()

def read_txt(file_name) -> list[float]:
    inE_x_values = []
    inE_y_values = []

    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("Nopt"):
            break

        x, y = map(float, line.split())

        inE_x_values.append(x)
        inE_y_values.append(y)

    return inE_x_values, inE_y_values


def plotting(inE, inAdE) -> None:
    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    plt.plot(inE[0], inE[1])
    plt.title("Input error values")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.subplot(1, 2, 2)
    plt.plot(inAdE[0], inAdE[1])
    plt.title("Adaptive method error values")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()

if __name__ == "__main__":
    main()
