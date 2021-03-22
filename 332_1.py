import collections
from typing import List


def findIitinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['jfk']
    while stack:
        print(stack)
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        print("응애! 나 아기 라우트", stack)
        route.append(stack.pop())

    # 다싣 뒤집어서 어휘 순 결과로
    print(route)
    return route[::-1]


rou = findIitinerary([["jfk", "sfo"], ["jfk", "atl"], ["sfo", "atl"], ["atl", "jfk"], ["atl", "sfo"]])
print()
print("answer:", rou)
