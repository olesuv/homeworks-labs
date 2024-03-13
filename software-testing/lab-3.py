import numpy as np


def mn_nk(m_1: list[int], m_2: list[int]):
    if len(m_1[0]) != len(m_2):
        raise ValueError("N from m_1 should be equal to N in m_2")

    result = []
    for i in range(len(m_1)):
        row = []
        for j in range(len(m_2[0])):
            element = 0
            for k in range(len(m_2)):
                element += m_1[i][k] * m_2[k][j]
            row.append(element)
        result.append(row)

    return result


if __name__ == "__main__":
    pass

