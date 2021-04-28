from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    print(heap)

    for _ in range(k - 1):
        heapq.heappop(heap)

        print(heap)

    return -heapq.heappop(heap)


input_gab = [3, 2, 3, 1, 2, 4, 5, 5, 6]
num = 4
res = findKthLargest(input_gab, num)
print(res)

