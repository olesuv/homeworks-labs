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


people = ["Анна", "Борис", "Віктор", "Галина"]
Q_other = np.array([[1, 0.6, 0.2, 0.8],
                   [0.6, 1, 0.4, 0.7],
                   [0.2, 0.4, 1, 0.5],
                   [0.8, 0.7, 0.5, 1]])

# Бінарне транзитивне замикання для людей
transitive_Q_other = transitive_closure(Q_other)

print("Транзитивне замикання для іншої сукупності:")
print(transitive_Q_other)

# Побудова графіку для бінарного нечіткого відношення Q_other
plt.figure(figsize=(8, 6))
plt.imshow(Q_other, cmap='Blues', interpolation='none')
plt.colorbar()
plt.title("Бінарне нечітке відношення Q_other")
plt.show()

# Побудова графіку для транзитивного замикання для іншої сукупності
plt.figure(figsize=(8, 6))
plt.imshow(transitive_Q_other, cmap='Blues', interpolation='none')
plt.colorbar()
plt.title("Транзитивне замикання для іншої сукупності")
plt.show()