import collections
import heapq
from typing import List


def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    graph = collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))
    # print(graph)
    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)
    # print(Q)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                # print(Q)
                heapq.heappush(Q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    # print(dist)
    if len(dist) == N:
        return max(dist.values())
    return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
cnt = networkDelayTime(times, N, K)
print(cnt)
