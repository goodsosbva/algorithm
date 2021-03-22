import itertools
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n + 1), k))


combi = combine(5, 3)
print(combi)
