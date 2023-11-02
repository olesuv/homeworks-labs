import math


def f(x):
    return math.sin(x)


def fp(x):
    return math.cos(x)


def fn(x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


def eps1(x, h):
    return abs(fn(x, h) - fp(x))


def eps2(x, h):
    return abs(fp(x) - (fn(x, h) + (fn(x, h) - fn(x, 2.0 * h)) / 3.0))


def eps3(x, h):
    return abs(fp(x) - (fn(x, 2.0 * h) * fn(x, 2.0 * h) - fn(x, h) * fn(x, 4 * h)) /
               (2.0 * fn(x, 2.0 * h) - (fn(x, h) + fn(x, 4.0 * h))))


def p(x, h):
    return 1 / math.log(2) * math.log((fn(x, 4.0 * h) - fn(x, 2.0 * h)) / (fn(x, 2.0 * h) - fn(x, h)))


x0 = 0.56
yp0 = 0.0
h = 1e-4
h0 = h1 = R0 = R1 = R2 = R3 = 0
min_error = 10.0


def func(x):
    return math.sin(x)


a = 0.1
b = 1.1
n = 50
h = (b - a) / n

with open("in.txt", "w") as output:
    for i in range(n + 1):
        x = a + i * h
        y = func(x)
        output.write(f"{x} \t {y}\n")

print("File 'in.txt' generated.")

with open("output.txt", "w") as fdata:
    for i in range(20, -4, -1):
        h = 10**(-i)
        fdata.write(f"{h}\t{eps1(x0, h)}\n")
        if eps1(x0, h) < min_error:
            min_error = eps1(x0, h)
            h0 = h

    por = int(math.log10(h0))
    hh = 10**por

    for i in range(1, abs(por - 1) + 1):
        hh /= 10.0

    for h in [hh * i for i in range(1, 101)]:
        fdata.write(f"{h}\t{eps1(x0, h)}\n")
        if eps1(x0, h) < min_error:
            min_error = eps1(x0, h)
            h0 = h

    yp0 = fp(x0)
    h1 = 1e-3
    R0 = eps1(x0, h0)
    R1 = eps1(x0, h1)
    R2 = eps2(x0, h1)
    R3 = eps3(x0, h1)
    pmet = p(x0, h1)

    fdata.write(f"yp0={yp0}\n")
    fdata.write(f"h0={h0}\n")
    fdata.write(f"h1={h1}\n")
    fdata.write(f"R0={R0}\n")
    fdata.write(f"R1={R1}\n")
    fdata.write(f"R2={R2}\n")
    fdata.write(f"R3={R3}\n")
    fdata.write(f"p={pmet}\n")

print("File 'output.txt' generated.")

h_values = []
eps_values = []

with open("output.txt", "r") as f:
    for line in f:
        if not line.startswith(('yp0=', 'h0=', 'h1=', 'R0=', 'R1=', 'R2=', 'R3=', 'p=')):
            h, eps = map(float, line.split())
            h_values.append(h)
            eps_values.append(eps)
