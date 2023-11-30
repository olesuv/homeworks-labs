import math

def f(x, y):
    return y + x * x

def fe(x):
    return -x * x - 2.0 * x + 2.0 * math.exp(x) - 2.0

def adams_bashforth_methods():
    kmax = 100
    a, b, yiv, h = 0, 1, 0, 0.01
    output = open("output_fc.txt", "w")

    x0, y0 = a, yiv
    eps = 1e-6
    epse = abs(fe(x0) - y0)
    eps_fc = 0.0
    output.write(f"{x0}\t{fe(x0)}\t{y0}\t{epse}\t{eps_fc}\n")

    x1 = x0 + h
    k1 = f(x0, y0)
    k2 = f(x0 + h * 0.5, y0 + h * k1 * 0.5)
    k3 = f(x0 + h * 0.5, y0 + h * k2 * 0.5)
    k4 = f(x0 + h, y0 + h * k3)
    y1 = y0 + h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    epse = abs(fe(x1) - y1)
    eps_fc = 0.0
    output.write(f"{x1}\t{fe(x1)}\t{y1}\t{epse}\t{eps_fc}\n")

    x2, y2 = x1, y1
    x1, y1 = x0, y0
    y1f, y1c = y0, y0
    y2f, y2c = 0, 0  # Initialize y2f and y2c

    while x2 <= b:
        x0, y0 = x1, y1
        x1, y1 = x2, y2
        y1f, y1c = y2f, y2c
        x2 = x1 + h
        y2f = y1 + h / 2.0 * (3.0 * f(x1, y1) - f(x0, y0))
        y2m = y2f + 5.0 / 6.0 * (y1c - y1f)
        yi1 = y2m
        k = 0

        while True:
            yi0 = yi1
            yi1 = y1 + h / 2.0 * (f(x2, yi0) + f(x1, y1))
            k += 1

            if k >= kmax:
                output.write(f"\n max iterations {k}\n")
                break

            if abs(yi1 - yi0) < eps:
                break

        y2c = yi1
        y2 = y2c - h / 6.0 * (y2c - y2f)

        if x2 >= b:
            break

        epse = abs(fe(x2) - y2)
        eps_fc = abs(y2c - y2f)
        output.write(f"{x2}\t{fe(x2)}\t{y2}\t{epse}\t{eps_fc}\t{k}\n")

    output.close()


def automatic_step():
    kmax = 100
    a, b, yiv, h = 0, 1, 0, 0.01
    output = open("output_h.txt", "w")

    x0, y0 = a, yiv
    eps = 1e-10
    epse = abs(fe(x0) - y0)
    eps_fc = 0.0
    output.write(f"{x0}\t{fe(x0)}\t{y0}\t{epse}\t{eps_fc}\t{h}\n")

    x1 = x0 + h
    k1 = f(x0, y0)
    k2 = f(x0 + h * 0.5, y0 + h * k1 * 0.5)
    k3 = f(x0 + h * 0.5, y0 + h * k2 * 0.5)
    k4 = f(x0 + h, y0 + h * k3)
    y1 = y0 + h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    epse = abs(fe(x1) - y1)
    eps_fc = 0.0
    output.write(f"{x1}\t{fe(x1)}\t{y1}\t{epse}\t{eps_fc}\t{h}\n")

    x2, y2 = x1, y1
    x1, y1 = x0, y0
    y1f, y1c = y0, y0

    while x1 <= b:
        while eps_fc <= eps and eps_fc >= eps / 10.0:
            x0, y0 = x1, y1
            x1, y1 = x2, y2
            y1f, y1c = y2f, y2c
            x2 = x1 + h
            y2f = y1 + h / 2.0 * (3.0 * f(x1, y1) - f(x0, y0))
            y2m = y2f + 5.0 / 6.0 * (y1c - y1f)
            yi1 = y2m
            k = 0

            while True:
                yi0 = yi1
                yi1 = y1 + h / 2.0 * (f(x2, yi0) + f(x1, y1))
                k += 1

                if k >= kmax:
                    output.write(f"\n max iterations {k}\n")
                    break

                if abs(yi1 - yi0) < eps:
                    break

            y2c = yi1
            y2 = y2c - h / 6.0 * (y2c - y2f)

            if x2 >= b:
                break

            epse = abs(fe(x2) - y2)
            eps_fc = abs(y2c - y2f)
            output.write(f"{x2}\t{fe(x2)}\t{y2}\t{epse}\t{eps_fc}\t{h}\t{k}\n")

        if eps_fc > eps:
            h = h / 2.0
            x1 = x0 + h
            k1 = f(x0, y0)
            k2 = f(x0 + h * 0.5, y0 + h * k1 * 0.5)
            k3 = f(x0 + h * 0.5, y0 + h * k2 * 0.5)
            k4 = f(x0 + h, y0 + h * k3)
            y1 = y0 + h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            x2 = x1
            y2 = y1
            x1 = x0
            y1 = y0
            y1f = y0
            y1c = y0

        if eps_fc < eps / 10:
            h = h * 2.0
            x1 = x0 + h
            k1 = f(x0, y0)
            k2 = f(x0 + h * 0.5, y0 + h * k1 * 0.5)
            k3 = f(x0 + h * 0.5, y0 + h * k2 * 0.5)
            k4 = f(x0 + h, y0 + h * k3)
            y1 = y0 + h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            x2 = x1
            y2 = y1
            x1 = x0
            y1 = y0
            y1f = y0
            y1c = y0

    output.close()

def main():
    adams_bashforth_methods()
    automatic_step()

if __name__ == "__main__":
    main()