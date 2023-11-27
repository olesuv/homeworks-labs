import numpy as np

def addition_triangle(A, B):
    result = np.maximum(A, B)
    return result

def subtraction_triangle(A, B):
    result = np.maximum(A, 1 - B)
    return result

def multiplication_triangle(A, B):
    result = np.convolve(A, B, mode='same')
    return result

def division_triangle(A, B):
    result = np.zeros_like(A)
    for i in range(len(A)):
        if B[i] != 0:
            result[i] = A[i] / B[i]
    return result

def addition_trapezoidal(A, B):
    result = np.maximum(A, B)
    return result

def subtraction_trapezoidal(A, B):
    result = np.maximum(A, 1 - B)
    return result

def multiplication_trapezoidal(A, B):
    result = np.convolve(A, B, mode='same')
    return result

def division_trapezoidal(A, B):
    result = np.zeros_like(A)
    for i in range(len(A)):
        if B[i] != 0:
            result[i] = A[i] / B[i]
    return result

AT = np.array([12, 2, 3])
BT = np.array([4, 0.5, 1])
CT = np.array([8, 2, 1])

result1 = multiplication_triangle(AT, BT)
result2 = multiplication_triangle(CT, BT)
result3 = addition_triangle(result1, result2)
result4 = subtraction_triangle(result3, AT)

print("Результат виразу (АТ·ВТ)+(СТ·ВТ)-АТ:")
print(result4)

def max_min_operation(A, B, C, D):
    min_AB = np.minimum(A, B)
    min_CD = np.minimum(C, D)
    result = np.maximum(min_AB, min_CD)
    return result

AT = np.array([10, 15, 2, 3])
BT = np.array([14, 20, 2, 1])
CT = np.array([5, 8, 0.5, 1])
DT = np.array([18, 22, 2, 2])

result = max_min_operation(AT, BT, CT, DT)

print("Результат порівняння трапецеподібних інтервалів:")
print(result)
