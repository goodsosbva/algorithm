# 행렬
import numpy as np


def fib(n):
    M = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])

    return np.matmul(M ** n, vec)[0]


n = int(input())
chk = fib(n)
print(chk)
