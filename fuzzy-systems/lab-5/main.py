import numpy as np
import matplotlib.pyplot as plt


# def transitive_closure(M):
#     n = len(M)
#     W = np.copy(M)

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 W[i][j] = W[i][j] or (W[i][k] and W[k][j])

#     return W

def transitive_closure(Q):
    n = Q.shape[0]

    R = Q.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i, j] = max(R[i, j], min(R[i, k], R[k, j]))

    return R


people = ["Анна", "Борис", "Віктор", "Галина"]

Q = np.array([[1, 0.3, 0.2, 0.8],
              [0.3, 1, 0.4, 0.6],
              [0.2, 0.4, 1, 0.5],
              [0.8, 0.6, 0.5, 1]])

ts_q = transitive_closure(Q)

print(f"{Q} \n\n {ts_q}")

plt.figure(figsize=(8, 6))
plt.imshow(Q, cmap='Blues', interpolation='none')
plt.xticks(np.arange(len(people)), people, rotation=45)
plt.yticks(np.arange(len(people)), people)
plt.title("На скільки добре знайомі люди (0-1)")
plt.colorbar()
plt.show()


plt.figure(figsize=(8, 6))
plt.imshow(ts_q, cmap='Blues', interpolation='none')
plt.xticks(np.arange(len(people)), people, rotation=45)
plt.yticks(np.arange(len(people)), people)
plt.title("Транзитивне замикання для людей")
plt.colorbar()
plt.show()
