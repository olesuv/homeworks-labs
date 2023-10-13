import numpy as np
import matplotlib.pyplot as plt


def dft(x, inv=False):
    X = np.empty_like(x, dtype=np.complex128)
    N = len(x)

    for k in range(N):
        for n in range(N):
            omega = 2 * np.pi * k * n / N
            if inv:
                omega = -omega
            S = X[k] + (np.cos(omega) + np.sin(omega) * 1j) * x[n]
            X[k] = S

    if inv:
        X = X / N

    return X


plt.rcParams["figure.figsize"] = (15, 7)

omega = 2 * np.pi
dt = 0.7
t = np.arange(0, 480, dt)
x = np.cos(t * omega / 10 + 1) + np.cos(t * omega / 40 + np.pi / 2)
N = len(x)
X = dft(x)
nu = np.arange(N) / dt / N
np.seterr(divide="ignore")
T = 1 / nu


# Create a figure with 3 subplots.
fig, axes = plt.subplots(3, 1, figsize=(10, 10))

# Plot the first subplot.
t = np.linspace(0, 10, 100)
x = np.sin(2 * np.pi * t)
axes[0].plot(t, x)
axes[0].set_title('First subplot')

# Plot the second subplot.
X = np.fft.fft(x)
N = len(x)
T = np.linspace(0, N / 2, N // 2)
f = T / N
axes[1].plot(f, np.abs(X[:N // 2]))
axes[1].set_title('Second subplot')

# Plot the third subplot.
P = np.real(X[:N // 2])**2 + np.imag(X[:N // 2])**2
axes[2].plot(f, P)
axes[2].set_title('Third subplot')

# Show the figure.
plt.tight_layout()
plt.show()
