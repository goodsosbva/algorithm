import collections
import heapq
from typing import List


def findCneapestPric(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w, in flights:
        graph[u].append((v, w))

    k = 0
    Q = [(0, src, k)]

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k <= K:
            k += 1
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, w))

    return -1


n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 1

search = findCneapestPric(n, edges, src, dst, K)
print(search)
