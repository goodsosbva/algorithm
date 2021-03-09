import collections
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqsHeap = []
    print(freqs)
    print(freqsHeap)
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqsHeap, (-freqs[f], f))
    print(freqs)
    print(freqsHeap)
    topk = list()
    # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqsHeap)[1])
    print(freqs)
    print(freqsHeap)
    return topk


nums = [1, 1, 1, 2, 2, 3]
k = 2
res = topKFrequent(nums, k)
print(res)

