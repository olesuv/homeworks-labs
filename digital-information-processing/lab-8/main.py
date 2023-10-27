import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 4))

Ns = 1024
Nlo = 0
Nhi = Ns
dt = 1

t = np.arange(0.0, dt * Ns, dt)
A = np.sin(2.0 * np.pi * t / 150)
B = np.sin(2.0 * np.pi * t / 50)
A[512:768] += B[0:256]
x = A[:]
plt.plot(t, x)
plt.xlim([0, Ns])
plt.show()

plt.figure(figsize=(15, 7))

def morlet(x, w0 = 6.0):
    return np.pi ** -0.25 * np.exp(1j * w0 * x) * np.exp(-0.5  * x ** 2)

m_x = np.linspace(-2 * np.pi, 2 * np.pi, 1024)
m = morlet(m_x)

plt.plot(m_x, np.real(m), label="Re")
plt.plot(m_x, np.imag(m), label="Lm")
_ = plt.legend()
plt.show()

def conj(a):
    return np.real(a) - 1j * np.imag(a)

n = np.arange(Nlo, Nhi)
s = np.array([1, 50, 100, 200])
w0 = 6
fwl = 4 * np.pi / (w0 + np.sqrt(2.0 + w0 ** 2))
sf = s / fwl
W = np.zeros([len(s), len(n)], dtype=np.complex_(64))

for i in range(len(s)):
    for j in range(len(n)):
        for n_ in range(Ns):
            W[i, j] = W[i, j] + x[n_] * conj(morlet((n_ - n[j]) * dt / sf[i], w0=w0))

plt.rcParams["figure.figsize"] = (15, 4)
im = plt.imshow(np.abs(W),
               cmap=plt.cm.jet,
               extent=[n[0], n[-1], s[-1], s[0]],
               aspect='auto',
               interpolation="nearest")
plt.ylim(s[0], s[-1])
_ = plt.yticks(s)
plt.show()
