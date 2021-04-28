from typing import List
import heapq


# 힙큐 매서드를 이용한 풀이
def findKthLargest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]  # -1은 k번째 인덱스가 된다


# 정렬을 이용한 풀이
def findKthLargest(nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]

