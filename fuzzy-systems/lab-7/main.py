import numpy as np


AT = np.array([12, 2, 3])
BT = np.array([4, 0.5, 1])
CT = np.array([8, 2, 1])

result1 = np.multiply(AT, BT) + np.subtract(np.multiply(CT, BT), AT)
print("Результат виразу (АТ·ВТ)+(СТ·ВТ)-АТ: ", result1)

AT = np.array([10, 15, 2, 3])
BT = np.array([14, 20, 2, 1])
CT = np.array([5, 8, 0.5, 1])
DT = np.array([18, 22, 2, 2])

def extended_maximum(AT, BT, CT):
    a = np.maximum(AT[0], AT[1])
    b = np.maximum(BT[0], BT[1])
    alpha = a - np.maximum(AT[0] - AT[2], AT[1] - AT[2])
    beta = np.maximum(BT[0] + CT[0] - BT[2], BT[1] + CT[1] - BT[2]) - b
    result = np.array([a, b, alpha, beta])
    return result

def extended_minimum(AT, BT, CT):
    a = np.minimum(AT[0], AT[1])
    b = np.minimum(BT[0], BT[1])
    alpha = a - np.minimum(AT[0] - AT[2], AT[1] - AT[2])
    beta = np.minimum(BT[0] + CT[0] - BT[2], BT[1] + CT[1] - BT[2]) - b
    result = np.array([a, b, alpha, beta])
    return result

result2 = np.maximum(extended_minimum(AT, BT, CT), extended_minimum(CT, BT, CT))
print("Результат виразу max{min{АТ,ВТ},min{СТ,ВТ}}: ", result2)