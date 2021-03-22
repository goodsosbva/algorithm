from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    res = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            res.append(elements[:])

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return res

cnt = combine(5, 3)
print(cnt)


