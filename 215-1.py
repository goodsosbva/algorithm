from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    print(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)
        print(nums)

    return heapq.heappop(nums)


input_gab = [3, 2, 3, 1, 2, 4, 5, 5, 6]
num = 4
res = findKthLargest(input_gab, num)
print(res)
