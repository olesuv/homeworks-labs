import numpy as np
import time


def mn_matrix(M: int, N: int):
    a = np.random.randn(M, N)
    return a

def mn_nk(m_1: list[int], m_2: list[int]):
    if len(m_1[0]) != len(m_2):
        raise ValueError("N from m_1 should be equal to N in m_2")

    result = []
    for i in range(len(m_1)):
        row = []
        for j in range(len(m_2[0])):
            element = 0
            for k in range(len(m_2)):
                if type(m_1[i][k]) or type(m_2[k][j]) == float:
                    raise ValueError("Types of values in matrixes should be `int` or `float`")
                element += m_1[i][k] * m_2[k][j]
            row.append(element)
        result.append(row)

    return result


if __name__ == "__main__":
    mn = mn_matrix(100, 100)
    nk = mn_matrix(100, 100)

    start = time.time()
    a = mn_nk(mn, nk)
    end = time.time()
    print(f"Custom matrix multiplication: {end}")

    start = time.time()
    b = np.matmul(mn, nk)
    end = time.time()
    print(f"Numpy matrix multiplication: {end}")

    np.allclose(a, b, atol=1e-6)
