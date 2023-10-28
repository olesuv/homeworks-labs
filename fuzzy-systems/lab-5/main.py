import numpy as np
import matplotlib.pyplot as plt

# Задане бінарне нечітке відношення Q (приклад)
Q = np.array([[1, 0.7, 0.3],
              [0.7, 1, 0.5],
              [0.3, 0.5, 1]])

def transitive_closure(Q):
    n = Q.shape[0]
    result = np.copy(Q)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                result[i, j] = max(result[i, j], min(result[i, k], result[k, j]))
    return result

# Знаходимо транзитивне замикання
transitive_Q = transitive_closure(Q)

# Виводимо транзитивне замикання
print("Транзитивне замикання:")
print(transitive_Q)

# Побудова графіку для заданого бінарного нечіткого відношення Q
plt.figure(figsize=(8, 6))
plt.imshow(Q, cmap='Blues', interpolation='none')
plt.colorbar()
plt.title("Бінарне нечітке відношення Q")
plt.show()

# Побудова графіку для транзитивного замикання
plt.figure(figsize=(8, 6))
plt.imshow(transitive_Q, cmap='Blues', interpolation='none')
plt.colorbar()
plt.title("Транзитивне замикання")
plt.show()
