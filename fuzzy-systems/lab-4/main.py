import numpy as np

def fuzzy_composition(relation1, relation2):
    if len(relation1[0]) != len(relation2):
        raise ValueError("Неможливо виконати композицію: розміри відношень не підходять")

    result = np.zeros((len(relation1), len(relation2[0])))

    for i in range(len(relation1)):
        for j in range(len(relation2[0])):
            max_min = max(min(relation1[i][k], relation2[k][j]) for k in range(len(relation2)))
            result[i][j] = max_min

    return result

# Введення матриць MS і MQ
MS = np.array([
    [0.8, 0.2, 0.1, 0.7, 0.6, 0.3, 0.9],
    [0.3, 0.9, 0.7, 0.4, 0.5, 0.8, 0.2],
    [0.2, 0.3, 0.8, 0.5, 0.1, 0.4, 0.6],
    [0.6, 0.5, 0.4, 0.9, 0.7, 0.2, 0.8]
])

MQ = np.array([
    [0.9, 0.3, 0.2, 0.8, 0.6, 0.7],
    [0.2, 0.8, 0.6, 0.4, 0.3, 0.9],
    [0.7, 0.4, 0.9, 0.5, 0.2, 0.1],
    [0.5, 0.6, 0.3, 0.7, 0.8, 0.4],
    [0.8, 0.2, 0.7, 0.1, 0.4, 0.5],
    [0.3, 0.7, 0.5, 0.9, 0.6, 0.8],
    [0.6, 0.9, 0.1, 0.2, 0.7, 0.3]
])

# Виклик функції для композиції
result = fuzzy_composition(MS, MQ)
print(result)
