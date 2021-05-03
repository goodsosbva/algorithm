import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))
            print(heap)

        result = []
        # 파이썬의 힙은 최소힙 구조이기 때문에
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result


sol = Solution()
k = sol.kClosest([[3,3],[5,-1],[-2,4]], 2)
print(k)