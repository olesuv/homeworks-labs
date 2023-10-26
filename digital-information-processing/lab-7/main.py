import matplotlib.pyplot as plt
import numpy as np
import timeit


def W(k, N, n=1):
    return np.exp(-2 * np.pi * 1j * k * n / N)


def dft2(x):
    N = len(x)

    if N % 2 > 0:
        raise ValueError("Pair count only should be")

    x1 = x[::2]
    x2 = x[1::2]

    return [x1[k] + W(k, N) * x2[k] for k in range(N/2)]


x2 = x[:500]

t1 = timeit.timeit('dft(2x)', setup='from __main__ import dft, x2', number=1)
print(t1)

t2 = timeit.timeit('dft(x2)', setup="from __main__ import dft2, x2", number=1)
print(t2)


X = dft2(x)

# Compute the magnitude and phase of X.
A = np.abs(X)
P = np.angle(X)

# Get the number of samples in x.
N = len(x)

# Compute the normalized frequencies.
nu = np.arange(N) / N * 1 / N

# Compute the period of the signal.
T = 1 / nu

# Plot the magnitude and phase of X.
plt.subplot(2, 1, 1)
plt.semilogy(T[0:N // 2], A[0:N // 2])
plt.xlim([0, 100])
plt.xticks(np.arange(0, 100, step=10))
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(T[0:N // 2], P[0:N // 2])
plt.xlim([0, 100])
plt.xticks(np.arange(0, 100, step=10))
plt.grid()

plt.show()
