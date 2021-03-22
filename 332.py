import collections
from typing import List


def findIitinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        print(a, b)
        graph[a].append(b)
    print(graph)
    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('jfk')
    # 다시 뒤지업 어휘 순 결고로
    return route[::-1]


# rou = findIitinerary([["jfk", "sfo"], ["jfk", "atl"], ["sfo", "atl"], ["atl", "jfk"], ["atl", "sfo"]])
# print(rou)
rou1 = findIitinerary([["mvc", "lhr"], ["jfk", "mvc"], ["sfo", "sjc"], ["lhr", "sfo"]])
print(rou1)